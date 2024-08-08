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
        with urllib.request.urlopen('{}'.format(req)) as res:
            body = res.read()
            print(body)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
