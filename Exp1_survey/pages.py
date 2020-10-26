from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):
    form_model = 'player'
    form_fields = ['name','gender','bloodgroup','education','age','first_language','second_language','guess']


page_sequence = [Survey]
