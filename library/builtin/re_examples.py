import re


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())


valid = re.compile(r"^[a2-9tjqk]{5}$")
print(displaymatch(valid.match("akt5q")))
print(displaymatch(valid.match('akt5e')))
print(displaymatch(valid.match('727ak')))
