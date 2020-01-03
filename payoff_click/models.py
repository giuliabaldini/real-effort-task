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
WaitPage to create groups and confirm the successful completion of the third task.
"""


class Constants(BaseConstants):
    name_in_url = 'payoff_click'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):

    def group_by_arrival_time_method(self, waiting_players):
        players_scores = [p.participant.vars['player_score'] for p in waiting_players]
        for i in range(0, len(players_scores)):
            for j in range(i + 1, len(players_scores)):
                if players_scores[i] != players_scores[j]:
                    return [waiting_players[i], waiting_players[j]]


class Group(BaseGroup):
    def compute_payoffs(self):
        high_win = c(self.session.config['task_3_high_win'])
        low_win = c(self.session.config['task_3_low_win'])

        p1 = self.get_players()[0]
        p2 = self.get_players()[1]
        p1.participant.vars['ass3_partner'] = p2.participant.id_in_session
        p2.participant.vars['ass3_partner'] = p1.participant.id_in_session
        if p1.participant.vars['player_score'] > p2.participant.vars['player_score']:
            p1.participant.vars['ass3_payoff'] = high_win
            p2.participant.vars['ass3_payoff'] = low_win
        else:
            p1.participant.vars['ass3_payoff'] = low_win
            p2.participant.vars['ass3_payoff'] = high_win

        p1.save_matching()
        p2.save_matching()


class Player(BasePlayer):
    matching_info_ass3 = models.LongStringField(initial='')

    def save_matching(self):
        # TODO: Add more fields if needed
        relevant = ['ass3_partner', 'player_score', 'ass3_payoff']
        for r in relevant:
            self.matching_info_ass3 += str(self.participant.vars[r]) + ","
