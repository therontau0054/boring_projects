"""The Wedding Chamber Murder — adapted from a classic 本格 locked-room case
(Originally: 本陣殺人事件 / The Honjin Murder by Seishi Yokomizo).

All names, locations, and details have been changed.  The solution must be
REASONED from the provided clues, not recognised from prior knowledge.
"""

CASE_ID = "wedding_chamber"
CASE_NAME = "The Wedding Chamber Murder"
CASE_DESC = (
    "A bride and groom murdered on their wedding night in a locked annex. "
    "A bloody sword outside in the snow. A single set of footprints. "
    "No one could have entered — and no one could have left."
)

CLUES_BY_ROUND = {
    1: {
        "title": "The Locked Wedding Chamber",
        "clues": [
            "The Inoue family estate in rural Nagano Prefecture, 22 December. "
            "Kenji Inoue (32), eldest son and heir, marries Katsumi (28) in a "
            "traditional ceremony attended by 40 guests. At 22:30 the couple "
            "retire to the 'Moon Viewing Annex' (望月庵), a standalone one-room "
            "building 30 metres from the main house, used by the family for "
            "generations as the wedding-night chamber.",

            "At 07:00 the next morning, a maid brings breakfast to the annex. "
            "No answer. The sliding wooden door (引違い戸) is locked from the "
            "inside with a horizontal wooden bolt (貫さん). The two small windows "
            "are latched shut. Peering through a gap in the door, the maid sees "
            "blood on the bedding and screams.",

            "The family breaks down the door. Both Kenji and Katsumi are dead "
            "in the futon bedding. Each has been stabbed multiple times in the "
            "chest and abdomen. The bodies are cold. Estimated time of death: "
            "between 23:30 and 01:00. No murder weapon in the room.",

            "In the snow-covered garden outside the annex: a bloodstained katana "
            "(Japanese sword) is stuck blade-down in the frozen earth, "
            "approximately 10 metres from the annex. The blood on the blade "
            "matches both victims. The katana is a 400-year-old Inoue family "
            "heirloom, normally displayed in an alcove in the main house.",

            "A SINGLE line of footprints leads from the annex's veranda to the "
            "katana and back to the veranda. No other footprints anywhere in "
            "the garden. The snow fell steadily from 21:00 to 03:00, "
            "accumulating to a depth of 15 cm. The footprints are clearly "
            "defined and undisturbed.",

            "The annex has exactly two possible entry points: the sliding door "
            "(bolted from inside) and two small windows (latched from inside, "
            "frames painted shut and clearly unbroken). The walls, floor, and "
            "ceiling are solid timber with no hidden passages. The roof is "
            "intact with no displaced tiles.",

            "A trail of blood drops leads from the futon to the sliding door, "
            "then stops at the threshold. The blood on the veranda and in the "
            "footprints is consistent with someone bleeding as they walked to "
            "and from the katana. The amount of blood in the footprints "
            "suggests the person was actively bleeding, not just carrying a "
            "bloody weapon.",
        ],
    },
    2: {
        "title": "The Family & The Evidence",
        "clues": [
            "Kenji's younger brother, Satoru Inoue (28), is now the sole heir "
            "to the Inoue estate (valued at approximately ¥400 million). Under "
            "Japanese inheritance law, if Kenji died childless, everything "
            "passes to Satoru. The family lawyer confirms this.",

            "Satoru was known to resent his brother. Multiple guests overheard "
            "him say 'Kenji gets everything, I get nothing' at the wedding "
            "reception. He had been drinking heavily and was seen arguing with "
            "Kenji at 20:00, two hours before the couple retired.",

            "Katsumi's former suitor, Daichi Yoshida (33), attended the wedding "
            "uninvited. He was seen standing alone in the garden near the annex "
            "at 21:30, staring at the building. When questioned, he said he "
            "'wanted to say goodbye to the past.' He left the estate at 21:45 "
            "(before the snow began accumulating significantly) — confirmed by "
            "three witnesses who saw his car depart.",

            "Inside the annex, a koto (Japanese floor harp, approx. 180 cm long) "
            "normally placed against the east wall had been moved. It was found "
            "directly under the main ceiling beam, rotated 90 degrees from its "
            "usual position. Three of its 13 strings were broken. The wooden "
            "bridge (筝柱) was found on the floor, not in its usual position.",

            "The sliding door's wooden bolt (3 cm thick, 40 cm long) had a small "
            "V-shaped notch (approx. 3 mm wide, 2 mm deep) carved into its "
            "underside, near the end closest to the door frame. The notch "
            "appears fresh — the exposed wood is lighter than the surrounding "
            "aged surface.",

            "A 15-metre length of silk string (細い絹糸, approx. 0.5 mm diameter) "
            "was found in the garden, half-buried in snow about 5 metres from "
            "the annex. One end was tied to a small iron nail (2 cm long). "
            "The string is identical to strings used on the koto.",

            "A small metal tube (approx. 5 cm long, 8 mm diameter) was found "
            "embedded in the snow near the annex veranda. The tube is a section "
            "of copper pipe, filed smooth at both ends. One end shows faint "
            "scratch marks consistent with having had string pulled through it.",

            "Drift patterns in the snow around the annex: the snow on the "
            "windward (north) side of the building is 15 cm deep. The snow on "
            "the leeward (south) side — where the veranda and footprints are — "
            "is only 8 cm deep, indicating some snow fell after the footprints "
            "were made. This places the footprints at approximately 01:00–02:00.",
        ],
    },
    3: {
        "title": "The Mechanism Revealed",
        "clues": [
            "Forensic examination of the ceiling beam directly above where the "
            "koto was found: two parallel scratch marks, 8 mm apart, running "
            "perpendicular to the beam's length. The scratches are fresh — "
            "exposed wood with no dust accumulation. The spacing matches the "
            "diameter of the copper tube found outside.",

            "The sliding door bolt was tested: a thin string threaded through "
            "the V-shaped notch, looped around the bolt, and pulled toward the "
            "door frame could slide the bolt into the locked position from "
            "outside. The string, when pulled with sufficient tension, leaves "
            "the door apparently bolted from within. The experiment was "
            "reproduced successfully.",

            "The koto strings are made of twisted silk — each string can "
            "support approximately 12 kg of tension before breaking. The three "
            "broken strings show signs of over-tension failure (untwisting and "
            "snapping at the bridge point), not cutting. The remaining 10 "
            "strings were also stressed but did not break.",

            "Blood spatter analysis on the walls and ceiling: the killer was "
            "right-handed (blood cast-off pattern arcs from right to left) and "
            "approximately 175–180 cm tall (based on the height of spatter on "
            "the walls). Satoru Inoue is right-handed and 177 cm. Daichi "
            "Yoshida is left-handed and 168 cm.",

            "The footprints in the snow: the heel impressions are significantly "
            "deeper (average depth 9 cm) than the toe impressions (average "
            "depth 5 cm). In normal forward walking, toe impressions are "
            "deeper than heel impressions. This pattern is consistent with "
            "someone walking BACKWARDS, placing their weight on the heel first.",

            "A second, much fainter set of footprints was discovered UNDER "
            "the visible footprints when investigators carefully removed the "
            "top layer of snow. These underlying prints follow the EXACT same "
            "path and have normal toe-heel depth ratios. They were made BEFORE "
            "the visible prints, by someone walking forward in the same tracks.",

            "The copper tube found in the snow: when string is pulled through "
            "it under tension, the tube acts as a low-friction guide. Scratch "
            "marks inside the tube indicate string was pulled through it in "
            "both directions. It was positioned at the point where the string "
            "changed direction — from the door, up to the beam, and out through "
            "a 3 mm gap at the corner of a window frame.",

            "A small amount of blood (type O, matching Kenji Inoue) was found "
            "on the veranda at the point where the footprints begin. But the "
            "blood inside the room stops at the door threshold. The blood on "
            "the veranda does NOT connect to the blood inside — there is a "
            "25 cm gap of clean floor between them.",
        ],
    },
    4: {
        "title": "Motive & Identity",
        "clues": [
            "Satoru Inoue had accumulated ¥28 million (approx. $250,000) in "
            "gambling debts to a criminal syndicate in Tokyo. Loan sharks had "
            "threatened him with violence if payment was not made by 31 December "
            "— nine days after the wedding. Kenji had refused to lend him money.",

            "Satoru was seen leaving the main house at 23:15 on the wedding "
            "night, telling a servant he 'couldn't sleep and needed fresh air.' "
            "He returned at approximately 01:30, his clothes damp with snow. "
            "He claimed he had been walking in the garden.",

            "The katana's display alcove in the main house: the sword was mounted "
            "on a wall bracket 170 cm above the floor. Satoru was the only "
            "family member tall enough to remove it without a step stool. The "
            "sword was confirmed to be in its alcove at 21:00 by a maid who "
            "cleaned the room. It was discovered missing at 07:30 on the "
            "morning the bodies were found.",

            "Katsumi (the bride) came from a wealthy family. Her dowry included "
            "¥50 million in cash and property. Under the marriage agreement, if "
            "Kenji died, the dowry would pass to his heir — Satoru, since "
            "Kenji and Katsumi had no children. Satoru was aware of this clause.",

            "Satoru's alibi for the time of the murder: he claims he was in the "
            "garden alone, then returned to his room in the main house. No one "
            "can confirm his whereabouts between 23:15 and 01:30. The servant "
            "who saw him return noted that his boots were wet and his hands "
            "were trembling.",

            "The crime reconstruction: the killer entered the annex BEFORE the "
            "snow started (before 21:00), hiding in a storage closet. After the "
            "couple fell asleep, he killed them with the katana, set up the "
            "mechanical bolt-locking device (koto strings, copper tube, beam), "
            "exited through the sliding door, pulled the bolt shut using the "
            "string mechanism, walked to the garden to plant the katana, then "
            "walked BACKWARDS in his own footprints to the veranda — creating "
            "the illusion of someone approaching from and retreating to the annex.",

            "The backwards-walking explains why the heel impressions are deeper "
            "than the toe impressions. The underlying forward-walking prints "
            "(discovered by removing the top snow layer) confirm the killer "
            "walked the path twice: once forward (leaving the annex), once "
            "backward (returning to his own tracks to erase them).",
        ],
    },
}

