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

from Exp1_questionnaire.models import (
    WaitingPeriod,
    GainedAmount,
    Treatment,
    OptionOfGetMoney,
)

import json

author = 'FuHsuan Tsai'

doc = """
印尼文實驗-說明部分
"""


class Constants(BaseConstants):
    name_in_url = 'Exp1_intro'
    players_per_group = None
    num_rounds = 2
    key_method = 'treatment_method'
    gainedamount_sooner = GainedAmount.soon
    futureTense = Treatment.futureTense


class Subsession(BaseSubsession):
    num_questions = models.IntegerField() # 實際上的回合數
    
    def creating_session(self):
        self.num_questions = len(WaitingPeriod.list)
        
        config = self.session.config
        json_string = config['available_waiting_periods']
        WaitingPeriod.list = json.loads(json_string)

        json_string = config['available_gained_amounts']
        GainedAmount.list =  json.loads(json_string)

        for p in self.get_players():
            p.treatment_method = Treatment.get_treatment(p)
    

class Group(BaseGroup):
    pass


class Player(BasePlayer):
     waiting_period = models.IntegerField()
     treatment_method = models.StringField()
     sooner_period = models.StringField()
     comprehend_correct = models.BooleanField()

     switch_point = models.StringField(
         label = 'Silakan pilih "situasi" Anda',
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
            

     comprehend = models.StringField(
        label = 'Berdasarkan pilihan anda, opsi manakah yang benar dibawah ini?', 
        widget = widgets.RadioSelect, 
     )    
     def comprehend_choices(self):
         return [
             ['a', 'Anda akan menerima 100 token hari ini.'],
             ['b', 'Anda akan menerima 100 token 3 minggu kemudian.'],
             ['c', 'Anda akan menerima 150 token hari ini.'],
             ['d', 'Anda akan menerima 150 token 3 minggu kemudian.'],
             ]


         

   