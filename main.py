#!/usr/bin/python

__author__ = 'ToFran'
__site__ = 'http://tofran.com/'
__description__ = 'Main UI to the gyazoCrawler.py class'

####### VARS ########

#files and folders
#the databse file, will overwrite (must exist) [@todo cerate the file]
DATABASE_FILE_PATH = "database.json"
#the path where images will be downloaded (must exist) [@todo cerate the directory]
DOWNLOAD_IMAGES_PATH = "download/"
#the name of the images.
#"original" for the original name,
#"order" for a ordered number (from the newest to oldest)
DOWNLOAD_IMAGES_NAME = "original"

#the session cookies
COOKIE_GYAZOSESSION = 'YOUR COOKIE HERE'
COOKIE_GA = 'YOUR COOKIE HERE'
COOKIE_GAT = '1'

#Gyazo cloud tab to be indexed.
#uploaded gyazos: "history"
#the gyazos you visit (from other users): "visits"
#your favorites: "favorites"
#for custom tabs use their UID ex: "8ag1adb8a8b1b0680f15ea5b6bc65t26"
GYAZO_TAB_TO_INDEX = "history"

##########################

import gyazoCrawler

def printHelp():
	print "1 - Download/Index database of gyazos\n" + \
	"2 - Calculate the size and download the all the images from the DB.\n" + \
	"3 - exit"
####

while True:
	printHelp()
	inp = raw_input()

	if inp == "1":
		result = gyazoCrawler.indexGyazos(GYAZO_TAB_TO_INDEX, COOKIE_GA, COOKIE_GAT, COOKIE_GYAZOSESSION, DATABASE_FILE_PATH)
		print "\nDone!"
		print str(result["pages"]) + " pages;"
		print str(result["imageCount"]) + " images;"
		print "in {0:.2f} seconds".format(result["time"])

	elif inp == "2":
		result = gyazoCrawler.getSize(DATABASE_FILE_PATH)
		print "\n" + str(result["size"]) + " MB (" + str(result["size_bytes"]) + " bytes) - " + str(result["countProcessed"]) + " images processed (out of " + str(result["countTotal"]) + ")"
		print "(Note: some images don't have the size atribute so, some are processed and other don't. But this will download them all!)"
		print "Do you wish to download? (y/*)"
		inp = raw_input().lower()

		if inp == "y":
			result = gyazoCrawler.downloadImages(DOWNLOAD_IMAGES_PATH, DOWNLOAD_IMAGES_NAME, DATABASE_FILE_PATH)
			print "\nDone!\nTime elapsed: {0:.2f} seconds".format(result["time"]);
			print "Downloaded " + str(result["count"]) + " images"

	elif inp == "3":
		break

	#end of if's
#end of while