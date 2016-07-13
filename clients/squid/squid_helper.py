from .squidhelper import *
import sys
import syslog
import re
import yaml

with open('./squid_helper.yml','r') as conf_file:
    conf = yaml.load(conf_file)

host = conf['redis']['server']
port = conf['redis']['port']
password = conf['redis']['password']

redis = squid_module.redis_con(host,port,password)

while True:
    ip_to_check = input()
    print(squid_module.check_ip_rule(redis, ip_to_check))