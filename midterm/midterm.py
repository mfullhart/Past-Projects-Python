"""
Midterm Exam

mfullhart20@georgefox.edu
"""

# TODO implement all the things

# Imports
import numpy
import matplotlib.pyplot as plt

# Define field indices
CENTER = 0
STATUS = 1
CASE_NUMBER = 2
PATENT_NUMBER = 3
APPLICATION_SN = 4
TITLE = 5
PATENT_EXPIRATION_DATE = 6


def load_data(filename):
    """Load data from CSV file."""
    return numpy.genfromtxt('NASA_Patents_20240301', delimiter=",", encoding="utf8", dtype=None, names=True)


def total_patent_applications(data):
    """Task 1: Total number of patent applications filed by all centers."""
    return len(data)


def total_issued_patents(data):
    """Task 2: Total number of patents issued by all centers."""
    issued_patents = data[data['STATUS'] == 'issued']
    return len(issued_patents)


def oldest_patent(data):
    """Task 3: Oldest patent information."""
    issued_patents = data[data['STATUS'] == 'issued']
    oldest_patent_index = numpy.argmin(issued_patents['PATENT_EXPIRATION_DATE'])
    return issued_patents[oldest_patent_index]


def nasa_centers(data):
    """Task 4: List of NASA centers that have filed patent applications."""
    return numpy.unique(data['CENTER'])


def patent_applications_by_center(data, unique_centers):
    """Task 5: Number of patent applications filed by each center."""
    center_counts = {center: numpy.sum(data['CENTER'] == center) for center in unique_centers}
    return center_counts


def percentage_awarded_by_center(data, unique_centers, center_counts):
    """Task 6: Percentage of patent applications awarded for each center."""
    percentage_awarded_by_center = {}
    for center in unique_centers:
        submitted = numpy.sum(data[(data['CENTER'] == center) & (data['STATUS'] != 'issued')])
        awarded = center_counts[center] - submitted
        percentage_awarded_by_center[center] = (awarded / center_counts[center]) * 100
    return percentage_awarded_by_center


def patents_expiring_by_year(data):
    """Task 7: Number of patents expiring each year from 2022 to 2035."""
    issued_patents = data[data['STATUS'] == 'issued']
    expiration_years = [int(date.split('-')[0]) for date in issued_patents['PATENT_EXPIRATION_DATE']]
    year_counts = {year: expiration_years.count(year) for year in range(2022, 2036)}
    return year_counts


def active_patents_by_center(data, unique_centers):
    """Task 8: Active patents per center as of the first day of next month."""
    issued_patents = data[data['STATUS'] == 'issued']
    active_patents_per_center = {}
    for center in unique_centers:
        active_patents_per_center[center] = numpy.sum(
            (issued_patents['CENTER'] == center) & (issued_patents['PATENT_EXPIRATION_DATE'] >= '2024-04-01')
        )
    return active_patents_per_center


def main():
    data = load_data('NASA_Patents_20240301.csv')

    print("Total number of patent applications filed by all centers:", total_patent_applications(data))

    print("Total number of patents issued by all centers:", total_issued_patents(data))

    oldest = oldest_patent(data)
    print("Oldest patent information:")
    print("  Patent Number:", oldest['PATENT_NUMBER'])
    print("  Patent Title:", oldest['TITLE'])
    print("  Patent Expiration Date:", oldest['PATENT_EXPIRATION_DATE'])

    print("NASA centers that have ever filed a patent application:", nasa_centers(data))

    unique_centers = nasa_centers(data)

    center_counts = patent_applications_by_center(data, unique_centers)
    sorted_center_counts = sorted(center_counts.items(), reverse=True)
    print("Number of patent applications filed by each center (sorted in descending order):")
    for center, count in sorted_center_counts:
        print(f"  {center}: {count}")

    percentage_awarded = percentage_awarded_by_center(data, unique_centers, center_counts)
    print("Percentage of patent applications awarded for each center:")
    for center, percentage in percentage_awarded.items():
        print(f"  {center}: {percentage: .2f}%")

    year_counts = patents_expiring_by_year(data)
    print("Number of patents expiring each year from 2022 to 2035:")
    for year, count in year_counts.items():
        print(f"  {year}: {count}")

    active_patents = active_patents_by_center(data, unique_centers)
    print("Active patents per center as of the first day of next month:")
    for center, count in active_patents.items():
        print(f"  {center}: {count}")

    # Plot number of patents expiring each year
    plt.figure()
    plt.bar(year_counts.keys(), year_counts.values())
    plt.title('Number of Patents Expiring Each Year (2022-2035)')
    plt.xlabel('Year')
    plt.ylabel('Number of Patents')
    plt.show()

    # Plot number of active patents per center
    plt.figure(2)
    plt.bar(active_patents.keys(), active_patents.values())
    plt.title('Number of Active Patents Per Center (as of April 1, 2024)')
    plt.xlabel('NASA Center')
    plt.ylabel('Number of Active Patents')
    plt.xticks(rotation=45)
    plt.show()
