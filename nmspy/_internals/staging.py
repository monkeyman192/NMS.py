# A place to store variables internally until they are ready to be used.
# Some things like cGcApplication will be instantiated, but the fields will be
# initially set to null pointers, so any attempt to access them will result in
# an access violation.
# To get around this we'll initially stage the variables here and then only
# assign them once they are ready to go.

_cGcApplication = None
