# Sales Skills

Prompts for sellers using Humantic AI through an AI assistant. Built for **Microsoft Copilot**, **Claude** and **ChatGPT**.

Every prompt here is written to be pasted as-is. Swap in the bracketed detail and send. No prompt asks you to know a tool name, a parameter, or what DISC stands for.

Each prompt sits in a grey box. Hover over the box and a **copy button** appears in its top-right corner: click it, paste into your assistant, then replace anything in [square brackets] with the real name or company. The line breaks you see in the box do not matter, paste them as they are.

## Skills

Seven installable skills that turn the prompts below into complete workflows. You ask in your own words, for example "prep me for my meeting with Acme tomorrow", and the matching skill takes over.

| Skill | What it does |
| :--- | :--- |
| [buyer-read](skills/buyer-read/) | How one person communicates, what drives them, and how to approach them |
| [meeting-prep](skills/meeting-prep/) | A one-page brief built around what the meeting has to produce |
| [pursuit-plan](skills/pursuit-plan/) | A plan for winning one named account |
| [prospecting](skills/prospecting/) | Who to work this week, with a reason attached to every name |
| [sales-email](skills/sales-email/) | Emails matched to the person reading them |
| [buying-committee](skills/buying-committee/) | Maps the people who decide and how to move them as a group |
| [expansion-play](skills/expansion-play/) | What an existing customer should buy next, and when to ask |

### Install them

Pick your assistant. Each guide has a copy-paste route and step-by-step instructions.

| Assistant | Guide | The short version |
| :--- | :--- | :--- |
| **Claude** | [INSTALL-CLAUDE.md](INSTALL-CLAUDE.md) | Paste the prompt below into Claude. All seven install together |
| **ChatGPT** | [INSTALL-CHATGPT.md](INSTALL-CHATGPT.md) | Your workspace admin imports this repo, or add it in the desktop app. All seven together |
| **Microsoft Copilot** | [INSTALL-COPILOT.md](INSTALL-COPILOT.md) | Upload [one plugin file](https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills/raw/main/dist/humantic-sales-skills-copilot.zip) in Cowork, or your admin deploys it. All seven together |
| **Gemini, or anything else** | [INSTALL.md](INSTALL.md) | Upload one at a time, or paste into a chat |

**Claude**, in one step. Paste this into a chat:

```text
Install the Humantic AI sales skills from
https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills

Check that repo, add it as a plugin marketplace, and install the
humantic-sales-skills plugin so all seven skills are available to me.
Then list the seven skill names.
```

**ChatGPT workspace admin**, in one step: open **Admin**, **Plugins**, **Add**, **Import marketplace**, and paste the repo URL above.

**Microsoft Copilot Cowork**, in one step: download [humantic-sales-skills-copilot.zip](https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills/raw/main/dist/humantic-sales-skills-copilot.zip), then in Cowork open **+**, **Customize**, **Plugins**, **Upload plugin**.

**Just want to try them?** Paste this into any assistant that can open links. All seven work for that chat:

```text
Read
https://raw.githubusercontent.com/humantic-ai-inc/HumanticAI-Sales-Skills/main/INSTALL.md
then load the seven skills listed under "Any assistant: paste into a
chat" and use them for the rest of this conversation. Tell me which
skill you used each time. List the seven names, then ask me what I am
working on.
```

First time with Humantic AI in your assistant? Connect it first with [SETUP.md](SETUP.md).

## Prompts

**New here? Start with [SETUP.md](SETUP.md)** to connect Humantic to your assistant, then come back to the index below.

## How to use these

**One identifier per person.** Give a LinkedIn URL *or* an email, never both in the same request. There is no linking step, so if you want both to work later, ask for each separately.

**Ask for the format you want.** If you want something you can share or print, say so in the prompt rather than relying on the default.

**Your other tools make these better, and none of them are required.** If your assistant can see your calendar, mail, CRM, meeting notes or files, these prompts use them. If it cannot, it asks you for what would help. If you would rather not share anything, you still get the best read Humantic alone can give. See [CONNECTORS.md](CONNECTORS.md) for what each connector adds and where.

## Index

| Section | Prompts | What it covers |
| :--- | :--- | :--- |
| [01 - Know a person](01-know-a-person.md) | 1 to 6 | Build a read on one individual, fix a thin profile, bring a stale one up to date |
| [02 - Prepare for a meeting](02-prepare-for-a-meeting.md) | 7 to 11 | Walk into the room knowing how each person in it wants to be talked to |
| [03 - Navigate a buying committee](03-buying-committee.md) | 12 to 17 | Several stakeholders, one deal. Who moves fast, who blocks, who to approach first |
| [04 - Write outreach](04-write-outreach.md) | 18 to 24 | First emails, replies, follow-ups, and several threads running at once |
| [05 - Research an account](05-research-an-account.md) | 25 to 31 | Company intelligence, pulled a section at a time rather than as a wall of text |
| [06 - Buyer-intent signals](06-buyer-signals.md) | 32 to 36 | What changed, on which account, and what to do about it |
| [07 - Run the deal and hand it over](07-deal-handover.md) | 37 to 41 | Full briefings, account plans, handovers, re-engagement |
| [08 - For sales managers](08-for-sales-managers.md) | 42 to 46 | Coaching, deal review and team preparation |
| [09 - Combine Humantic with your other tools](09-connected-tools.md) | 47 to 51 | Calendar, mail, CRM, meeting notes and files, chained with Humantic |
| [10 - Keep the data honest](10-keep-data-honest.md) | 52 to 55 | Feedback prompts that improve what everyone gets back |
| [INSTALL.md](INSTALL.md) | - | Pick your assistant, plus Gemini and paste-into-a-chat |
| [INSTALL-CLAUDE.md](INSTALL-CLAUDE.md) | - | Install the skills in Claude |
| [INSTALL-CHATGPT.md](INSTALL-CHATGPT.md) | - | Install the skills in ChatGPT and Codex |
| [INSTALL-COPILOT.md](INSTALL-COPILOT.md) | - | Install the skills in Microsoft Copilot and GitHub Copilot |
| [SETUP.md](SETUP.md) | - | How to connect Humantic AI to your assistant |
| [CONNECTORS.md](CONNECTORS.md) | - | What each connected tool adds, and how to supply context by hand |
| [TOOLS.md](TOOLS.md) | - | Plain-language reference for what sits behind these prompts |

## Two things to know before you rely on this

**A personality read is a guide, not a verdict.** It tells you how to approach someone. It does not tell you whether a deal will close, and it belongs alongside what you already know rather than in place of it. This matters most in the buying-committee prompts, where the value is in spotting a pattern worth checking rather than in treating the read as settled.

**Section 09 needs at least one other tool connected.** Those prompts combine Humantic with your calendar, mail, CRM or files, so they depend on what your assistant can reach. Everything in sections 01 to 08 and 10 works with Humantic alone.
