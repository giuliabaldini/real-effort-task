from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, return_fields
import random
import time


class InstructionsAssignment4(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.round_number == 1

    def before_next_page(self):
        self.participant.vars['expiry_total'] = time.time() + self.session.config['minutes_per_task'] * 60


class Assignment4(Page):
    form_model = 'player'
    timer_text = 'Time left for this matrix:'

    def get_timeout_seconds(self):
        return self.session.config['seconds_per_round']

    def get_time_left(self):
        return self.participant.vars['expiry_total'] - time.time()

    def is_displayed(self):
        # Do not show if there are less than three seconds
        return self.get_time_left() > 3

    def get_form_fields(self):
        return return_fields(self.session.vars['task_4_nums'][str(self.player.round_number)])

    def vars_for_template(self):
        curr_nums = self.session.vars['task_4_nums'][str(self.player.round_number)]
        form_label = zip(self.get_form_fields(), curr_nums)
        num = Constants.task_4_find[self.player.round_number - 1]
        return {'form_label': form_label, 'find_num': num, 'expiry_total': self.participant.vars['expiry_total']}

    def before_next_page(self):
        self.player.compute_score()


class Completed4(Page):
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {'score': self.participant.vars['player_score4']}

    def before_next_page(self):
        self.player.score = self.participant.vars['player_score4']


page_sequence = [
    InstructionsAssignment4,
    Assignment4,
    Completed4,
]
