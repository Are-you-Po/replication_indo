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


author = 'Po-Yueh'

doc = """
印尼文實驗後問卷
"""


class Constants(BaseConstants):
    name_in_url = 'Exp1_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.StringField(label = "1. Apa jenis kelamin anda", widget = widgets.RadioSelect, choices = ["Pria", "Wanita", "Tidak ada yang di atas"])
    bloodgroup = models.StringField(label = "2. Apa golongan darah anda", widget = widgets.RadioSelect, choices = ["Tipe A", "Tipe B", "Tipe AB", "Tipe O", "Tidak tahu", "Tidak ada yang di atas"])
    education = models.StringField(label = "3. Apa tingkat pendidikan Anda", widget = widgets.RadioSelect, choices = ["SD", "SMTP", "SMTA", "S1","S2", "S3"])
    age = models.StringField(label = "4. Berapa usia anda?", )
    first_language = models.StringField(label = "5. Bahasa apa yang paling sering anda gunakan? (Bahasa yang paling nyaman untuk kalian gunakan? Pilih satu saja)", widget = widgets.RadioSelect, choices = ["Bahasa Indonesia", "Jawa", "Sunda", "Madura", "Bugis", "Inggris", "Cina, Taiwan,Hakka, Hokkien, Kanton...", "Lain"])
    second_language= models.StringField(label = "7.Selain bahasa Indonesia bahasa ibu Anda, apakah Anda bisa berbicara bahasa lain dengan lancar? Pilih satu saja)", widget = widgets.RadioSelect, choices = ["Bahasa Indonesia", "Jawa", "Sunda", "Madura", "Bugis", "Inggris", "Cina, Taiwan,Hakka, Hokkien, Kanton...", "Lain"])
    guess = models.LongStringField(label = "8.Menurut anda, apakah tujuan eksperimen ini?", )
    
