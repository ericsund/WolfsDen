Wolf's Den
========

Wolf's Den - a lightweight Twitter client in Python
Copyright (C) 2013  Eric Sund
epsund@e2esolution.com

The full GNU GPLv3 license is found at /LICENSE.txt

SUMMARY

Wolf's Den is adesigned to be the most resource-friendly Twitter client while providing a graphical interface.
It makes use of Twitter's v1.1 API and several other modules.



FEATURES

> Interaction with Twitter v1.1 API
<<<<<<< HEAD
> Authenticate and deauthenticate user
=======
> Authenticate user
>>>>>>> f96e8d0e9a9043e0c728cd60b08e18ef5c5e9bb3
> Remember user authentication on restart
> Send tweet
> Send tweet with attached photo
> Tweet photo with no accompanying text.
> Exit client
<<<<<<< HEAD
> Success/failure while making API calls
> Cancel option
> Update profile photo
=======
> Success/failure sending tweet
> Cancel option
>>>>>>> f96e8d0e9a9043e0c728cd60b08e18ef5c5e9bb3



UPCOMING FEATURES

> Live Character count
<<<<<<< HEAD
> Timeline view
> Mentions and direct messages view
> Update cover and background photos



CHANGE LOG

> January 2, 2014
>
	Tweet options integrated into sub-menu
	Customization options sub-menu created
> December 17, 2013
>
	Created error checking with API interaction
	Loop issues with menus fixed
	Change log created

=======
> Multiple user support
> Timeline view
> Mentions and direct messages view



>>>>>>> f96e8d0e9a9043e0c728cd60b08e18ef5c5e9bb3
INSTALLATION NOTICES - See /INSTALL.txt

> 1.  As of now Wolf's Den runs explicitly with Python 2.x+.  Its dependencies do not support Python 3.x+ currently.
Problems running because of Tkinter?  Install it to setup Python with Tk.
>
	Arch:
	sudo pacman -S tk  (or tk-python)
	Debian:
	sudo apt-get install tk  (or tk-python)
	Fedora:
	sudo yum install tk  (or tk-python)

> 2.  No module named setuptools?  Run these commands:
>
	wget http://python-distribute.org/distribute_setup.py
	sudo python2 distribute_setup.py install



ACKNOWLEDGEMENTS

Wolf's Den makes use of the following unmodified libraries:
> EasyGUI 0.96 Copyright (c) 2010, Stephen Raymond Ferg (Revised BSD License)
> Tweepy 2.1 Copyright (c) 2009-2010 Joshua Roesslein (MIT License)
> Twython 3.1.0 Copyright (c) 2013 Ryan McGrath (MIT License)



BUGS
<<<<<<< HEAD
> Pressing cancel in easygui.fileopenbox() returns NoneType error
=======
> None currently known
>>>>>>> f96e8d0e9a9043e0c728cd60b08e18ef5c5e9bb3



If you have any questions, comments or concerns, please email epsund@e2esolution.com.
