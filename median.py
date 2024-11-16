import numpy as np

data = np.genfromtxt(r"C:\Users\user\Desktop\MCL\Wholesale customers data.csv", delimiter=',', skip_header=1)

fresh_mean = np.mean(data[:, 0])
milk_mean = np.mean(data[:, 1])
grocery_mean = np.mean(data[:, 2])
frozen_mean = np.mean(data[:, 3])
detergents_paper_mean = np.mean(data[:, 4])
delicatessen_mean = np.mean(data[:, 5])

fresh_median = np.median(data[:, 0])
milk_median = np.median(data[:, 1])
grocery_median = np.median(data[:, 2])
frozen_median = np.median(data[:, 3])
detergents_paper_median = np.median(data[:, 4])
delicatessen_median = np.median(data[:, 5])

print("Average:")
print("Fresh: ", fresh_mean)
print("Milk: ", milk_mean)
print("Grocery: ", grocery_mean)
print("Frozen: ", frozen_mean)
print("Detergents_Paper: ", detergents_paper_mean)
print("Delicatessen: ", delicatessen_mean)

print("\nMedian:")
print("Fresh: ", fresh_median)
print("Milk: ", milk_median)
print("Grocery: ", grocery_median)
print("Frozen: ", frozen_median)
print("Detergents_Paper: ", detergents_paper_median)
print("Delicatessen: ", delicatessen_median)

