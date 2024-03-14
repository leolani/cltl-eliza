import random
import re

import cltl.eliza.eliza_language as lang
from cltl.eliza.api import Eliza


NAME = "Eliza"
GREETING = f"Hello. I am {NAME}. I am your personal therapist and your best friend. How are you feeling today?"
LANG = "EN"

class ElizaImpl(Eliza):
    def __init__(self):
        self.started = False

    def respond(self, statement: str) -> str:
        if not statement and not self.started:
            self.started = True
            return GREETING

        if not statement:
            # TODO
            return

        return self._analyze(statement)

    def _reflect(self, fragment):
        tokens = fragment.lower().split()
        for i, token in enumerate(tokens):
            if LANG=="NL":
                if token in lang.REFLECTIONS_NL:
                    tokens[i] = lang.REFLECTIONS_NL[token]
            else:
                if token in lang.REFLECTIONS:
                    tokens[i] = lang.REFLECTIONS[token]
        return ' '.join(tokens)

    def _analyze(self, statement):
        if LANG=="NL":
            for pattern, responses in lang.PSYCHOBABBLE_NL:
                match = re.match(pattern, statement.rstrip(".!").lower())
                if match:
                    response = random.choice(responses)
                    return response.format(*[self._reflect(g) for g in match.groups()])
        else:
            for pattern, responses in lang.PSYCHOBABBLE:
                match = re.match(pattern, statement.rstrip(".!").lower())
                if match:
                    response = random.choice(responses)
                    return response.format(*[self._reflect(g) for g in match.groups()])
