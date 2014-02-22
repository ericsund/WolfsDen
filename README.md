Wolf's Den
========

Wolf's Den - a lightweight Twitter client in Python
Copyright (C) 2014  Eric Sund
ericsund@pyroh.tk

--
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.  You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
See License.txt for more information.

### The full GNU GPLv3 license is found at /LICENSE.txt


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
