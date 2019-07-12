#!/usr/bin/env bash
mkdir /var/bnms/{{cookiecutter.project_name}}
cd /var/bnms/{{cookiecutter.project_name}}
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements
cp setupfiles/{{cookiecutter.app_name}}.conf /etc/httpd/conf.d/.
chown -R apache:apache /var/bnms/{{cookiecutter.project_name}}

