# class ClassName(object):
#     """docstring for ClassName"""
#     def __init__(self, arg):
#         super(ClassName, self).__init__()
#         self.arg = arg
        
        
"""This file should have our order classes in it."""

class AbstractMelonOrder(object):

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, selford).__init__(species, qty, 
                                            order_type = "domestic",
                                            tax = 0.08)# check tax

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



# class InternationalMelonOrder(AbstractMelonOrder):
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes"""
#         super(InternationalMelonOrder, self).__init__(species, qty, "international")

#         self.country_code = country_code



#     def get_total(self):
#         """Calculate price."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price
#         return total

#     def mark_shipped(self):
#         """Set shipped to true."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code