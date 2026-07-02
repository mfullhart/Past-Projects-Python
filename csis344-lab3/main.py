# import numpy
import numpy
import matplotlib.pyplot as plt

# define field indices
NAME = 0
MASS = 4
YEAR = 6


# conversion function for mass values
# take in a string that hopefully contains a mass value
# convert it to a float
# if it's blank or zero or negative, return numpy.nan to easily exclude
def convert_mass_field_to_value(mass_field):
	if mass_field == '':
		mass_value = numpy.nan
	else:
		mass_value = float(mass_field)
		if mass_value <= 0:
			mass_value = numpy.nan
	return mass_value


# conversion function for year values
def convert_year_field_to_value(year_field):
	if year_field == '':
		year_value = numpy.nan
	else:
		# year_field: "01/01/1880 12:00:00 AM"
		date, _, _ = year_field.split(' ')
		m, d, y = date.split('/')
		year_value = int(y)
	return year_value


# dictionary of converters
# key: column index
# value: conversion function for that column
converters = {
	MASS: convert_mass_field_to_value,
	6: convert_year_field_to_value
}

# use numpy to load the data from file
data = numpy.genfromtxt('Meteorite_Landings.tsv', delimiter="\t", encoding="utf8", dtype=None,
						converters=converters, names=True)

# keep just the meteorites with a mass
data = data[numpy.where(~numpy.isnan(data['mass_g']))]

print(data.dtype)

# get masses
masses = data['mass_g']

# get years
years = data['year']

# an x–y scatter of year (x-axis) versus mass (y-axis, using a log scale
plt.figure()
plt.scatter(years, masses)
plt.xlabel("year")
plt.ylabel("mass (g)")
plt.yscale('log')
plt.title("Year vs Mass")
plt.show()
# plt.savefig('year_vs_mass.png) <- to add to the repository

# ploting the bar graph  of the count of each unique class (as recorded in the recclass column)
# of lunar meteorite across all years

# get just the lunar meteorites
lunar_meteorites = data[numpy.where(numpy.char.startswith(data['recclass'], 'Lunar'))]

# get the count of each unique type of lunar meteorite
lunar_classes, lunar_counts = numpy.unique(lunar_meteorites['recclass'], return_counts=True)

# now, plot it
plt.figure(2)
plt.bar(lunar_classes, lunar_counts)
plt.xlabel("class")
plt.ylabel("count")
plt.xticks(rotation=90)
plt.title("Class Count")
plt.show()

# setting the bins for 10 decades
bin_bounds = numpy.arange(860, 2031, 10)

plt.figure(3)
plt.hist(data['year'], bins=bin_bounds, weights=data['mass_g'])
plt.xlabel('decade')
plt.ylabel('total mass (g)')
plt.title('Mass by Decade')
plt.show()

exit()
