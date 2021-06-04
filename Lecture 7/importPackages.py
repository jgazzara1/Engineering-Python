import camelcase
c = camelcase.CamelCase()
print c.hump("life is good")

import myModule
var = myModule.x + myModule.y

import numpy as np
cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
C = np.array(cvalues)
print C
print C*9/5 + 32 # converts to farenheight

import matplotlib.pyplot as plt
plt.plot(C)
plt.show()
