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


author = 'PoYueh'

doc = """
確認聽力設備
"""


class Constants(BaseConstants):
    name_in_url = 'Exp1_pretest'
    players_per_group = None
    num_rounds = 1
    pretest_num = 'dua puluh lima'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sound_check = models.BooleanField(
        label = 'Mohon pilih angka yang anda dengarkan dari audio di atas.', widget=widgets.RadioSelect, 
        choices=[
            [False, '45'],
            [False, '21'],
            [True, '25'],
            [False, '46'],
            ]
        )

    # 聽了幾次，單位為次數 (hidden，根據使用者行為紀錄)
    num_listen_times = models.IntegerField(initial = 0)

    # 決策時長，單位為秒數 (hidden，根據使用者行為紀錄)
    decision_duration = models.FloatField(initial = 0)
