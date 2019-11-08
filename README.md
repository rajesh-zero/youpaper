# youpaper
#made on django and postgresql


Application that allows you to track your Movies and TV shows

https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04
https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04


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
