from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    # dict(
    #    name='public_goods',
    #    display_name="Public Goods",
    #    num_demo_participants=3,
    #    app_sequence=['public_goods', 'payment_info']
    # ),
    dict(
        name='Indonesian_Experiment',
        display_name="Exp1",
        num_demo_participants=3,
        app_sequence=[
            # 'Exp1_pretest',
            # 'Exp1_intro',
            'Exp1_questionnaire',
            # 'Exp1_survey',
            # 'Exp1_selection_result',
            # 'Exp1_finished',
            ],

        # Configure sessions https://otree.readthedocs.io/en/latest/treatments.html#configure-sessions
        available_waiting_periods='[10, 20, 40, 80, 54, 64, 84, 124]',
        #available_waiting_periods='[["present", 1], ["present", 2], ["present", 4], ["present", 8], ["4 weeks from present", 5], ["4 weeks from present", 6], ["4 weeks from present", 8], ["4 weeks from present", 12]]',
        available_gained_amounts='[110, 120, 130, 140, 150, 160, 170, 180, 190]',
        doc="""
            請在「Configure session 的 Custom 中」定義所有「等待週數」和「獲得金額」的列表
            """
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'xwh-a^^ly_(cgw*^cabtz8anzs8!ak7tcf$req)==%ox4_j*6@'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
