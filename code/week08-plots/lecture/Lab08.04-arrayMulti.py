# This is just to show you numpy exists
# Author: Brid Kennedy

import numpy as np

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint (minSalary, maxSalary,numberOfEntries)

print (salaries)

salariesPlus = salaries + 5000 # this will add 5000 to each value
print(salariesPlus)

salariesMult = salaries * 1.05 # add 5% by multiplying by 1.05
print(salariesMult)
# This is a float array, here I convert it to an int array 
newSalaries = salariesMult.astype(int)
print(newSalaries)