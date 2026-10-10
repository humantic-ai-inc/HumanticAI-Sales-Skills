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

Gemini cannot read files from GitHub, so step 1 is needed.

### On a work or school account: make a Gem

1. Open the skill you want in the [skills](skills) folder, for example `meeting-prep`, then open its `SKILL.md`.
2. Select the **Copy raw file** button at the top right of the file.
3. Go to gemini.google.com and open **Gems** in the sidebar.
4. Select **New Gem**.
5. In **Name**, type the skill's name, for example `Meeting prep`.
6. Click into **Instructions** and paste.
7. Select **Save**.
8. To use it, open **Gems** and select your Gem. Then type what you need.

Repeat for each skill you want.

---

## Any assistant: paste into a chat

Good for trying the skills. It lasts for that chat only.

### If your assistant can open links (Claude or ChatGPT)

1. Start a new chat.
2. Turn on web search. In Claude, select **+** at the bottom left of the message box, then switch on **Web search**. In ChatGPT, select **+**, then **Web search**.
3. Copy the block below with the copy button at its top right.
4. Paste it into the chat and send it.
5. The assistant lists the seven skill names. Now ask for what you need.

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

### If it cannot open links (Gemini, Copilot Chat)

1. Open the skill you want in the [skills](skills) folder, then open its `SKILL.md`.
2. Select the **Copy raw file** button at the top right of the file.
3. Start a new chat in your assistant.
4. Type the two lines in the block below, then paste the skill underneath them.
5. Send it. The assistant confirms in one line. Now ask for what you need.

```text
Below is a skill definition. Follow it for the rest of this conversation.
Reply with one line to confirm, then ask me what you are working on.

[open a skill in the skills folder of this repo, copy all of it,
and paste it here]
```

---

## Check it worked

1. Pick a colleague who is happy to be the test, and copy their LinkedIn URL.
2. Start a new chat in your assistant.
3. Copy the block below, paste it in, and swap in their URL and company.
4. Send it.

```text
Prep me for my meeting with [their LinkedIn URL] at [their company]
tomorrow. The goal is to book a second meeting with their manager.
```

**It worked if** the answer has all of these: the outcome the meeting has to produce and a fallback, a short read on the person, what changed at their company, two to four questions, the objection to expect, and the ask.

**It did not work if** you get a general answer with none of that structure. Go back to the install guide for your assistant and check each step.

---

## Trouble

**The upload is rejected.**

1. Check which folder you downloaded from.
2. For Claude, download again from [dist/one-skill/claude](dist/one-skill/claude).
3. For ChatGPT, Copilot or Gemini, download again from [dist/one-skill/chatgpt-copilot-gemini](dist/one-skill/chatgpt-copilot-gemini).
4. Upload the new file.

**The skill installed but never runs.**

1. Start a new chat.
2. Ask in plain words, for example `prep me for my meeting with Acme tomorrow`.
3. If it still does not run, type `/` in Claude, Gemini or Codex, or `@` in ChatGPT, and pick the skill by name.

**The answers have no Humantic AI research in them.** Connect Humantic AI with [the setup guide](docs/setup-humantic.md).

**A screen does not match these steps.** Tell your Humantic AI contact and we will fix the page.
