from helper import md5, Log
import requests
from helper.Log import logger
import json


def sdk_post(url, query):
	q = query+ '&sig=' +md5(query)
	logger.info(q)
	r = requests.post(url, q)
	if r.status_code == 200:
		res = json.loads(r.content)
		logger.info(res["result"])
		if res["result"]["code"]:
			return False
		return True
	return False