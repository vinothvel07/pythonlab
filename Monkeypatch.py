import monk
import sys

# m = globals()[monk.A]()
# app = sys.modules[monk.A]
# cb = monk.A()
# print(type(cb))
# fun_name = sys.argv[1]
# print(type(fun_name))
# print(fun_name)
# getattr(monk.A(),sys.argv[1])("testing")
# func('sample arg')
cb = monk.A()

print(cb.input)