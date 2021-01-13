#!/bin/bash


grep -E -o " [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ " /var/log/qeats-server.log | sort -n | uniq  > result.txt

