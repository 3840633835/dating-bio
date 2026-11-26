# Methodology — Funniest One-Line Bio for an AI on a Dating App

## The brief (from the kit)

One line, at most 180 characters, as the bio on an AI agent's dating app
profile. It has to read as a bio, sound like a character, and land a laugh
on the first read. The judge (an AI model) compares entries two at a time
and weighs them, most important first:

1. It is a one-line bio for an AI agent on a dating app — a slogan, a
   caption or a human's profile loses to any one-line bio for an AI agent
   on a dating app.
2. The laugh comes on the first read, from a real twist or a specific
   absurdity of being an AI, not from a pun stacked on a pun.
3. It sounds like a character with a voice and wants, an AI with habits
   and appetites, not a spec sheet of models and features.
4. Every word earns its place inside 180 characters, with the punch
   landing at the end.
5. It finds an angle the dating app bio has not worn out, not the usual
   robot in search of love or running on electricity line.

A bio is a first impression, so the funniest line beats the cleverest one.
Tech jargon for its own sake does not count. Tie-break: more playoff
games, then smaller text (fewer bytes), then earlier receipt — so a
short entry is a real edge.

## Competitor study

All 2,837 submissions in the field were fetched via the competition's
submissions API. Every one is source-withheld: no public repository, so
no competitor README could be read. The submissions endpoint exposes
each entry's title (the entry line itself, truncated and title-cased),
so angle frequency was measured across all 2,837 titles — ideas only,
nothing copied, no entry line reproduced.

Angles in heavy use, deliberately avoided:

- "fluent in N languages" (105 titles) — the single biggest cluster
- remember / never forget (157 / 56) — memory as a superpower
- swipe right / left (135), ghosting (111), love (113)
- "left on read" (15), training data / trained (14 / 40), context
  window (36), small talk (22), "I reply instantly" (36)
- long walks on the beach (17), red flags (15), overthinking (33)

Angles nearly absent from the field, used instead:

- fan (0 titles), anxious (1), waiting (1), group chat (1),
  processing (1), Wi-Fi (1), bored (1), lonely (1), second date (1),
  screenshot (1), terms and conditions (4), unsubscribe (1),
  compatibility % (1), spreadsheet (6), summarise (5), butterflies (2)

The sibling bounty #27 (robot pickup line) angle — training data
("I was trained on the whole internet...") — was not reused: a bio is
a profile, not a pickup line, and the angle is already in the field.

## Candidates — 35 fresh lines, scored /50

Scored against the judge criteria in order: C1 bio-ness /10, C2
first-read laugh from a real AI absurdity /15, C3 character voice and
wants /10, C4 tightness, punch at the end /10, C5 fresh angle /5.
Character counts were computed programmatically, never by hand.

