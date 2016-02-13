import re

week = {}.fromkeys(('Mon', 'Thu', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun'), 0)
st = '^(' + '|'.join(week.keys()) + ')'

with open('redata.txt', 'r') as f:
    for eachLine in f:
        m = re.match(st, eachLine)
        if m is not None:
            week[m.group()] += 1

print week