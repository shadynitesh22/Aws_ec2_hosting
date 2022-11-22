#!/bin/sh

#<-----------Access Jump Server---------->

sudo ssh -i password.pem nileshp@jump.benekiva.io -p 2020

#<-------Create .pem file in jump server-------------->

touch selenium-server-key.pem
sudo nano selenium-server-key.pem

#<----Make .pem private by denying access to others.----->
chmod 700 selenium-server-key.pem

#<-------Acess Test server--------->

ssh -i selenium-server-key.pem ubuntu@18.219.125.205

