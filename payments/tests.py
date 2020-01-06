from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Payments
        yield pages.Feedback, dict(feedback="Bot feedback")
        yield Submission(pages.Completion, check_html=False)
