Wolf's Den
========

Wolf's Den - a lightweight Twitter client in Python
Copyright (C) 2014  Eric Sund
ericsund@pyroh.tk

The full GNU GPLv3 license is found at /LICENSE.txt

SUMMARY

Wolf's Den is adesigned to be the most resource-friendly Twitter client while providing a graphical interface.
It makes use of Twitter's v1.1 API and several other modules.



FEATURES

> Interaction with Twitter v1.1 API
> Authenticate user
> Remember user authentication on restart
> Send tweet
> Send tweet with attached photo
> Tweet photo with no accompanying text.
> Exit client
> Success/failure sending tweet
> Cancel option



UPCOMING FEATURES

> Live Character count
> Multiple user support
> Timeline view
> Mentions and direct messages view



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
> None currently known



If you have any questions, comments or concerns, please email ericsund@pyroh.tk.
