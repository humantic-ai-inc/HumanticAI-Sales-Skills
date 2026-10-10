# Install in Claude

All seven skills install together as one plugin, called **Sales Skills by Humantic AI**. No GitHub account is needed.

[Back to all assistants](../../INSTALL.md)

---

## Fastest: ask Claude to do it

1. Open Claude and start a new chat.
2. Copy the block below with the copy button at its top right.
3. Paste it into the chat and send it.

```text
Install the Humantic AI sales skills from
https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills

Check that repo, add it as a plugin marketplace, and install the
humantic-sales-skills plugin so all seven skills are available to me.
Then list the seven skill names and tell me one thing each is good for.

If you cannot install it yourself here, say so and walk me through
doing it, one step at a time.
```

4. Claude reads the repo and installs the plugin. When it is done, it lists the seven skill names.
5. If Claude says it cannot install it for you, follow the menu steps below instead.

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

1. Download the skill you want from [dist/one-skill/claude](../../dist/one-skill/claude). Open the file, then select **Download raw file**.
2. In Claude, open **Customize**, then **Skills**.
3. Select **+**, then **Create skill**, then **Upload a skill**. Choose the file.
4. Find the skill under **Your skills** and select **Turn on**.

**If you cannot see Skills in step 2:**

1. Open **Settings**, then **Capabilities**.
2. Switch on **Code execution and file creation**.
3. Go back to step 2 above.

On Team and Enterprise, an Owner switches this on for everyone under **Organization settings**, **Capabilities**.

---

## Staying up to date

**If you installed the plugin:**

1. Open **Customize**, then **Plugins**.
2. Find **Sales Skills** and remove it.
3. Add it again with the steps in "From the menu" above. You get the latest version.

In Claude Code, run `/plugin`, open **Marketplaces**, select **humantic-ai**, then **Update**.

**If you uploaded single skill files:**

1. Download the skill again from [dist/one-skill/claude](../../dist/one-skill/claude).
2. Open **Customize**, then **Skills**, and remove the old copy.
3. Upload the new file, as in "One skill at a time" above.

You never need a GitHub login. The **Sync from GitHub** option in organisation settings is for private company repos, so skip it.

---

## Check it worked

1. Connect Humantic AI first, if you have not: follow [the setup guide](../setup-humantic.md).
2. Start a new chat.
3. Type: `Prep me for my meeting with [a colleague's LinkedIn URL] tomorrow.`
4. Send it.

**It worked if** you get the meeting outcome, a read on the person, questions to ask and the ask. **It did not work if** you get a general answer with none of that. Go back over the steps above.
