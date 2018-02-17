import os
import sys
import site

# Add virtualenv site packages
site.addsitedir(os.path.join(os.path.dirname(__file__), 'veni/lib/site-packages'))

# Path of execution
sys.path.append('/var/www/html/strPalindrome')

# Fired up virtualenv before include application
activate_env = os.path.expanduser(os.path.join(os.path.dirname(__file__), 'veni/Scripts/activate'))
with open(activate_env) as file_:
        exec(file_.read(), dict(__file__=activate_env))

# import my_flask_app as application
from strPalindrome import app as application
