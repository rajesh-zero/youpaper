# youpaper
#made on django and postgresql


Application that allows you to track your Movies and TV shows

https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04
https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04



-------------------------ufw settings on linux vm-----------------------------------------------------
sudo vim /etc/default/ufw #IPV6=yes
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh or sudo ufw allow 22
sudo ufw enable

-----------------------installing pip postgresql and apache2-------------------
sudo apt update
sudo apt install python3-pip
sudo apt install python3-dev libpq-dev postgresql postgresql-contrib
sudo apt install apache2 libapache2-mod-wsgi-py3


-----------------------for apache2-------------------
sudo ufw app info "Apache Full"
sudo ufw allow in "Apache Full"

-----------------------for postgresql-------------------
sudo -u postgres psql
CREATE DATABASE youpaper;
CREATE USER youpaperuser WITH PASSWORD 'admin123';
ALTER ROLE youpaperuser SET client_encoding TO 'utf8';
ALTER ROLE youpaperuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE youpaperuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE youpaper TO youpaperuser;
\q

-----------------------for project-------------------
git clone https://github.com/rajesh-zero/youpaper.git
cd youpaper/
sudo pip3 install virtualenv
virtualenv env
source env/bin/activate
pip install django psycopg2 Pillow requests

vim youpaper/settings.py
    settings.py edit below

    ALLOWED_HOSTS = ['youpaper.westus2.cloudapp.azure.com','13.77.171.27']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'youpaper',
            'USER':'youpaperuser',
            'PASSWORD':'admin123',
            'HOST':'localhost'
        }
    }

    STATIC_ROOT = os.path.join(BASE_DIR, "static/")

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
sudo ufw allow 8000
python manage.py runserver 0.0.0.0:8000

sudo chown -R www-data:www-data /home/rajesh/youpaper/media

-----------------------for wsgi to host on apache2-------------------

sudo vim /etc/apache2/sites-available/000-default.conf

<VirtualHost *:80>
    . . .

    Alias /static /home/rajesh/youpaper/static
    <Directory /home/rajesh/youpaper/static>
        Require all granted
    </Directory>

    <Directory /home/rajesh/youpaper/youpaper>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess youpaper python-path=/home/rajesh/youpaper python-home=/home/rajesh/youpaper/env
    WSGIProcessGroup youpaper
    WSGIScriptAlias / /home/rajesh/youpaper/youpaper/wsgi.py

</VirtualHost>

sudo service apache2 restart

-------------------------------------------------------------------------------
