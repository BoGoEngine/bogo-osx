#!/usr/bin/env python

from Cocoa import *
from InputMethodKit import *
from itertools import takewhile
import bogo


class BogoController(IMKInputController):
	def __init__(self):
		# Cocoa doesn't call this method at all
		self.reset()
		self.initialized = True

	def reset(self):
		self.composing_string = ""
		self.raw_string = ""

	def inputText_client_(self, string, client):
		if not hasattr(self, 'initialized'):
			self.__init__()

		if string == ' ':
			self.reset()
			return NO
		
		self.raw_string += string
		result = bogo.process_sequence(self.raw_string)

		same_initial_chars = list(takewhile(lambda tupl: tupl[0] == tupl[1],
                                            zip(self.composing_string,
                                                result)))

		n_backspace = len(self.composing_string) - len(same_initial_chars)
		string_to_commit = result[len(same_initial_chars):]

		start = self.client().length() - n_backspace 
		length = len(string_to_commit)

		self.client().insertText_replacementRange_(
			string_to_commit,
			NSMakeRange(start, length))

		self.composing_string = result

		return YES


def main():
	pool = NSAutoreleasePool.alloc().init()

	connectionName = "Bogo_1_Connection"

	identifier = NSBundle.mainBundle().bundleIdentifier()
	
	NSLog(NSBundle.mainBundle().bundleIdentifier())
	server = IMKServer.alloc().initWithName_bundleIdentifier_(
		connectionName,
		"com.ngochin.inputmethod.BoGo")

	# NSBundle.loadNibNamed_owner_(
	# 	"MainMenu",
	# 	NSApplication.sharedApplication())

	NSLog("here")

	NSApplication.sharedApplication().run()

	pool.release()

if __name__ == "__main__":
	main()
