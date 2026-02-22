# # mytup = ('banana', 'apple', 'cherry')
# # myit = iter(mytup)

# # print(next(myit))
# # print(next(myit))
# # print(next(myit))
# #####################################


# class MyIterator:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
    
# some = MyIterator()
# myiter = iter(some)


# print(next(myiter))
# print(next(myiter))

# #######################
# class SomeIter:
#     def __init__(self, n):
#         self.n = n
#         self.current = 1

#     def __iter__(self):             #First neccecary method for iter class, makes class
#         return self
    
#     def __next__(self):             #second, contains main function that continues cycle
#         if self.current < self.n:
#             x = self.current
#             self.current += 1
#             return x
#         else:
#             raise StopIteration
        
# obj = SomeIter(10)
# print(next(obj))
# print(next(obj))
# print(next(obj))

# ###############################

# class S:
#     def __init__(self, n):
#         self.n = n
#         self.cur = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.cur <= self.n:
#             x = self.cur
#             self.cur += 1
#             return x
#         else:
#             raise StopIteration
        
# bshit = S(3)

# for x in bshit:
#     print(x)
######################################
# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# g = my_generator()
# print(next(g))
# print(next(g))
# print(next(g))

########################################
def func(max):
    count = 1
    while count <= max:
        yield count
        count += 1

ctr = func(5)
for i in ctr:
    print(i)
    
