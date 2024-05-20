import re
import statistics

# Path to the iperf test result file
file_path = r"C:\Users\hani_\Downloads\Wifi lab\WifiPerformance\Second trial\Ethernet_UDP100_Receiver.txt"
# Define the function to append statistics to the log file
def append_statistics_to_file(file_path, statistics_text):
    with open(file_path, 'a') as file:
        file.write("\n")
        file.write(statistics_text)

# Read the file content
with open(file_path, 'r') as file:
    iperf_results = file.read()

# Regex to find the bitrate and lost/total datagrams values from the summary lines
pattern = re.compile(r'\[ *\d+\] +0\.00-10+\.\d+ +sec +[\d\.]+ +MBytes +([\d\.]+) +(M|K)bits/sec +\d+\.\d+ ms +(\d+)/(\d+)')

# Find all matches in the text
matches = pattern.findall(iperf_results)
print(matches)
# Extract bitrates, lost datagrams, and total datagrams
bitrates = []
total_lost_datagrams = 0
total_received_datagrams = 0

for bitrate, unit, lost, total in matches:
    if unit == 'K':
        bitrate = float(bitrate) / 1000  # Convert Kbits to Mbits
    bitrates.append(float(bitrate))
    total_lost_datagrams += int(lost)
    total_received_datagrams += int(total)

# Calculate percentage of lost datagrams
percentage_lost = (total_lost_datagrams / total_received_datagrams) * 100 if total_received_datagrams > 0 else 0

# Calculate statistics
if bitrates:
    min_bitrate = min(bitrates)
    max_bitrate = max(bitrates)
    avg_bitrate = sum(bitrates) / len(bitrates)
    std_bitrate = statistics.stdev(bitrates) if len(bitrates) > 1 else 0.0  # Standard deviation is 0 if only one value

    # Print the results
    stat=(f"Minimum Bitrate: {min_bitrate:.2f} Mbits/sec\n"
    f"Maximum Bitrate: {max_bitrate:.2f} Mbits/sec\n"
    f"Average Bitrate: {avg_bitrate:.2f} Mbits/sec\n"
    f"Standard Deviation of Bitrate: {std_bitrate:.2f} Mbits/sec\n"
    f"Total Lost Datagrams: {total_lost_datagrams}\n"
    f"Total Received Datagrams: {total_received_datagrams}\n"
    f"Percentage of Lost Datagrams: {percentage_lost:.2f}%\n")
    print(stat)
    append_statistics_to_file(file_path, stat)

else:
    print("No bitrate values found in the file.")
