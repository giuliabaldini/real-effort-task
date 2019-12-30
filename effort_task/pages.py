from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    form_model = ['player']
    form_fields = ['consent']

    def error_message(self, values):
        if values['consent'] == 0:
            return "You must consent to participate in the study."


class Assignment1(Page):
    pass


class Assignment2(Page):
    pass


class Assignment3(Page):
    pass


class Assignment4(Page):
    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Assignment1,
    Assignment2,
    Assignment3,
    Assignment4,
    ResultsWaitPage,
    Results]
