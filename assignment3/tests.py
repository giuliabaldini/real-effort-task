from . import pages
from ._builtin import Bot
from .models import Constants
import time


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield pages.InstructionsAssignment3

        yield pages.Assignment3, dict(cb_0=1)

        if self.round_number == Constants.num_rounds:
            yield pages.Completed3
