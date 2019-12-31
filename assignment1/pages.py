from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class InstructionsAssignment1(Page):
    def is_displayed(self):
        return self.player.round_number == 1

    def before_next_page(self):
        self.participant.vars['expiry_total'] = time.time() + Constants.total_minutes * 60
        self.participant.vars['expiry_current'] = time.time() + Constants.seconds_per_round


class Assignment1(Page):
    form_model = 'player'
    form_fields = ['user_text']

    timeout_seconds = Constants.seconds_per_round

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_total'] - time.time()

    def is_displayed(self):
        # Do not show if there are less than three seconds
        return self.get_timeout_seconds() > 3

    def vars_for_template(self):
        current_sentence = Constants.sentences[self.player.round_number - 1]
        return {'sentence': current_sentence, 'expiry_current': self.participant.vars['expiry_current']}


page_sequence = [
    InstructionsAssignment1,
    Assignment1]
