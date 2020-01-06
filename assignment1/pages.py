from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class InstructionsAssignment1(Page):
    def is_displayed(self):
        return self.player.round_number == 1

    def before_next_page(self):
        self.participant.vars['expiry_total'] = time.time() + self.session.config['minutes_per_task'] * 60


class Assignment1(Page):
    form_model = 'player'
    form_fields = ['user_text']

    timer_text = 'Time left for this sentence:'

    def get_timeout_seconds(self):
        return self.session.config['seconds_per_round']

    def get_time_left(self):
        return self.participant.vars['expiry_total'] - time.time()

    def is_displayed(self):
        # Do not show if there are less than three seconds
        return self.get_time_left() > 3

    def vars_for_template(self):
        current_sentence = Constants.task_1[self.player.round_number - 1]
        return {'sentence': current_sentence, 'expiry_total': self.participant.vars['expiry_total']}


class Completed1(Page):
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds


page_sequence = [
    InstructionsAssignment1,
    Assignment1,
    Completed1,
]
