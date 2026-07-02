import csv
import numpy as np
import matplotlib.pyplot as plt

# Define field indices
CALORIES = 1
PROTEINS = 2
FAT = 3
CARBOHYDRATE = 4

# Lists to store data
calories = []
proteins = []
fat = []
carbohydrate = []

# Open the CSV file
with open("nutrition.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        # Convert data to float and append to respective lists
        calories.append(float(row[CALORIES]))
        proteins.append(float(row[PROTEINS]))
        fat.append(float(row[FAT]))
        carbohydrate.append(float(row[CARBOHYDRATE]))

# Convert lists to NumPy arrays for easy computation
calories = np.array(calories)
proteins = np.array(proteins)
fat = np.array(fat)
carbohydrate = np.array(carbohydrate)

# Compute descriptive statistics
total_foods = len(calories)
mean_calories = np.mean(calories)
mean_proteins = np.mean(proteins)
mean_fat = np.mean(fat)
mean_carbohydrate = np.mean(carbohydrate)

# Print descriptive statistics
print("Descriptive Statistics:")
print("Total number of foods:", total_foods)
print("Mean calories per serving:", mean_calories)
print("Mean proteins per serving:", mean_proteins)
print("Mean fat per serving:", mean_fat)
print("Mean carbohydrate per serving:", mean_carbohydrate)

# Generate three figures
# Figure 1: Histogram of calories
plt.figure(figsize=(8, 6))
plt.hist(calories, bins=20, color='blue', edgecolor='black')
plt.title('Distribution of Calories per Serving')
plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Figure 2: Scatter plot of proteins vs fat
plt.figure(figsize=(8, 6))
plt.scatter(proteins, fat, color='red', alpha=0.5)
plt.title('Proteins vs Fat per Serving')
plt.xlabel('Proteins (g)')
plt.ylabel('Fat (g)')
plt.grid(True)
plt.show()

# Figure 3: Box plot of carbohydrate
plt.figure(figsize=(8, 6))
plt.boxplot(carbohydrate, vert=False)
plt.title('Distribution of Carbohydrate per Serving')
plt.xlabel('Carbohydrate (g)')
plt.xlabel('Serving (100 g)')
plt.grid(True)
plt.show()
