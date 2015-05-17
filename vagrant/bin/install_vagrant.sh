#!/bin/bash

VIRTUALENV_PATH=/home/vagrant/virtualenv
BACKEND_PATH=/home/vagrant/games

# Env vars
echo "export DJANGO_SETTINGS_MODULE='project.settings.vagrant'" >> /home/vagrant/.bash_profile

source /home/vagrant/.bash_profile


# Change to home vagrant folder.
cd ~

printf "\n* Preparing to install ubuntu required packages\n"
read -p "Press any key to continue..." -n1 -s

export DEBIAN_FRONTEND=noninteractive

# Use UTF-8 locale.
sudo locale-gen en_US.UTF-8

# Add postgres Apt repo.
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update
sudo apt-get -q -y install virtualenvwrapper
sudo apt-get -q -y install libpq-dev postgresql-9.4 postgresql-contrib-9.4 postgresql-client-9.4
sudo apt-get -q -y install python-dev
sudo apt-get -q -y install vim
sudo apt-get -q -y install git

printf "\n* Preparing to install virtualenv required packages from requirements.txt\n"
read -p "Press any key to continue..." -n1 -s
virtualenv virtualenv
source ${VIRTUALENV_PATH}/bin/activate
pip install -r ${BACKEND_PATH}/requirements.txt

printf "\n* Preparing to migrate django database (./manage.py migrate)\n"
read -p "Press any key to continue..." -n1 -s
${VIRTUALENV_PATH}/bin/python ${BACKEND_PATH}/manage.py migrate

printf "\n* Create default users\n"
read -p "Press any key to continue..." -n1 -s
${VIRTUALENV_PATH}/bin/python ${BACKEND_PATH}/manage.py createsuperuser