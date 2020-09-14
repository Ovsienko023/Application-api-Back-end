import os
import json
from scripts.server.server_flask import app


def main():
    app.run(*conf_server(), debug=True)


def conf_server():
    """Returns tuple(host, server) from the file: config.json"""
    path = os.getcwd() + "/Application/config.json"
    with open(path) as config:
        json_str = config.read()
        json_str = json.loads(json_str)

    host = json_str['server']['host']
    port = json_str['server']['port']
    return host, port


if __name__ == "__main__":
    main()
