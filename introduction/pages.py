from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    form_model = 'player'
    form_fields = ['consent']

    def is_displayed(self):
        return Constants.general_instructions

    def vars_for_template(self):
        email = 'projectMC2020@gmail.com'
        return {'email': email, 'participation': self.session.config['participation_fee'], 'conversion': c(6),
                'dollar': '$1'}

    def error_message(self, values):
        if values['consent'] == 0:
            return "You must consent to participate in the study."


class Part1(Page):
    pass


page_sequence = [
    Instructions,
    Part1]
