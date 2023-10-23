class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A):
    pass

class E(B, D):
    pass


# tests

print('TEST_1:')
print(issubclass(E, B))
print(issubclass(E, C))
print(issubclass(E, D))

print('TEST_2:')
print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(D, A))

print('TEST_3:')
print(E.mro())

print('TEST_4:')
print(issubclass(E, A))