# Adding or changing a skill

## Change an existing skill

1. Edit `skills/<skill-name>/SKILL.md`.
2. Run the checks and rebuild the downloads:

```text
python3 scripts/validate-skills.py
python3 scripts/build-packages.py
```

3. Commit the skill and everything that changed in `dist/` together, so the downloads always match the skills.

## Add a new skill

1. Copy `templates/SKILL.template.md` to `skills/<new-skill-name>/SKILL.md`. Use lowercase and hyphens for the name.
2. Set `name` in the file to exactly the folder name. Every assistant rejects a skill whose name and folder differ.
3. Write the `description` as what the seller gets, then the phrases a seller would actually say, then the mistake it prevents. Keep it under 1,024 characters.
4. Add a short `README.md` in the same folder, written for a seller browsing the repo.
5. Add the skill to `packaging/microsoft/manifest.json` under `agentSkills`, and to the tables in `README.md` and `skills/README.md`.
6. Run both scripts above, then commit.

A Microsoft Copilot agent holds at most eight skills, and a Cowork plugin at most twenty. Check those limits before adding the eighth.

## How every skill is written

- **Open with the mistake it prevents.** That is what makes a seller reach for it.
- **Run on whatever the seller has.** List the evidence as Minimum, Better with and Best with, so the skill works without Humantic AI and gets sharper with it.
- **Say where each point came from:** Humantic AI, a connected tool, the seller, or inference.
- **Plain language.** No setup steps inside a skill, and no personality-model jargon unless the seller uses it first.
- **Never put a personality read into anything the buyer might see.**

## Before you release

1. Raise the version in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `plugin.json` and `packaging/microsoft/manifest.json`. Keep all four the same. Microsoft rejects a version that starts with 0.
2. Add a line to `CHANGELOG.md`.
3. Check the plugins:

```text
claude plugin validate ./
```

For the Copilot package, run Microsoft's check while signed in to Microsoft 365:

```text
npx @microsoft/m365agentstoolkit-cli validate --package-file dist/humantic-sales-skills-copilot.zip
```
