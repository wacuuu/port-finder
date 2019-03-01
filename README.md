# port-finder
[![Build Status](https://travis-ci.com/wacuuu/port-finder.svg?branch=master)](https://travis-ci.com/wacuuu/port-finder)
Small utility for service discovery in small networks.
## How it works

You configure service with json.

```json
{
    "<port>": [
        "tag1",
        "tag2"
    ],
    "<port>": [
        "tag1",
        "tag3"
    ]
}
```
Then after restarting the service, for each port a TCPServer is created. When contacted, it
responds with set of tags.

On the other hand you have my_port_finder utility. It is a script that coops with mentioned service.
If you don't specify to analise only localhost, it will make a map of all possible addresses on all
interfaces(hardcoded exclude for lo and docker0), and it will try to contact all IPs on specified port.
Moreover you can specify a tag that will be processed. If remote responds with tag, it's IP will be printed.

## Instalation
Simply run INSTALL(you may need sudo). Service will get started and enabled. Configuration in /etc/port-listener.json

## Sandboxing
To run this without instalation, simply start port-listener.py with --config with path to config file.