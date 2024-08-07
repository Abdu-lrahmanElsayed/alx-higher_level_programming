#!/bin/bash
size=$(curl -s -o /dev/null -w '%{size_download}' $0)
echo $size
