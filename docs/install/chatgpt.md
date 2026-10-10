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

**What your sellers do next:**

1. In the ChatGPT sidebar, select **Plugins**.
2. Open the tab with your workspace's name.
3. Open **Sales Skills**. If you chose **Available** in step 5, select **Install plugin**.
4. In a new chat, type `@`, select **Sales Skills**, and ask for what they need.

**To pull an update straight away:** open **Admin**, then **Plugins**, then **Marketplaces**, and select **Sync now** next to **humantic-ai**. Otherwise it refreshes once a day.

---

## ChatGPT desktop app and Codex

The ChatGPT desktop app and Codex share the same plugins. Adding the repo once makes all seven skills available in both. This route uses the Terminal app on your computer.

1. Open **Terminal** on a Mac, or **PowerShell** on Windows.
2. If you do not have Codex yet, paste this and press Enter:

```text
npm install -g @openai/codex
```

3. Paste these two lines and press Enter:

```text
codex plugin marketplace add humantic-ai-inc/HumanticAI-Sales-Skills
codex plugin add humantic-sales-skills@humantic-ai
```

4. You should see `Added plugin humantic-sales-skills`.
5. Quit the ChatGPT desktop app and open it again.
6. Open **Plugins**. You will see **Sales Skills** from **Humantic AI**.

**To use a skill in Codex:** type `$meeting-prep`, or any skill name, or just ask for what you want.

**To update later:** open Terminal, paste `codex plugin marketplace upgrade` and press Enter.

---

## Upload the skills yourself

Skills are on ChatGPT **Business, Enterprise, Healthcare and Edu**. ChatGPT takes one skill per upload.

1. Download the skills you want from [dist/one-skill/chatgpt-copilot-gemini](../../dist/one-skill/chatgpt-copilot-gemini). Open each file, then select **Download raw file**. All seven are also in [all-skills.zip](https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills/raw/main/dist/all-skills.zip).
2. In ChatGPT, open **Plugins** in the sidebar.
3. Open the **Skills** tab.
4. Select **Create**, then **Upload from your computer**, and choose one file.
5. Wait while ChatGPT scans the file. When it finishes, the skill shows in the **Skills** tab.
6. Repeat steps 4 and 5 for each skill.
7. In a new chat, ask for what you need, for example `prep me for my meeting with Acme tomorrow`. ChatGPT picks the right skill.

**If ChatGPT rejects a file:**

1. Download the same skill from [dist/one-skill/claude](../../dist/one-skill/claude) instead.
2. Upload that file, as in step 4.

---

## On Free, Plus or Pro

You cannot upload skills on these plans yet. Two ways to use them anyway.

### In one chat

1. Start a new chat.
2. Select **+** in the message box, then **Web search**.
3. Copy the block below with the copy button at its top right.
4. Paste it into the chat and send it.
5. ChatGPT lists the seven skill names. Now ask for what you need.

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

This lasts for that chat only.

**If ChatGPT says it cannot open the links:**

1. Open the skill you want in the [skills](../../skills) folder, then open its `SKILL.md`.
2. Select the **Copy raw file** button at the top right of the file.
3. Paste it into the chat with `Follow this skill for the rest of this conversation.` on the line above, and send it.

### In a Project, so it lasts

1. In the ChatGPT sidebar, select **New project**.
2. Name it after the skill, for example `Meeting prep`, and select **Create project**.
3. On the project page, select **Instructions**.
4. Open the skill in the [skills](../../skills) folder, open its `SKILL.md`, and select **Copy raw file**.
5. Paste it into **Instructions** and select **Save**.
6. Start every chat for that job inside this project. Each one follows the skill.

---

## Check it worked

1. Connect Humantic AI first, if you have not: follow [the setup guide](../setup-humantic.md).
2. Start a new chat.
3. Type: `Prep me for my meeting with [a colleague's LinkedIn URL] tomorrow.`
4. Send it.

**It worked if** you get the meeting outcome, a read on the person, questions to ask and the ask. **It did not work if** you get a general answer with none of that. Go back over the steps above.
