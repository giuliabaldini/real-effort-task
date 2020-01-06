from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield pages.InstructionsAssignment2

        yield pages.Assignment2, dict(user_text=Constants.task_2[self.round_number - 1])

        if self.round_number == Constants.num_rounds:
            yield pages.Completed2
