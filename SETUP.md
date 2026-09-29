# Setup: connect Humantic AI to your assistant

**This page connects Humantic AI itself.** To install the seven sales skills, see [INSTALL.md](INSTALL.md). Do this page first, then that one.

Connect Humantic AI to your assistant once, then every skill and every prompt in this library works.

You will need your Humantic MCP endpoint and credentials from your Humantic account. If you do not have them, ask your Humantic contact or your internal admin.

---

## Claude

The quickest of the three. Claude accepts a remote MCP server directly.

1. Open **Settings**, then **Connectors**.
2. Choose **Add custom connector**.
3. Paste the Humantic MCP server URL.
4. Complete the sign-in when prompted.
5. Start a new chat and paste any prompt from this library.

**On Claude Team and Enterprise**, an Owner or Admin has to add the connector once at the organisation level before members can enable it. If you cannot see the option, that is why, and it is an admin action rather than a fault on your side.

**Check it worked:** ask Claude "what Humantic tools do you have available?" It should list them by name.

---

## ChatGPT

1. Open **Settings**.
2. Find the connector or plugin directory area.
3. Add the Humantic connector and complete sign-in.
4. Start a new chat and paste any prompt from this library.

**Note:** OpenAI has renamed this area more than once. If the menu path above does not match what you see, look for wherever third-party connectors or apps are managed in your version.

**Check it worked:** ask "what Humantic tools do you have available?"

---

## Microsoft Copilot

Copilot is the most involved of the three, because what you do depends on which Copilot your organisation runs.

### Which Copilot do you have?

| | Standard Copilot | Microsoft 365 Copilot |
| :--- | :--- | :--- |
| **Included with** | Most Microsoft 365 business plans | Paid add-on licence |
| **Can see** | Public web only | Your mail, chat, files and calendar |
| **Sections 01 to 08, 10** | Works | Works |
| **Section 09 chains** | Does not work | Works |

If you are unsure, ask your IT administrator which licence you hold.

### Route A: Teams sideload (recommended)

The packaged Humantic app, installed through the Teams Admin Center. This is the route that works most reliably.

1. Your Teams administrator uploads the Humantic app package in **Teams Admin Center**, under **Teams apps**, then **Manage apps**.
2. The admin approves it.
3. Users find Humantic in their Teams app list, or the admin pushes it to them.

### Route B: Copilot Studio custom agent

For organisations that already run a custom agent, or where sideloading is blocked.

1. In **Copilot Studio**, open your agent.
2. Add the Humantic MCP server as a **custom tool**, using the server URL and a bearer token.
3. Under **Settings**, then **Security**, then **Authentication**, choose how users authenticate.
4. Publish the agent.

**Two things for the administrator to be aware of on this route.**

Authentication mode decides who gets access and how usage is attributed. With a single shared credential, everyone using the agent reaches Humantic regardless of individual licensing, and all activity appears as one identity. Choose deliberately rather than by default.

To make it seamless for users, an Entra administrator can grant tenant-wide admin consent for the agent under **API Permissions** in the Entra Admin Center. This stops every user being asked individually to approve sharing their profile with the agent.

### Pushing it to everyone

An administrator can install and pin the agent for the whole organisation, or for one group, without users doing anything:

1. **Teams Admin Center**, then **Teams apps**, then **Setup policies**.
2. Select the Global (Org-wide default) policy, or create one targeting a specific group.
3. Add the agent under **Installed apps** so it installs silently.
4. Add it under **Pinned apps** so it appears in the Teams sidebar.

---

## Troubleshooting

**"It says it cannot find any Humantic tools."** The connection did not complete. Re-run the setup for your assistant and confirm the sign-in finished rather than timing out.

**"Nothing comes back and there is no error."** Often a network policy inside your organisation silently blocking the endpoint. Ask IT whether the Humantic MCP domain is allowed through your web filtering.

**"It returns a profile for the wrong person."** Use prompt 52 in [10 - Keep the data honest](10-keep-data-honest.md). Takes seconds, costs nothing, and improves the match for everyone.

**"The profile came back thin or with no personality read."** There was not enough public information. Use prompt 3 in [01 - Know a person](01-know-a-person.md) to add what you know.

**"A file download was refused."** Some assistants and some corporate networks block file downloads from third-party tools. Ask for the result in the chat window, or as a link, instead of as a file.
