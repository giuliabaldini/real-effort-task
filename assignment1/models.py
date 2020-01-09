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

    task_1 = [  # TODO: Change these to change the different sentences
        "quiet bag the are nights",
        "odorous pig the was bags",
        "light night the was streets",
        "lovely boy the are pigs",
        "red cat the is hotels",
        "red coat the was cows",
        "small house the are statues",
        "odorous pig the is planes",
        "fat rabbit the is tables",
        "quiet cat the were dogs",
        "fat table the were villages",
        "rude hotel the was boys",
        "blue bag the was boys",
        "blue coat the is bags",
        "rude pig the were hats",
        "red teacher the were statues",
        "purple coat the is hospitals",
        "nice girl the is streets",
        "blue horse the are dogs",
        "blue teacher the is boys",
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
        "hats the quiet are stupid",
        "planes the white were noisy",
        "cows the quiet were dark",
        "teachers the light are vicious",
        "hats the awful were disgusting",
        "streets the red were disgusting",
        "streets the awesome are miserable",
        "horses the white are stupid",
        "girls the strong are old",
        "towns the white were kind",
        "roooms the quiet were weak",
        "nights the awful were tired",
        "rabbits the strong are disgusting",
        "boys the quiet were rosy",
        "nights the nice are kind",
        "cats the light are green",
        "planes the red are sad",
        "pigs the joyous were attractive",
        "coats the rude are attractive",
        "hotels the odorous are tired",
        "hospitals the fat are tiny",
        "dogs the repulsive are miserable",
        "hospitals the huge are happy",
        "boys the purple are angry",
        "villages the purple were happy",
    ]

    num_rounds = len(task_1)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    user_text = models.StringField(verbose_name='Please form a sentence of four words with the above words.')
