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
    name_in_url = 'payoff_click'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def compute_payoffs(self):
        high_win = c(self.session.config['task_3_high_win'])
        low_win = c(self.session.config['task_3_low_win'])

        p1 = self.get_players()[0]
        p2 = self.get_players()[1]
        if random.randint(0, 1):
            p1.participant.vars['ass3_payoff'] = high_win
            p2.participant.vars['ass3_payoff'] = low_win
        else:
            p1.participant.vars['ass3_payoff'] = low_win
            p2.participant.vars['ass3_payoff'] = high_win

        for p in self.get_players():
            print(p.participant.vars)


class Player(BasePlayer):
    pass
