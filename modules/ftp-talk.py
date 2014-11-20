#!/usr/bin/env python
import random
def ftp_trigger(jenni, input):
    channels = ['#/g/ftp', '#installgentoo', '#help']

    if input.sender in channels:
	messages = ['check the topic in #/g/ftp for the current password!', 'duh']
	return jenni.say(messages[random.randint(0, len(messages)-1)])
#        return jenni.say("check the topic in #/g/ftp for the current password!")
ftp_trigger.rule = r'(.*ftp pass.*|.*book pass.*)'
ftp_trigger.priority = 'high'

if __name__ == '__main__':
    print __doc__.strip()


