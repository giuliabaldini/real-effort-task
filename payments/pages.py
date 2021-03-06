from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Payments(Page):
    def vars_for_template(self):
        return {'min_draw': c(self.participant.session.config['low_win']),
                'max_draw': c(self.participant.session.config['high_win']),
                'high_score': c(self.participant.session.config['high_win']),
                'low_score': c(self.participant.session.config['low_win']),
                'high_win': c(self.participant.session.config['high_win']),
                'low_win': c(self.participant.session.config['low_win']),
                'increase': c(self.participant.session.config['increase']),
                'decrease': c(self.participant.session.config['decrease']),
                'participation': self.session.config['participation_fee'],
                'conversion': c(1 / self.session.config['real_world_currency_per_point']),
                'dollar': '$1'
                }


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
