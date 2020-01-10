from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield pages.InstructionsAssignment4

        # time.sleep(5)
        # if self.participant.vars['expiry_total'] - time.time() > 3:
        yield pages.Assignment4, dict(cb_0=1)

        if self.round_number == Constants.num_rounds:
            yield pages.Completed4
