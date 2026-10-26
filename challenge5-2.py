# You can raise an exception with the raise statement. For example, to raise ZeroDivisionError:

# raise ZeroDivisionError
# You can catch exceptions in a try/except block:

# try:
#     x = 10 / y
#     print(x)  # This line is not reached if y is 0!
# except ZeroDivisionError:
#     print("You tried to divide by 0! That's just wrong.")


# Implement wrapped_divide() so that it calls divide() but converts the ZeroDivisionError into a return value of -1.

# Implement wrapped_get_element() that it calls get_element(), but converts that -1 return value into a thrown IndexError.

# You must call the originals from your wrappers. Your goal is not to reimplement the functionality; your only goal is to translate the return value to what you want

# Do not change this function!
def divide(n, d):
    if d == 0:
        raise ZeroDivisionError

    return n / d

# Do not change this function!
def get_element(a, i):
    if i < 0 or i >= len(a):
        return -1

    return a[i]

def wrapped_divide(n, d):
   try:
      divide(n,d)
   except: 
    return -1
   

print(wrapped_divide(1,0))

list = [1,2,3]
def wrapped_get_element(a, i):
    if get_element(a,i) == -1:
       raise IndexError

print(wrapped_get_element(list,6))