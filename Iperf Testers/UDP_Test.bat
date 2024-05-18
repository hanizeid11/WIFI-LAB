@echo off
rem Loop to repeat the iperf3 command 10 times
for /l %%i in (1,1,10) do (
    "C:\iperf3\iperf-3.1.3-win64\iperf3.exe" -c 192.168.1.145 -u >> UDP_Ethernet.txt
)
