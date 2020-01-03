from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Payments(Page):
    def vars_for_template(self):
        return {'min_draw': c(self.participant.session.config['task_1_low_win']),
                'max_draw': c(self.participant.session.config['task_1_high_win']),
                'high_score': c(self.participant.session.config['task_1_high_win']),
                'low_score': c(self.participant.session.config['task_1_low_win']),
                'red_high': c(self.participant.session.config['redistribution_high']),
                'red_low': c(self.participant.session.config['redistribution_low']),
                'inc_1': c(self.participant.session.config['inc_1']),
                'dec_1': c(self.participant.session.config['dec_1']),
                'inc_2': c(self.participant.session.config['inc_2']),
                'dec_2': c(self.participant.session.config['dec_2']),
                'participation': self.session.config['participation_fee']}


class Feedback(Page):
    form_model = 'player'
    form_fields = ['feedback']


page_sequence = [
    Payments,
    Feedback]
