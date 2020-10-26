from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class pretest_instruction(Page): 
    form_model = 'player'

class pretest_1(Page): 
    form_model = 'player'
    form_fields = ['sound_check','num_listen_times','decision_duration']  
    
      

class pretest_success(Page):
    form_model = 'player' 
    def is_displayed(self):
        return self.player.sound_check == True#   
            # 一沒過就去二，ex. return player.Ans_two == '正確答案' #
       

class pretest_fail(Page): 
    form_model = 'player'
    def is_displayed(self):
        return self.player.sound_check != True            
        # 一沒過就去二，ex. return player.Ans_two == '正確答案' #
        

        

page_sequence = [pretest_instruction, pretest_1, pretest_success, pretest_fail]

