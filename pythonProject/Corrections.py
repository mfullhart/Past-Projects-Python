# Program to calculate hot dog cookout

def calculate_packages(attendance, hotdogs_per_person):
    # Calculate total hot dogs and buns needed
    total_hotdogs_needed = attendance * hotdogs_per_person
    hotdogs_per_package = 10
    buns_per_package = 8

    # Calculate minimum number of packages for hot dogs and buns
    packages_hotdogs = total_hotdogs_needed // hotdogs_per_package
    packages_buns = total_hotdogs_needed // buns_per_package

    # Calculate leftovers
    leftover_hotdogs = total_hotdogs_needed % hotdogs_per_package
    leftover_buns = total_hotdogs_needed % buns_per_package

    return packages_hotdogs, packages_buns, leftover_hotdogs, leftover_buns


def main():
    # Get user inputs
    attendance = int(input("Enter the total attendance: "))
    hotdogs_per_person = int(input("Enter the hot dogs per person: "))

    # Calculate package details
    hotdog_packages, bun_packages, leftover_hotdogs, leftover_buns = calculate_packages(attendance, hotdogs_per_person)

    # Display results
    print(f"Minimum number of hot dog packages: {hotdog_packages}")
    print(f"Minimum number of bun packages: {bun_packages}")
    print(f"Leftover hot dogs: {leftover_hotdogs}")
    print(f"Leftover buns: {leftover_buns}")

main()
