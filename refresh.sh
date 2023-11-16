#!/bin/sh
bench build --apps ams
sudo supervisorctl stop all
sudo supervisorctl start all