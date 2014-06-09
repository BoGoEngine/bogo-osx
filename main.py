#!/usr/bin/env python

from Cocoa import *
from InputMethodKit import *


class BogoController(IMKInputController):
	def inputText_client_(self, string, client):
		NSLog("inputText_client_({0}, {1})".format(string, client))
		return YES


def main():
	pool = NSAutoreleasePool.alloc().init()

	connectionName = "Bogo_1_Connection"

	identifier = NSBundle.mainBundle().bundleIdentifier()
	
	NSLog(NSBundle.mainBundle().bundleIdentifier())
	server = IMKServer.alloc().initWithName_bundleIdentifier_(
		connectionName,
		"com.ngochin.inputmethod.BoGo")

	NSBundle.loadNibNamed_owner_(
		"MainMenu",
		NSApplication.sharedApplication())

	NSLog("here")

	NSApplication.sharedApplication().run()

	pool.release()

if __name__ == "__main__":
	main()
