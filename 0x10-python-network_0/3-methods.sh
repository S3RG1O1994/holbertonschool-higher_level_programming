#!/bin/bash
# THe script print methods allowed for querys with http.
curl -sI "$1" | grep "Allow:" | cut -d ' ' -f2-
