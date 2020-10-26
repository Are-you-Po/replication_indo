from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from Exp1_questionnaire.pages import Questionnaire
from Exp1_questionnaire.models import OptionOfGetMoney


class Intro_1(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.round_number == 1


class Intro_2(Page):
    form_model = 'player'
    def is_displayed(self):
        self.player.waiting_period = 3
        return self.round_number == 1


class Intro_4(Page):
    form_model = 'player'


    
class Intro_5(Page):
    form_model = 'player'
    


class Intro_comprehend_1(Questionnaire):
    form_model = 'player'
    form_fields = [ 
        'switch_point',
        'sooner_period',
        'waiting_period',
        'treatment_method',
        ]
    def is_displayed(self):
        self.player.waiting_period = 3
        self.player.sooner_period = 'hari ini'
        return True

    # def vars_for_template(self):
    #     return dict(
    #         audio_1 = OptionOfGetMoney.formatted_option(self.player) + " " + '110' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
    #         audio_2 = OptionOfGetMoney.formatted_option(self.player) + " " + '120' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
    #         audio_3 = OptionOfGetMoney.formatted_option(self.player) + " " + '130' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
    #         audio_4 = OptionOfGetMoney.formatted_option(self.player) + " " + '140' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
    #         audio_5 = OptionOfGetMoney.formatted_option(self.player) + " " + '150' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
    #         audio_6 = OptionOfGetMoney.formatted_option(self.player) + " " + '160' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
    #         audio_7 = OptionOfGetMoney.formatted_option(self.player) + " " + '170' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
    #         audio_8 = OptionOfGetMoney.formatted_option(self.player) + " " + '180' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
    #         audio_9 = OptionOfGetMoney.formatted_option(self.player) + " " + '190' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
    #         audio_10 = 'Saya menolak untuk menunggu.'
    #     )



class Intro_comprehend_2(Page):
    form_model = 'player'
    form_fields = [
        'comprehend',
        ]
    
    def before_next_page(self):
        if int(self.player.switch_point) < 5 and self.player.comprehend == 'd':
            self.player.comprehend_correct = True
        
        elif int(self.player.switch_point) >= 5 and self.player.comprehend == 'a':
            self.player.comprehend_correct = True

        else: self.player.comprehend_correct = False
        
        # elif int(self.player.switch_point) <= 5 and self.player.comprehend == 'a':
        #     self.player.comprehend_correct = False
        
        # elif int(self.player.switch_point) <= 5 and self.player.comprehend == 'b':
        #     self.player.comprehend_correct = False
        
        # elif int(self.player.switch_point) <= 5 and self.player.comprehend == 'c':
        #     self.player.comprehend_correct = False
        
        # elif int(self.player.switch_point) > 5 and self.player.comprehend == 'b':
        #     self.player.comprehend_correct = False
        
        # elif int(self.player.switch_point) and self.player.comprehend == 'c':
        #     self.player.comprehend_correct = False
        
        # elif int(self.player.switch_point) and self.player.comprehend == 'd':
        #     self.player.comprehend_correct = False


class Intro_success(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.player.comprehend_correct == True#   
        

class Intro_fail(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.player.comprehend_correct == False and self.round_number == 1#  

class Intro_fail_2(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.player.comprehend_correct == False and self.round_number == 2#  
    
    
# page_sequence = [Intro_7, Intro_8, Intro_fail]

page_sequence = [Intro_1, Intro_2, Intro_4, Intro_5, Intro_comprehend_1, Intro_comprehend_2, Intro_success, Intro_fail, Intro_fail_2]

