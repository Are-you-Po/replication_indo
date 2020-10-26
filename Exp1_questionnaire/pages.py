from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, WaitingPeriod, GainedAmount, OptionOfGetMoney
from random import randint
import random

class Questionnaire(Page):
    form_model = 'player'
    form_fields = [
        'waiting_period',
        'sooner_period',
        'treatment_method',
        'switch_point', # 等於是allen的'get_money_now_or_future'決策變數
        ]

    def generate_questionnaire_parameters(self):
        shuffled_waiting_period = WaitingPeriod.list
        random.shuffle(shuffled_waiting_period) # 打亂順序
        return shuffled_waiting_period # 產生random的「延後週數數列」

    def setup_questionaire_parameters_pairs(self):
        # 如果還不存在，就現在產生「週數和金額的組合」並存起來
        # 如果已經存在，就取出
        if Constants.key_params not in self.participant.vars:
            shuffled_waiting_period = self.generate_questionnaire_parameters()
            self.participant.vars[Constants.key_params] = shuffled_waiting_period
        params = self.participant.vars[Constants.key_params]

        # 設定每一 round 的參數，並寫入 db
        idx = self.round_number - 1 # list 從0開始 但 round_bnumber 從1開始
        self.player.waiting_period = int(params[idx] / 10)
        sooner_period = int(params[idx] % 10)
        
        if sooner_period == 0:
            self.player.sooner_period = 'hari ini'
        elif sooner_period == 4:
            self.player.sooner_period = '4 minggu kemudian'

    def select_questionaire(self):
        q_params = self.participant.vars[Constants.key_params] #存入random的「延後週數數列」
        selected_idx = randint(1, Constants.actual_num_rounds()) - 1 # list 的 index 從0開始 但 round_bnumber 從1開始 / 需再確認allen的actual_num_rounds()函數意思
        selected_q_parama = q_params[selected_idx]
        selected_player = self.player.in_all_rounds()[selected_idx]
        selected_player.is_selected = True
        self.participant.vars[Constants.key_selected_q] = dict(
            selected_round_number = selected_idx + 1,  #儲存抽中的回合數
            selected_waiting_period = selected_q_parama, #儲存由「random的延後週數數列」抽到的延後週數
            selected_sooner_period = self.player.sooner_period, #抓出儲存受試者在被抽到的那個回合的sooner period
            selected_gained_amount = Constants.select_num *10 + 100, #儲存抽報酬用的基準點，相對應的金額
            selected_get_money_later = int(selected_player.switch_point) > int(Constants.select_num), #selected_get_money_later是一Dummy Variable: get sooner reward=1;get later reward==0。若受試者在被抽到那回合的switch_point > select_num，代表她不想換過去。
            )
            
    def is_displayed(self): # 一定會跑的
        # 設定每一 round 的參數（如週數和金額）
        self.setup_questionaire_parameters_pairs()
        return True

    def before_next_page(self):
        if self.round_number == Constants.num_rounds:
            # 只在最後一回合才抽結果
            self.select_questionaire()

    def vars_for_template(self):
        return dict(
            audio_1 = OptionOfGetMoney.formatted_option(self.player) + " " + '110' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
            audio_2 = OptionOfGetMoney.formatted_option(self.player) + " " + '120' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
            audio_3 = OptionOfGetMoney.formatted_option(self.player) + " " + '130' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
            audio_4 = OptionOfGetMoney.formatted_option(self.player) + " " + '140' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
            audio_5 = OptionOfGetMoney.formatted_option(self.player) + " " + '150' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
            audio_6 = OptionOfGetMoney.formatted_option(self.player) + " " + '160' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
            audio_7 = OptionOfGetMoney.formatted_option(self.player) + " " + '170' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
            audio_8 = OptionOfGetMoney.formatted_option(self.player) + " " + '180' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
            audio_9 = OptionOfGetMoney.formatted_option(self.player) + " " + '190' + " token, " + str(self.player.waiting_period) + " " + OptionOfGetMoney.part3,
            audio_10 = "Saya menolak untuk menunggu."
            # audio = audio_1 + " " + audio_2 +  " " + audio_3 + " " + audio_4 + " " + audio_5 + " " + audio_6 + " " + audio_7 + " " + audio_8 + " " + audio_9 + " " + audio_10
        )


page_sequence = [Questionnaire]
