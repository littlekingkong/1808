#!/bin/bash
ps -ef | grep /usr/local/nginx/html/sync-oss.py | grep -v grep
if [ $? -ne 0 ]; then
    python /usr/local/nginx/html/sync-oss.py
fi
