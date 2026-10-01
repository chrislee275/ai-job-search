#!/usr/bin/env python3
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "job-search-assistant"
PRIVATE_DATA_PATTERNS = {
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "international phone number": re.compile(r"\+(?:60|65)[\s-]?\d{4}[\s-]?\d{4,6}\b"),
    "salary amount": re.compile(r"\b(?:SGD|MYR|RM)\s*\d[\d,]*(?:\.\d{2})?\b"),
}


def fail(message):
    print(f"ERROR: {message}")
    sys.exit(1)


def read(path):
    return path.read_text(encoding="utf-8")


def validate_frontmatter():
    text = read(SKILL / "SKILL.md")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter missing or invalid")
    keys = []
    for line in match.group(1).splitlines():
        if ":" in line:
            keys.append(line.split(":", 1)[0].strip())
    if keys != ["name", "description"]:
        fail(f"Unexpected SKILL.md frontmatter keys: {keys}")
    if "name: job-search-assistant" not in match.group(1):
        fail("Skill name is not job-search-assistant")


def validate_required_files():
    required = [
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "install.sh",
        "uninstall.sh",
        "docs/COMMANDS.md",
        "docs/INSTALL.md",
        "docs/JD_LINK_ACCESS.md",
        "scripts/extract_jd.py",
        "skills/job-search-assistant/scripts/extract_jd.py",
        "skills/job-search-assistant/references/jd-link-access.md",
        ".github/workflows/validate.yml",
        "skills/job-search-assistant/SKILL.md",
        "skills/job-search-assistant/agents/openai.yaml",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            fail(f"Missing required file: {rel}")


def validate_links():
    readme = read(ROOT / "README.md")
    for link in re.findall(r"\]\(([^)]+)\)", readme):
        if link.startswith(("http://", "https://", "#")):
            continue
        if not (ROOT / link).exists():
            fail(f"README link target missing: {link}")


def validate_counts_and_commands():
    examples = list((ROOT / "examples").glob("*.md"))
    tests = list((ROOT / "tests").glob("*.md"))
    if len(examples) < 10:
        fail("Expected at least 10 examples")
    if len(tests) < 13:
        fail("Expected at least 13 manual QA tests")
    if not (ROOT / "tests" / "fixtures" / "public_job.html").exists():
        fail("Missing JD link access fixture")
    if not (ROOT / "tests" / "fixtures" / "linkedin_public_job.html").exists():
        fail("Missing LinkedIn JD link access fixture")
    skill_text = read(SKILL / "SKILL.md")
    for command in [
        "setup",
        "review",
        "batch",
        "apply-prep",
        "resume",
        "profile",
        "reply",
        "interview",
    ]:
        token = f"/ai-job-search:{command}"
        if token not in skill_text and token not in read(ROOT / "docs" / "COMMANDS.md"):
            fail(f"Missing command: {token}")


def validate_private_data_and_placeholders():
    text_exts = {".md", ".py", ".yml", ".yaml", ".sh", ".txt", ".json", ".html"}
    paths = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and path.suffix in text_exts
    ]
    for path in paths:
        content = read(path)
        for label, pattern in PRIVATE_DATA_PATTERNS.items():
            if pattern.search(content):
                fail(f"Possible private {label} in {path.relative_to(ROOT)}")
        for pattern in ["TO" + "DO", "[" + "TO" + "DO"]:
            if pattern in content:
                fail(f"Placeholder found in {path.relative_to(ROOT)}")


def validate_privacy_rules():
    # Fictional samples keep this check useful without publishing personal details.
    samples = {
        "email address": "sample.person" + "@example.test",
        "international phone number": "+65 " + "9123 4567",
        "salary amount": "SGD " + "9,999",
    }
    for label, sample in samples.items():
        if not PRIVATE_DATA_PATTERNS[label].search(sample):
            fail(f"Privacy rule did not detect synthetic {label}")


def validate_jd_extractor():
    import json
    import subprocess

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "extract_jd.py"), str(ROOT / "tests" / "fixtures" / "public_job.html")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    if payload.get("title") != "Product Analyst":
        fail("JD extractor did not extract fixture title")
    if payload.get("company") != "ExampleCo":
        fail("JD extractor did not extract fixture company")
    if not payload.get("visible_text"):
        fail("JD extractor did not return visible text")
    result = subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "extract_jd.py"), str(ROOT / "tests" / "fixtures" / "public_job.html")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    if payload.get("title") != "Product Analyst":
        fail("Bundled JD extractor did not extract title")
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "extract_jd.py"), str(ROOT / "tests" / "fixtures" / "linkedin_public_job.html")],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    if payload.get("title") != "AI Specialist":
        fail("LinkedIn fixture did not extract title")
    if payload.get("company") != "Confidential":
        fail("LinkedIn fixture did not extract company")
    if "Similar jobs" in payload.get("visible_text", ""):
        fail("LinkedIn fixture included similar jobs in visible_text")


def main():
    validate_required_files()
    validate_frontmatter()
    validate_links()
    validate_counts_and_commands()
    validate_privacy_rules()
    validate_private_data_and_placeholders()
    validate_jd_extractor()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
