# from model.economy import Economy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model.economy import Economy

iterations_count = 100
items_count = 10

economy = Economy(items_count)
economy.iterate(iterations_count)

x_axis = np.arange(0, iterations_count, step=1)

# --------------
y_axis = [stat.total_units_count for stat in economy.statistics]
df = pd.DataFrame(y_axis)
plt.plot(df, label='tuc', linestyle='-', marker='o', color="red")

y_axis = [stat.total_food for stat in economy.statistics]
df = pd.DataFrame(y_axis)
plt.plot(df, label='food', linestyle='-', marker='+', color="green")
# --------------


plt.xticks(x_axis)


tbl = pd.DataFrame.from_records([s.to_dict() for s in economy.statistics])
print(tbl)

plt.show()