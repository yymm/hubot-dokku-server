# ubuntu 14.04
sudo apt-get update -y
sudo apt-get install python-pip -y
sudo pip install flask gunicorn
sudo apt-get install supervisor -y
sudo cat supervisor.conf.example > /etc/supervisor/conf.d/hubot-dokku-server.conf
sudo supervisorctl update
