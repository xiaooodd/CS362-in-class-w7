def is_p(string):
    if not string:
        return "Empty string"
    a = reversed(list(string))
    if list(a) == list(string):
        return True
    else:
        return False
        