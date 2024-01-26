import sys

def calculate_change_frequency(data_records):
    num_records = len(data_records)
    num_positions = len(data_records[0])
    
    change_frequencies = []

    for position in range(num_positions):
        change_counter = 0
        prev_value = None

        for record in data_records:
            current_value = record[position]

            if prev_value is not None and current_value != prev_value:
                change_counter += 1

            prev_value = current_value

        change_frequency = change_counter / (num_records - 1)
        change_frequencies.append(change_frequency)

    return change_frequencies

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data_records = [line.strip() for line in file]

    return data_records

def plot_histogram(change_frequencies):
    max_width = 50
    max_value = max(change_frequencies)
    scale_factor = max_width / max_value if max_value > 0 else 1

    print("Change Frequencies Histogram:")
    
    for i, frequency in enumerate(change_frequencies):
        bar_width = int(frequency * scale_factor)
        bar = "#" * bar_width
        print(f"Position {i:2d}:{bar} ({frequency:.2%})")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]
    data_records = read_data_from_file(file_path)

    result = calculate_change_frequency(data_records)
    plot_histogram(result)
