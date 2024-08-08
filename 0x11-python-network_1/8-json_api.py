#!/usr/bin/python3
"""
script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


if __name__ == '__main__':
    import sys
    import requests

    r = requests.get('http://0.0.0.0:5000/search_user')
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ''

    try:
        result = r.josn()
        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
