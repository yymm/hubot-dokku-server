# hubot-dokku-server

[hubot-dokku](https://github.com/yymm/hubot-dokku "yymm/hubot-dokku: hubot script for dokku")'s server side app.

This app must run on the dokku server.

Require a fresh VM running Ubuntu 14.04 x64.

Require python 2.7 later, Flask (optional: and gunicorn and supervisor).

# Bootstraping

It is assumed vagrant VM.

```
$ git clone https://github.com/yymm/hubot-dokku-server.git
$ cd hubot-dokku-server
$ sudo bash bootstrap.sh
```

Before run supervisor daemon process: 0.0.0.0:5050.

If not vagrant VM, you rewrite supervisor.conf.example:

```
directory=/home/vagrant/hubot-dokku-server
```

to

```
directory=/home/<you>/hubot-dokku-server
```
