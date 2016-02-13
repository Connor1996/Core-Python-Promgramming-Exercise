from re import match

def foo():
    pass

ret = type(foo)
m = match(r'''<type '(\w+)'>''', str(ret))
if m is not None:
    print m.group(1)