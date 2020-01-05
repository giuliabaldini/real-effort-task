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
    name_in_url = 'assignment1'
    players_per_group = None

    total_minutes = 5  # Total duration
    seconds_per_round = 20  # Duration of one round

    task_1 = [  # TODO: Change these to change the different sentences
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
        "tables the joyous were old",
        "teachers the empty are happy",
        "tables the repulsive are colorful",
        "birds the red were kind",
        "planes the lovely are heavy",
    ]

    num_rounds = len(task_1)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    user_text = models.StringField(verbose_name='Please form a sentence of four words with the above words.')
