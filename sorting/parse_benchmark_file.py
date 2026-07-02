import re
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


def convert_to_ns(value, unit):
    """Convert time values to nanoseconds with proper unit handling"""
    unit = unit.lower().strip()
    if unit == 'µs':
        return value * 1000
    elif unit == 'ms':
        return value * 1000000
    elif unit == 's':
        return value * 1000000000
    return value  # Default to ns if no unit specified


def parse_benchmark_file(file_path):
    """Robust parser that handles all algorithm timings"""
    data = {
        'sizes': [],
        'QuickSortRecursive': [],
        'QuickSortIterative': [],
        'InsertionSort': [],
        'SortInts': []
    }

    print(f"\nReading benchmark data from: {os.path.abspath(file_path)}")

    with open(file_path, 'r') as f:
        current_size = None
        current_values = {}

        for line in f:
            line = line.strip()

            # Size detection
            if line.startswith('Size:'):
                if current_size is not None:
                    # Save previous entry
                    data['sizes'].append(current_size)
                    for algo in data:
                        if algo != 'sizes':
                            data[algo].append(current_values.get(algo, None))

                # Reset for new entry
                try:
                    current_size = int(line.split(':')[1].strip())
                    current_values = {}
                except (IndexError, ValueError):
                    print(f"Warning: Couldn't parse size from line: {line}")
                    current_size = None
                continue

            # Time value parsing
            if ':' in line:
                try:
                    algo_part, time_part = line.split(':', 1)
                    algo = algo_part.strip()
                    time_str = time_part.strip()

                    if algo in data:
                        # Extract numeric value and unit
                        match = re.match(r'([\d.]+)\s*(\D+)', time_str)
                        if match:
                            value = float(match.group(1))
                            unit = match.group(2).strip()
                            ns_time = convert_to_ns(value, unit)
                            current_values[algo] = ns_time
                        else:
                            print(f"Warning: Couldn't parse time from: {time_str}")
                except Exception as e:
                    print(f"Warning: Error parsing line '{line}': {e}")

    # Add the last entry if exists
    if current_size is not None:
        data['sizes'].append(current_size)
        for algo in data:
            if algo != 'sizes':
                data[algo].append(current_values.get(algo, None))

    # Validate InsertionSort data
    if all(t is None or t <= 1 for t in data['InsertionSort']):
        print("\nERROR: Invalid InsertionSort data detected!")
        print("Please ensure your file contains actual InsertionSort timings")
        print("Example format:")
        print("InsertionSort: 5.1104ms  # For 10100 elements")
        return None

    print("\nSuccessfully parsed data:")
    print("-----------------------")
    for i, size in enumerate(data['sizes']):
        print(f"Size: {size}")
        for algo in data:
            if algo != 'sizes' and data[algo][i] is not None:
                print(f"  {algo}: {data[algo][i]:.2f} ns")
    print("-----------------------\n")

    return data


def plot_results(data):
    """Generate professional performance plots"""
    if not data or not data['sizes']:
        raise ValueError("No valid data to plot")

    plt.figure(figsize=(12, 8))
    plt.style.use('seaborn-v0_8')

    # Configure algorithms and styles
    algorithms = [
        ('QuickSortRecursive', '#1f77b4', '-'),
        ('QuickSortIterative', '#ff7f0e', '--'),
        ('InsertionSort', '#d62728', ':'),
        ('SortInts', '#2ca02c', '-.')
    ]

    # Plot each algorithm
    for algo, color, style in algorithms:
        if algo in data and len(data[algo]) == len(data['sizes']):
            valid_points = [(size, t) for size, t in zip(data['sizes'], data[algo]) if t is not None and t > 0]
            if valid_points:
                sizes, times = zip(*valid_points)
                plt.plot(sizes, times,
                         label=algo,
                         color=color,
                         linestyle=style,
                         linewidth=2.5,
                         marker='o',
                         markersize=5)

    # Configure plot appearance
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Input Size (elements)', fontsize=12)
    plt.ylabel('Time (nanoseconds)', fontsize=12)
    plt.title('Sorting Algorithm Performance', fontsize=14, pad=20)
    plt.grid(True, which="both", ls="-", alpha=0.4)
    plt.legend(fontsize=10, framealpha=1)

    # Format axes
    ax = plt.gca()
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_major_formatter(ScalarFormatter())
        axis.set_minor_formatter(ScalarFormatter())

    # Save output
    output_file = 'sorting_performance.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Successfully generated {output_file}")


if __name__ == "__main__":
    try:
        # Locate input file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(script_dir, 'file.txt')

        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Could not find file.txt in {script_dir}")

        # Parse and plot
        benchmark_data = parse_benchmark_file(input_file)
        if benchmark_data:
            plot_results(benchmark_data)

    except Exception as e:
        print(f"\nERROR: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure file.txt exists in the script directory")
        print("2. Verify the file contains all algorithm timings")
        print("3. Example format:")
        print("""
Size: 100
  QuickSortRecursive: 10.2µs
  QuickSortIterative: 9.8µs
  InsertionSort: 50.1µs  # MUST have actual values
  SortInts: 4.3µs""")