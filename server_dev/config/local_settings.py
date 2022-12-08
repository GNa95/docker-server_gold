
SECRET_KEY = 'ts5zvye^bxn8jnry3c!1amy4-xwcr@^4j1vba!s9@b(2ne@1&5'

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'golddb',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '172.31.29.179',
        'PORT': '3306',
    }
}
