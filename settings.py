from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
        name='effort_task',
        display_name="Real Effort Task",
        num_demo_participants=100,
        app_sequence=[
            'introduction',
            'assignment1',
            'payoff_scramble',
            'assignment3',
            'payoff_click',
            'payments'
        ],
        participation_fee=2,
        task_1_high_win=6,
        task_1_low_win=0,
        task_3_high_win=6,
        task_3_low_win=0,
        redistribution_high=6,
        redistribution_low=0,
        inc_1=1,
        dec_1=1,
        inc_2=1,
        dec_2=2,
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

OTREE_PRODUCTION = 1
# OTREE_AUTH_LEVEL = 'DEMO'
OTREE_AUTH_LEVEL = 'STUDY'

# DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'mln9uy&2yx!1o(5n5@#1lqw50ft+t570d#c%-%a)li)f-@9u07'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
