from squidhelper import squid_module
import sys
import syslog
import re

redis = squid_module.redis_con("172.17.0.2")

while True:
    ip_to_check = input()
    #print(squid_module.check_ip_rule(redis, sys.argv[0]))
    print(squid_module.check_ip_rule(redis, ip_to_check))