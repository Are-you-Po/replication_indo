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


author = 'Po Yueh'

doc = """
Attention Check
"""


class Constants(BaseConstants):
    name_in_url = 'Exp1_attention_check'
    players_per_group = None
    num_rounds = 1
    sentence_one = 'Siapa presiden Indonesia saat ini' #誰是印尼現任的總統？
    sentence_two = 'Apa Ibukota Indonesia saat ini?' #哪個是印尼現在的首都？
    sentence_three = 'Saya harap pesan film ini bisa sampai tentang perlunya komunikasi dalam keluarga.'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Ans_one = models.BooleanField(
        label = '請根據您聽到的問題，選出最適合的答案', widget=widgets.RadioSelect, 
        choices=[
            [False, 'Jakarta'],
            [False, 'Kucing'],
            [True, 'Joko Widodo'],
            [False, 'Maynila Mahathir bin Mohamad'],
            ]
        )

    Ans_two = models.BooleanField(
        label = '請根據您聽到的問題，選出最適合的答案', widget=widgets.RadioSelect, 
        choices=[
            [False, 'Joko Widodo'],
            [False, 'Mahathir bin Mohamad'],
            [True, 'Jakarta'],
            [False, 'Surabaya'],
            ]
        )

    Ans_three = models.LongStringField(label = '請用印尼文寫下您聽到的句子')
        

    # 聽了幾次，單位為次數 (hidden，根據使用者行為紀錄)
    num_listen_times = models.IntegerField(initial = 0)

    # 決策時長，單位為秒數 (hidden，根據使用者行為紀錄)
    decision_duration = models.FloatField(initial = 0)
