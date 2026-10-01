#!/usr/bin/env python3
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class JobHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta = {}
        self.json_ld = []
        self.text_parts = []
        self._tag_stack = []
        self._capture_title = False
        self._capture_script = False
        self._script_type = ""
        self._script = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self._tag_stack.append(tag)
        if tag == "title":
            self._capture_title = True
        elif tag == "meta":
            key = attrs.get("property") or attrs.get("name")
            if key and attrs.get("content"):
                self.meta[key.lower()] = attrs["content"].strip()
        elif tag == "script":
            self._capture_script = True
            self._script_type = attrs.get("type", "").lower()
            self._script = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._capture_title = False
        elif tag == "script":
            if self._capture_script and self._script_type == "application/ld+json":
                raw = "".join(self._script).strip()
                if raw:
                    self.json_ld.append(raw)
            self._capture_script = False
            self._script_type = ""
            self._script = []
        if self._tag_stack and self._tag_stack[-1] == tag:
            self._tag_stack.pop()

    def handle_data(self, data):
        value = " ".join(data.split())
        if not value:
            return
        if self._capture_script:
            self._script.append(data)
        elif self._capture_title:
            self.title += value + " "
        elif not any(tag in {"script", "style", "noscript"} for tag in self._tag_stack):
            self.text_parts.append(value)


def load_source(source):
    if source.startswith(("http://", "https://")):
        request = Request(source, headers={"User-Agent": "Mozilla/5.0 job-search-assistant/1.0"})
        with urlopen(request, timeout=20) as response:
            return response.read().decode(response.headers.get_content_charset() or "utf-8", "replace")
    path = Path(source)
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    raise FileNotFoundError(source)


def flatten_json_ld(value):
    if isinstance(value, list):
        for item in value:
            yield from flatten_json_ld(item)
    elif isinstance(value, dict):
        if "@graph" in value:
            yield from flatten_json_ld(value["@graph"])
        yield value


def find_jobposting(json_ld_items):
    for raw in json_ld_items:
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            continue
        for item in flatten_json_ld(parsed):
            kind = item.get("@type")
            if isinstance(kind, list):
                is_job = "JobPosting" in kind
            else:
                is_job = kind == "JobPosting"
            if is_job:
                return item
    return {}


def clean_text(parts):
    text = " ".join(parts)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def pick_work_mode(text):
    lower = text.lower()
    modes = []
    for mode in ["remote", "hybrid", "onsite", "on-site"]:
        if mode in lower:
            modes.append("onsite" if mode == "on-site" else mode)
    return sorted(set(modes))


def linkedin_cleanup(source, title, text):
    if "linkedin.com/jobs" not in source and "LinkedIn" not in title:
        return title, None, None, text

    company = None
    location = None
    role = title

    match = re.match(r"(.+?) hiring (.+?) in (.+?) \| LinkedIn", title)
    if match:
        company, role, location = [part.strip() for part in match.groups()]

    jd_text = text
    start = jd_text.find("Report this job")
    if start != -1:
        jd_text = jd_text[start + len("Report this job") :].strip()
    if "Responsibilities:" in jd_text and (
        jd_text.startswith("Use AI")
        or jd_text.startswith("Sign in")
        or ("Sign in" in jd_text[: jd_text.find("Responsibilities:")])
    ):
        resp_start = jd_text.find("Responsibilities:")
        window_start = max(0, resp_start - 160)
        window = jd_text[window_start:resp_start]
        role_start = window.rfind(role) if role else -1
        if role_start != -1:
            jd_text = jd_text[window_start + role_start :].strip()
        else:
            jd_text = jd_text[resp_start:].strip()
    elif start == -1 and "Responsibilities:" in jd_text:
        resp_start = jd_text.find("Responsibilities:")
        window_start = max(0, resp_start - 160)
        window = jd_text[window_start:resp_start]
        role_start = window.rfind(role) if role else -1
        if role_start != -1:
            jd_text = jd_text[window_start + role_start :].strip()
    for marker in [
        "Referrals increase",
        "Get notified",
        "Similar jobs",
        "Show more jobs like this",
        "People also viewed",
        "Explore top content on LinkedIn",
        "LinkedIn ©",
    ]:
        end = jd_text.find(marker)
        if end != -1:
            jd_text = jd_text[:end].strip()
            break

    return role, company, location, jd_text or text


def split_section(text, start_label, end_labels):
    start = text.lower().find(start_label.lower())
    if start == -1:
        return None
    section = text[start + len(start_label) :]
    end_positions = [section.lower().find(label.lower()) for label in end_labels]
    end_positions = [pos for pos in end_positions if pos != -1]
    if end_positions:
        section = section[: min(end_positions)]
    return section.strip(" :-•")


def extract(source):
    result = {
        "source": source,
        "status": "ok",
        "access": "visible",
        "confidence": "Low",
        "title": None,
        "company": None,
        "location": None,
        "work_mode": [],
        "salary": None,
        "requirements": None,
        "responsibilities": None,
        "visible_text": "",
        "notes": [],
    }
    try:
        html = load_source(source)
    except (HTTPError, URLError, TimeoutError, FileNotFoundError) as exc:
        result.update({"status": "blocked", "access": "blocked", "confidence": "None"})
        result["notes"].append(f"Could not access source: {exc}")
        return result

    parser = JobHTMLParser()
    parser.feed(html)
    text = clean_text(parser.text_parts)
    job = find_jobposting(parser.json_ld)

    title = job.get("title") or parser.meta.get("og:title") or parser.title.strip() or None
    org = job.get("hiringOrganization") or {}
    company = org.get("name") if isinstance(org, dict) else None
    location = job.get("jobLocation")
    if isinstance(location, list):
        location = location[0] if location else None
    if isinstance(location, dict):
        address = location.get("address")
        if isinstance(address, dict):
            location = ", ".join(str(address.get(k)) for k in ["addressLocality", "addressRegion", "addressCountry"] if address.get(k))
        else:
            location = location.get("name")

    salary = job.get("baseSalary")
    if isinstance(salary, dict):
        salary = json.dumps(salary, ensure_ascii=False)

    description = clean_text([str(job.get("description", ""))]) if job.get("description") else ""
    visible = description or text
    title, linked_company, linked_location, visible = linkedin_cleanup(source, title or "", visible)
    company = company or linked_company
    location = location or linked_location

    result.update(
        {
            "title": title,
            "company": company,
            "location": location,
            "work_mode": pick_work_mode(visible),
            "salary": salary,
            "requirements": split_section(visible, "Requirements", ["Working Schedule", "Seniority level", "Employment type", "Industries"]),
            "responsibilities": split_section(visible, "Responsibilities", ["Requirements", "Working Schedule", "Seniority level", "Employment type", "Industries"]),
            "visible_text": visible[:8000],
        }
    )

    if job:
        result["confidence"] = "High" if title and visible else "Medium"
        result["notes"].append("Extracted structured JobPosting data.")
    elif title and len(visible) > 500:
        result["confidence"] = "Medium"
        result["notes"].append("Extracted visible HTML text without structured JobPosting data.")
    elif visible:
        result["confidence"] = "Low"
        result["notes"].append("Only limited visible text was extracted.")
    else:
        result.update({"status": "blocked", "access": "no_visible_content", "confidence": "None"})
        result["notes"].append("No visible JD content found. Ask for JD text or screenshot.")

    return result


def main():
    parser = argparse.ArgumentParser(description="Extract visible JD content from a public job page or local HTML file.")
    parser.add_argument("source", help="http(s) URL or local HTML file")
    args = parser.parse_args()
    print(json.dumps(extract(args.source), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
