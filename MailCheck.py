# Import libraries
import poplib
from email import parser
import time, datetime
from wakeonlan import wol

# Variables
MAC = 'AA:BB:CC:DD:EE:FF'
user = 'jacopo.nasi'
pwd = '1234jacopo'

# Gmail POP3 Server
try:
    pop_link = poplib.POP3_SSL('pop.gmail.com')
except:
    print(time.strftime("%d/%m %H:%M") + ' - POP3 Error');
    raise SystemExit()

try:
    pop_link.user(user)
except:
    print(time.strftime("%d/%m %H:%M") + ' - LOGIN Error');
    raise SystemExit()

try:
    pop_link.pass_(pwd)
except:
    print(time.strftime("%d/%m %H:%M") + ' - LOGIN Error');
    raise SystemExit()

# Get messages from server:
msg = [pop_link.retr(i) for i in range(1, len(pop_link.list()[1]) + 1)]
# Concat message pieces:
msg = ["\n".join(mssg[1]) for mssg in msg]
msg = [parser.Parser().parsestr(mssg) for mssg in msg]

# Printing log and cheching MSG syntax
for msg in msg:
    if msg['subject']=='WOL': # Correct Message receiver
        print(time.strftime("%d/%m %H:%M") + ' - WOL Packet Sended (' + msg['from'] + ')');
        # Sending MP to MAC, Broadcast IP and Port 9
        wol.send_magic_packet(MAC, ip_address='255.255.255.255', port=9)
    else: # Wrong message receiver
        print(time.strftime("%d/%m %H:%M") + ' - WRONG Message');

# Close the active connection
pop_link.quit()
