"""The Decagon Island Mystery — adapted from a classic 本格 locked-island case
(Originally: 十角館の殺人 / The Decagon House Murders by Yukito Ayatsuji).

All names, locations, and details have been changed.  The solution must be
REASONED from the provided clues, not recognised from prior knowledge.
"""

CASE_ID = "decagon_island"
CASE_NAME = "The Decagon Island Mystery"
CASE_DESC = (
    "Six university students on a remote island retreat. "
    "A decagon-shaped house with ten rooms. One by one, they die. "
    "The killer must be among them — or is one death a lie?"
)

CLUES_BY_ROUND = {
    1: {
        "title": "Arrival at Decagon Island",
        "clues": [
            "Six students from Northwood University's Mystery Literature Club "
            "travel to Decagon House on remote Tsunojima Island for a one-week "
            "retreat (17–24 March). The house was built 20 years ago by a "
            "reclusive architect who died shortly after its completion.",

            "The six students: Eric Mason (24, architecture), Charles Carr (23, "
            "medicine), Agnes Clarke (22, literature), Louis Leroy (25, law), "
            "Peter Owen (23, history), and Olga Orczy (22, chemistry).",

            "Decagon House is a regular decagon: a central hall surrounded by "
            "10 identical rooms. Each room's door faces the hall. Six rooms are "
            "assigned to the students; Room 7 and three others are unoccupied. "
            "Each occupied room has a hand-written nameplate on the door.",

            "Thomas Briggs (61), the island's caretaker, lives alone in a small "
            "cottage 60 metres from the main house. His wife died two years ago. "
            "He maintains the property and operates the motorboat that is the "
            "only transport to the mainland (3 km away).",

            "On the morning of Day 3 (19 March), the students find Briggs dead "
            "in his cottage. Cause: cyanide poisoning in his morning tea. His "
            "cottage door was unlocked, no signs of forced entry or struggle.",

            "The motorboat has been sabotaged: fuel line cut, spark plugs removed. "
            "The radio in the main house is smashed beyond repair. There is no "
            "mobile signal on the island. The students are completely stranded.",

            "Eric Mason searches the cottage and finds a typed note under Briggs's "
            "pillow: 'You knew what they did. You stayed silent. First to pay.' "
            "The paper is ordinary printer paper — identical to a ream found in "
            "the main house study.",

            "A thorough search of the entire island (0.3 km², mostly bare rock "
            "with sparse pine trees) confirms: no one else is present. The "
            "students conclude the killer is one of them.",
        ],
    },
    2: {
        "title": "The Killings Begin",
        "clues": [
            "Day 4 morning (20 March): Eric Mason is found dead in his room "
            "(Room 3). Door bolted from inside. Window latched. Cause: cyanide "
            "in his drinking water. A glass on the bedside table contains traces. "
            "Eric's left hand has been severed at the wrist and is MISSING from "
            "the scene. The cut is clean — consistent with a surgical instrument.",

            "Day 5 morning (21 March): Agnes Clarke is found strangled in her "
            "room (Room 5). Door bolted from inside. A thin cord is still around "
            "her neck — it matches curtain cord from the central hall. Her "
            "nameplate has been removed from the door.",

            "Day 6 morning (22 March): Charles Carr is found dead in his room "
            "(Room 2). Blunt-force trauma to the head. The weapon — a heavy "
            "bronze statue from the central hall — lies beside the bed. Door "
            "bolted from inside. His nameplate is also missing.",

            "The three remaining students — Leroy, Owen, Orczy — now stay "
            "together in the central hall at all times, taking shifts to keep "
            "watch during the night. No further deaths occur on Day 7.",

            "A search of Eric Mason's belongings reveals a detailed architectural "
            "sketch of Decagon House. Room 7 is annotated with a note in Eric's "
            "handwriting: 'False wall — hollow space behind, approx 1.2 × 2.5 m. "
            "Access via removable panel in the back of the built-in wardrobe.'",

            "The hidden space behind Room 7's wardrobe is discovered. It contains "
            "a blanket, several empty water bottles, biscuit wrappers, a torch "
            "with dead batteries, and a surgical bone saw (wiped clean, no "
            "fingerprints). The space smells of sweat and has clearly been "
            "occupied recently — for multiple days, judging by the waste.",

            "All room keys are accounted for. Each student had their own key. "
            "The caretaker's master key was found in his cottage, hanging on "
            "its usual hook. No duplicates or lock-picking marks on any door.",

            "Peter Owen recalls a detail about Eric Mason: Eric was left-handed "
            "and had a prominent burn scar on the back of his left hand — a "
            "childhood injury from a kitchen accident. Eric never wore rings "
            "or watches on that hand because the scar tissue was sensitive.",
        ],
    },
    3: {
        "title": "Past Sins & Inconsistencies",
        "clues": [
            "Eleven months before the retreat (April of the previous year): "
            "Clara Hastings, a 21-year-old art student at Northwood University, "
            "died of acute alcohol poisoning at an off-campus party attended by "
            "Mystery Literature Club members. The coroner ruled it accidental.",

            "Clara Hastings was Eric Mason's girlfriend of three years. After "
            "her death, Eric withdrew from university for a full semester. He "
            "returned only three months before the island retreat, and he was "
            "the one who proposed the trip to Decagon House to the club.",

            "A witness from the party (interviewed by police at the time, and "
            "re-contacted during this investigation) stated: Agnes Clarke and "
            "Charles Carr poured 200 ml of laboratory-grade ethanol into Clara's "
            "fruit punch as a 'taste test prank.' The other club members at the "
            "party — Leroy, Owen, and Orczy — knew about the prank beforehand "
            "and did not warn Clara. Eric Mason was not at the party; he arrived "
            "two hours later and discovered Clara unconscious.",

            "Olga Orczy reports feeling unusually drowsy on the night of Day 3 "
            "(the night before Eric's body was discovered). She had shared a "
            "bottle of wine with the group at dinner. Her symptoms — dizziness, "
            "prolonged sleep — are consistent with a mild sedative.",

            "Louis Leroy examines Eric's body (kept in cold storage in the "
            "basement) and notices something disturbing: the body in Room 3 has "
            "a faded anchor tattoo on the RIGHT forearm. He is certain Eric "
            "Mason had NO tattoos anywhere on his body. The other survivors "
            "confirm this.",

            "The caretaker Thomas Briggs was a retired sailor in the Merchant "
            "Navy (1956–1994). His personnel record from the shipping company "
            "mentions 'anchor tattoo, right forearm' in his identification "
            "profile. The record was obtained via the emergency radio frequency "
            "that was partially repaired on Day 6.",

            "The severed left hand has never been found. The three survivors "
            "searched the entire island, the shoreline, and every room of "
            "Decagon House. It has simply vanished.",

            "A timeline reconstruction: the caretaker died on Night 2 (between "
            "22:00 on 18 March and 06:00 on 19 March). Eric Mason 'died' on "
            "Night 3. Agnes Clarke died on Night 4. Charles Carr died on "
            "Night 5. The survivors have been together continuously since "
            "Night 5 — no one could have moved a body or hidden evidence.",
        ],
    },
    4: {
        "title": "The Hidden Truth",
        "clues": [
            "The cyanide used in the caretaker's poisoning and in Eric Mason's "
            "water came from a 500 g container of potassium cyanide kept in "
            "Briggs's gardening shed (used legally for pest control). The "
            "container is now empty. All six students were shown the shed "
            "during a tour on Day 1 and knew about the cyanide.",

            "Eric Mason's architectural dissertation, submitted two months "
            "before the retreat, was titled 'Concealed Spaces in 20th Century "
            "Domestic Architecture.' It included a case study of Decagon House "
            "and its architect. Eric had visited the island twice before — once "
            "in January and once in February — to 'research' the house. No "
            "other student had ever been to the island before this trip.",

            "The bone saw found in the hidden room belongs to a surgical kit "
            "that Charles Carr brought to the island (he was a medical student "
            "and carried basic instruments). Carr reported the saw missing on "
            "Day 3, before Eric's body was discovered.",

            "Eric Mason changed his last will and testament three months ago. "
            "He owned very little (a small savings account and his personal "
            "belongings). Everything was left to Clara Hastings's 16-year-old "
            "younger sister, Emma Hastings. He had no family of his own.",

            "Analysis of the wine bottle from Day 3 dinner: traces of "
            "zolpidem (a fast-acting sedative) found in the residue at the "
            "bottom of the bottle. The bottle was opened and poured by Eric "
            "Mason, who insisted on being 'sommelier for the evening.' This "
            "explains Olga Orczy's drowsiness — and suggests Eric wanted at "
            "least some of the group incapacitated that night.",

            "The hidden space behind Room 7's wardrobe had a narrow gap "
            "(approx. 2 cm) between the removable panel and the wardrobe's "
            "back wall. Through this gap, a person hiding inside could see "
            "and hear activity in Room 7 and the central hall. Fibres matching "
            "Eric Mason's jacket were caught on the rough edge of the panel.",
        ],
    },
}

