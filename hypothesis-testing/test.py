import numpy
import matplotlib.pyplot as plt
from scipy.stats import shapiro, normaltest, ttest_ind, mannwhitneyu

# Define field indices
REVIEW_NUMBER = 0
BRAND = 1
VARIETY = 2
STYLE = 3
COUNTRY = 4
STARS = 5
TOP_TEN = 6


def load_data(filename):
    """Load data from CSV file."""
    return numpy.genfromtxt('ramen-ratings.csv', delimiter=",", dtype=None, names=True, encoding="utf8")


def clean_data(data):
    """Remove rows with missing ratings."""
    return data[~numpy.isnan(data['Stars'])]


def plot_histogram(group, label):
    """Plot histogram of stars for a group."""
    plt.hist(group, bins=20, alpha=0.5, label=label)
    plt.axvline(group.mean(), color='k', linestyle='dashed', linewidth=1)


def perform_normality_tests(group):
    """Perform Shapiro-Wilk and D'Agostino's K² tests for normality."""
    shapiro_stat, shapiro_p = shapiro(group)
    normaltest_stat, normaltest_p = normaltest(group)
    return shapiro_p, normaltest_p


def perform_statistical_test(group1, group2):
    """Perform statistical test (t-test or Mann-Whitney U test)."""
    shapiro_p1, normaltest_p1 = perform_normality_tests(group1)
    shapiro_p2, normaltest_p2 = perform_normality_tests(group2)

    if shapiro_p1 > 0.05 and shapiro_p2 > 0.05:
        # Data is normally distributed
        t_stat, t_p = ttest_ind(group1, group2)
        return t_p
    else:
        # Data is not normally distributed
        mwu_stat, mwu_p = mannwhitneyu(group1, group2)
        return mwu_p


def analyze_ramen_ratings(data):
    """Analyze ramen ratings."""
    # Clean data
    data_cleaned = clean_data(data)

    # Split data into two groups based on whether ramen is in a bowl or cup
    group_bowl = data_cleaned[data_cleaned['Style'] == 'Bowl']['Stars']
    group_cup = data_cleaned[data_cleaned['Style'] == 'Cup']['Stars']

    # Plot histograms for each group
    plt.figure()
    plot_histogram(group_bowl, 'Bowl')
    plt.xlabel('Stars')
    plt.ylabel('Frequency')
    plt.title('Histogram of Stars for Ramen in Bowl')
    plt.legend()
    plt.savefig('hist_bowl.pdf')

    plt.figure()
    plot_histogram(group_cup, 'Cup')
    plt.xlabel('Stars')
    plt.ylabel('Frequency')
    plt.title('Histogram of Stars for Ramen in Cup')
    plt.legend()
    plt.savefig('hist_cup.pdf')

    # Perform statistical test
    p_value = perform_statistical_test(group_bowl, group_cup)
    print("p-value of statistical test:", p_value)
    if p_value <= 0.05:
        print("Reject null hypothesis. There is a significant difference between the groups.")
    else:
        print("Fail to reject null hypothesis.")


# Load data from CSV file
data = load_data("ramen-ratings.csv")

# Analyze ramen ratings
analyze_ramen_ratings(data)
