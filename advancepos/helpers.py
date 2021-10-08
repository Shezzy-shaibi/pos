

from advancepos.models import CustomerType

def get_customertype_for_choices():
    outer = []
    ctypes = CustomerType.objects.filter(status=1)
    for ctype in ctypes:
        inner = (ctype.name, ctype.description)
        outer.append(inner)
    return outer
