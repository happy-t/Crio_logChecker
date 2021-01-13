import json
import requests
import subprocess
base_url = "https://freegeoip.app/json/"
i = open("result.txt")
subprocess.call("/home/ubuntu/gather.sh")


print("*******************************Lets start with countries************************************")

for i in i:
	url = base_url + i.strip()
	r = requests.get(url)
	jsonres = r.json()
	print("*******************************")
	print(" " + jsonres["country_name"])
	print(i)

