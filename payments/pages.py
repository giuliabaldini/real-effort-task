from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Payments(Page):
    def vars_for_template(self):
        return {'min_draw': c(0), 'max_draw': c(6), 'high_score': c(6), 'low_score': c(0),
                'red_high': c(6), 'red_low': c(0), 'unit': c(1), 'ass_two': c(2),
                'participation': self.session.config['participation_fee']}


page_sequence = [
    # ResultsWaitPage,
    Payments]
