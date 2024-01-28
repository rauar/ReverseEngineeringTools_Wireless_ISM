import sys

def calculate_change_frequency(data_records, width):
    change_frequencies = {}

    for position in range(len(data_records[0]) - width + 1):
        change_counter = 0
        prev_value = data_records[0][position:position+width]

        for record in data_records[1:]:
            current_value = record[position:position+width]
            if current_value != prev_value:
                change_counter += 1
            prev_value = current_value

        change_frequencies[(position,width)] = change_counter / (len(data_records) - 1)

    return change_frequencies

def calculate_character_spread(data_records, width=1):
    char_spread = {}

    for position in range(len(data_records[0]) - width + 1):
        unique_tokens = set()

        for record in data_records:
            token = record[position:position + width]
            unique_tokens.add(token)

        char_spread[position,width] = len(unique_tokens) - 1

    return char_spread

def calculate_differential_values(data_records, byte_width=1):
    differential_values = []

    for i in range(1, len(data_records)):
        current_row = data_records[i]
        previous_row = data_records[i - 1]

        current_values = [current_row[j:j + byte_width] for j in range(0, len(current_row), byte_width)]
        previous_values = [previous_row[j:j + byte_width] for j in range(0, len(previous_row), byte_width)]

        # Calculate XOR of corresponding bytes
        xor_values = [format(int(current, 16) ^ int(previous, 16), '1x') for current, previous in zip(current_values, previous_values)]

        differential_values.append(''.join(xor_values))

    return differential_values

def print_histogram(data):

    print("\nChange Frequencies:")
    max_length = max(data.values())
    
    for position, value in data.items():
        bar_length = int(value / max_length * 40)
        percentage = value * 100
        print(f"Pos {position[0]}+{position[1]}: {'#' * bar_length} {percentage:.2f}%")

def print_character_spread_histogram(char_spread, width):

    print("Character Spread:")

    max_value = 0xF**width  # Assuming max_value to be 0xF^width

    for position, value in char_spread.items():
        bar_length = int(value / max_value  * 100)
        print(f"Pos {position[0]}+{position[1]}: {'#' * bar_length} {value}")

def print_differential_values(differential_values):
    for row in differential_values:
        print("".join(row))


def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <data_file> <width>")
        sys.exit(1)

    data_file = sys.argv[1]
    width = int(sys.argv[2])

    with open(data_file, 'r') as file:
        data_records = [line.strip() for line in file]

    change_frequencies = calculate_change_frequency(data_records, width)
    char_spread = calculate_character_spread(data_records, width)

    print_histogram(change_frequencies)

    print_character_spread_histogram(char_spread, width)

    print_differential_values( calculate_differential_values(data_records) )

if __name__ == "__main__":
    main()
