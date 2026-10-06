# Install the skills

Pick your assistant. Each page has a copy-paste route and step-by-step instructions.

| Assistant | Install guide | All seven in one go? |
| :--- | :--- | :--- |
| **Claude** | [Claude guide](docs/install/claude.md) | Yes. Paste one prompt, or add the repo from the menu |
| **ChatGPT** | [ChatGPT guide](docs/install/chatgpt.md) | Yes, through your workspace admin or the desktop app. One at a time on the web |
| **Microsoft Copilot** | [Copilot guide](docs/install/copilot.md) | Yes. Upload one plugin file in Cowork, or your admin deploys it |
| **Gemini** | [Below](#gemini) | One at a time |
| **Anything else** | [Below](#any-assistant-paste-into-a-chat) | For one chat, no install |

**Two separate things, in this order:**

1. **Connect Humantic AI** to your assistant, once. That is [the setup guide](docs/setup-humantic.md).
2. **Install the skills**, using the guide for your assistant.

The skills work without Humantic AI connected. They get much better with it.

Steps checked in October 2026. These assistants change their menus often. If a screen does not match, tell your Humantic AI contact.

---

## Which download to use

| File | Use it for |
| :--- | :--- |
| `dist/humantic-sales-skills-copilot.zip` | Microsoft Copilot Cowork: all seven in one upload |
| `dist/humantic-sales-skills-claude.zip` | Claude, uploaded by an Owner for the whole organisation |
| `dist/humantic-sales-skills-chatgpt.zip` | ChatGPT and Codex: all seven as one plugin |
| `dist/all-skills.zip` | All seven skill folders in one download |
| `dist/one-skill/claude/` | One skill at a time in Claude |
| `dist/one-skill/chatgpt-copilot-gemini/` | One skill at a time in ChatGPT, Copilot or Gemini |

Everything in `dist/` is built from `skills/` by `scripts/build-packages.py`. See [CONTRIBUTING.md](CONTRIBUTING.md) to change a skill.

---

## Gemini

Skills in Gemini are for personal Google accounts today. Work and school accounts get them later, so use a Gem until then.

1. Download the skills you want from [dist/one-skill/chatgpt-copilot-gemini](dist/one-skill/chatgpt-copilot-gemini). Open each file, then select **Download raw file**.
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

**The upload is rejected.** Claude wants the skill inside its folder: use [dist/one-skill/claude](dist/one-skill/claude). Gemini and Copilot want SKILL.md at the top: use [dist/one-skill/chatgpt-copilot-gemini](dist/one-skill/chatgpt-copilot-gemini).

**The skill installed but never runs.** Ask in plain words, for example "prep me for my meeting with Acme". If it still does not run, type `/` or `@` and pick it by name, where your assistant supports that.

**The answers have no Humantic AI research in them.** Connect Humantic AI with [the setup guide](docs/setup-humantic.md).

**A screen does not match these steps.** Tell your Humantic AI contact and we will fix the page.
