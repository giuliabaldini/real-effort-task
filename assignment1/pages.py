from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InstructionsAssignment1(Page):
    def is_displayed(self):
        return Constants.instructions and self.player.round_number == 1


class Assignment1(Page):
    pass


page_sequence = [
    InstructionsAssignment1,
    Assignment1]
