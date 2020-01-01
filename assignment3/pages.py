from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, return_fields
import random
import time


class InstructionsAssignment3(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.round_number == 1

    def get_form_fields(self):
        return return_fields(Constants.example)

    def vars_for_template(self):
        form_label = zip(self.get_form_fields(), Constants.example)
        return {'form_label': form_label}

    def before_next_page(self):
        curr_nums = Constants.task_3_nums[self.player.round_number]
        random.shuffle(curr_nums)
        self.participant.vars["shuffled_nums"] = curr_nums
        self.participant.vars['expiry_total'] = time.time() + Constants.total_minutes * 60


class Assignment3(Page):
    form_model = 'player'
    timeout_seconds = Constants.seconds_per_round
    timer_text = 'Time left for this matrix:'

    def get_form_fields(self):
        return return_fields(Constants.task_3_nums[self.player.round_number])

    def vars_for_template(self):
        curr_nums = self.participant.vars["shuffled_nums"]
        form_label = zip(self.get_form_fields(), curr_nums)
        num = Constants.task_3_find[self.player.round_number - 1]
        return {'form_label': form_label, 'find_num': num}


class Completed3(Page):
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {'score': 0}


page_sequence = [
    InstructionsAssignment3,
    Assignment3,
    Completed3
]
