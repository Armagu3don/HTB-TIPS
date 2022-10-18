#!/usr/bin/env python3


import requests,sys,re
from urllib.parse import urlencode, quote_plus
import urllib




def get_rev_shell():
	try:
		url = "here your url"
		ip = input("HTB IP ")
		p = input("Listening port: ")
		payload = (the payload)
		headers = {"all the headers"}
		data = "datas"
		r = requests.post(url, headers=headers, data=data)
	except:
		print("Failed!")




def __init__():
	try:
		print("OPTIONS: rev-shell")
		choice = input("Pick An Option Above: ")
		if choice == "rev-shell":
			get_rev_shell()
	except:
		print("Failed!")


__init__()	
