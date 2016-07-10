import os
import redis
import rq

def redis_con(host,port,password):
    con = redis.Redis(host=host,port=port,password=password)
    return con

def check_ip_rule(obj,key=""):
    value = obj.get(key)
    return value