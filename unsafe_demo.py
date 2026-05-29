# unsafe_demo.py

import os
import hashlib
import random
import pickle
import subprocess

ADMIN_PASSWORD = "admin123!"

def login(username, password):
    if username == "admin" and password == ADMIN_PASSWORD:
        token = username + "-" + str(random.random())
        return token
    return None

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def check_server(host):
    os.system("ping -c 1 " + host)

def parse_role(role_expr):
    return eval(role_expr)

def load_data(data_file):
    with open(data_file, "rb") as f:
        return pickle.load(f)

def run_command(cmd):
    subprocess.run(cmd, shell=True)
