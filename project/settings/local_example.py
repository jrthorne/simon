###########################################################################
FileName        = 'local.py'
# By:            Jason Thorne
# Date:            19-08-2015
# Description:     The simon project. This is an example of what is needed
# in each local settings file. Each social auth key needs to be tied to 
# the domain it is served from, so a different set of keys is needed
# for each instance of this app. Though the application will run without
# this file, no one will be able to log in.
# NOTE: This is an example file. Rename to 'local.py' to use it.
##################################################################
import sys
globals().update(vars(sys.modules['settings']))

# to install a local only application
#INSTALLED_APPS += ('another_app',)

SITE_ID = 1

DEBUG=True
# don't send emails from development machine
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ""
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ""

# twitter
SOCIAL_AUTH_TWITTER_KEY =  ""
SOCIAL_AUTH_TWITTER_SECRET = ""
