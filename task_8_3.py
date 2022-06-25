
def type_logger(fn):

   def wrapper(*arg):
       prnt_str = []
       results = []
       for el in arg:

           prnt_str.append (fn.__name__ + '(' + str(el) + ':' + str(type(el)) + ')')
           results.append(fn(el))
       print(*prnt_str, sep=', ')
       return results

   return wrapper



@type_logger
def calc_cube(x):

   return x ** 3


results = calc_cube(5,5)
print(results)

