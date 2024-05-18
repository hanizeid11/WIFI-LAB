import re
import statistics

# Define the function to extract bandwidth and datagram info from the iperf log
def extract_info(log_content):
    # Regular expression to find the Bandwidth and Lost/Total Datagrams lines
    bandwidth_pattern = re.compile(r'Bandwidth\s*\n.*?\b(\d+\.\d+) Mbits/sec\b')
    datagram_pattern = re.compile(r'Lost/Total Datagrams\s*\n.*?\b(\d+)/(\d+)')
    
    bandwidths = [float(bw) for bw in bandwidth_pattern.findall(log_content)]
    lost_datagrams, total_datagrams = zip(*[map(int, match) for match in datagram_pattern.findall(log_content)])
    
    return bandwidths, lost_datagrams, total_datagrams

# Define the function to append statistics to the log file
def append_statistics_to_file(file_path, statistics_text):
    with open(file_path, 'a') as file:
        file.write("\n")
        file.write(statistics_text)

# Read the log content from the specified file path
log_file_path = r'C:\Users\hani_\Downloads\Wifi lab\WifiPerformance\TCP_EthernetWIFI.txt'
with open(log_file_path, 'r') as file:
    log_content = file.read()

# Extract bandwidths and datagram info
bandwidths, lost_datagrams, total_datagrams = extract_info(log_content)

# Calculate statistics for bandwidth
if bandwidths:
    min_bandwidth = min(bandwidths)
    max_bandwidth = max(bandwidths)
    avg_bandwidth = sum(bandwidths) / len(bandwidths)
    stddev_bandwidth = statistics.stdev(bandwidths) if len(bandwidths) > 1 else 0
    
    bandwidth_statistics_text = (
        "Statistics for bandwidth:\n"
        f"Minimum Bandwidth: {min_bandwidth} Mbits/sec\n"
        f"Maximum Bandwidth: {max_bandwidth} Mbits/sec\n"
        f"Average Bandwidth: {avg_bandwidth} Mbits/sec\n"
        f"Standard Deviation: {stddev_bandwidth} Mbits/sec\n"
    )
else:
    bandwidth_statistics_text = "No bandwidth data found.\n"

# Calculate statistics for datagrams
if lost_datagrams and total_datagrams:
    total_sent = sum(total_datagrams)
    total_lost = sum(lost_datagrams)
    percentage_lost = (total_lost / total_sent) * 100 if total_sent > 0 else 0
    min_lost = min(lost_datagrams)
    max_lost = max(lost_datagrams)
    avg_lost = sum(lost_datagrams) / len(lost_datagrams)
    stddev_lost = statistics.stdev(lost_datagrams) if len(lost_datagrams) > 1 else 0

    datagram_statistics_text = (
        "Statistics for lost datagrams:\n"
        f"Minimum Lost Datagrams: {min_lost}\n"
        f"Maximum Lost Datagrams: {max_lost}\n"
        f"Average Lost Datagrams: {avg_lost}\n"
        f"Standard Deviation: {stddev_lost}\n"
        f"Total Datagrams Sent: {total_sent}\n"
        f"Total Data Loss: {total_lost}\n"
        f"Percentage Lost: {percentage_lost:.2f}%\n"
    )
else:
    datagram_statistics_text = "No datagram loss data found.\n"

# Combine the statistics text
statistics_text = bandwidth_statistics_text + "\n" + datagram_statistics_text

# Append statistics to the log file
append_statistics_to_file(log_file_path, statistics_text)

# Print the statistics
print(statistics_text)
