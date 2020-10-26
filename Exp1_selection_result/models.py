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

from Exp1_questionnaire.models import GainedAmount

author = 'Po Yueh'

doc = """
印尼文實驗-結果部分
"""


class Constants(BaseConstants):
    name_in_url = 'Exp1_selection_result'
    players_per_group = None
    num_rounds = 1

    gained_amount_soon = GainedAmount.soon


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
