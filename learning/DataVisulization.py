import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
XYZ_web = {'day':[1,2,3,4,5,6],
           "visitors":[1000,700,600,1000,400,350],
           "Bounce_rate":[20,20,23,15,10,34]}
df = pd.DataFrame(XYZ_web)
df.set_index("day",inplace=True)
df.plot()
plt.show()
#print(df)