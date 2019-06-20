#!/usr/bin/env python

import time
import socket
from emokit.emotiv import Emotiv

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("localhost", 38366))
serversocket.listen(1)
print("Waiting for Matlab")
clientsocket, address = serversocket.accept()
print("Connected to Matlab")

def sendToMatlab(packet):
    message = ''

    for channel in ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']:
	       message = message + str(packet.sensors[channel]['value']) + ","

    message = message + "\r\n"

    clientsocket.send(message.encode("ascii"))


def main():
    with Emotiv(display_output=False, verbose=False, write=False, force_epoc_mode=True, is_research=True) as headset:
        while headset.running:
            try:
                packet = headset.dequeue()
                if packet is not None:
                    sendToMatlab(packet)
                time.sleep(0.001)
            except Exception:
                clientsocket.close()
                headset.stop()


if __name__ == '__main__':
    main()
