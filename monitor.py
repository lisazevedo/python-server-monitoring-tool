import sys 
from datetime import datetime 
from scapy.all import sr1, sr, srp, IP, ICMP, TCP
import time

TARGET="192.168.1.9"
PORTS=[22]

def monitor():

    while(True):
        # sr(): send and receive packets. The packets must be layer 3
        # flags: S (SYN a control bit in the incoming segment, occupying one sequence number, used at the initiation of a connection, to indicate where the sequence numbering will start) 
        ans, unans = sr(IP(dst=TARGET)/TCP(dport=PORTS,flags="S"), timeout=1, verbose=0)
        
        hour_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S") # get current time 

        if (str(ans) == "<Results: TCP:0 UDP:0 ICMP:0 Other:0>"):
            print("The server {} was DOWN at ".format(TARGET) + hour_time)        
        else:
            print("The server {} was UP at ".format(TARGET) + hour_time)

        time.sleep(5)    

monitor()