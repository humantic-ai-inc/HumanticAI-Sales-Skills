# Install the skills

Pick your assistant. Each page has a copy-paste route and step-by-step instructions.

| Assistant | Install guide | All seven in one go? |
| :--- | :--- | :--- |
| **Claude** | [INSTALL-CLAUDE.md](INSTALL-CLAUDE.md) | Yes. Paste one prompt, or add the repo from the menu |
| **ChatGPT** | [INSTALL-CHATGPT.md](INSTALL-CHATGPT.md) | Yes, through your workspace admin or the desktop app. One at a time on the web |
| **Microsoft Copilot** | [INSTALL-COPILOT.md](INSTALL-COPILOT.md) | Yes. Upload one plugin file in Cowork, or your admin deploys it |
| **Gemini** | [Below](#gemini) | One at a time |
| **Anything else** | [Below](#any-assistant-paste-into-a-chat) | For one chat, no install |

**Two separate things, in this order:**

1. **Connect Humantic AI** to your assistant, once. That is [SETUP.md](SETUP.md).
2. **Install the skills**, using the guide for your assistant.

The skills work without Humantic AI connected. They get much better with it.

Steps checked in October 2026. These assistants change their menus often. If a screen does not match, tell your Humantic AI contact.

---

## What is in the repo

| File | What it is for |
| :--- | :--- |
| `.claude-plugin/` | The Claude plugin. Claude, Claude Code and GitHub Copilot read it |
| `plugin.json` and `.agents/plugins/` | The OpenAI plugin. ChatGPT and Codex read it |
| `m365/cowork/` | The Microsoft Copilot Cowork plugin manifest and icons |
| `skills/` | The seven skills themselves |
| `dist/humantic-sales-skills-copilot.zip` | Ready-made Copilot Cowork plugin, all seven |
| `dist/humantic-sales-skills-claude.zip` | Ready-made Claude plugin, for an organisation upload |
| `dist/humantic-sales-skills-chatgpt.zip` | Ready-made OpenAI plugin, all seven |
| `dist/all-skills.zip` | All seven skill folders in one download |
| `dist/claude/` | One skill per file, with the skill inside its folder |
| `dist/gemini-copilot/` | One skill per file, with SKILL.md at the top |

Everything in `dist/` is built from `skills/` by `scripts/build-packages.py`. Run it after changing a skill.

---

## Gemini

Skills in Gemini are for personal Google accounts today. Work and school accounts get them later, so use a Gem until then.

1. Download the skills you want from [dist/gemini-copilot](dist/gemini-copilot). Open each file, then select **Download raw file**.
2. Go to gemini.google.com. Open **Settings**, then **Skills**.
3. Select **Upload** and choose the file.
4. Open the skill and select **More**, then **Activate**.
5. In a chat, type `/` and pick the skill, or just describe what you need.

**On a work or school account:** open **Gems** in the sidebar and select **New Gem**. Name it after the skill. Paste the full text of the skill from the [skills](skills) folder into **Instructions**, then save.

Gemini cannot read files from GitHub, so you need to download them first.

---

## Any assistant: paste into a chat

Good for trying the skills. It lasts for that chat only.

**If your assistant can open links** (Claude with web search on, or ChatGPT with web search on):

```text
Load the Humantic AI sales skills and use them for the rest of this
conversation. Read all seven files:

https://raw.githubusercontent.com/humantic-ai-inc/HumanticAI-Sales-Skills/main/skills/buyer-read/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/HumanticAI-Sales-Skills/main/skills/meeting-prep/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/HumanticAI-Sales-Skills/main/skills/pursuit-plan/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/HumanticAI-Sales-Skills/main/skills/prospecting/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/HumanticAI-Sales-Skills/main/skills/sales-email/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/HumanticAI-Sales-Skills/main/skills/buying-committee/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/HumanticAI-Sales-Skills/main/skills/expansion-play/SKILL.md

From now on, when what I ask matches one of them, follow that skill and
tell me in one line which one you used. List the seven names, then ask
me what I am working on.
```

**If it cannot open links** (Gemini, Copilot Chat), paste the skill itself:

```text
Below is a skill definition. Follow it for the rest of this conversation.
Reply with one line to confirm, then ask me what you are working on.

[open a skill in the skills folder of this repo, copy all of it,
and paste it here]
```

---

## Check it worked

Ask this, using a real colleague who is happy to be the test:

```text
Prep me for my meeting with [their LinkedIn URL] at [their company]
tomorrow. The goal is to book a second meeting with their manager.
```

A working skill gives you the meeting outcome and a fallback, a short read on the person, what changed at their company, two to four questions, the objection to expect, and the ask. A generic answer means the skill did not load.

---

## Trouble

**The upload is rejected.** Claude wants the skill inside its folder: use [dist/claude](dist/claude). Gemini and Copilot want SKILL.md at the top: use [dist/gemini-copilot](dist/gemini-copilot).

**The skill installed but never runs.** Ask in plain words, for example "prep me for my meeting with Acme". If it still does not run, type `/` or `@` and pick it by name, where your assistant supports that.

**The answers have no Humantic AI research in them.** Connect Humantic AI with [SETUP.md](SETUP.md).

**A screen does not match these steps.** Tell your Humantic AI contact and we will fix the page.
