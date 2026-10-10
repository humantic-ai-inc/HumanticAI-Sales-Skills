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

1. Open [humantic-sales-skills-copilot.zip](https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills/raw/main/dist/humantic-sales-skills-copilot.zip). It downloads straight away. Do not unzip it.
2. In Cowork, select **+**, then **Customize**.
3. Open the **Plugins** tab.
4. Select **Upload plugin**. Choose the file.
5. When asked who can use it, choose **Only you**, then **Apply**.

6. **Sales Skills** now shows in the **Plugins** tab. In a new Cowork session, ask for what you need, for example `prep me for my meeting with Acme tomorrow`.

**To share it with colleagues:**

1. Open **+**, then **Customize**, then **Plugins**.
2. Open **Sales Skills** and select **Share**.
3. Choose **Specific users in your organization** and add their names.
4. Select **Apply**.

Sharing with the whole organisation needs your admin to approve it.

**To add one skill at a time instead:**

1. Download the skill from [dist/one-skill/chatgpt-copilot-gemini](../../dist/one-skill/chatgpt-copilot-gemini). Open the file, then select **Download raw file**.
2. In Cowork, select **+**, then **Customize**.
3. Open the **Skills** tab.
4. Select the arrow next to **Add**, then **Upload skill**.
5. Choose the file.

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

**Then check Cowork is switched on for those people.** Cowork is off until an admin turns it on.

1. In the Microsoft 365 admin center, open **Copilot**.
2. Go to **Cost Management**, then **Configuration**.
3. Select **+ Add spending policy**, or open the policy you already have.
4. Include Cowork, and add the same users or groups you chose in step 5 above.
5. Save the policy.

---

## Copilot Chat: Agent Builder

Skills in Agent Builder are in preview. They are only available to organisations in Microsoft's Frontier programme. One agent holds up to eight skills, so all seven fit.

1. In Copilot Chat, open **Agents & Skills**, then **New agent**.
2. Name it, for example "Sales Skills".
3. On the **Configure** tab, open **Skills** and select **Add**.
4. Upload one file from [dist/one-skill/chatgpt-copilot-gemini](../../dist/one-skill/chatgpt-copilot-gemini). Do not upload the SKILL.md file on its own.
5. Repeat for each of the seven skills.
6. Test it on the **Try it** tab, then select **Create**.

**To give the agent to your team:**

1. Open the agent and select **Share**.
2. Select **Copy chat link**.
3. Send the link to your team. They open it and start chatting.

---

## Copilot Chat: in one chat

Copilot Chat cannot reliably open links, so you paste the skill itself.

1. Open the skill you want in the [skills](../../skills) folder, then open its `SKILL.md`.
2. Select the **Copy raw file** button at the top right of the file.
3. Start a new Copilot Chat.
4. Type the two lines in the block below, then paste the skill underneath them.
5. Send it. Copilot confirms in one line. Now ask for what you need.

```text
Below is a skill definition. Follow it for the rest of this conversation.
Reply with one line to confirm, then ask me what you are working on.

[open a skill in the skills folder of this repo, copy all of it,
and paste it here]
```

This lasts for that chat only. For something that sticks, send your admin the "For your whole organisation" steps above.

---

## GitHub Copilot

### Copilot CLI

1. Open **Terminal** on a Mac, or **PowerShell** on Windows.
2. Paste these two lines and press Enter:

```text
copilot plugin marketplace add humantic-ai-inc/HumanticAI-Sales-Skills
copilot plugin install humantic-sales-skills@humantic-ai
```

3. You should see `Installed 7 skills`.

### VS Code

1. Open **Settings**, search for `chat.plugins.enabled`, and tick it.
2. Open the Command Palette: **Cmd+Shift+P** on a Mac, **Ctrl+Shift+P** on Windows.
3. Type `Chat: Install Plugin From Source` and press Enter.
4. Paste `https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills` and press Enter.

---

## The Humantic AI connector

The plugin carries the seven skills. It does not connect Humantic AI itself. The skills work without it, and get much sharper with it.

To connect Humantic AI to Copilot, follow the Microsoft Copilot steps in [the setup guide](../setup-humantic.md#microsoft-copilot).

---

## Check it worked

1. Start a new chat or Cowork session.
2. Type: `Prep me for my meeting with [a colleague's LinkedIn URL] tomorrow.`
3. Send it.

**It worked if** you get the meeting outcome, a read on the person, questions to ask and the ask. **It did not work if** you get a general answer with none of that. Go back over the steps above.
