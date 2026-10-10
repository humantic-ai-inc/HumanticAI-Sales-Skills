# Connect Humantic AI to your assistant

Do this once. After that, every skill and every prompt in this repo can use Humantic AI.

[Back to the repo home](../README.md)

**This page connects Humantic AI.** To install the seven sales skills, use [INSTALL.md](../INSTALL.md). Do this page first.

**What you need:** a Humantic AI account. When the sign-in window opens, you sign in with that account.

**The server address** you paste in every step below:

```text
https://mcp.humantic.ai/mcp
```

Steps checked in October 2026. If a screen does not match, tell your Humantic AI contact.

---

## Claude

Works on every Claude plan. On the Free plan you can add one custom connector.

### On your own account (Free, Pro or Max)

1. Open Claude on the web or in the desktop app.
2. In the left sidebar, select **Customize**.
3. Open **Connectors**.
4. Select **+ Add**, then **Add custom connector**.
5. In the name box, type `Humantic AI`.
6. In the server URL box, paste `https://mcp.humantic.ai/mcp`. Select **Continue**.
7. Claude shows the settings it found. Select **Continue**.
8. Under **Authentication**, choose **Sign in now**.
9. Under **OAuth client**, choose **Register automatically**.
10. Select **Add**.
11. A Humantic AI sign-in window opens. Sign in and select **Approve**.

You are done when **Humantic AI** shows in your list under **Customize**, **Connectors**.

### On a Team or Enterprise plan

Only an Owner can add the connector. They do it once for everyone.

**The Owner:**

1. Open **Organization settings**, then **Connectors**.
2. Select **Add**. Hover over **Custom**, then select **Web**.
3. In the name box, type `Humantic AI`.
4. In the server URL box, paste `https://mcp.humantic.ai/mcp`. Select **Continue**.
5. Select **Continue** again on the settings Claude found.
6. Under **Authentication**, choose **Sign in now**.
7. Under **OAuth client**, choose **Register automatically**.
8. Select **Add**.

**Then each person on the team:**

1. In the left sidebar, select **Customize**, then **Connectors**.
2. Find **Humantic AI**. It has a **Custom** label.
3. Select **Connect**.
4. Sign in to Humantic AI and select **Approve**.

### Turn it on in a chat

1. Start a new chat.
2. Select the **+** button at the bottom left of the message box.
3. Hover over **Connectors**.
4. Switch **Humantic AI** on.

The first time Claude uses a Humantic AI tool, it asks your permission. Select **Always allow** so it stops asking.

**Check it worked:** type `What Humantic AI tools do you have?` Claude lists them by name.

---

## ChatGPT

Custom connectors are on ChatGPT **Business, Enterprise and Edu**, on the web. On Business, only an admin or owner can add one. ChatGPT needs the Humantic AI sign-in, so you never paste a key.

### The admin adds it

1. Go to chatgpt.com on a computer.
2. In the sidebar, select **Plugins**.
3. Select the **+** button, then **Add custom MCP server**.
4. In the name box, type `Humantic AI`.
5. Under **Connection**, choose **Server URL** and paste `https://mcp.humantic.ai/mcp`.
6. Under **Authentication**, choose **OAuth**.
7. Read the warning and select **I understand and want to continue**.
8. Select **Create as a plugin**.
9. A Humantic AI sign-in window opens. Sign in and select **Approve**.
10. ChatGPT lists the Humantic AI tools it found. Check the list is there.

**If you do not see "Add custom MCP server" in step 3,** your workspace uses the older screen:

1. Open **Settings**, then **Apps**, then **Advanced settings**.
2. Switch on **Developer mode**.
3. Go back to **Settings**, then **Apps**, and select **Create**.
4. Paste `https://mcp.humantic.ai/mcp` as the server address and choose **OAuth**.
5. Sign in to Humantic AI when the window opens.
6. Select **Scan Tools**, wait for the list, then select **Create**.

### Share it with the workspace

1. In the sidebar, select **Plugins**.
2. Open **Humantic AI**.
3. Select the **•••** menu, then **Share plugin**.
4. Under **Who has access**, choose **Visible in workspace directory**.
5. Select **Save**.

On the older screen, go to **Workspace settings**, **Apps**, **Drafts**, open Humantic AI and select **Publish**.

### Each person connects it

1. In the sidebar, select **Plugins**.
2. Open **Humantic AI** and select **Install plugin**.
3. Select **Connect**, sign in to Humantic AI and select **Approve**.

### Use it in a chat

1. Start a new chat.
2. Type `@` and select **Humantic AI**.
3. Type your question.

**Check it worked:** type `@Humantic AI what tools do you have?` ChatGPT lists them.

---

## Microsoft Copilot

Copilot connects through a Copilot Studio agent. The full guide, with screens for the admin, is the **Humantic AI on Microsoft Copilot setup guide**. Ask your Humantic AI contact for it. The short version for the person building the agent:

1. Open **Copilot Studio** and open your agent, or create one called `Humantic AI`.
2. Go to **Tools**.
3. Select **Add a tool**, then **New tool**, then **Model Context Protocol**.
4. In **Server name**, type `Humantic AI`.
5. In **Server description**, paste:

```text
Buyer intelligence. Personality profiles for individual prospects,
account research reports on target companies, buyer-intent signals,
and outreach personalised to the recipient.
```

6. In **Server URL**, paste `https://mcp.humantic.ai/mcp`.
7. Under **Authentication**, choose **OAuth 2.0**, then **Dynamic discovery**.
8. Select **Create**, then **Add to agent**.
9. Go to **Settings**, **Security**, **Authentication**, and check **Authenticate with Microsoft** is selected.
10. Go to **Channels**, open **Teams and Microsoft 365 Copilot**, tick **Make agent available in Microsoft 365 Copilot**, and select **Add channel**.

The first time each person uses the agent, Copilot shows a **Connect** card in the chat. They select it and sign in to Humantic AI once.

---

## Troubleshooting

**"It cannot find any Humantic AI tools."** The sign-in did not finish.

1. Go back to the connector or plugin list.
2. Remove Humantic AI.
3. Add it again, and finish the sign-in window before closing it.

**"Nothing comes back and there is no error."** Your company network may be blocking the server.

1. Send IT this address: `https://mcp.humantic.ai/mcp`.
2. Ask them to allow it through web filtering.

**"It returns a profile of the wrong person."**

1. Open [prompt 52 in Keep the data honest](../prompts/10-keep-data-honest.md).
2. Copy it, add the right LinkedIn URL, and send it.

**"The profile came back thin."**

1. Open [prompt 3 in Know a person](../prompts/01-know-a-person.md).
2. Copy it, paste in a bio, a recent post or your call notes, and send it.

**"A file download was refused."**

1. Ask again, and add `show it in the chat` to the end of your message.
