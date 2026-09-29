# Install the skills

Pick your assistant, follow the steps, done in a few minutes. No terminal, no GitHub account.

**Two separate things, in this order:**

1. **Connect Humantic AI** to your assistant, once. That is [SETUP.md](SETUP.md).
2. **Install the skills** from this page.

The skills work without Humantic AI connected, and they get much better with it. Steps checked in September 2026. If a screen does not match, tell your Humantic AI contact.

**Want the whole set in one go?** Claude is the only assistant with a true one-step install for all seven, and it takes about thirty seconds. ChatGPT and Gemini take the skills one file at a time, so [`dist/all-skills.zip`](dist/all-skills.zip) holds all seven in one download. For Microsoft Copilot, one admin can deploy the set to everyone: ask your Humantic AI contact.

| Assistant | The short version |
| :--- | :--- |
| [Claude](#claude) | Add this repo once and get all seven skills |
| [ChatGPT](#chatgpt) | Upload each skill under Plugins, Skills. Business, Enterprise, Healthcare and Edu plans |
| [Gemini](#gemini) | Upload each skill under Settings, Skills. Personal accounts |
| [Microsoft Copilot](#microsoft-copilot) | Upload each skill in Cowork, or ask your admin to deploy them for everyone |
| [None of the above](#no-install-paste-the-skill-into-a-chat) | Paste one skill into a chat and use it there |

---

## Let your assistant do it: prompts you can paste

Four prompts. The first works anywhere and takes ten seconds. The rest ask the assistant to do the installing for you.

### 1. Use all seven right now, in this chat

Paste this into **Claude** or **ChatGPT** with web access turned on. In Claude, select **+** in the chat box and turn on **Web search** first.

```text
Load the Humantic AI sales skills and use them for the rest of this
conversation. Read all seven files:

https://raw.githubusercontent.com/humantic-ai-inc/sales-skills/main/skills/buyer-read/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/sales-skills/main/skills/meeting-prep/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/sales-skills/main/skills/pursuit-plan/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/sales-skills/main/skills/prospecting/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/sales-skills/main/skills/sales-email/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/sales-skills/main/skills/buying-committee/SKILL.md
https://raw.githubusercontent.com/humantic-ai-inc/sales-skills/main/skills/expansion-play/SKILL.md

From now on, when what I ask matches one of them, follow that skill and
tell me in one line which one you used. List the seven names, then ask
me what I am working on.
```

**This lasts for one conversation.** It is the fastest way to see what the skills do. Install them properly, using one of the sections above, once you want them every day.

### 2. Install everything in Claude

```text
Install the Humantic AI sales skills from
https://github.com/humantic-ai-inc/sales-skills

Check that repo, add it as a plugin marketplace, and install the
humantic-sales-skills plugin so all seven skills are available to me.
Then list the seven skill names.
```

### 3. Have your assistant walk you through the real install

Paste this into whichever assistant you use. It reads our instructions and gives you only the steps that apply to you.

```text
Read
https://raw.githubusercontent.com/humantic-ai-inc/sales-skills/main/INSTALL.md
and walk me through installing all seven Humantic AI sales skills in
this assistant. Ask me anything you need, give me one step at a time,
and wait for me to say done before the next one.
```

### 4. Ask your assistant to create the skills for you

Some assistants can build a skill from what you paste in.

**ChatGPT** can, on Business, Enterprise, Healthcare and Edu plans. Open **Plugins**, the **Skills** tab, then **Create**, then **Create with chat**, and paste:

```text
Create a skill called meeting-prep. Use exactly the content of
https://raw.githubusercontent.com/humantic-ai-inc/sales-skills/main/skills/meeting-prep/SKILL.md
as its instructions, and keep its name and description as written
there. Do not summarise or shorten it.
```

Repeat for the other six: `buyer-read`, `pursuit-plan`, `prospecting`, `sales-email`, `buying-committee`, `expansion-play`. If ChatGPT cannot open the link, open the file yourself, copy everything, and paste it in place of the link.

**Copilot Cowork** can save files for you. Ask it:

```text
Save these seven Humantic AI sales skills into my OneDrive under
Documents / Cowork / skills, one folder per skill, each folder holding
its SKILL.md exactly as written. The files are at
https://github.com/humantic-ai-inc/sales-skills/tree/main/skills
```

If it cannot reach GitHub, download `dist/all-skills.zip`, unpack it, and drag the seven folders into that OneDrive folder yourself. Either way, Cowork picks them up at the start of your next session.

**Gemini** cannot read files from GitHub, so upload them as described above.

---

## Claude

### Ask Claude to install them (easiest)

Paste this into Claude and it takes care of the rest:

```text
Install the Humantic AI sales skills from
https://github.com/humantic-ai-inc/sales-skills

Check that repo, add it as a plugin marketplace, and install the
humantic-sales-skills plugin so all seven skills are available to me.
Then list the seven skill names and tell me one thing each is good for.

If you cannot install it yourself here, say so and walk me through
doing it, one step at a time.
```

Claude reads the repo, adds it, and installs all seven. If you are in a version of Claude that cannot install things for you, it will say so and talk you through the menu steps below instead.

### Add it yourself, from the menu

1. In the left sidebar, open **Customize**.
2. Open the **Plugins** tab.
3. Select **Add**, then **Add marketplace**.
4. Type `humantic-ai-inc/sales-skills` and confirm.
5. Find **Humantic Sales Skills** in the list and select **Add**.

That is it. No GitHub account and no sign-in: this repo is public, and Claude reads it anonymously.

**In Claude Code**, the same thing in two lines:

```text
/plugin marketplace add humantic-ai-inc/sales-skills
/plugin install humantic-sales-skills@humantic-ai
```

This is the whole set, installed once: all seven skills arrive together, and there is nothing to keep in sync by hand.

### One skill at a time

Use this if you only want, say, meeting prep, or if your plan does not offer plugins.

1. Download the skill you want from [`dist/claude/`](dist/claude): open the file and select **Download raw file**.
2. In Claude, open **Customize**, then **Skills**.
3. Select **+**, then **Create skill**, then **Upload a skill**, and choose the file you downloaded.
4. Turn it on.

Skills need code execution switched on. If you do not see the option, check **Settings**, **Capabilities**, and turn on **Code execution and file creation**. On Team and Enterprise an Owner turns it on for the organisation.

### For a whole team

An Owner can install these for everyone: **Organization settings**, **Plugins & skills**, **Add**, then upload, and set the availability to **Installed by default**.

### Staying up to date

Nothing signs you up for automatic updates, and nothing needs a GitHub login.

- **Added as a marketplace:** you get the current version whenever you add or refresh it. In Claude Code, `/plugin` has an update option per marketplace.
- **Uploaded as a file:** that copy stays as it was. To take an update, download the file again and re-upload it.
- The "sync from GitHub" option in organisation settings is a different feature, for private company repos, and it is the one that asks you to connect a GitHub account. You do not need it for these skills.

---

## ChatGPT

Skills are available on ChatGPT **Business, Enterprise, Healthcare and Edu**. On a personal Plus or Pro account, use the Project method below instead.

ChatGPT takes one skill at a time, so repeat step 4 for each. [`dist/all-skills.zip`](dist/all-skills.zip) gives you all seven in one download to unpack first.

1. Download the skills you want from [`dist/claude/`](dist/claude) (the same files work here): open a file and select **Download raw file**.
2. In ChatGPT, open **Plugins** in the sidebar.
3. In the Plugin Directory, open the **Skills** tab.
4. Select **Create**, then **Upload from your computer**, and choose the file.
5. Repeat for each skill you want.

Then just ask for what you want, for example "prep me for my meeting with Acme tomorrow", and ChatGPT picks the skill.

**To give them to your whole workspace**, an admin can share a skill from its menu, or publish it to everyone. Ask your ChatGPT workspace admin.

**No Skills on your plan?** Make a Project instead. Create a project, open its instructions, and paste in the text of the skill you want from the `skills/` folder in this repo. Every chat inside that project then follows it. A Custom GPT works the same way: paste the skill into **Instructions**.

---

## Gemini

Skills in Gemini are for **personal Google accounts** today. Work and school accounts get them later, so use the Gem method below until then.

1. Download the skills you want from [`dist/gemini-copilot/`](dist/gemini-copilot): open a file and select **Download raw file**.
2. Go to gemini.google.com and open **Settings**, then **Skills**.
3. Select **Upload** and choose the file.
4. Open the skill and select **More**, then **Activate**.
5. In a chat, type `/` and pick the skill, or simply describe what you need.

Gemini takes one skill at a time. [`dist/all-skills.zip`](dist/all-skills.zip) gives you all seven in one download to unpack first.

**On a work or school account**, make a Gem: open **Gems** in the sidebar, select **New Gem**, give it the skill's name, and paste the text of the skill from the `skills/` folder into **Instructions**. Save it, then start a chat with that Gem.

Gemini cannot read files straight from GitHub, so the download step is required.

---

## Microsoft Copilot

### For yourself, in Copilot Cowork

You need a Microsoft 365 Copilot licence.

1. Download the skills you want from [`dist/gemini-copilot/`](dist/gemini-copilot): open a file and select **Download raw file**.
2. In Cowork, select **+**, then **Customize**.
3. Open the **Skills** tab.
4. Select the arrow next to **Add**, then **Upload skill**, and choose the file.

Cowork picks the right skill up automatically when what you ask matches it.

**All seven at once:** download [`dist/all-skills.zip`](dist/all-skills.zip), unpack it, and drop the seven folders into your OneDrive under `Documents / Cowork / skills`. Cowork picks them up at the start of your next session.

### For everyone, through your admin

Your admin can deploy the skills to the whole organisation, or to a chosen group, so nobody installs anything. Send them the Humantic AI Sales Skills admin guide, which your Humantic AI contact can supply.

**Microsoft 365 Copilot Chat**, the ordinary Copilot without Cowork, has no way for a person to add a skill. Use the paste method below, or ask your admin about the agent routes in the admin guide.

---

## No install: paste the skill into a chat

Good for trying one skill, or for any assistant not listed above. It lasts for that conversation only.

**If your assistant can open a link** (Claude with web search on, and usually ChatGPT):

```text
Read
https://raw.githubusercontent.com/humantic-ai-inc/sales-skills/main/skills/meeting-prep/SKILL.md
and follow those instructions for the rest of this conversation.
Reply with one line to confirm, then ask me for what you need.
```

Swap `meeting-prep` for any skill name: `buyer-read`, `pursuit-plan`, `prospecting`, `sales-email`, `buying-committee`, `expansion-play`.

**If it cannot open a link** (Gemini, and Copilot Chat), paste the skill itself:

```text
Below is a skill definition. Follow it for the rest of this conversation.
Reply with one line to confirm, then ask me for what you need.

[open the skill in the skills folder of this repo, copy everything,
and paste it here]
```

---

## Check it worked

Ask this, with a real colleague who is happy to be the test:

```text
Prep me for my meeting with [their LinkedIn URL] at [their company]
tomorrow. The goal is to book a second meeting with their manager.
```

A working skill comes back with the outcome the meeting has to produce and a fallback, a short read on the person, what changed at their company, two to four questions, the objection to expect, and the ask. A generic answer with none of that means the skill did not load.

---

## Trouble

**Claude says the upload is not a skill.** Use the file from `dist/claude/`, not one you zipped yourself. Claude expects the skill's folder inside the file.

**Gemini or Copilot rejects the file.** Use the file from `dist/gemini-copilot/`. Those two expect the skill file at the top level.

**The skill installed but never runs.** Say what you want in plain language rather than naming the skill, for example "prep me for my meeting with Acme". If it still does not fire, type `/` and pick it by name where your assistant supports that.

**The answers have no Humantic AI research in them.** The skills run without Humantic AI, they just have less to work with. Connect it with [SETUP.md](SETUP.md).

**Something here does not match your screen.** These assistants change their menus often. Tell your Humantic AI contact and we will fix the page.
