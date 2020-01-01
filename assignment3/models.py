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
    name_in_url = 'assignment3'
    players_per_group = None

    example = [123, 231, 952, 864, 123, 791, 283, 123, 641, 820, 462, 123]

    task_3_nums = {  # TODO: Add the correct numbers for every round
        1: [123, 231, 952, 864, 123, 791, 283, 123, 641, 820, 462, 123, 123, 231, 952, 864, 123, 791, 283, 123, 641,
            820, 462, 123],
        2: [123, 231, 952, 864, 123, 791, 283, 123, 641, 820, 462, 123, 123, 231, 952, 864, 123, 791, 283, 123, 641,
            820, 462, 123]
    }

    task_3_find = [123, 231]  # TODO: Add the correct numbers to find
    num_rounds = len(task_3_find)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_checkbox():
    return models.IntegerField(default=0, blank=True)


def return_fields(nums):
    start = 'cb_'
    forms = []
    for i in range(0, len(nums)):
        forms.append(start + str(i))
    return forms


class Player(BasePlayer):
    cb_0 = make_checkbox()
    cb_1 = make_checkbox()
    cb_2 = make_checkbox()
    cb_3 = make_checkbox()
    cb_4 = make_checkbox()
    cb_5 = make_checkbox()
    cb_6 = make_checkbox()
    cb_7 = make_checkbox()
    cb_8 = make_checkbox()
    cb_9 = make_checkbox()
    cb_10 = make_checkbox()
    cb_11 = make_checkbox()
    cb_12 = make_checkbox()
    cb_13 = make_checkbox()
    cb_14 = make_checkbox()
    cb_15 = make_checkbox()
    cb_16 = make_checkbox()
    cb_17 = make_checkbox()
    cb_18 = make_checkbox()
    cb_19 = make_checkbox()
    cb_20 = make_checkbox()
    cb_21 = make_checkbox()
    cb_22 = make_checkbox()
    cb_23 = make_checkbox()
    cb_24 = make_checkbox()
    cb_25 = make_checkbox()

    # TODO: Add as many as the number of numbers per task
