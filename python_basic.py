# tuple (immutable)----- indexing,slicing,for,ops and function
a = 3,3,4,4,5 # its also a tuple
print(a)
tup = ( ) # empty tupel
tup2 = ( 32,2,34,3,23) # tuple of integers num
tup3 = ( 3.4,5.5,6.6,7.7,8.8) # tuple of float num
tup4 = ('First' ,'Second' , 'third','Fourth') # string tuple
tup5 = ('ram','shyam',('hello','world')) # nested tuple
tup6 = ('hello',45.5,34,('world'))# tuple of mix data type 
tup7 = ('asif', 25, [ 50,60,70],{'john','david'},(88,99,77))
print(len(tup7))

# tuple indexing 
print(tup3[4])
print(tup6[0][0]) # nested indexing
print(tup7[-1]) 
# tuple slicing 
my_tuple = ('first','second','third','fourth')
print(my_tuple[-3:])
for i in my_tuple: 
    print(i)
for i in enumerate(my_tuple):
    print(i)
print('')
# function 
tuple1 = (32,3,3,4,4)
print(type(tuple1))
print(tuple1.count)
print(tuple1.__add__)
#compliment, or xor not left shift and right sshift
# package and module and function 
#flore and ceil(),sqrt