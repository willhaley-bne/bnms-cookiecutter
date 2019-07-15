#!/usr/bin/env bash
cd /var/bnms/{{cookiecutter.project_name}}
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp setupfiles/{{cookiecutter.app_name}}.conf /etc/httpd/conf.d/.
semanage port -a -t http_port_t -p tcp {{cookiecutter.port_number}}
firewall-cmd --zone=public --add-port={{cookiecutter.port_number}}/tcp --permanent
chown -R apache:apache /var/bnms/{{cookiecutter.project_name}}

echo "Now verify settings, append the proxy configs, and restart httpd"
