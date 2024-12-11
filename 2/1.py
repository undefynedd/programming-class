import time
import sys
import math
import matplotlib.pyplot as plt
import numpy

b=[]
c=[]
sys.set_int_max_str_digits(1000000)

for i in range(10000):
    start_time = time.time()
    a=math.factorial(10*i)
    end_time = time.time()

    print(end_time-start_time)
    print(a)
    b.append(i)
    c.append(end_time-start_time)

#print(math.factorial(100000))

# x axis values
x = b 
# corresponding y axis values
y = c

plt.plot(x,y)
plt.show()
