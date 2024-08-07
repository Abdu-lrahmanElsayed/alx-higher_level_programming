#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

URL=$0

size=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

echo $size
