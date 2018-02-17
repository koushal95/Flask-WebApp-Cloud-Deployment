# Flask-WebApp-Cloud-Deployment
A simple web application using flask that is deployed on Cloud

### Application
I have written a simple web application using flask that checks if an input string is a palindrome or not. The home page itself contains a form that lets the user to input the string to be checked for palindrome. The form data is posted to the server using post method and computation is done by the server and the result is returned. The result is displayed on the same page. The user interface is populated using the bootstrap theme that is embedded using the CDN. A link to the home is provided in the navigation bar just to reset the previous result.

### File Organization
The entry point to the application is the strPalindrome.py in the root folder. 

The application is developed in a virtual environment veni. 

All the configurations for the application are included in a file (config.py) seperate from the main file. 

The application is populated as a package thus containing its variables in __init__.py. 

The web forms are built as classes seperated from the control and are imported when needed. 

All the routes on url path are included in the routes.py

The views are maintained as seperate html files included in templates folder and rendered as needed.

### Python setup using wsgi for apache to handle the requests
First check if mod_wsgi is installed.
$ httpd -M | grep wsgi

if we could not find anything, we need to install mod_wsgi. we can search for wsgi using:

yum search wsgi

Choose the suitable version based on the apache and python version installed. I have python36 and apache24 so I did:

sudo yum install mod24_wsgi-python36.x86_64

Now, we need to create the .wsgi file for communication between apache and python wsgi. Note, the name should be same as the application folder. Thus I have strPalindrome.wsgi

The contents of the file, considering my folders, should be:

import os

import sys

import site

site.addsitedir(os.path.join(os.path.dirname(__file__), 'veni/lib/site-packages'))

sys.path.append('/var/www/html/strPalindrome')

activate_env = os.path.expanduser(os.path.join(os.path.dirname(__file__), 'veni/Scripts/activate'))

with open(activate_env) as file_:

    exec(file_.read(), dict(__file__=activate_env))

from strPalindrome import app as application

Now, we need to configure the apache to handle these requests. Since I am using a virtual environment I am creating a vhost.conf file in /etc/httpd/conf.d/vhost.conf

<VirtualHost *:80>

        WSGIDaemonProcess strPalindrome threads=5

        WSGIScriptAlias / /var/www/html/strPalindrome/strPalindrome.wsgi

        <directory /var/www/html/strPalindrome>

                WSGIProcessGroup strPalindrome

                WSGIApplicationGroup %{GLOBAL}

                WSGIScriptReloading On

                Require all granted

        </directory>

</VirtualHost>

Now, since the configuration is changed, we need to restart the server. It can be done using:

sudo service httpd restart

Note, all the files are supposed to be in the apache root directory (/var/www/html/). We should copy the files into this directory if we have build the application somewhere else. Note that the linking provided in linux will not work. Apache would not allow if we use the linking of directories. It simply does not allow symbolic links.

Also note that the above vhost.conf file is written for apache2.4 as it is the version I used, for previous versions the syntax for file permissions varies greatly. Instead of Require all granted we need to use

Order deny, allow

Allow from all

Also, please ensure that we have the permissions for the directory we are using (www/html/strPalindrome). This can be configured in /etc/httpd/conf/httpd.conf 

All the content above is compiled from different sources on the internet and personal experience handling obsolete directions in the sources. 
