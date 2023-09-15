# from model.economy import Economy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model.economy import Economy

iterations_count = 5
items_count = 10

economy = Economy(items_count)
economy.Iterate(iterations_count)

x_axis = np.arange(0, iterations_count, step=1)

# --------------
y_axis = [stat.avg_goods_produced for stat in economy._statistics]
df = pd.DataFrame(y_axis)
plt.plot(df, label='average', linestyle='-', marker='o', color="red")
# --------------


# --------------
for i in range(items_count):
    y_axis = economy._units[i]._history_data["goods_produced"]
    df = pd.DataFrame(y_axis)
    plt.plot(df, label='unit', linestyle='-', marker='o', color="green")
# --------------

plt.xticks(x_axis)


# for i,j in zip(x_axis,y_axis):
#    plt.annotate(str(j), xy=(i,j))

plt.show()