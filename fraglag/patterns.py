# fraglag/patterns.py

import re
from enum import Enum


class XPTitle(str, Enum):
    FIRST_BLOOD = "first_blood"
    DOUBLE_KILL = "double_kill"
    TRIPLE_KILL = "triple_kill"
    MULTI_KILL = "multi_kill"
    MEGA_KILL = "mega_kill"
    ULTRA_KILL = "ultra_kill"
    MONSTER_KILL = "monster_kill"
    UNSTOPPABLE = "unstoppable"
    GODLIKE = "godlike"


XP_PROGRESSION = [
    XPTitle.FIRST_BLOOD,
    XPTitle.DOUBLE_KILL,
    XPTitle.TRIPLE_KILL,
    XPTitle.MULTI_KILL,
    XPTitle.MEGA_KILL,
    XPTitle.ULTRA_KILL,
    XPTitle.MONSTER_KILL,
    XPTitle.UNSTOPPABLE,
    XPTitle.GODLIKE,
]


ANNOUNCER_TITLES = {
    XPTitle.FIRST_BLOOD: "First Blood",
    XPTitle.DOUBLE_KILL: "Double Kill",
    XPTitle.TRIPLE_KILL: "Triple Kill",
    XPTitle.MULTI_KILL: "Multi Kill",
    XPTitle.MEGA_KILL: "Mega Kill",
    XPTitle.ULTRA_KILL: "Ultra Kill",
    XPTitle.MONSTER_KILL: "Monster Kill",
    XPTitle.UNSTOPPABLE: "Unstoppable",
    XPTitle.GODLIKE: "Godlike",
}


EVENT_PATTERNS = {
    XPTitle.FIRST_BLOOD: [r"\bfirst blood\b"],
    XPTitle.DOUBLE_KILL: [r"\bdouble kill\b", r"\b2k\b"],
    XPTitle.TRIPLE_KILL: [r"\btriple kill\b", r"\b3k\b"],
    XPTitle.GODLIKE: [r"\bgodlike\b"],

    "kill": [
        r"\b(?P<player>\w+)\s+(?:killed|eliminated|fragged|dropped)\s+(?P<target>\w+)\b",
    ],

    "headshot": [
        r"\bheadshot\b",
    ],

    "clutch": [
        r"\bclutched\s+1v[2-5]\b",
        r"\b1v[2-5]\b",
    ],

    "match_point": [
        r"\bmatch point\b",
    ],
}


def compile_patterns(pattern_map):
    return {
        event: [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
        for event, patterns in pattern_map.items()
    }


COMPILED_EVENT_PATTERNS = compile_patterns(EVENT_PATTERNS)