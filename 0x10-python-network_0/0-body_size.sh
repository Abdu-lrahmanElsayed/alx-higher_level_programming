#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body
curl -s -w '%{size_download}' "http://$1"
