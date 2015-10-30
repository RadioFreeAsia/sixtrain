from zope.interface import Interface
from zope.interface import Attribute

class IShoe(Interface):
    """ A Shoe
    """

    color = Attribute("color of the shoes")
    size = Attribute("shoe Size")


class ICloset(Interface):
    """A place to put our shoes and get them later
    """

    closet = Attribute("where are your clothes go")
   
    def find(size, color, article_type):
        """get items of a particular size and color"""

    def put_away(artiles):
        """put the articles back into the closet"""

class IDamaged(Interface):
    """ Marker Interface for damaged goods """


class IPerson(Interface):
    """ A person """
    name = Attribute("The person's Name")
    age = Attribute("The person's age")
    shoe_size = Attribute("The person's shoe size")
    apparel = Attribute("a list of Apparel")


class IShoeWearing(Interface):
    """ Something that wears a shoe """
    
    def wear(left, right):
        """ Wear the provided shoes """


