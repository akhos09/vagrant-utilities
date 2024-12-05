#!/bin/bash
sudo ps -faux | grep 'python3 \-m http.server 80' | sudo kill -9 $(awk {print $2})