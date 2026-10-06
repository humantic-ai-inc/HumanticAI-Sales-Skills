# Install in Microsoft Copilot

"Copilot" is several different products. Find yours first.

[Back to all assistants](../../INSTALL.md)

| You use | Best route | You get |
| :--- | :--- | :--- |
| **Copilot Cowork** (Microsoft 365 Copilot) | [Upload the plugin](#copilot-cowork) | All seven, in one upload |
| You are a **Microsoft 365 admin** | [Deploy the plugin to everyone](#for-your-whole-organisation-admin) | All seven, for everyone or a group |
| **Copilot Chat**, with Agent Builder | [Build an agent with the skills](#copilot-chat-agent-builder) | All seven inside one agent |
| **Copilot Chat**, without Agent Builder | [Use them in a chat](#copilot-chat-in-one-chat) | Works now, no install |
| **GitHub Copilot** (CLI or VS Code) | [Install from the repo](#github-copilot) | All seven, in one command |

---

## Copilot Cowork

You need a Microsoft 365 Copilot licence, and your admin needs to have switched Cowork on for you.

1. Download [humantic-sales-skills-copilot.zip](https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills/raw/main/dist/humantic-sales-skills-copilot.zip). Do not unzip it.
2. In Cowork, select **+**, then **Customize**.
3. Open the **Plugins** tab.
4. Select **Upload plugin**. Choose the file.
5. When asked who can use it, choose **Only you**, then **Apply**.

That installs all seven skills. Cowork uses the right one when what you ask matches it.

Want it for colleagues too? In step 5 choose **Specific users in your organization**. Sharing with the whole organisation needs your admin to approve it.

**One skill at a time instead:** open **Customize**, then **Skills**. Select the arrow next to **Add**, then **Upload skill**, and choose a file from [dist/one-skill/chatgpt-copilot-gemini](../../dist/one-skill/chatgpt-copilot-gemini).

Custom plugins do not work in Cowork on mobile yet.

---

## For your whole organisation (admin)

This puts all seven skills in front of everyone, with nothing for them to install.

1. Download [humantic-sales-skills-copilot.zip](https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills/raw/main/dist/humantic-sales-skills-copilot.zip).
2. Open the Microsoft 365 admin center at admin.microsoft.com.
3. Go to **Agents**, then **Tools**, then **Registry**.
4. Select **Upload** and choose the file. Review it and select **Next**.
5. Under **Scope users**, choose **All users** or **Specific users or groups**. Select **Install**.

People see it labelled **Managed by your organization**, and it stays installed for them.

**Check Cowork is switched on.** Cowork is off until an admin turns it on. Under **Copilot**, **Cost Management**, **Configuration**, users need to be in a spending policy that includes Cowork.

---

## Copilot Chat: Agent Builder

Skills in Agent Builder are in preview. They are only available to organisations in Microsoft's Frontier programme. One agent holds up to eight skills, so all seven fit.

1. In Copilot Chat, open **Agents & Skills**, then **New agent**.
2. Name it, for example "Sales Skills".
3. On the **Configure** tab, open **Skills** and select **Add**.
4. Upload one file from [dist/one-skill/chatgpt-copilot-gemini](../../dist/one-skill/chatgpt-copilot-gemini). Do not upload the SKILL.md file on its own.
5. Repeat for each of the seven skills.
6. Test it on the **Try it** tab, then select **Create**.

To give it to your team, use **Share**, then **Copy chat link**.

---

## Copilot Chat: in one chat

Copilot Chat cannot reliably open links, so paste the skill itself:

```text
Below is a skill definition. Follow it for the rest of this conversation.
Reply with one line to confirm, then ask me what you are working on.

[open a skill in the skills folder of this repo, copy all of it,
and paste it here]
```

This lasts for that chat only. For something that sticks, ask your admin about the plugin above.

---

## GitHub Copilot

### Copilot CLI

```text
copilot plugin marketplace add humantic-ai-inc/HumanticAI-Sales-Skills
copilot plugin install humantic-sales-skills@humantic-ai
```

Copilot confirms "Installed 7 skills".

### VS Code

1. Open the Command Palette.
2. Run **Chat: Install Plugin From Source**.
3. Paste `https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills`.

The `chat.plugins.enabled` setting must be on.

---

## The Humantic AI connector

The plugin carries the seven skills. It does not connect Humantic AI itself. The skills work without it, and get much sharper with it.

To connect Humantic AI to Copilot, follow the Microsoft Copilot setup guide your Humantic AI contact can send you. It covers Copilot Studio and the admin steps.

---

## Next

Check it worked: ask "prep me for my meeting with [a colleague's LinkedIn URL] tomorrow". You should get the meeting outcome, a read on the person, questions to ask and the ask. A generic answer means the skill did not load.
