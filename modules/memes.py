#!/usr/bin/env python

def bigguy(jenni, input):
    jenni.say("For you.")
bigguy.rule = r'(you are a big guy)'

def hue(jenni, input):
    jenni.say("hueHUEhuehueheUHEUehueHUE")
hue.rule = r'(hue)'

def bait(jenni, input):
    jenni.say("Gr8 b8, m8. I rel8, str8 appreci8, and congratul8. I r8 this b8 "
	      "an 8/8. Plz no h8, I'm str8 ir8. Cre8 more, can't w8. We should "
	      "convers8, I won't ber8, my number is 8888888, ask for N8. No "
	      "calls l8 or out of st8. If on a d8, ask K8 to loc8. Even with a "
	      "full pl8, I always have time to communic8 so don't hesit8.")
bait.commands = ['b8']

def pw(jenni, input):
    target = input.group(2)
    jenni.say(target + ", I have put you on a permanent ignore, "
                       "public and private. I have found you disturbing, "
                       "rude and generally not worth talking to. According "
                       "to the channels you hang on, it strengtens the "
                       "effect of wanting to put you on ignore because of "
                       "my lack of interest in you as a person. This "
                       "message is not meant to be rude to you, just to "
                       "inform you that i won't see anything of what you post")
pw.commands = ['pw']   

def pa(jenni, input):
    target = input.group(2)
    jenni.say(target + ", you really need to be careful how you talk about me "
                       "on the forum, i dont appreciate it. tone down the "
                       "disrespect, i dont know where you're from but where "
                       "i am from, we dont tolerate that. dont even reply to "
                       "this, just keep your mouth shut. consider yourself warned.")
pa.commands = ['pa']

if __name__ == '__main__':
    print __doc__.strip()
