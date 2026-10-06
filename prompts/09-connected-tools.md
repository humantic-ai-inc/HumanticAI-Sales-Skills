# 09 - Combine Humantic with your other tools

Humantic knows the person. Your own tools know the deal. These prompts use both.

[Back to the prompt index](README.md)

> **These need at least one other tool connected** to your assistant: calendar, mail, CRM, meeting notes or a document store. Which ones you have depends on your organisation. See [the connectors page](../docs/connectors.md).
>
> Each prompt still degrades gracefully. If a connector is missing, the assistant should tell you what would help and offer to take it as a paste, then answer with whatever it has.

---

## 47. Prepare for everyone on tomorrow's calendar

**When:** The flagship. You type nothing about any individual.

**Better with:** Calendar. Richer with CRM.

```text
Look at my calendar for tomorrow. For every external attendee in my
meetings, pull their Humantic profile and give me one briefing per
meeting: who is in the room, how each of them communicates, and what to
lead with. If you can also see the deal in our CRM, include where it
stands. If you cannot see my calendar, ask me for the attendee list
instead.
```

**What you get back:** A prepared day, without naming a single person yourself.

---

## 48. Read the last thread and draft the reply

**When:** Removes the copy-and-paste step from prompt 20.

**Better with:** Email. Richer with meeting notes.

```text
Find my most recent email thread with [Name or email], then write me a
reply matched to how they communicate, based on their Humantic profile.
If we have notes from a recent call with them, use those too. If you
cannot reach my mail, ask me to paste the thread.
```

**What you get back:** A reply drafted from the real thread rather than one you retyped.

---

## 49. Turn a call recording into a stakeholder read

**When:** You had the call, the notetaker captured it, and you want more than a summary.

**Better with:** Meeting notetaker (Gong, Fathom, Grain, Otter, Fireflies). Richer with CRM.

```text
Pull the notes or transcript from my most recent call with [company].
For each external person who spoke, pull their Humantic profile, then
tell me what each of them actually pushed on, how that fits their
communication style, and what I should do differently with each of them
next time. If no recording is available, I will paste my notes.
```

**What you get back:** What was said, read against who said it, which neither the transcript nor the profile gives you on its own.

---

## 50. Check a past proposal against current priorities

**When:** Useful to presales and bid teams more than to a rep.

**Better with:** Document store (SharePoint, Google Drive, Notion). Richer with CRM.

```text
Find our most recent proposal document for [company name], then pull the
Humantic research on that account and tell me where the proposal no
longer matches what they appear to care about now. If you cannot find
the document, ask me to upload it.
```

**What you get back:** A gap read between what you proposed and what they now want.

---

## 51. Build the account picture from everything available

**When:** Taking over an account, or going in properly for the first time.

**Better with:** CRM, team chat, meeting notes, document store. Any one of them helps.

```text
Build me the full picture on [company name]. Pull the Humantic account
research and buyer-intent signals. Then add whatever you can see from
our own systems: the CRM record and deal history, what colleagues have
said about this account in chat, notes from past calls, and any
proposals or plans on file. Tell me what we know, what has changed
recently, and where the gaps are. Name anything you could not reach so I
know what is missing.
```

**What you get back:** Internal knowledge and external intelligence in one answer, with the gaps named rather than papered over.

> The last sentence matters. Asking the assistant to name what it could not reach is the difference between a confident partial answer and an honest one.
