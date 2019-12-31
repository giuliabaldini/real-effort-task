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
    name_in_url = 'assignment1'
    players_per_group = None
    total_minutes = 5
    seconds_per_round = 20
    sentences = [
        "bag books sky of a",
        "sky blue is the old",
        "bag books sky of a",
        "sky blue is the old",
        "bag books sky of a",
        "sky blue is the old",
        "bag books sky of a",
        "sky blue is the old",
        "bag books sky of a",
        "sky blue is the old"
    ]

    num_rounds = len(sentences)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    user_text = models.StringField(verbose_name='Please form a sentence of four words with the above words.')
