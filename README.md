# AnomalyDetectionTool
The initial design concept of this cybersecurity tool encompasses a comprehensive approach to network packet analysis. 
This cybersecurity tool leverages the Scapy library to capture and dissect network packets on a specified network interface, notably the 'Wi-Fi' interface on a Windows system. As data packets flow into or out of your computer, the tool meticulously records various attributes of the network traffic. These attributes include packet type, size, source and destination addresses, and timestamps of network activity initiation.
The collected network data is then transformed into informative data visualizations. Additionally, the tool applies the Benford test for statistical analysis while concurrently scrutinizing the data for any irregularities. This dual approach enables users to uncover abnormal network behavior, potentially signaling a data breach or compromised network security.
Users have the flexibility to select which attributes they wish to visualize, tailoring the tool's output to their specific analytical needs.



*WILL NOT WORK WITHOUT NPCAP INSTALLED ON YOUR MACHINE!*
