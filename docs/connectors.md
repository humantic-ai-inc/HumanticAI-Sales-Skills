# Using your other connected tools

Humantic tells you about **people and companies**. Your own tools tell you about **this deal**. The prompts in this library are written to use both when both are there.

[Back to the prompt index](../prompts/README.md)

## How every prompt behaves

Each prompt follows the same three-step rule, so you never have to think about what is connected and what is not.

1. **Use what is connected.** If your assistant can already see your calendar, mail, CRM or meeting notes, it should use them without being asked.
2. **Ask for what is missing, once.** If something would clearly improve the answer and is not available, the assistant should tell you what would help and offer to take it as a paste.
3. **Answer anyway.** If you have nothing to add, or do not want to share it, you still get the best read Humantic alone can give. No prompt should refuse to work because a connector is absent.

You never need a connector to use this library. They make good answers better, not possible.

## What each connector adds

| If you have this connected | It adds | Most useful in |
| :--- | :--- | :--- |
| **Calendar** (Outlook, Google Calendar) | Who you are actually meeting, and when | Meeting preparation. Section 02, and prompt 47 |
| **Email** (Outlook, Gmail) | The real thread, so you stop pasting it | Outreach and follow-ups. Section 04 |
| **CRM** (Salesforce, HubSpot, Dynamics) | Deal stage, history, contact roles, past notes, open opportunities | Deal briefings, account plans, pipeline review. Sections 07 and 08 |
| **Meeting notetaker** (Gong, Fathom, Grain, Otter, Fireflies) | What was actually said: objections raised, commitments made, who spoke | Follow-ups, coaching, committee reads. Sections 03, 04 and 08 |
| **Document store** (SharePoint, Google Drive, OneDrive, Notion, Confluence) | Past proposals, decks, account plans, mutual action plans | Account research and proposal checks. Sections 05 and 07 |
| **Team chat** (Teams, Slack) | What colleagues already know about this account | Account research and handovers. Sections 05 and 07 |
| **Support or ticketing** (Zendesk, Jira, ServiceNow) | Open issues that will surface in a renewal conversation | Renewal and QBR preparation. Prompts 10 and 40 |

## Turning any prompt into a connector-aware one

If you want to be explicit, append this to any prompt in the library:

```text
Use anything you can see in my calendar, email, CRM, meeting notes and
files to make this more specific. If something important is missing,
tell me what would help and I will paste it. If I cannot, give me your
best answer from what you have.
```

That one line makes the three-step rule explicit for assistants that would otherwise stick to Humantic alone.

## Supplying context by hand

No connectors, or not allowed to connect them? Paste instead. These are the four things that improve an answer most, in order:

1. **The last message or two** from the thread, for anything about outreach
2. **Notes from your last call**, for anything about a person or a committee
3. **The deal stage and what is blocking it**, for anything about the deal
4. **The role each person plays** in the decision, for anything about a committee

A pasted paragraph of call notes usually changes the answer more than any single connector does.
