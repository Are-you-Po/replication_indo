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
from enum import Enum
import random
import json
author = 'Fushuan Tsai'

doc = """
印尼文實驗：問卷主體
"""
class WaitingPeriod(object):
    list = [10, 20, 40, 80, 54, 64, 84, 124]

class GainedAmount(object):
    list = []
    soon = 100

class Treatment(object):
    futureTense = "akan"
    def get_treatment(player):
        participant = player.participant
        # lazy loading: 若不存在就決定並起來，若已存在就直接取出
        if Constants.key_method not in participant.vars:
            participant.vars[Constants.key_method] = random.choice(["FT", "NFT"])
        method = participant.vars[Constants.key_method]
        return method


class Constants(BaseConstants):
    name_in_url = 'Exp1_questionaire'
    players_per_group = None
    gainedamount_sooner = GainedAmount.soon
    num_rounds =8  # 這裡代表最大可能 rounds (SINGLE SOURCE OF THE TRUTH)
    key_params = 'questionnaire_parameters'
    key_selected_q = 'selected_questionaire' # 這個變數作用還要需搞清楚
    key_method = 'treatment_method'
    futureTense = Treatment.futureTense
    select_num = random.randint(1, 9) #這個是拿來抽報酬用的基準點，還不確定這樣寫是否正確

    def actual_num_rounds():
        return Constants.num_rounds
    

class OptionOfGetMoney(object):
    part1 = 'Saya'
    part2 = 'menerima'
    part3 = 'minggu kemudian.'
    def formatted_option(player):  #self代表OptionGetMoney,從自己身上得到part1~3
        if player.treatment_method == "NFT":
            return OptionOfGetMoney.part1 + " " + OptionOfGetMoney.part2
        elif player.treatment_method == "FT":
            return OptionOfGetMoney.part1 + " " + Constants.futureTense + " " + OptionOfGetMoney.part2
        

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.treatment_method = Treatment.get_treatment(p)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    waiting_period = models.IntegerField()
    treatment_method = models.StringField()
    sooner_period = models.StringField()

    # audio_1 = str(OptionOfGetMoney.formatted_option） + " " + '110' + " token, " + str(self.waiting_period) + " " + OptionOfGetMoney.part3


    switch_point = models.StringField(
        label = 'Silakan pilih "situasi" Anda', # 須看這句是否通順
        widget = widgets.RadioSelect,
    )
    
    def switch_point_choices(self):
        options_part1 = OptionOfGetMoney.formatted_option(self)
        options_1 = options_part1 + " "
        options_2 = " token, " + str(self.waiting_period) + " " + OptionOfGetMoney.part3

        return [
            #['test', str(type(Constants.spaces))],
            ['1', options_1 + '110' + options_2],
            ['2', options_1 + '120' + options_2],
            ['3', options_1 + '130' + options_2],
            ['4', options_1 + '140' + options_2],
            ['5', options_1 + '150' + options_2],
            ['6', options_1 + '160' + options_2],
            ['7', options_1 + '170' + options_2],
            ['8', options_1 + '180' + options_2],
            ['9', options_1 + '190' + options_2],
            ['10', 'Saya menolak untuk menunggu.'],
        ]

    # 是否為最後電腦選中的 round (hidden，最後一回合會抽出並寫入)
    is_selected = models.BooleanField(initial = False)

        

    


