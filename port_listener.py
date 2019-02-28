#!/usr/bin/python3
"""
    Point of this script is to spawn tcp servers based on
    configuration provided in proper file in etc.
"""

import socketserver
import json
import threading

# CONFIG_PATH = "./port-listener.json"
CONFIG_PATH = "/etc/port-listener.json"
IP = "0.0.0.0"
CONFIG = {}


def start_listener(listener_data):
    """
    Wrapper function to start tcp server.

    Args:
    listener_data (tuple): data for tcp serever to start
    """
    with socketserver.TCPServer(listener_data, MyTCPHandler) as server:
        server.timeout = 3
        server.serve_forever()


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Handler to serve a response to asking client
    """
    def handle(self):
        """
        Handling function. It reads proper response from config dict
        based on port which is added to object in default constructor
        """
        print("Incomiong connection on port {}".format(
            str(self.server.server_address[1])))
        self.request.sendall(
            bytes(" ".join(
                CONFIG[str(self.server.server_address[1])]), "utf-8"))


if __name__ == "__main__":
    with open(CONFIG_PATH, 'r') as infile:
        CONFIG = json.loads(infile.read())
    SERVICES = [(IP, int(i)) for i in CONFIG.keys()]
    THREADS = []
    for service in SERVICES:
        print("Binding to port {}".format(service[1]))
        t = threading.Thread(target=start_listener, args=[service])
        t.daemon = True
        t.start()
        THREADS.append(t)
    THREADS[0].join()
