class A:
    def met(self):
        print("Methode from A")


class B(A):
    pass
    # def met(self):
    #     print("Methode from B")


class C(A):
    pass
    # def met(self):
    #     print("Methode from C")


class D(B, C):
    pass
    # def met(self):
    #     print("Methode from D")


a = A()
b = B()
c = C()
d = D()

d.met()

# B inherits A..
# C inherits A
# D inherits B and C
