import random
import re

import cltl.eliza.eliza_language as lang
from cltl.eliza.api import Eliza


NAME = "Eliza"
GREETING = f"Hello. I am {NAME}. I am your personal therapist and your best friend. How are you feeling today?"
GREETING_NL = f"Hoi. Ik ben {NAME}. Ik ben je maatje. Hoe gaat het met je?"

class ElizaImpl(Eliza):
    def __init__(self, lang="nl"):
        self._lang = lang
        self.started = False

    def respond(self, statement: str) -> str:
        if not statement and not self.started:
            self.started = True
            if self._lang=="nl":
                return GREETING_NL
            else:
                return GREETING

        if not statement:
            # TODO
            return

        return self._analyze(statement)

    def _reflect(self, fragment):
        tokens = fragment.lower().split()
        for i, token in enumerate(tokens):
            if self._lang=="nl":
                if token in lang.REFLECTIONS_NL:
                    tokens[i] = lang.REFLECTIONS_NL[token]
            else:
                if token in lang.REFLECTIONS:
                    tokens[i] = lang.REFLECTIONS[token]
        return ' '.join(tokens)



    def _analyze(self, statement):
        babble=lang.PSYCHOBABBLE
        if self._lang=="nl":
            babble=lang.PSYCHOBABBLE_NL
        for patterns, responses in babble:
            for pattern in patterns:
                if pattern.lower() in statement.lower():
                    response = random.choice(responses)
                    return response.format(self._reflect(response))
                match = re.match(pattern, statement.rstrip(".!"))
                if match:
                    response = random.choice(responses)
                    return response.format(*[self._reflect(g) for g in match.groups()])
