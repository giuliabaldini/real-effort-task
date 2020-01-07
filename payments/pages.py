from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Payments(Page):
    def vars_for_template(self):
        return {'min_draw': c(self.participant.session.config['task_1_low_win']),
                'max_draw': c(self.participant.session.config['task_1_high_win']),
                'high_score': c(self.participant.session.config['task_3_high_win']),
                'low_score': c(self.participant.session.config['task_3_low_win']),
                'red_high': c(self.participant.session.config['high_win']),
                'red_low': c(self.participant.session.config['low_win']),
                'increase': c(self.participant.session.config['increase']),
                'decrease': c(self.participant.session.config['decrease']),
                'participation': self.session.config['participation_fee']}


class Feedback(Page):
    form_model = 'player'
    form_fields = ['feedback']


class Completion(Page):
    pass


page_sequence = [
    Payments,
    Feedback,
    Completion,
]
