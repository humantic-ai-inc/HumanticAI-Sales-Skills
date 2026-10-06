# Sales Skills by Humantic AI

Seven sales skills for Claude, ChatGPT and Microsoft Copilot. You ask in your own words, for example "prep me for my meeting with Acme tomorrow", and the right skill does the work.

Every skill works on its own. Each one gets much sharper when Humantic AI is connected to your assistant.

## The seven skills

| Skill | What it does for you |
| :--- | :--- |
| [buyer-read](skills/buyer-read/) | How one person communicates, what drives them, and how to approach them |
| [meeting-prep](skills/meeting-prep/) | A one-page brief built around what the meeting has to produce |
| [pursuit-plan](skills/pursuit-plan/) | A plan for winning one named account |
| [prospecting](skills/prospecting/) | Who to work this week, with a reason attached to every name |
| [sales-email](skills/sales-email/) | Emails matched to the person reading them |
| [buying-committee](skills/buying-committee/) | Maps the people who decide and how to move them as a group |
| [expansion-play](skills/expansion-play/) | What an existing customer should buy next, and when to ask |

## Install

All seven install together. Pick your assistant.

| Assistant | Quickest route | Full guide |
| :--- | :--- | :--- |
| **Claude** | Paste the prompt below into a chat | [Claude guide](docs/install/claude.md) |
| **ChatGPT** | Your workspace admin imports this repo under **Admin**, **Plugins**, **Import marketplace** | [ChatGPT guide](docs/install/chatgpt.md) |
| **Microsoft Copilot** | Upload [this one file](https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills/raw/main/dist/humantic-sales-skills-copilot.zip) in Cowork under **Customize**, **Plugins** | [Copilot guide](docs/install/copilot.md) |
| **Gemini, or anything else** | Upload one at a time, or paste into a chat | [All assistants](INSTALL.md) |

**Claude, in one step.** Paste this into a chat:

```text
Install the Humantic AI sales skills from
https://github.com/humantic-ai-inc/HumanticAI-Sales-Skills

Check that repo, add it as a plugin marketplace, and install the
humantic-sales-skills plugin so all seven skills are available to me.
Then list the seven skill names.
```

**Just want to try them first?** Paste this into any assistant that can open links. All seven work for that chat:

```text
Read
https://raw.githubusercontent.com/humantic-ai-inc/HumanticAI-Sales-Skills/main/INSTALL.md
then load the seven skills listed under "Any assistant: paste into a
chat" and use them for the rest of this conversation. Tell me which
skill you used each time. List the seven names, then ask me what I am
working on.
```

## Connect Humantic AI

The skills use Humantic AI for the read on each person, the account research and the buying signals. Connect it once with the [setup guide](docs/setup-humantic.md).

## Prefer single prompts?

The [prompt library](prompts/README.md) has 55 ready-to-paste prompts, one request each. Use it when you want one quick answer rather than a full workflow.

## What is where

| Folder | What is in it |
| :--- | :--- |
| `skills/` | The seven skills |
| `prompts/` | The prompt library |
| `docs/` | Install guides, the Humantic AI setup guide, and reference pages |
| `dist/` | Ready-made downloads: one plugin file per assistant, and single skills |
| `packaging/` | The Microsoft Copilot and OpenAI plugin files and icons |
| `templates/` | The starting point for a new skill |
| `scripts/` | Checks the skills and builds the downloads |

The Claude plugin lives in `.claude-plugin/` and the OpenAI plugin in `plugin.json` and `.agents/plugins/`. Those stay at the top because Claude, ChatGPT, Codex and GitHub Copilot look for them there.

## Two things to know

**A personality read is a guide, not a verdict.** It tells you how to approach someone. It does not tell you whether a deal will close.

**Nothing is sent for you.** The skills draft emails and plans. You decide what goes out.

---

Want to add or change a skill? See [CONTRIBUTING.md](CONTRIBUTING.md). What changed in each version is in [CHANGELOG.md](CHANGELOG.md).

[MIT licence](LICENSE). Copyright Humantic AI.
