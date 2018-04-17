import pandas as pd
import matplotlib.pyplot as plt

#In this case, the separator is \t
data = pd.read_csv("wages_hours.csv", sep="\t")
data.head()

print ("Data:\n{}\n".format(data))

#We need only AGE and RATE from the data.
useful_data = data[["AGE", "RATE"]]
useful_data.head()

#Sorting the values - sort_values is deprecated ?
data_sorted = useful_data.sort_values("AGE")
data_sorted.head()

#data_sorted.head()
data_sorted.set_index("AGE", inplace=True)
data_sorted.head()

#Plot of the sorted data
data_sorted.plot()
plt.show()