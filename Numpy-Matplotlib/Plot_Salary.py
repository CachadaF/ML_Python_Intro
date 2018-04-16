#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

#fromfile is useful to read numbers.
salary = np.fromfile("salaries.txt", dtype=int, sep=",")
#genfromtxt is useful for reading strings, fromfile is not good for that.
names = np.genfromtxt("names.txt", dtype='str', delimiter=",")

#Arrange for the names
x = np.arange(len(names))

#Showing the plot of salaries,names.
plt.bar(x, salary)
#xticks: All it does it is replace the numbers in x with names. s
plt.xticks(x, names)
plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of {} random people".format(len(names)))
plt.show()

#Testing more supported functions
print("Max:{}\nMin:{}\nAvg:{}\nMed:{}".format(np.max(salary), np.min(salary), np.average(salary), np.median(salary)))

#Delete upper and lower values
salaries_new = salary[2:-2]
names_new = names[2:-2]

y = np.arange(len(names_new))

plt.bar(y, salaries_new)
plt.xticks(y, names_new)
plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of {} random people".format(len(names_new)))
plt.show()

print("Max:{}\nMin:{}\nAvg:{}\nMed:{}".format(np.max(salaries_new), np.min(salaries_new), np.average(salaries_new), np.median(salaries_new)))

