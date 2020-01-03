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
    name_in_url = 'payoff_scramble'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def compute_payoffs(self):
        high_win = c(self.session.config['task_1_high_win'])
        low_win = c(self.session.config['task_1_low_win'])

        p1 = self.get_players()[0]
        p2 = self.get_players()[1]
        p1.participant.vars['ass1_partner'] = p2.participant.id_in_session
        p2.participant.vars['ass1_partner'] = p1.participant.id_in_session
        if random.randint(0, 1):
            p1.participant.vars['ass1_payoff'] = high_win
            p2.participant.vars['ass1_payoff'] = low_win
        else:
            p1.participant.vars['ass1_payoff'] = low_win
            p2.participant.vars['ass1_payoff'] = high_win

        p1.save_matching()
        p2.save_matching()


class Player(BasePlayer):
    matching_info_ass1 = models.LongStringField(initial='')

    def save_matching(self):
        # TODO: Add more fields if needed
        relevant = ['ass1_partner', 'ass1_payoff']
        for r in relevant:
            self.matching_info_ass1 += str(self.participant.vars[r]) + ","
