# abs()
print abs(-1)
print abs(1.5)

# all()
trueset = [1, 1, 1, 1]
print all(trueset)
print all(range(1, 4))

# any()
trueset = [0, 1, 0, 1]
print any(trueset)
trueset = [0, 0, 0, 0]
print any(trueset)

# bin()
print bin(15) # return a binary string
print hex(155)
print oct(1222)

# bytearray()
print bytearray(2)
print bytearray([2, 5, 255])[1]

# chr() and ord()
print chr(80)
print ord('d')

# cmp()
print cmp(3, 5)

# compile()

# complex()
complex('1+2j')
print cmp(complex('1+2j'), complex(1, 2))

# container:
# dict, list, set, tuple

# dir()
print dir()

# divmod()
print divmod(112, 44)

# enumerate
#TODO:: what is enumerate???
homework = ['ACA', 'algor', 'nework']
print enumerate(homework)
print list(enumerate(homework))

# eval()
x = 1
print eval("x+1")
# repr()??
print eval("trueset")

# exec(), execfile()
notes1 = "eval can be used to execute arbitrary code objects(maybe created by \
        complie()"
notes2 = "dynamic execution of statements is supported by the exec, execfile \
        or eval statement"
note3 = "The globals() and locals() functions returns the current global and \
        local dictionary, respectively, which may be useful to pass around for\
         use by eval() or execfile()"

# filter()
# filter(function, iterable)
trueset = [1, 0, 1, 0, 0]
print filter(None, trueset)
print trueset
print [item for item in trueset if item]

# float
print float('inf')

# id(), the identity of an object; (address in memory in cpython)
print id(trueset)

#TODO: iter()

print locals()

# map & reduce
# map(function, iterable, ...)
print map(abs, [0, -1, 2, -4])
print reduce(lambda x, y: x+y, [1,2,3,4])

print trueset
iterset = iter(trueset)
print next(iterset)
print next(iterset)

print pow(2, 3, 5)
print cmp(pow(2, 3) % 5, pow(2, 3, 5)) # more efficient way

note4 = "property: useful class attribute manager"

# s = raw_input('___>')

print list(reversed([1,2,3,4]))

# sorted()
xrange(4)
range(4)

x = [1,2,3,4]
y = [2,3,4,5]
z = [4,5,6,7]
zipped = zip(x, y, z)
print zipped
x2, y2, z2 = zip(*zipped)
print x2
print y2
print type(y2)
