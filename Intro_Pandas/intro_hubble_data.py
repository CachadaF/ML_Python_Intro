import pandas as pd
import matplotlib.pyplot as plt
#%pylab inline -> para usar en una Jupyter-Notebook

#How to read the file with a header
data = pd.read_csv("hubble_data.csv")
data.head()

print ("Data:\n{}\n".format(data))

#Reading the same file, without a header
headers = ["dist", "rec_vel"]
data_no_headers = pd.read_csv("hubble_data_no_headers.csv", names=headers)
data_no_headers.head()

print ("Data:\n{}\n".format(data_no_headers))

#Using again the .csv with a header
data.set_index("distance", inplace= True)
data.head()

print ("Data:\n{}\n".format(data))

#Plot
data.plot()
plt.show()