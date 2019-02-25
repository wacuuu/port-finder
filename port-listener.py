#!/usr/bin/python3

import socketserver
import json
import threading

CONFIG_PATH = "/etc/port-listener.json"
# CONFIG_PATH = "./port-listener.json"
IP = "0.0.0.0"
CONFIG = {}


def start_listener(listener_data):
    with socketserver.TCPServer(listener_data, MyTCPHandler) as server:
        server.timeout = 3
        server.serve_forever()


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("Incomiong connection on port {}".format(str(self.server.server_address[1])))
        self.request.sendall(bytes(" ".join(CONFIG[str(self.server.server_address[1])]), "utf-8"))


if __name__ == "__main__":
    with open(CONFIG_PATH, 'r') as infile:
        CONFIG = json.loads(infile.read())
    SERVICES = [(IP, int(i)) for i in CONFIG.keys()]
    threads = []
    for service in SERVICES:
        print("Binding to port {}".format(service[1]))
        t = threading.Thread(target=start_listener, args=[service])
        t.daemon = True
        t.start()
        threads.append(t)
    threads[0].join()
