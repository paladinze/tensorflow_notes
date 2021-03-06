from __future__ import print_function

import pandas as pd

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

table = pd.DataFrame({ 'City name': city_names, 'Population': population })

table.hist('Population')
print(table)
