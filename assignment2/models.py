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
        "purple colorful a is rooom",
        "huge boring a was plane",
        "blue big a was bird",
        "red colorful a was night",
        "white angry a is rabbit",
        "rude stupid a is cow",
        "blue kind a was coat",
        "nice sad a is plane",
        "purple happy a was village",
        "blue colorful a is house",
        "coats the white were shiny",
        "cats the white were stupid",
        "rooms the repulsive were attractive",
        "rabbits the fat were boring",
        "hotels the awesome are weak",
        "thin village the were girls",
        "quiet cow the is coats",
        "fat corridor the was cats",
        "ugly room the is dogs",
        "fat street the was birds",
        "hot smelly a is room",
        "awful kind a is dog",
        "hot weak a was table",
        "quiet miserable a was table",
        "white angry a is hotel",
        "villages the odorous are miserable",
        "rabbits the fat were colorful",
        "dogs the purple were charming",
        "streets the purple were dark",
        "hats the rude are bright",
        "rude boy the were hotels",
        "hot bird the were corridors",
        "thin doctor the were teachers",
        "awesome coat the are pigs",
        "awful night the is pigs",
        "awful girl the was doctors",
        "joyous hospital the is boys",
        "quiet dog the were doctors",
        "orange town the were horses",
        "orange night the is hats",
        "ugly doctor the are planes",
        "light rabbit the are rabbits",
        "red teacher the were corridors",
        "thin hotel the are hospitals",
        "joyous hat the is boys",
        "orange hat the is corridors",
        "huge cow the are coats",
        "huge village the was doctors",
        "red dog the were bags",
        "repulsive boy the was pigs",
    ]

    num_rounds = len(task_2)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    user_text = models.StringField(verbose_name='Please form a sentence of four words with the above words.')
