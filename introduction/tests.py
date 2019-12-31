from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        if Constants.general_instructions:
            yield pages.Instructions
        yield pages.Part1
