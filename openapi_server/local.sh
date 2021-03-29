#!/bin/sh

eval $(lean env | grep export)

python wsgi.py