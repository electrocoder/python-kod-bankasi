#!/usr/bin/python
#-*- coding: utf-8 -*-

# all directory *.py remover for django
# https://electrocoder.wordpress.com/
# 14/10/2015
# usage : python remove_py.py

import os

protected_file = [
		'remove_migrations.py', 
		'remove_py.py', 
		'manage.py', 
		'wsgi.py', 
		'__init__.py', 
		]

for root, dirs, files in os.walk("."):
	for file in files:
		if file.endswith(".py") and not file in protected_file:
			print(os.path.join(root, file))
			os.remove(os.path.join(root, file))
