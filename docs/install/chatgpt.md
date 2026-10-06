# Install in ChatGPT

How you install depends on your plan and on who you are.

[Back to all assistants](../../INSTALL.md)

| You are | Best route | You get |
| :--- | :--- | :--- |
| A workspace admin on Business, Enterprise or Edu | [Import the repo for your workspace](#for-your-whole-workspace-admin) | All seven, for everyone, kept up to date |
| A user on the ChatGPT desktop app | [Add the plugin from the repo](#chatgpt-desktop-app-and-codex) | All seven, in one step |
| A user on Business, Enterprise or Edu, on the web | [Upload each skill](#upload-the-skills-yourself) | One skill per upload |
| On Free, Plus or Pro | [Use them in a chat, or in a Project](#on-free-plus-or-pro) | Works now, no install |

ChatGPT cannot install anything from a GitHub link you paste into a chat. The routes below are the ways that do work.

---

## For your whole workspace (admin)

This installs all seven skills for everyone, and keeps them in sync with this repo.

1. Open **Admin**, then **Plugins**.
2. Select **Add**, then **Import marketplace**.
3. In **Source**, paste:

```text
https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills
```

4. Leave **Path** empty. Authorise GitHub when asked.
5. Set the **Installation policy** to **Installed** for the roles that should have it. Choose **Available** if people should add it themselves.

The marketplace refreshes once a day. To pull an update straight away, open **Admin**, **Plugins**, **Marketplaces**, and select **Sync now**.

Sellers then find **Sales Skills** under **Plugins**, on your workspace tab. In a chat, they type `@` to call it.

---

## ChatGPT desktop app and Codex

The ChatGPT desktop app and Codex share the same plugins. Adding the repo once makes all seven skills available in both.

You need Codex installed. Then run:

```text
codex plugin marketplace add humantic-ai-inc/HumanticAI-Sales-Skills
codex plugin add humantic-sales-skills@humantic-ai
```

Restart the desktop app. Open **Plugins** and you will see **Sales Skills** from **Humantic AI**.

In Codex, call a skill by name, for example `$meeting-prep`, or just ask for what you want.

To update later:

```text
codex plugin marketplace upgrade
```

---

## Upload the skills yourself

Skills are on ChatGPT **Business, Enterprise, Healthcare and Edu**. ChatGPT takes one skill per upload.

1. Download the skills you want from [dist/one-skill/chatgpt-copilot-gemini](../../dist/one-skill/chatgpt-copilot-gemini). Open each file, then select **Download raw file**. All seven are also in [all-skills.zip](https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills/raw/main/dist/all-skills.zip).
2. In ChatGPT, open **Plugins** in the sidebar.
3. Open the **Skills** tab.
4. Select **Create**, then **Upload from your computer**, and choose one file.
5. Repeat for each skill.

ChatGPT scans each upload before you can use it. Then just ask for what you want, and ChatGPT picks the right skill.

If ChatGPT rejects a file, try the same skill from [dist/one-skill/claude](../../dist/one-skill/claude), which keeps the skill inside its own folder.

---

## On Free, Plus or Pro

You cannot upload skills on these plans yet. Two ways to use them anyway.

### In one chat

Turn on web search, then paste:

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

This lasts for that chat only. If ChatGPT says it cannot open the links, open a skill in the [skills](../../skills) folder, copy all of it, and paste it in instead.

### In a Project, so it lasts

1. Create a Project, for example "Meeting prep".
2. Open its instructions.
3. Paste in the full text of one skill from the [skills](../../skills) folder.

Every chat in that Project now follows the skill.

---

## Next

- Connect Humantic AI to ChatGPT so the skills can use it: [the setup guide](../setup-humantic.md).
- Check it worked: ask "prep me for my meeting with [a colleague's LinkedIn URL] tomorrow". You should get the meeting outcome, a read on the person, questions to ask and the ask. A generic answer means the skill did not load.
