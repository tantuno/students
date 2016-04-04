import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        #'USER': 'students_db_user',
        'USER': 'tantuno',
        'PASSWORD': 'hal1995',
        'NAME': 'students_db',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }
    }
}
