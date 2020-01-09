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
        "horses the red were stupid",
        "statues the purple are stupid",
        "statues the blue are sad",
        "planes the nice were stupid",
        "bags the red were boring",
        "boys the red were boring",
        "hotels the blue are colorful",
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
        "dirty village the is pigs",
        "joyous hospital the is boys",
        "red dog the were doctors",
        "huge hat the was villages",
        "awful night the were rooms",
        "repulsive doctor the are planes",
        "nice rabbit the are rabbits",
        "empty teacher the were corridors",
        "orange hotel the are hospitals",
        "joyous hat the is boys",
        "hot hat the is corridors",
        "orange cow the are coats",
        "orange village the was doctors",
        "crowded dog the were bags",
        "nice boy the was pigs",
        "hot bag the are nights",
        "small pig the was bags",
        "repulsive night the was streets",
        "huge boy the are pigs",
        "rude cat the is hotels",
        "strong coat the was cows",
        "rude house the are statues",
        "odorous pig the is planes",
        "small rabbit the is tables",
        "nice cat the were dogs",
        "quiet table the were villages",
        "strong hotel the was boys",
        "strong bag the was boys",
        "white coat the is bags",
        "blue pig the were hats",
        "nice teacher the were statues",
        "white coat the is hospitals",
        "blue girl the is streets",
        "red horse the are dogs",
        "blue pig the is hats",
        "blue teacher the is boys",
        "red corridor the was houses",
        "blue doctor the are coats",
    ]

    num_rounds = len(task_2)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    user_text = models.StringField(verbose_name='Please form a sentence of four words with the above words.')
