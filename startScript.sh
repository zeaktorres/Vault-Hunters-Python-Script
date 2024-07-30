#!/bin/bash
yum update -y
yum install -y python
yum install -y pip
yum install -y java
python -m pip install boto3
wget -P /home/ec2-user https://raw.githubusercontent.com/zeaktorres/Vault-Hunters-Python-Script/main/run.py
python /home/ec2-user/run.py > /home/ec2-user/out.txt
