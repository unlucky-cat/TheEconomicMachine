# from model.economy import Economy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model.economy import Economy


economy = Economy(100)
economy.Iterate(20)

y_axis = economy._total_goods_produced_history
x_axis = np.arange(0, len(y_axis), step=1)

df = pd.DataFrame(y_axis)

df.plot(kind='line', marker='o')
plt.xticks(x_axis)


# for i,j in zip(x_axis,y_axis):
#    plt.annotate(str(j), xy=(i,j))

plt.show()