TRUTH = """
============================================================
 CASE RESOLUTION — THE TRUTH
============================================================

Eric Mason is alive.  He faked his own death and murdered four people on
Decagon Island: the caretaker Thomas Briggs, Agnes Clarke, Charles Carr —
and he would have killed the remaining three if the investigation had not
intervened.

WHAT REALLY HAPPENED:

Night 2 (18 March): Eric went to the caretaker's cottage, drugged Briggs's
evening tea with cyanide, and waited for him to die.  He left the typed
accusation note to make it look like a revenge killing from an outside party.

Night 3 (19 March): Eric drugged the wine at dinner so the others would
sleep heavily.  He then retrieved Briggs's body from the cottage, carried it
to his room (Room 3), dressed it in his own pyjamas, and severed its LEFT
hand — the hand that would have shown whether or not the body had Eric's
distinctive burn scar.  By removing the hand entirely, he prevented
identification.  He placed the cyanide-laced water by the bed, bolted the
door from inside using a simple string-and-wedge trick (the string was thin
enough to pass under the door and be pulled out from the corridor), then hid
in the secret room behind Room 7's wardrobe.

Night 4 (20 March): Eric emerged from hiding, strangled Agnes Clarke in her
room, bolted the door from inside (same string trick), and removed her
nameplate to create a symbolic "erasure" of his victims.  He returned to the
hidden room.

Night 5 (21 March): Eric killed Charles Carr with the bronze statue.  Same
method, same removal of the nameplate.  He had stolen Carr's bone saw on Day 2
to use for the amputation.

The CRITICAL CLUES that reveal the truth:

1. The tattoo on the right forearm: the "Eric" body had an anchor tattoo.
   Eric Mason had NO tattoos.  Thomas Briggs was a retired sailor with an
   anchor tattoo on his right forearm.  The body in Room 3 was Briggs, not Eric.

2. The missing left hand: the only part of Eric's body that carried a unique,
   unmistakable identifying mark (the burn scar).  By removing it, Eric
   prevented the others from confirming the body was NOT his.  He could not
   risk cutting off the right forearm (which would have revealed the tattoo
   mismatch), so he hid the left hand somewhere it would never be found —
   likely thrown into the sea.

3. Eric was the only person who knew about the hidden room behind Room 7.
   His architectural research had uncovered it during his earlier visits.
   It was his hiding place, his base of operations.  His jacket fibres were
   found on the panel edge.

4. The sedative in the wine: only Eric (who poured the wine) could have
   drugged the group that night.  He needed them asleep to move the body.

5. The surgical saw from Carr's kit: stolen by Eric before Carr died, used to
   amputate the hand.  Its presence in the hidden room ties Eric to the
   dismemberment.

6. Motive: Clara Hastings died because of a cruel prank by Agnes Clarke and
   Charles Carr, witnessed and tolerated by Leroy, Owen, and Orczy.  Eric had
   been planning revenge for 11 months.  The island trip was his trap.  He
   selected Decagon House specifically because of its hidden room — essential
   for his plan to "die" and continue killing from the shadows.

7. The changed will (leaving everything to Clara's sister) and the architectural
   dissertation on Decagon House both show premeditation spanning months.

THE VERDICT: Eric Mason murdered four people and would be charged with
premeditated homicide.  His elaborate "locked room" killings from a hidden
base within a decagon-shaped house form a classic 本格 (honkaku) mystery —
every clue was presented fairly, and the solution is deducible from the
evidence alone.

============================================================
"""
