class MROHelper:
    def len(self):
        return len(self.mro())
    
    def class_by_index(self, n=0):
        return self.mro()[n]
    
    def index_by_class(self, parent):
        return self.mro().index(parent)
    

# tests


print('TEST_1:')
class A:
    pass
    
class B(A):
    pass
    
class C(A):
    pass
    
class D(B, C):
    pass
    
print(MROHelper.len(D))

print('TEST_2:')
class A:
    pass
    
class B(A):
    pass
    
class C(A):
    pass
    
class D(B, C):
    pass
    
print(MROHelper.class_by_index(D, 2))
print(MROHelper.class_by_index(B))

print('TEST_3:')
class A:
    pass
    
class B(A):
    pass
    
class C(A):
    pass
    
class D(B, C):
    pass
    
print(MROHelper.index_by_class(D, A))

print('TEST_4:')
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


class E(B, C, D):
    pass


class F(B, C):
    pass


print(MROHelper.len(E))
print(MROHelper.class_by_index(E, 4))
print(MROHelper.index_by_class(E, C))