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

    total_minutes = 5  # Total duration
    seconds_per_round = 20  # Duration of one round

    task_2 = [  # TODO: Change these to change the different sentences
        "strong shiny a was coat",
        "nice big a is night",
        "blue young a was bird",
        "red young a is coat",
        "fat green a was room",
        "villages the awful are heavy",
        "planes the white are weak",
        "villages the orange were bright",
        "dogs the repulsive were beautiful",
        "teachers the quiet were shiny",
        "rude doctor the is tables",
        "joyous table the is hats",
        "small street the was boys",
        "thin hat the were rooms",
        "joyous room the was hospitals",
        "lovely vicious a was room",
        "empty charming a is room",
        "strong shiny a was town",
        "red happy a was dog",
        "hot tired a was bird",
        "statues the cold are angry",
        "teachers the empty were shiny",
        "pigs the quiet were miserable",
        "rooms the strong were big",
        "statues the small are kind",
        "rude doctor the is cows",
        "awesome house the are rooms",
        "blue hotel the is coats",
        "odorous room the were rooms",
        "lovely hospital the is coats",
        "orange kind a is street",
        "lovely boring a was statue",
        "awesome heavy a was room",
        "lovely old a is cat",
        "thin angry a was statue",
        "teachers the thin are young",
        "pigs the brown are green",
        "houses the joyous were beautiful",
        "statues the joyous are smelly",
        "tables the rude were weak",
        "huge horse the is nights",
        "light rabbit the are towns",
        "purple bag the was doctors",
        "crowded bag the were towns",
        "repulsive plane the were teachers",
        "yellow sad a is street",
        "nice noisy a is town",
        "ugly green a was village",
        "light young a was pig",
        "thin old a was corridor",
    ]

    num_rounds = len(task_2)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    user_text = models.StringField(verbose_name='Please form a sentence of four words with the above words.')
