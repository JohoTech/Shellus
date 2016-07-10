import os
import redis
import rq
import yaml

with open('../squid_helper.yml','r') as conf_file:
    conf = yaml.load(conf_file)

host = conf['redis']['server']
port = conf['redis']['port']
password = conf['redis']['password']

def redis_con(host,port,password):
    con = redis.Redis(host=host,port=port,password=password)
    return con

def check_ip_rule(obj,key=""):
    value = obj.get(key)
    return value