"""The Alpine Express Murder — adapted from a classic locked-room mystery.

Names, places, and details have been changed so the solution must be REASONED
from the clues, not recognised from prior knowledge.
"""

CASE_ID = "alpine_express"
CASE_NAME = "The Alpine Express Murder"
CASE_DESC = (
    "A luxury train stranded in the Alps. A wealthy businessman found dead "
    "in his locked compartment. 12 passengers, each with an alibi."
)

CLUES_BY_ROUND = {
    1: {
        "title": "Crime Scene Discovery",
        "clues": [
            "Victor Blackwood, 52, American businessman, found dead in his first-class "
            "compartment (No. 1) on the Alpine Express (Zurich to Vienna).",

            "Body discovered at 07:00 by the train attendant who came to deliver "
            "morning coffee. The 'Do Not Disturb' sign had been hung on the door handle.",

            "Compartment door was locked from the inside with the chain-bolt engaged. "
            "The bolt had to be cut by railway staff to gain entry.",

            "Compartment window was partially open — approximately 15 cm. Fresh snow "
            "had blown in and accumulated on the carpet directly beneath the window.",

            "The victim was in silk pyjamas, lying face-up on the bed. Multiple stab "
            "wounds visible through the pyjama top. No murder weapon found in the "
            "compartment or in the corridor.",

            "A half-finished cup of chamomile tea on the bedside table. Still faintly "
            "warm when the body was discovered (per the attendant's statement).",

            "The Alpine Express was immobilised by an avalanche at approximately 01:00. "
            "The train has been stranded in a remote section of the Alps since then. "
            "No one has entered or left the train.",

            "There are 12 first-class passengers in this carriage (compartments 1–12) "
            "plus 2 train staff: the conductor Pierre Laurent and the attendant Marco "
            "Bianchi.",

            "The victim had been seen alive at 22:30 the previous evening when the "
            "attendant delivered his chamomile tea. He was travelling alone.",
        ],
    },
    2: {
        "title": "Forensic Evidence & Physical Clues",
        "clues": [
            "The victim was stabbed exactly 12 times. No other injuries.",

            "Wound depth analysis: 3 deep wounds (4–5 inches, delivered with substantial "
            "force), 6 medium wounds (2–3 inches), 3 shallow wounds (less than 1 inch, "
            "described by the pathologist as 'tentative or hesitant').",

            "Wound angle analysis: 5 wounds track right-to-left (consistent with a "
            "right-handed attacker facing the victim), 7 wounds track left-to-right "
            "(consistent with a left-handed attacker). No single dominant pattern.",

            "No defensive wounds on the victim's hands, forearms, or anywhere else. "
            "The victim did not fight back.",

            "Toxicology report: the chamomile tea contained chloral hydrate, a fast-acting "
            "sedative. Concentration was high enough to render an adult male unconscious "
            "within 10–15 minutes of ingestion.",

            "Estimated time of death: between 00:30 and 02:00. Body temperature and "
            "rigor mortis are consistent with death occurring near 01:15.",

            "The victim's pocket watch (on the bedside table) was smashed — the glass "
            "face broken and the hands frozen at 01:15. The watch was an expensive "
            "Swiss piece; the damage appears deliberate.",

            "A white linen handkerchief found under the victim's pillow. High-quality "
            "fabric, hand-embroidered with the letter 'E' in one corner. No blood on it.",

            "A partially burned piece of notepaper in the ashtray. The readable fragments: "
            "'…must pay for what you did to little Lily…' and '…never forgive…'. "
            "The handwriting is feminine, in blue ink.",

            "A brass button from a train conductor's uniform found on the floor, partially "
            "under the bed. The thread still attached suggests it was torn off, not cut.",

            "Multiple types of ash residue found in the compartment's ashtray: cigarette "
            "ash (fine, grey), cigar ash (coarse, dark), and pipe ash (flaky, tan). "
            "The victim was a non-smoker (confirmed by his personal physician's records).",

            "The train conductor, Pierre Laurent, reports that his spare uniform — kept "
            "in a storage cupboard at the end of the carriage — is missing. He last saw "
            "it at 22:00 the previous evening.",
        ],
    },
    3: {
        "title": "Passenger Testimonies & Observations",
        "clues": [
            "All 12 passengers were interviewed separately. Each claims to have been "
            "in their own compartment sleeping between 00:00 and 07:00.",

            "Alibi cross-check: every passenger's claim is corroborated by at least one "
            "other passenger. Examples: Mrs. Schmidt (compartment 3) says she heard "
            "Mr. Dubois (compartment 4) snoring; Mr. Dubois confirms he 'sleeps heavily "
            "and snores'. Count Volkov (compartment 5) says his wife (compartment 6, "
            "connecting door) was with him all night; the Countess confirms. Dr. Thornton "
            "(compartment 7) says he checked on his 'sleeping wife' at 01:00; "
            "Mrs. Thornton (compartment 8) confirms she took a sleeping draught. "
            "The pattern repeats for all 12 — no passenger's alibi stands alone.",

            "Mrs. Elizabeth Thornton (compartment 8) states she woke briefly at ~00:45 "
            "and, through the frosted glass of her compartment door, saw a figure in a "
            "red robe walking down the corridor toward the victim's end of the carriage.",

            "Mr. James Whitfield (compartment 11) reports hearing a 'rhythmic thumping "
            "sound, like something heavy being dropped repeatedly' from the direction "
            "of the victim's compartment at approximately 01:15.",

            "The communicating door between compartments 1 and 2 (victim in 1, "
            "unoccupied in 2) was found unlocked. These doors are normally bolted "
            "unless a family books both compartments.",

            "A woman's red silk robe was found stuffed behind a luggage rack in "
            "compartment 2 (the unoccupied one next to the victim). No other luggage "
            "in that compartment.",

            "The passenger in compartment 12 (end of carriage) reports that her "
            "compartment door does not close properly — a 2 cm gap remains. She "
            "states she could see the corridor and is 'certain' no one passed between "
            "01:00 and 01:30.",

            "No footprints were found in the fresh avalanche snow outside the train. "
            "The snow surface around the carriage is completely undisturbed.",

            "Conductor Pierre Laurent appeared visibly nervous during questioning — "
            "sweating, avoiding eye contact, voice trembling. He has worked this route "
            "for 15 years with an immaculate record.",

            "Countess Natalia Volkova (compartment 6) had originally requested "
            "compartment 12 (farthest from the victim). She changed her booking to "
            "compartment 6 (closer to the victim) three weeks before departure.",

            "Sister Mary Catherine (compartment 9), an Irish nun, states she was "
            "praying the rosary aloud in her compartment 'from midnight until about "
            "01:30'. Two other passengers confirm hearing prayer sounds.",

            "The carriage attendant, Marco Bianchi, states he was in the staff compartment "
            "at the rear of the carriage from 23:30 onwards. He 'heard nothing unusual'.",
        ],
    },
    4: {
        "title": "Victim's Background & Hidden Connections",
        "clues": [
            "Victor Blackwood was travelling under a false identity. His real name was "
            "Marcus Kane, age 54.",

            "Five years ago, Marcus Kane was arrested in London for the kidnapping and "
            "murder of 6-year-old Lily Armstrong. The child was taken from her family's "
            "estate; her body was found two weeks later in a remote cottage Kane had "
            "rented under a pseudonym.",

            "Kane was acquitted at trial. The key evidence — Lily's belongings found "
            "in Kane's possession — was ruled inadmissible because the police had "
            "searched his property without a proper warrant.",

            "Lily's mother, Catherine Armstrong, died 8 months after the trial. "
            "The coroner recorded 'accidental overdose of chloral hydrate' — the same "
            "sedative found in the victim's tea. She had been prescribed it for "
            "'nervous exhaustion' following her daughter's death.",

            "Lily's father, Lord Richard Armstrong, died 14 months after the trial. "
            "Cause: self-inflicted gunshot wound. He left a note reading only: "
            "'There is no justice in this world.'",

            "The Armstrong household staff at the time of Lily's death included: "
            "a German governess (Helga), a French cook (Claude), a British nanny "
            "(Eleanor), an Italian chauffeur (Marco), an Irish maid (Mary), and a "
            "French butler (Pierre). All were dismissed after the estate was sold.",

            "Other people closely connected to Lily Armstrong included: her godmother "
            "(a Russian countess living in Vienna), the family doctor (British, retired "
            "to Switzerland), the family lawyer (American, now based in Zurich), her "
            "music teacher (Swedish), and her father's brother (a British Army colonel).",

            "The Armstrong murder case file was checked out from Scotland Yard archives "
            "two months ago by a retired detective. The file has not been returned.",

            "Marcus Kane had been receiving threatening letters for three years, "
            "always signed 'We remember Lily.' He had recently hired a private "
            "investigator — a former Scotland Yard detective — to identify the sender.",

            "Passenger manifest analysis: 10 of the 12 first-class passengers on this "
            "train booked their tickets within a 4-day window, approximately three "
            "weeks before departure. Only Mr. James Whitfield (American businessman) "
            "and Sister Mary Catherine (Irish nun) booked more than a month in advance.",

            "The real name listed on Countess Volkova's passport is Natalia Armstrongova. "
            "She was born Natalia Armstrong — she is Lily Armstrong's maternal aunt "
            "(her mother's sister), who married into Russian nobility.",

            "The retired Scotland Yard detective who checked out the Armstrong file "
            "matches the description of the passenger in compartment 10, a 'William "
            "Baker, retired civil servant'.",
        ],
    },
}

