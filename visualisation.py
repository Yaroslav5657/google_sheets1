import matplotlib as mplt
import matplotlib.pyplot as plt
from client import MyClient as Cli, Settings
import pandas as pd
import numpy as np

#def main():
    #client = Cli(Settings.URL, Settings.SCOPES, Settings.SECRET_FILE)
    #data = client.data.sheet1
    #pdata = pd.DataFrame(data.get_all_records())
    #pdata.plot(x='Імя', y='Оцінки')
    #plt.show()

plt.style.use('_mpl-gallery')

x = 0.5 + np.arange(8)
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

fig, ax = plt.subplots()

ax.stem(x, y)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

#if __name__ == '__main__':
#    main()