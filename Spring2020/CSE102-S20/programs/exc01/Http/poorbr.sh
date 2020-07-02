#!/bin/bash
/usr/bin/nc sofpower.com 80 <<HERE
GET /index.html HTTP/1.1
HOST: sofpower.com

HERE
