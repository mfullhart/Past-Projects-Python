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

# determine the number of meteorites ignoring the ones with nan mass
num_meteorites = numpy.count_nonzero(~numpy.isnan(masses))

# determine smallest and largest meteorites and their names and years by indexes
min_index = numpy.nanargmin(masses)
min_row = data[min_index]
min_mass = min_row['mass_g']
min_name = min_row['name']
min_year = min_row['year']

max_index = numpy.nanargmax(masses)
max_row = data[max_index]
max_mass = max_row['mass_g']
max_name = max_row['name']
max_year = max_row['year']

# add the total mass
mean_mass = numpy.nanmean(masses)

# print out our findings
print(f'number of meteorites: {num_meteorites}')
print(f'average mass: {mean_mass} g')
print(f'smallest meteorite: "{min_name}", {min_mass} g, {min_year}')
print(f'largest meteorite: "{max_name}", {max_mass} g, {max_year}')