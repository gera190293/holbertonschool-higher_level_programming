class SwimMixin:
    """Mixin class for swimming behavior"""
    
    def swim(self):
        """Method for swimming behavior"""
        print("The creature swims!")

class FlyMixin:
    """Mixin class for flying behavior"""
    
    def fly(self):
        """Method for flying behavior"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon that can both swim and fly"""
    
    def roar(self):
        """Method for dragon's roaring behavior"""
        print("The dragon roars!")
