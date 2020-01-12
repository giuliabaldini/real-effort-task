from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.16666666666,
    participation_fee=1.00,
    doc="",
    mturk_hit_settings=dict(
        keywords='study, effort, economic, behaviour',
        title='Real Effort Task',
        description='Four effort tasks.',
        frame_height=500,
        template='global/mturk_template.html',
        minutes_allotted_per_assignment=60,
        expiration_hours=30 * 24,
        qualification_requirements=[
            {
                'QualificationTypeId': "3L1AJVA23GBAEV215TS6UOUNIITYLD",
                'Comparator': "DoesNotExist",
            },
        ],
        grant_qualification_id='3L1AJVA23GBAEV215TS6UOUNIITYLD',  # To prevent retakes
    )
)

SESSION_CONFIGS = [
    dict(
        name='effort_task',
        display_name="Real Effort Task",
        num_demo_participants=96,
        app_sequence=[
            'introduction',
            'assignment1',
            'assignment2',
            'assignment3',
            'assignment4',
            'payments'
        ],
        seconds_per_round=20,  # Duration of one round
        seconds_per_round_matrix=60,  # Duration of one matrix round
        minutes_per_task=5,  # Total duration
        high_win=6,
        low_win=0,
        increase=1,
        decrease=1,
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'GBMBMF'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# OTREE_PRODUCTION = 1
# OTREE_AUTH_LEVEL = 'DEMO'

# DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'mln9uy&2yx!1o(5n5@#1lqw50ft+t570d#c%-%a)li)f-@9u07'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
