#!/usr/bin/python2

#
#   secure-chromium
# -------------------
#
# Starts Chromium browser in incognito mode with Tor.
#
# Tor must be configured and running before using the script.
#

import gtk
import os
import subprocess
import sys

startUrl = "https://check.torproject.org/"

## Displays error message
def errorDialog(message):
  md = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE,
    message)
  md.run()
  md.destroy()

## Check if Chromium is already running.
fnull = open(os.devnull, "w")
result = subprocess.call("pidof chromium", shell = True, stdout = fnull, stderr = fnull)
fnull.close()
if result != 0:
  fnull = open(os.devnull, "w")
  subprocess.Popen(
    "chromium --incognito --proxy-server=\"socks://localhost:9050\" \""+startUrl+"\"",
    shell = True, stdout = fnull, stderr = fnull)
else:
  errorDialog("Chromium is already running")
  sys.exit()


#
# Copyright 2010-2011 Vilius Normantas <code@norma.lt>
#
# secure-chromium is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# secure-chromium is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with secure-chromium. If
# not, see <http://www.gnu.org/licenses/>.
#