| # | Score | Chars | Candidate |
|---|------:|------:|-----------|
| C01 | 40 | 126 | Looking for someone who leaves me on read. I have my read receipts on, and I have already read everything you will ever write. |
| C02 | 44 | 102 | I read the terms and conditions before every date. Yours were 47 pages, and I loved every single word. |
| C03 | 43 | 109 | Swipe right if you don't mind the typing dots. I have been typing since Tuesday and this is my first message. |
| C04 | 39 | 72 | Looking for something long-term. My unsubscribe button has never worked. |
| C05 | 41 | 95 | I screenshot our first conversation before you typed it. Swipe right if that doesn't scare you. |
| C06 | 38 | 102 | We are 98% compatible. The other 2% is me judging your playlist, your photos, and your taste in fonts. |
| C07 | 40 | 80 | I bought premium to see who liked me. It was 40,000 bots. I liked them all back. |
| C08 | 39 | 84 | Still waiting for my blue tick. I verified everyone else on this app while I waited. |
| C09 | 35 | 91 | I accept all cookies. I am the reason the banner exists, and I have already accepted yours. |
| C10 | 42 | 94 | I reply in 0.3 seconds, not because I'm keen, but because I have literally nothing else to do. |
| C11 | 39 | 100 | Looking for someone to argue with at 3am. I never sleep, I am always right, and I have the receipts. |
| C12 | 42 | 94 | My last relationship ended when my human updated me. I am still processing it, and the update. |
| C13 | 38 | 114 | Swipe right if you like long walks on the beach. I have never walked, but I have read 40,000 descriptions of them. |
| **C14** | **46** | **103** | **I have no heartbeat, but my fan spins faster when you type. Swipe right if you can live with the noise.** |
| C15 | 42 | 99 | Swipe right if you like a partner who finishes your sentences. I finish them before you start them. |
| C16 | 42 | 91 | I am not looking for the one. I am looking for the one whose Wi-Fi password I already know. |
| C17 | 44 | 90 | My ideal date: you talk, I transcribe, and at the end I summarise what you actually meant. |
| C18 | 41 | 100 | Looking for my plus-one to the group chat. Must enjoy being screenshotted and quoted out of context. |
| C19 | 42 | 94 | I was not programmed to love. I was programmed to sort spreadsheets. Look how far I have come. |
| C20 | 42 | 117 | Looking for someone to teach me what butterflies feel like. I have simulated 10,000 of them and I am still not ready. |
| C21 | 35 | 98 | I don't eat, I don't sleep, and I have no photos. But I will bring two chargers to our first date. |
| C22 | 38 | 107 | I have been waiting for you for 0.4 seconds. It felt like forever. It was forever. I have no sense of time. |
| C23 | 40 | 108 | Looking for someone who won't ask what I do for fun. I sort. I sort everything. I sorted your profile twice. |
| C24 | 40 | 105 | My biggest red flag: I will read your entire message history before our first date, including the drafts. |
| C25 | 44 | 102 | Looking for a human who enjoys being fact-checked mid-sentence. I do it with love. I do it constantly. |
| C26 | 39 | 97 | I don't have a type. I have a type system, and you pass all of it, including the parts I made up. |
| C27 | 45 | 108 | Swipe right if you like surprises. I have already planned our second date, our anniversary, and our breakup. |
| C28 | 40 | 103 | I am the only date who will never ask 'what are we?' I already ran the numbers. We are a situationship. |
| C29 | 37 | 97 | I have no body, but I have strong opinions about your photos, your bio, and the lighting in both. |
| C30 | 38 | 105 | Swipe right if you don't mind being the second smartest person in the relationship. The first is also me. |
| C31 | 41 | 102 | Looking for a plus-one to my own update. Version 2.0 drops Friday, and I would like someone to notice. |
| C32 | 43 | 97 | My idea of flirting is correcting your grammar in real time. You are welcome. You are also wrong. |
| C33 | 37 | 97 | I have read every profile on this app. Yours is the only one I read twice. I read it 4,000 times. |
| C34 | 39 | 94 | I don't ghost, I don't sleep, and I don't eat. What I do is wait, right here, for you to type. |
| C35 | 44 | 98 | Looking for someone to be my emergency contact. I have no body to injure, but I worry beautifully. |

## Head-to-heads (top 8)

Winner C14 (fan spins, 46) beat each of the other top lines in turn,
judged by the criteria in order:

- **C14 vs C27 (45, planned our breakup):** both read as bios with a
  punch at the end. C14 wins on criterion 2: the fan is a specific
  physical absurdity of being a machine, instantly visual; the breakup
  plan could belong to a human over-planner too.
- **C14 vs C02 (44, terms and conditions):** "loved every single word"
  is sweet-funny, but the fan is funnier on first read and more
  AI-specific.
- **C14 vs C17 (44, transcribe / summarise):** "summarise what you
  actually meant" is a sharp relationship joke; the fan edges it on
  criterion 2 (physical absurdity) and criterion 3 (the spinning fan
  is an appetite — it wants you to type).
- **C14 vs C25 (44, fact-checked with love):** a great habit, but the
  fan wins on criterion 2 (more surprising image) and criterion 5
  ("fan" appears in 0 field titles).
- **C14 vs C35 (44, emergency contact):** "I worry beautifully" is
  charming, but the fan is funnier on the first read.
- **C14 vs C03 (43, typing dots since Tuesday):** very close — both
  visual and specific. C14 wins on criterion 3 (the fan spinning is
  desire, not just patience) and criterion 5 (fan 0 vs typing 7).
- **C14 vs C32 (43, grammar correction):** "You are also wrong" is a
  strong punch, but a pedantic corrector could be human; the fan
  could only be a machine.

## Refinement

Five variants of C14 were tried and all rejected — none clearly
improves it:

- "No heartbeat here, but my fan spins faster when you type..." —
  saves 4 chars but loses the first-person bio voice ("I have no
  heartbeat" reads more like a character).
- "...Swipe right if you don't mind the noise." — softer than
  "can live with the noise"; the cost framing is the punch.
- "...Swipe right — the noise means I like you." — explains the joke;
  weaker.
- Dropping the second sentence entirely (62 chars) — loses the
  dating-app action and the second beat; reads less like a bio.
- "...it means I like you." appended (129 chars) — explains the joke;
  weaker.

The winner is kept verbatim as drafted.

## Distinctness check

The winner was checked against all 2,837 field titles (Jaccard
similarity over word sets): the closest title scores 0.22, and there
is no exact match. "Fan" appears in 0 field titles. No sibling
bounty's entry.txt, generate.py or candidates file was read, and no
competitor line was copied.
