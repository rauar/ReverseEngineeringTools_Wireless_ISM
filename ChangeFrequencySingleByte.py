import sys

def calculate_change_frequency(data_records, num_neighbored_positions):
    if num_neighbored_positions < 1:
        print("Error: The number of neighbored positions must be greater than or equal to 1.")
        sys.exit(1)

    total_records = len(data_records)

    print(f"\nChange Frequency for {num_neighbored_positions} neighbored positions:")
    print("Positions            Change Frequency")

    for i in range(len(data_records[0]) - num_neighbored_positions + 1):
        change_counter = 0

        for j in range(total_records - 1):
            current_values = data_records[j][i:i + num_neighbored_positions]
            next_values = data_records[j + 1][i:i + num_neighbored_positions]

            if current_values != next_values:
                change_counter += 1

        change_frequency = change_counter / (total_records - 1) * 100
        positions_interval = f"{i}-{i + num_neighbored_positions - 1}"
        
        # Calculate the length of the bar based on change frequency
        bar_length = int(change_frequency / 2)
        bar = "|" + "=" * bar_length

        print(f"   [{positions_interval}]          {bar} {change_frequency:.2f}%")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <data_file> <num_neighbored_positions>")
        sys.exit(1)

    data_file = sys.argv[1]
    num_neighbored_positions = int(sys.argv[2])

    with open(data_file, 'r') as file:
        data_records = [line.strip() for line in file]

    calculate_change_frequency(data_records, num_neighbored_positions)
