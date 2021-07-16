import sys
import time
from socket import *

# Creation of client's socket
# AF_INET means underlying network is using IPv4
# SOCK_DGRAM indicates socket is of UDP type
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
# Initializing an array of times
times = []
# Initialize number of lost packets to 0
lost = 0
# Sending ping <host> as message
message = 'ping' + gethostname()

# Get host ip address
host_ip = gethostbyname(gethostname())
addr = (host_ip, 12000)
print('Pinging localhost ['  + addr[0] + '] with ' + str(sys.getsizeof(message)) + ' bytes of data:')
message = message.encode()

print('')

# Send 10 ping messages to the server
for pings in range(10):

    # Send ping and record intial time
    start = time.time()
    clientSocket.sendto(message, addr)

    # If data is received back from server, the following gets done
    try:
        message, server = clientSocket.recvfrom(1024)
        # Calculate elapsed time
        elapsed = time.time() - start
        # Append to array of times
        times.append(elapsed)
        message.decode()
        print('Reply from ' + addr[0] + ': time=' + str(elapsed) + 'ms')
        print('')

    # If data is not received back from server, print "Request timed out" msg
    # and keep track of no. of lost packets
    except timeout:
        print('Request timed out.')
        print('')
        lost = lost + 1

print('')

# Output all packet info to screen
print ('Ping statistics for ' + addr[0] + ':')
print ('  Packets: Sent = 10, Received = ' + str(10-lost) + ', Lost = ' + str(lost) + ' (' + str(lost/10*100) + '% loss' + ')')

print('')

# Use min, max, and sum functions on the times array to output RTT stats
print ('Approximate round trip times (RTT) in milli-seconds:')
print ('  Minimum = ' + str(min(times)) + 'ms, Maximum = ' + str(max(times)), 'ms, Average = ' + str(sum(times)/(10)) + 'ms')
