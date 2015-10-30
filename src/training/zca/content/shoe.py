
from zope.interface import implements
from training.zca.interfaces import IShoe

class Shoe(object):
    """ A regular Shoe
    """
    
    implements(IShoe)

    color = u''
    size = 0



