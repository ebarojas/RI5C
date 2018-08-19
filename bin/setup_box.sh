#!/usr/bin/env bash

echo "=> Start config box..."
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev wget python-pip python-dev libffi-dev
sudo apt-get install -y git
sudo pip install -U pip
sudo pip install -U pyOpenSSL

# Install PostgreSQL
echo "=> Installing postgresql"
sudo apt-get install -y libpq-dev postgresql postgresql-contrib libxml2-dev libxslt1-dev zlib1g-dev build-essential libssl-dev libffi-dev
# Create database if not exist
sudo -i -u postgres psql -tc "SELECT 1 FROM pg_database WHERE datname = 'mydb'" | grep -q 1 || sudo -i -u postgres psql -c "CREATE DATABASE mydb"

# Create user
echo "=> Creating psql user and granting privileges"
sudo -i -u postgres psql -c "CREATE USER vagrant WITH PASSWORD 'vagrant';"
sudo -i -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE mydb TO vagrant;"

echo "=> Installing requirements..."
sudo pip install -r /vagrant/requirements.txt

echo "=> End config box..."
