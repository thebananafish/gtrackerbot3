from datetime import datetime
from collections import deque

votes = {}
def votekick(jenni, input):
    if not input.sender.startswith('#'):
        return
    text = input.group().split()
    argc = len(text)
    if argc < 2: return
    nick = text[1]
    channel = input.sender
    if input.nick == nick: return
    if nick == jenni.config.nick: return
    ballot = votes.get(nick)
    if not ballot:
        votes[nick] = deque(maxlen=5)
        ballot = votes[nick]
    now = datetime.utcnow()
    old_votes = []
    for vote in ballot:
        if (now - vote['then']).total_seconds() > 300:
            old_votes.append(vote)
        if input.nick == vote['voter']: return
    for vote in old_votes:
        ballot.remove(vote)
    ballot.append(dict(then=datetime.utcnow(), voter=input.nick))

    if len(ballot) == ballot.maxlen:
        reason = "You're not wanted here."
        jenni.write(['KICK', channel, nick, reason])
    else:
        jenni.say("%d vote(s) out of 5 for %s" % (len(ballot), nick))
votekick.commands = ['vk', 'votekick']
votekick.priority = 'high'
