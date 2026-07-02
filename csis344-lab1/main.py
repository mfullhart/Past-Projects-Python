# import csv
import csv

# define field indices
NAME = 0
MASS = 4
YEAR = 6

# setting up values to keep track of vital information
num_meteorites = 0
total_mass = 0
min_mass = None
max_mass = None

# open the file
with open("Meteorite_Landings.csv", encoding="utf8",) as f:
    # the file is now open, and the variable f refers to it
    # now it reads the csv
    csv_reader = csv.reader(f, delimiter=',', quotechar='"')

    # get the header row
	header = next(csv_reader)

    # for every row in the file, it does the following
	for row in csv_reader:

        # get the mass field as a string
		mass_field = row[MASS]

        # if the mass field is not empty, then it does the following
		if mass_field != '':
            # convert that string to a float
			mass = float(mass_field)

            # if mass value is greater than zero
			if mass > 0:
                # accumulate
				total_mass += mass
                num_meteorites += 1

                # if there is no minimum mass yet;
				# or this one is smaller than the existing minimum
				if min_mass is None or (0 < mass < min_mass):
                    # it's now the new minimum, so keep track of it's attributes
					min_mass = mass
                    min_name = row[NAME]
                    min_year = row[YEAR]

                # if there is no maximum mass yet,
				# or this is larger than the existing maximum
				if max_mass is None or mass > max_mass:
                    # it's now the new maximum, so it's attributes need to be saved
					max_mass = mass
                    max_name = row[NAME]
                    max_year = row[YEAR]

    # print out our findings
	print(f'number of meteorites: {num_meteorites}')
    print(f'average mass: {total_mass / num_meteorites} g')
    print(f'smallest meteorite: "{min_name}", {min_mass} g, in {min_year}')
    print(f'largest meteorite: "{max_name}", {max_mass} g, in {max_year}')

    exit()
