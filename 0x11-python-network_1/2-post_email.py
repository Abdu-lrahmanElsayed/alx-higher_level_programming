#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    inemail = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(inemail)
    email = email.encode('ascii')
    req = urllib.request.Request(url, email)

    with urllib.request.urlopen(req) as res:
        con = res.read()
    print(con.decode('utf-8'))
