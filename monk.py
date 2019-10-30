from Reportproperties import Reportproperties


class A(Reportproperties):
    def __init__(self):
        self.input :
        pass

    def sampleFunc(self, arg):
        print('you called sampleFunc({})'.format(arg))

    def simple(self,arg):
        print("test")

# m = globals()['A']()
# # func = getattr(m, 'sampleFunc')
# # func('sample arg')
