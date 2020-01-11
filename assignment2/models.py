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

author = 'Giulia Baldini, Maria Bigoni, Marco Fabbri'

doc = """
Effort task in which the players create sentences of four words out of five given words.
"""


class Constants(BaseConstants):
    name_in_url = 'assignment2'
    players_per_group = None

    task_2 = [  # TODO: Change these to change the different sentences
        "purple table the were bags",
        "awesome doctor the was birds",
        "ugly room the was birds",
        "orange bird the are towns",
        "cold bag the was boys",
        "dirty tiny a is corridor",
        "small young a was girl",
        "dirty happy a is coat",
        "light rosy a is room",
        "huge beautiful a is hat",
        "cows the light were stupid",
        "streets the awful are weak",
        "corridors the white were stupid",
        "statues the small were vicious",
        "planes the joyous are bright",
        "huge pig the are rooms",
        "red plane the was corridors",
        "light boy the was bags",
        "nice cow the was cats",
        "lovely rabbit the was corridors",
        "blue noisy a is doctor",
        "repulsive sad a was coat",
        "rude happy a was hat",
        "huge weak a is plane",
        "lovely bright a is street",
        "cold green a is girl",
        "fat weak a is room",
        "orange old a was doctor",
        "cold weak a is village",
        "cold old a is street",
        "light happy a is cat",
        "awful dark a is street",
        "rude old a is bird",
        "awesome smelly a was town",
        "ugly miserable a was statue",
        "ugly big a is horse",
        "rude shiny a is table",
        "repulsive happy a was plane",
        "joyous shiny a was rooom",
        "joyous dark a was table",
        "ugly smelly a was coat",
        "orange boring a is rooom",
        "strong angry a is bag",
        "awesome weak a is cow",
        "huge vicious a was corridor",
        "nice sad a was dog",
        "red happy a was plane",
        "purple sad a is bag",
        "fat weak a was village",
        "fat big a is rooom",
    ]

    num_rounds = len(task_2)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    user_text = models.StringField(verbose_name='Please form a sentence of four words with the above words.')
