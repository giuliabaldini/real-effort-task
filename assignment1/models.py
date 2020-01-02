from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'assignment1'
    players_per_group = None

    total_minutes = 1  # Total duration
    seconds_per_round = 20  # Duration of one round

    task_1 = [  # TODO: Change these to change the different sentences
        "bag books sky of a",
        "sky blue is the old",
        "bag books sky of a",
        "sky blue is the old",
        "bag books sky of a",
        "sky blue is the old",
        "bag books sky of a",
        "sky blue is the old",
        "bag books sky of a",
        "sky blue is the old",
    ]

    num_rounds = len(task_1)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    user_text = models.StringField(verbose_name='Please form a sentence of four words with the above words.')

    def add_payoff(self):
        curr_payoff = 0
        high_win = c(self.session.config['task_1_high_win'])
        low_win = c(self.session.config['task_1_low_win'])
        if self.user_text != 0:
            curr_payoff = high_win if random.random() else low_win
        if 'payoff_array' in self.participant.vars:
            self.participant.vars['payoff_array'].append(curr_payoff)
        else:
            self.participant.vars['payoff_array'] = [curr_payoff]
