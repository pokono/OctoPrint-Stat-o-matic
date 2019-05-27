#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive

sudo apt update -y
sudo DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade

# General tools.
sudo apt-get install -y \
   software-properties-common \
   apt-transport-https \
   ca-certificates \
   curl \
   vim \
   wget \
   unzip \
   nginx \
   zsh

# OctoPrint & tools.
sudo apt-get install -y \
    python \
    python-pip \
    python-dev \
    python-setuptools \
    python-virtualenv \
    git \
    libyaml-dev \
    build-essential

# UFW
sudo ufw allow 'Nginx HTTP'

# Fix line endings before using any provision files.
find /home/vagrant/provision -type f -print0 | xargs -0 dos2unix

# Nginx
#sudo mkdir --parents /etc/nginx/ssl
#sudo cp -r /home/vagrant/provision/ssl/* /etc/nginx/ssl/
sudo cp -r /home/vagrant/provision/sites-enabled/* /etc/nginx/sites-enabled/

# Secure config and restart services
sudo sed -i "s/^user www-data/user vagrant/" /etc/nginx/nginx.conf
sudo service nginx restart

# Setup OctoPrint.
git clone https://github.com/foosel/OctoPrint.git
cd OctoPrint
virtualenv venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -e .[develop,plugins]

# First start.
timeout 60 octoprint serve

# Enabling virtual printer.
cd ~/.octoprint
cat ~/provision/virtual-printer-config.yaml >> config.yaml

# Install Stat'o'matic plugin in dev mode.
cd ~/octoprint-stat-o-matic && octoprint dev plugin:install

# ZSH
# Install oh-my-zsh
sudo apt-get -y install zsh
sudo git clone git://github.com/robbyrussell/oh-my-zsh.git /home/vagrant/.oh-my-zsh
sudo cp /home/vagrant/provision/zshrc /home/vagrant/.zshrc
sudo chsh -s $(which zsh) vagrant
sudo git clone https://github.com/zsh-users/zsh-syntax-highlighting.git /home/vagrant/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
