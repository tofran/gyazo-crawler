#!/usr/bin/python

__author__ = 'ToFran'
__site__ = 'http://tofran.com/'
__description__ = 'This simple library crawles a Gyazo.com account, in order to index and download you gyazo history'

##########################

import json
import time
import sys
import requests	
import urllib
import os
import os.path

##########################

def getSize(database_file):
	countProcessed = 0
	countTotal = 0
	totalbytes = 0
	rs = {"error": True}
	startTime = time.time()

	try:
		with open(database_file) as inFile:	
			data = json.load(inFile)
	except Exception, e:
		rs["error_message"] = "Could not open " + database_file
		return rs

	for image in data:
		countTotal += 1
		file_size = image["file_size"]
		if file_size is not None:
			countProcessed += 1
			totalbytes += file_size

	rs["error"] = False 
	rs["size"] = totalbytes/8388608 #in megabytes
	rs["size_bytes"] = totalbytes
	rs["countTotal"] = countTotal
	rs["countProcessed"] = countProcessed
	return rs
#####

def indexGyazos(index_tab, cookie_ga, cookie_gat, cookie_GyazoSession, database_file):
	jsonData = []
	rs = {"error": True}
	page = 1
	imageCount = 0

	try:
		outfile = open(database_file, 'w+')
	except Exception, e:
		rs["error_message"] = "Could not open or create " + database_file
		return rs

	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0"}
	cookies = {"_ga": cookie_ga,"Gyazo_session": cookie_GyazoSession,"_gat": cookie_gat}

	startTime = time.time()

	while True:
		url = "https://gyazo.com/tabs/" + index_tab + "/images.json?page=" + str(page)
		
		print ("downloading page " + str(page) + "...")

		resp = requests.get(url, headers=headers, cookies=cookies)
		jsonResp = resp.json()

		if resp.text == "[]" or len(jsonResp) == 0:
			print "... " + str(page) + " is empty! Terminating!"
			break

		for imageIn in jsonResp:
			imageCount += 1
			imageOut = {
				"page": page,
				"created_at": imageIn["created_at"],
				"file_size": imageIn["file_size"],
				"image_id": imageIn["permalink_path"][1:],
				"alias_id": imageIn["alias_id"],
				"url": imageIn["url"],
				"permalink_url": imageIn["permalink_url"],
				"thumb_url": imageIn["thumb_url"],
				"large_thumb_url": imageIn["large_thumb_url"],
				"search_thumb_url": imageIn["search_thumb_url"]
			}
			jsonData.append(imageOut)
		#end of for each image

		print "...done"

		page += 1
	#end of while

	#with open(database_file, 'w') as outfile:
	json.dump(jsonData, outfile, ensure_ascii=True, sort_keys=False, indent=1)
	outfile.close()

	rs["error"] = False 
	rs["time"] = time.time()-startTime
	rs["pages"] = page
	rs["imageCount"] = imageCount

	return rs
#####

def downloadImages(downloadPath, file_name_type, database_file):
	originalName = True
	if file_name_type == "order":
		originalName = False

	count = 1
	rs = {"error": True}

	startTime = time.time()

	if not os.path.exists(downloadPath):
		os.makedirs(downloadPath)

	try:
		with open(database_file) as inFile:	
			data = json.load(inFile)
	except Exception, e:
		rs["error_message"] = "Could not open " + database_file
		return rs

	print "downloading! (this may take a while)"

	if originalName:
		for image in data:
			urllib.urlretrieve(image["url"], downloadPath + image["image_id"] + ".png")
			count += 1
	else:
		for image in data:
			urllib.urlretrieve(image["url"], downloadPath + str(count) + ".png")
			count += 1

	rs["error"] = False
	rs["count"] = count
	rs["time"] = time.time()-startTime	
	return rs
####