TRUTH = """
============================================================
 CASE RESOLUTION — THE TRUTH
============================================================

Victor Blackwood (Marcus Kane) was murdered by ALL 12 passengers acting in concert.

Every passenger in the first-class carriage was connected to Lily Armstrong and her
devastated family. They had planned this for months — booking tickets in the same
window, arranging the carriage layout so the conspirators surrounded Kane, and
coordinating their alibis.

THE NIGHT OF THE MURDER:
1. The conspirators drugged Kane's chamomile tea with chloral hydrate — the same
   substance that had "accidentally" killed Lily's mother. The tea was delivered
   by the attendant Marco Bianchi (formerly Marco, the Armstrong chauffeur).
2. Once Kane was unconscious (~00:45), the conspirators entered his compartment
   through the unlocked communicating door from compartment 2.
3. One by one, each of the 12 passengers stabbed the unconscious man once.
   This explains: exactly 12 wounds, varying depths (different physical strength),
   varying angles (different dominant hands), and no defensive wounds.
4. The conductor, Pierre Laurent (formerly Pierre, the Armstrong butler), used
   his spare uniform to move through the train unnoticed while coordinating.
5. The red silk robe was worn by Eleanor (now "Elizabeth Thornton") when she moved
   through the corridor — seen by a co-conspirator, not an innocent witness.
6. The pocket watch was smashed and set to 01:15 to create a false time reference.
   The "thumping sound" heard at 01:15 was part of the staged evidence.
7. The handkerchief with "E" was left deliberately — "E" for Eleanor (the nanny)
   and also for "Elizabeth," her alias.
8. The burned note mentioning "Lily" was planted to ensure investigators would
   eventually discover the motive.
9. The unlocked window with undisturbed snow outside proves no one exited —
   the killer(s) were still on the train. The scene was staged.
10. All 12 alibis interlock because they were coordinated in advance. No passenger
    can be singled out without the entire conspiracy unravelling.

THE 12 CONSPIRATORS (passenger names to true identities):
- Helena Schmidt (German) = Helga, the German governess
- Pierre Dubois (French) = Claude, the French cook
- Count Andrei Volkov (Russian) = husband of Lily's aunt
- Countess Natalia Volkova (Russian) = Natalia Armstrongova, Lily's maternal aunt
- Dr. Henry Thornton (British) = the Armstrong family doctor
- Elizabeth Thornton (British) = Eleanor, Lily's British nanny
- James Whitfield (American) = the Armstrong family lawyer
- Sister Mary Catherine (Irish) = Mary, the Irish maid
- Antonio Ferrari (Italian) = Marco (posing as passenger; actually the chauffeur)
- Greta Johansson (Swedish) = Lily's music teacher
- Colonel Hugh Armstrong (British) = Lord Richard Armstrong's brother, Lily's uncle
- William Baker (British, retired) = the former Scotland Yard detective who
  worked the original Armstrong case

MOTIVE: Collective justice. The legal system failed them, so 12 people whose
lives were shattered by Marcus Kane took justice into their own hands —
forming a jury of 12 to deliver the verdict that the courts could not.

The irony: they became a literal "jury" of 12, just like a criminal trial jury.
Each delivered their own "sentence" with a single stab wound.

============================================================
"""
