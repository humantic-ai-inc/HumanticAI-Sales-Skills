# What sits behind these prompts

You do not need this to use the library. It is here for people who want to know what is actually running, and for anyone writing their own prompts.

[Back to the prompt index](../prompts/README.md)

Humantic exposes three families of capability through the MCP server.

## Personality profiling

Builds and reads a behavioural profile for one individual from public information.

| What it does | Notes |
| :--- | :--- |
| Build a profile | Takes exactly one identifier: a LinkedIn URL, an email, or free text. Never two at once |
| Read an existing profile | Several output formats. Ask for the one you want rather than accepting the default |
| Enrich a profile with text you supply | The fix for a thin or low-confidence profile |
| Rebuild a profile from current sources | The fix for someone who changed job. Different from enriching |
| Record feedback on a profile | Wrong person, accuracy, usefulness |

## Content personalisation

Generates or rewrites outreach matched to a recipient.

| Mode | What it needs |
| :--- | :--- |
| First-pitch email | A pain point and your own context, both at least a sentence |
| Rewrite an existing draft | The draft |
| Reply or follow-up | The earlier message in the thread |

It works without a pre-built profile, but building one first gives a faster and more confident result.

## Account intelligence and buyer-intent signals

| What it does | Notes |
| :--- | :--- |
| Build an account report | Runs in the background. Usually ready in about two minutes, sometimes fifteen to twenty |
| Check whether a report is ready | |
| Read a finished report | |
| List the sections of a report | |
| Pull specific sections | More readable than pulling the whole report. Prefer this |
| List every report you have | Check here before starting new research |
| Regenerate an existing report | The original stays available at its own reference |
| Buyer-intent signals for one account | Retains roughly the last 60 days, whatever window you request. The response states the window it used |
| Buyer-intent signals across all accounts | Returns in pages. Filter by company or impact at source rather than pulling everything |

## Writing your own prompts

Four rules, drawn from how these tools actually behave.

**Name the job, not the tool.** "Help me prepare for this meeting" works. "Call the profile tool" is brittle and makes the user learn your product.

**One identifier per person.** Two in the same request will fail.

**Ask for sections, not whole reports.** A full account report is long enough to be unreadable in a chat window. Named sections are not.

**Ask the assistant to say what it could not reach.** This is the single most useful line you can add to any prompt that touches several systems. Without it, a partial answer looks complete.
