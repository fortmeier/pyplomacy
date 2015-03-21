#!/usr/bin/python
# -*- coding: utf-8 -*-

from werkzeug.serving import run_simple
from jsonrpcserver import application

if __name__ == '__main__':
    run_simple('localhost', 4000, application)