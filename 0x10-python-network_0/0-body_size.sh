#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body
echo $(curl -s -o /dev/null -w '%{size_download}' $0)
