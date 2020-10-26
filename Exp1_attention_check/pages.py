from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Attention_instruction(Page): 
    form_model = 'player'

class Attention_1(Page): 
    form_model = 'player'
    form_fields = ['Ans_one','num_listen_times','decision_duration']  
    

class Attention_2(Page): 
    form_model = 'player'
    form_fields = ['Ans_two','num_listen_times','decision_duration']  #這裡存的是要在這頁顯示給受試者看得變數們
  
            

class Attention_3(Page): 
    form_model = 'player'
    form_fields = ['Ans_three','num_listen_times','decision_duration']  #待改
    
      


        

page_sequence = [Attention_instruction, Attention_1, Attention_2, Attention_3]
