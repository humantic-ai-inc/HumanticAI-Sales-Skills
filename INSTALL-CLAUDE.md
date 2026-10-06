# Install in Claude

All seven skills install together as one plugin, called **Sales Skills by Humantic AI**. No GitHub account is needed.

[Back to all assistants](INSTALL.md)

---

## Fastest: ask Claude to do it

Paste this into a Claude chat:

```text
Install the Humantic AI sales skills from
https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills

Check that repo, add it as a plugin marketplace, and install the
humantic-sales-skills plugin so all seven skills are available to me.
Then list the seven skill names and tell me one thing each is good for.

If you cannot install it yourself here, say so and walk me through
doing it, one step at a time.
```

Claude reads the repo and installs all seven. If your version of Claude cannot install things for you, it walks you through the menu steps below.

---

## From the menu

1. In the left sidebar, open **Customize**.
2. Open the **Plugins** tab.
3. Select **Add**, then **Add marketplace**.
4. Type `humantic-ai-inc/HumanticAI-Sales-Skills` and confirm.
5. Find **Sales Skills** in the list and select **Add**.

---

## In Claude Code

```text
/plugin marketplace add humantic-ai-inc/HumanticAI-Sales-Skills
/plugin install humantic-sales-skills@humantic-ai
```

---

## For your whole team

An Owner on a Team or Enterprise plan can install the set for everyone.

1. Download [humantic-sales-skills-claude.zip](https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills/raw/main/dist/humantic-sales-skills-claude.zip).
2. Open **Organization settings**, then **Plugins & skills**.
3. Select **Add**, then upload the file.
4. Set it to **Installed by default**, so everyone has it without doing anything.

---

## One skill at a time

Use this if you only want one skill, or your plan does not show **Plugins**.

1. Download the skill you want from [dist/claude](dist/claude). Open the file, then select **Download raw file**.
2. In Claude, open **Customize**, then **Skills**.
3. Select **+**, then **Create skill**, then **Upload a skill**. Choose the file.
4. Turn the skill on.

Skills need code execution. If you cannot see the option, open **Settings**, then **Capabilities**, and turn on **Code execution and file creation**.

---

## Staying up to date

- **Installed as a plugin:** you get the latest version when you add or refresh the marketplace. You never need a GitHub login.
- **Uploaded as a file:** that copy stays as it is. To update it, download the file again and upload it again.
- The "Sync from GitHub" option in organisation settings is a different feature, for private company repos. You do not need it.

---

## Next

- Connect Humantic AI so the skills can use it: [SETUP.md](SETUP.md).
- Check it worked: ask "prep me for my meeting with [a colleague's LinkedIn URL] tomorrow". You should get the meeting outcome, a read on the person, questions to ask and the ask. A generic answer means the skill did not load.
