from zope.component import adapts
from zope.interface import implements

from training.zca.interfaces import IShoeWearing, IPerson


class PersonWearingShoes(object):
    """Adapter allowing a person to wear shoes"""
    implements(IShoeWearing)
    adapts(IPerson)
    
    def __init__(self, context):
        self.context = context

    def wear(self, left, right):
        self.context.apparel += (left, right)
        if min(left.size, right.size) >= self.context.shoe_size:
            print "ahh, confy"
        else:
            print "ooh, a bit tight"

        
