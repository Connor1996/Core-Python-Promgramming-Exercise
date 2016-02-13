name = raw_input('module name')
obj = __import__(name)
Is = dir(obj)
for item in Is:
    print 'name', item
    print 'type', type(getattr(obj, item))
    print 'value', getattr(obj, item)
    print