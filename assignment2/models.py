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

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'effort_task'
    players_per_group = None
    num_rounds = 1
    general_instructions = True


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.IntegerField(initial=None,
                                  choices=[
                                      [1, 'Yes'],
                                      [0, 'No'],
                                  ],
                                  verbose_name='I have read and understood the the above and want to participate in this study.',
                                  widget=widgets.RadioSelectHorizontal())