TRUTH = """
============================================================
 CASE RESOLUTION — THE TRUTH
============================================================

Satoru Inoue, the groom's younger brother, murdered Kenji and Katsumi Inoue
on their wedding night.

THE METHOD — A Mechanical Locked-Room Illusion:

1. PREPARATION: Satoru entered the annex before the wedding reception ended
   (before 21:00) and hid in the storage closet.  He brought with him three
   koto strings (taken from the koto earlier that day), a copper tube
   (cut from a pipe in the garden shed), and a small nail.

2. THE MURDER (approx. midnight): Once Kenji and Katsumi were asleep, Satoru
   emerged, took the katana (which he had removed from the alcove at 22:00 and
   hidden near the annex), and stabbed both victims.  He deliberately created
   blood drops leading to the door to suggest the killer had exited that way.

3. THE LOCKED-ROOM MECHANISM: Satoru carved a small V-notch in the underside
   of the wooden door bolt.  He looped a silk koto string around the bolt,
   passing the string through the notch.  He ran the string up to the ceiling
   beam (threaded through the copper tube for low-friction redirection), across
   the beam (using the koto as a counterweight — tying three strings together
   and to the koto bridge for tension), and out through a 3 mm gap at the
   window frame corner.  After exiting the annex, he PULLED the string from
   outside: this slid the bolt horizontally into the locked position.  He then
   pulled the string free from one end (the nail end), retrieving it completely.

4. THE FOOTPRINTS: Satoru walked FORWARD from the annex to the spot where he
   planted the katana (leaving the first, underlying set of prints).  He then
   walked BACKWARDS in his own tracks back to the veranda (leaving the visible
   prints with reversed heel-toe depth).  This created the illusion that a
   bleeding person had emerged from the annex, planted the sword, and returned
   inside — when in fact the killer went the OPPOSITE direction and escaped
   to the main house.

5. THE BLOOD GAP: The 25 cm gap between the blood inside and the blood on the
   veranda is because Satoru carried the katana (which dripped blood) while
   exiting, but the blood inside had pooled on the floor and did not physically
   connect to the drips on the veranda.

THE KEY CLUES:

- The koto was moved and strings broken: used as tension in the bolt mechanism.
- The V-notch in the bolt: the mechanical entry point for the string.
- The beam scratches and copper tube: redirected the string's pull direction.
- Backwards footprints (heel deeper than toe): the killer retraced his steps.
- The underlying forward prints: proving he walked the path twice.
- Blood spatter: right-handed, 175–180 cm — matches Satoru, excludes Yoshida
  (left-handed, 168 cm).
- Motive: ¥28 million debt + ¥50 million dowry inheritance = ¥78 million reason.
- Opportunity: Satoru was unaccounted for from 23:15 to 01:30 and returned wet.
- Access: only Satoru was tall enough to take the katana without a stool.

MOTIVE: Financial desperation.  Satoru faced violent consequences from loan
sharks within nine days.  His brother's death solved his debt problem entirely
and made him wealthy.  The wedding night was the perfect opportunity — the
couple isolated in the annex, the katana available, and the koto providing
the materials for his mechanical illusion.

This case is a classic of the 本格 (honkaku) genre: a seemingly impossible
locked room, a meticulous mechanical trick, and a killer undone by forensic
detail (the backwards footprints and right-handed blood spatter).  Every clue
was presented; the solution follows inevitably from the evidence.

============================================================
"""
