def show_instances(v):
    print("object: {0} (count this objects {1})".format(v, v.numInstances))
    try:
        print("{0}, class: {1}, dictionary: {2}".format(type(v),
                                                        v.__class__, v.__dict__))
        print("id=0x{0:012x}, hash={1:012}[0x{0:012x}]".format(id(v),
                                                               hash(v), hash(v)))
    except TypeError:
        print("Not hashed type! : {0}".format(type(v)))


class key0(object):
    numInstances = 0

    def __init__(self, id):
        self.id = id
        key0.numInstances = key0.numInstances + 1


class key1(key0):
    numInstances = 0

    def __init__(self, id):
        key0.__init__(self, id)
        key1.numInstances = key1.numInstances + 1

    def __hash__(self):
        return self.id * self.id


class key2(key0):
    numInstances = 0

    def __init__(self, id):
        key0.__init__(self, id)
        key2.numInstances = key2.numInstances + 1

    def __hash__(self):
        return 123


class key3(key0):
    numInstances = 0

    def __init__(self, id):
        key0.__init__(self, id)
        key3.numInstances = key3.numInstances + 1

    def __hash__(self):
        raise TypeError


class key4(key0):
    numInstances = 0

    def __init__(self, id):
        key0.__init__(self, id)
        key4.numInstances = key4.numInstances + 1

    def __hash__(self):
        return None


tk = (key0, key1, key2, key3, key4)  # tuple of classes
for clas in tk:  # choose class!
    print("--------------------------------")
    t = [clas(x) for x in range(1, 4)]  # list of clss
    show_instances(t[2])
    try:
        d = {t[0]: "#1", t[1]: "#2", t[2]: "#3"}  # Dict with class keys
        print(d)
        print(d[t[1]])
    except TypeError:
        print("Cannot be used as a dictionary key!")
    print("---------------------------------------------------------")