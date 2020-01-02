from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ResultsWaitPage(WaitPage):
    group_by_arrival_time = True

    def after_all_players_arrive(self):
        self.group.compute_payoffs()


class Completed1(Page):
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds


page_sequence = [
    ResultsWaitPage,
    Completed1
]
