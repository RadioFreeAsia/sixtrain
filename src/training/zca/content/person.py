from training.zca.interfaces import IPerson
from zope.interface import implements

class Person(object):
    implements(IPerson)
    
    name = u""
    age = 6
    shoe_size = 1
    apparel = ()




