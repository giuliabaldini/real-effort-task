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

author = 'Giulia Baldini'

doc = """
Computes the matchings for the Real Effort task.
"""


class Constants(BaseConstants):
    name_in_url = 'payments'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    feedback = models.LongStringField(blank=True,
                                      verbose_name="Finally, if you have any comments or suggestions related to "
                                                   "this experiment please write them down in the blank space below. "
                                                   "Your feedback is very important to improve our research.")
