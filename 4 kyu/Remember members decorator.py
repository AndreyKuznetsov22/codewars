#https://www.codewars.com/kata/571957959906af00f90012f3

class CallDict(dict):
    def __call__(self, *args):
        key = args[0] if len(args)==1 else args
        if key not in self:
            self[key] = self.create(*args)
        return self[key]

def remember(cls):
    members = CallDict()
    members.create = lambda *args: cls(*args)
    return members