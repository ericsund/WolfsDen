"""
__        __    _  __ _       ____             
\ \      / /__ | |/ _( )___  |  _ \  ___ _ __  
 \ \ /\ / / _ \| | |_|// __| | | | |/ _ \ '_ \ 
  \ V  V / (_) | |  _| \__ \ | |_| |  __/ | | |
   \_/\_/ \___/|_|_|   |___/ |____/ \___|_| |_|

|----------------------------------------------------------|
|Wolf's Den - a lightweight Twitter client in Python       |
|Copyright (C) 2014  Eric Sund                             |
|                                                          |
|The full GNU GPLv3 license is found at /LICENSE.txt	   |
|----------------------------------------------------------|

Wolf's Den makes use of the following unmodified libraries:
> EasyGUI 0.96 Copyright (c) 2010, Stephen Raymond Ferg (Revised BSD License)
> Tweepy 2.1 Copyright (c) 2009-2010 Joshua Roesslein (MIT License)
> Twython 3.1.0 Copyright (c) 2013 Ryan McGrath (MIT License)

Bugs:
None currently known

Times told to stop coding by dad:
1
"""
#!/usr/bin/env python
import sys, os, twython, easygui, tweepy
from easygui import *
from twython import Twython

#Wolf's Den app keys
consumer_key = 'oJFCnwf9pOu2LIT8rvs4nQ'
consumer_secret = 'rVDUj8TknQc9GA0Eqz7uvGo7aAYah3FRSqJqhjXZ66k'

#check for existing authentication
KeysExist = open("userkeys.txt", "r")
readKeysExist = KeysExist.readline()
authTrue = readKeysExist[0]
if authTrue == "0":  #if no authentication
	#get user keys
	auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret, secure = True)
	auth_url = auth.get_authorization_url()
	enterbox("Please obtain your PIN here: ", "Authorize Wolf's Den", auth_url)
	pin = enterbox('Enter PIN: ').strip()
	auth.get_access_token(pin)
	accessKey = auth.access_token.key
	accessSecret = auth.access_token.secret
	accessKey = str(accessKey)
	accessSecret = str(accessSecret)
	#save user keys
	with open('userkeys.txt', 'r') as file:
		fileContents = file.readlines()
	fileContents[0] = "1\n"
	fileContents[1] = accessKey + "\n"
	fileContents[2] = accessSecret + "\n"
	with open('userkeys.txt', 'w') as file:
		file.writelines(fileContents)

KeysExist.close()
#read keys
getUserKeys = open("userkeys.txt", "r+")
readUserKeys = getUserKeys.readlines()
accessKey = readUserKeys[1]
accessSecret = readUserKeys[2]
accessKey = accessKey[:-1]
accessSecret = accessSecret[:-1]
t = Twython(consumer_key, consumer_secret, accessKey, accessSecret)

tweetErrors = (
("There was a problem sending your tweet!  Check your network connection and userkeys file!"),
("You've reached the maximum API calls!  Wait before trying again."),
("Problem! - Wolf's Den")
)

def tweetAttempt(): #media syntax
  try:
    t.update_status_with_media(media = m, status = s)
    tweeting = False
  except twython.TwythonError:
    msgbox(tweetErrors[0], tweetErrors[2], "Try Again!")
  except twython.TwythonRateLimitError:
    msgbox(tweetErrors[1], tweetErrors[2], "Okay")
  else:
    msgbox("Tweet sent!", "Wolf's Den", "Okay")

on = True
while on:
  menu = buttonbox(" ", "Wolf's Den", ["Tweet", "Customize", "Close", "Sign Out"])
  if menu == "Tweet":
	INtweetmenu = True
	while INtweetmenu:
		tweetmenu = buttonbox(" ", "Tweet - Wolf's Den", ["Tweet", "Tweet Photo", "Back"])
		if tweetmenu == "Tweet":
			tweeting = True
			while tweeting:
				s = enterbox("What's happening?", "New Tweet - Wolf's Den")
				if s == None: tweeting = False
				else:
					try:
						t.update_status(status = s)
						tweeting = False
						INtweetmenu = False
					except twython.TwythonError:
						msgbox(tweetErrors[0], tweetErrors[2], "Try Again!")
					except twython.TwythonRateLimitError:
						msgbox(tweetErrors[1], tweetErrors[2], "Okay")
					else:
						msgbox("Tweet sent!", "Wolf's Den", "Okay")
		elif tweetmenu == "Tweet Photo":
			tweeting = True
			while tweeting:
				m = fileopenbox("Select Picture - Wolf's Den", "Tweet Photo")
				m = open(m, "r")
				s = enterbox("Say something about this photo!", "Tweet Photo - Wolf's Den")
				if s == None: tweeting = False
				else:
					if s == "":
						tweetAttempt()
						tweeting = False
						INtweetmenu = False
					if s != "":
						tweetAttempt()
						tweeting = False
						INtweetmenu = False
		elif tweetmenu == "Back":
			INtweetmenu = False
  elif menu == "Customize":
	  customizing = True
	  while customizing:
		  customizeMenu = buttonbox(" ", "Customize - Wolf's Den", ["Profile Picture", "Cover Photo", "Background Image", "Back"])
		  if customizeMenu == "Profile Picture":
			  updatePic = True
			  while updatePic:
				  pic = fileopenbox("Select Picture - Wolf's Den", "Update Profile Picture")
				  pic = open(pic, 'r')
				  try:
					t.update_profile_image(image = pic)
					updatePic = False
				  except twython.TwythonError:
					  msgbox(tweetErrors[0], tweetErrors[2], "Try Again!")
				  except twythonTwythonRateLimitError:
					  msgbox(tweetErrors[1], tweetErrors[2], "Okay")
				  else:
					  msgbox("Profile picture updated!", "Wolf's Den", "Okay")
		  elif customizeMenu == "Cover Photo":
			  """
			  In Development
			  ---------------------------------------------
			  #img = open("test.jpg", "rb")
			  #t.update_profile_banner_image(banner = img)
			  ---------------------------------------------
			  """
			  msgbox("In development.")
		  elif customizeMenu == "Background Image":
			  msgbox("In development")
		  elif customizeMenu == "Back":
			  customizing = False			  
  elif menu == "Close":
    on = False
  elif menu == "Sign Out":
	  with open('userkeys.txt', 'r') as file:
		  fileContents = file.readlines() #set access secret and key to blank lines
          fileContents[0] = "0\n"
          fileContents[1] = "\n"
          fileContents[2] = "\n"
	  with open('userkeys.txt', 'w') as file:
		  file.writelines(fileContents)
	  on = False
