# from model.economy import Economy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model.economy import Economy


economy = Economy(20)
economy.Iterate(20)

x_axis = np.arange(0, 20, step=1)

for i in range(20):
    y_axis = economy._units[i]._productivity_history
    df = pd.DataFrame(y_axis)
    plt.plot(df, label='line1', linestyle='-', marker='o')

plt.xticks(x_axis)


# for i,j in zip(x_axis,y_axis):
#    plt.annotate(str(j), xy=(i,j))

plt.show()