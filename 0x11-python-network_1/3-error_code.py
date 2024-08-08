#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays the body of the response
"""


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.error

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
