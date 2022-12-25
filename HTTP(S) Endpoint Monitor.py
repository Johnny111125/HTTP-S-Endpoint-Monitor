import re
import requests
import time

def print_green(text):
    print(f"\033[92m{text}\033[0m")

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def check_endpoint(endpoint, pattern):
    try:
        r = requests.get(endpoint)
        if r.status_code == 200:
            if re.search(pattern, r.text):
                print_green(f"{endpoint} is up and the pattern was found")
            else:
                print_red(f"{endpoint} is up but the pattern was not found")
        else:
            print_red(f"{endpoint} is down")
    except:
        print_red(f"{endpoint} is down")

endpoints = ["http://example.com", "http://example.org", "http://example.net"]
pattern = input("Enter the pattern to search for: ")

while True:
    for endpoint in endpoints:
        check_endpoint(endpoint, pattern)
    time.sleep(60)