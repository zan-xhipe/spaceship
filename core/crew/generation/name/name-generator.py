#! /usr/bin/python3

import random
import json
import configparser

config = configparser.ConfigParser()
config.read('name.config')

first_file = config['Files']['First']
last_file = config['Files']['Last']

def name_list(filename):
    with open(filename) as in_file:
        return [line.strip() for line in in_file]

def random_name(first_names, last_names):
    first = random.choice(first_names)
    last = random.choice(last_names)
    return {"first": first, "last": last}
    
def random_names(num, first=first_file, last=last_file):
    first_names = name_list(first)
    last_names = name_list(last)
    return [random_name(first_names, last_names) for i in range(num)]    
    
names = random_names(3)
print(json.dumps(names))
