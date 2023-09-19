# from model.economy import Economy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model.economy import Economy


economy = Economy(100)
economy.Iterate(20)

y_axis = [stat.total_productivity for stat in economy._statistics]
x_axis = np.arange(0, len(y_axis), step=1)

df = pd.DataFrame(y_axis)

df.plot(kind='line', marker='o')
plt.xticks(x_axis)


# for i,j in zip(x_axis,y_axis):
#    plt.annotate(str(j), xy=(i,j))

plt.show()

tbl = pd.DataFrame.from_records([s.to_dict() for s in economy._statistics])
print(tbl)