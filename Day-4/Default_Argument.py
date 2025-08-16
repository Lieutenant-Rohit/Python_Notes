#default argument = A default value for a certain parameters
#                    default is used when that argument is omitted
#                    make your function more flexible, reduces # of arguments
#

def net_price(list_price, discount = 0.0, sales_tax = 0.05):
    return list_price * (1 - discount) * (1 + sales_tax)

print(net_price(500))
print(net_price(200,0.10 ,0.04))

import time
# default arguments should follow by non default arguments.
def count(end, start=0):
  for x in range(start , end+1):
    print(x)
    time.sleep(1)

count(10)

