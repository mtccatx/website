#!/usr/bin/bash

# Send headers
echo "Content-Type: text/html"
echo
echo

# Send the content!
ls /home | grep -v root
