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
