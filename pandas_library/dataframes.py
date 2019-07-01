#working with strictured arrays with pands library

import numpy as np
import pandas as pd

my_array = np.ones(4, dtype=([('foo', int),('bar', float)]))

print(my_array['foo'])

my_array2 = my_array.view(np.recarray)

print(my_array2.foo)
