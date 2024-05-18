import re
import statistics

# Define the function to extract sender bandwidth values from the iperf log
def extract_bandwidths(log_content, keyword):
    # Regular expression to find the bandwidth lines for the given keyword (sender or receiver)
    pattern = re.compile(rf'\b{keyword}\s*\n.*?\b(\d+\.\d+) Mbits/sec\b')
    bandwidths = pattern.findall(log_content)
    return [float(bw) for bw in bandwidths]

# Define the function to append statistics to the log file
def append_statistics_to_file(file_path, statistics_text):
    with open(file_path, 'a') as file:
        file.write("\n")
        file.write(statistics_text)

# Read the log content from the specified file path
log_file_path = r'C:\Users\hani_\Downloads\Wifi lab\WifiPerformance\TCP_EthernetWIFI.txt'
with open(log_file_path, 'r') as file:
    log_content = file.read()

# Extract sender and receiver bandwidth values
sender_bandwidths = extract_bandwidths(log_content, 'sender')
receiver_bandwidths = extract_bandwidths(log_content, 'receiver')

# Calculate statistics for the sender bandwidth results
if sender_bandwidths:
    min_sender_bw = min(sender_bandwidths)
    max_sender_bw = max(sender_bandwidths)
    avg_sender_bw = sum(sender_bandwidths) / len(sender_bandwidths)
    stddev_sender_bw = statistics.stdev(sender_bandwidths)
    
    sender_statistics_text = (
        "Statistics for sender bandwidths:\n"
        f"Minimum Bandwidth: {min_sender_bw} Mbits/sec\n"
        f"Maximum Bandwidth: {max_sender_bw} Mbits/sec\n"
        f"Average Bandwidth: {avg_sender_bw} Mbits/sec\n"
        f"Standard Deviation: {stddev_sender_bw} Mbits/sec\n"
    )
else:
    sender_statistics_text = "No sender bandwidth data found.\n"

# Calculate statistics for the receiver bandwidth results
if receiver_bandwidths:
    min_receiver_bw = min(receiver_bandwidths)
    max_receiver_bw = max(receiver_bandwidths)
    avg_receiver_bw = sum(receiver_bandwidths) / len(receiver_bandwidths)
    stddev_receiver_bw = statistics.stdev(receiver_bandwidths)
    
    receiver_statistics_text = (
        "Statistics for receiver bandwidths:\n"
        f"Minimum Bandwidth: {min_receiver_bw} Mbits/sec\n"
        f"Maximum Bandwidth: {max_receiver_bw} Mbits/sec\n"
        f"Average Bandwidth: {avg_receiver_bw} Mbits/sec\n"
        f"Standard Deviation: {stddev_receiver_bw} Mbits/sec\n"
    )
else:
    receiver_statistics_text = "No receiver bandwidth data found.\n"

# Combine the statistics text
statistics_text = sender_statistics_text + "\n" + receiver_statistics_text

# Append statistics to the log file
append_statistics_to_file(log_file_path, statistics_text)

# Print the statistics
print(statistics_text)