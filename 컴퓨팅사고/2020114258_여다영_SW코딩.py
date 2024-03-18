#1. Numpy
import numpy as np

data = np.array([1, 2, 3, 4, 5])

mean_value = np.mean(data)

#2. Pandas
import pandas as pd

data = {'이름': ['Alice', 'Bob', 'Charlie'],
        '나이': [25, 30, 35],
        '직업': ['학생', '개발자', '분석가']}
df = pd.DataFrame(data)

print(df)

#3. Matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

sns.histplot(df['나이'], bins=10, kde=True)
plt.show()
