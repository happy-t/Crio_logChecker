import json
import requests
import subprocess
base_url = "https://freegeoip.app/json/"
inn = open("result.txt", "w+")
subprocess.call("/home/ubuntu/gather.sh")


print("*******************************Lets start with countries************************************")

for i in inn:
	url = base_url + i.strip()
	r = requests.get(url)
	jsonres = r.json()
	print("*******************************")
	print(" " + jsonres["country_name"])
	if (len(jsonres["city"]) == 0):
		print(" City not found")
	else:
		print(" " + jsonres["city"])
	print(i)

