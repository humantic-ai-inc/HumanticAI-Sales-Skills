#!/usr/bin/env python3
"""Build every downloadable package in dist/ from the skills/ folder.

Run from anywhere:  python3 scripts/build-packages.py

Outputs
  dist/one-skill/claude/<skill>.zip                  one skill, folder inside (Claude)
  dist/one-skill/chatgpt-copilot-gemini/<skill>.zip  one skill, SKILL.md at the top
  dist/all-skills.zip                all seven skill folders in one download
  dist/humantic-sales-skills-copilot.zip   Microsoft Copilot Cowork plugin (all seven)
  dist/humantic-sales-skills-chatgpt.zip   OpenAI plugin for ChatGPT and Codex (all seven)
  dist/humantic-sales-skills-claude.zip    Claude plugin for an organisation upload (all seven)
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)  # stable zips, so unchanged skills give unchanged files


def add(z, src: Path, arcname: str):
    info = zipfile.ZipInfo(arcname, FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    z.writestr(info, src.read_bytes())


def skill_dirs():
    return sorted(p for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").exists())


def skill_files(d: Path):
    return sorted(f for f in d.rglob("*") if f.is_file() and not f.name.startswith("."))


def main():
    for sub in ("claude", "chatgpt-copilot-gemini"):
        (DIST / "one-skill" / sub).mkdir(parents=True, exist_ok=True)
    skills = skill_dirs()

    for d in skills:
        with zipfile.ZipFile(DIST / "one-skill" / "claude" / f"{d.name}.zip", "w") as z:
            for f in skill_files(d):
                add(z, f, f"{d.name}/{f.relative_to(d).as_posix()}")
        with zipfile.ZipFile(DIST / "one-skill" / "chatgpt-copilot-gemini" / f"{d.name}.zip", "w") as z:
            for f in skill_files(d):
                add(z, f, f.relative_to(d).as_posix())

    with zipfile.ZipFile(DIST / "all-skills.zip", "w") as z:
        for d in skills:
            for f in skill_files(d):
                add(z, f, f"{d.name}/{f.relative_to(d).as_posix()}")

    cowork = ROOT / "packaging" / "microsoft"
    with zipfile.ZipFile(DIST / "humantic-sales-skills-copilot.zip", "w") as z:
        for name in ("manifest.json", "color.png", "outline.png"):
            add(z, cowork / name, name)
        for d in skills:
            for f in skill_files(d):
                add(z, f, f"skills/{d.name}/{f.relative_to(d).as_posix()}")

    with zipfile.ZipFile(DIST / "humantic-sales-skills-chatgpt.zip", "w") as z:
        add(z, ROOT / "plugin.json", "plugin.json")
        for name in ("icon.png", "logo.png"):
            add(z, ROOT / "packaging" / "openai" / name, f"packaging/openai/{name}")
        for d in skills:
            for f in skill_files(d):
                add(z, f, f"skills/{d.name}/{f.relative_to(d).as_posix()}")

    with zipfile.ZipFile(DIST / "humantic-sales-skills-claude.zip", "w") as z:
        add(z, ROOT / ".claude-plugin" / "plugin.json", ".claude-plugin/plugin.json")
        for d in skills:
            for f in skill_files(d):
                add(z, f, f"skills/{d.name}/{f.relative_to(d).as_posix()}")

    print(f"Built packages for {len(skills)} skills in {DIST.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
