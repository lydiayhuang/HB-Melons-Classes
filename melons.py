# class ClassName(object):
#     """docstring for ClassName"""
#     def __init__(self, arg):
#         super(ClassName, self).__init__()
#         self.arg = arg
        
        
"""This file should have our order classes in it."""

class AbstractMelonOrder(object):

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        self.shipped = False
   

    def get_total(self):
        
        if self.species == 'Christmas':
            base_price = 5*1.5
            total = (1 + self.tax) * self.qty * base_price
            return total
        else:    
            base_price = 5
            total = (1 + self.tax) * self.qty * base_price
            return total

    def mark_shipped(self):
        """Set shipped to true."""
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code

    order_type = "international"
    tax = 0.17

    

    def get_total(self):
        """Calculate price."""
        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            return total + 3
        else:
            return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
