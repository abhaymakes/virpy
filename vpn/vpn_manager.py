import os
import subprocess
import random
import json
import time
from rich.console import Console

console = Console()

class VPNServersNotFoundError(Exception):
    pass

class VPNNotFoundError(Exception):
    pass

class NoMoreAvailableServersError(Exception):
    pass


class VPNManager:
    def __init__(self, logger):
        self.logger = logger

        self.servers = self.get_available_servers()
        self.vpn_cli_path = self.get_vpn_path

    def get_available_servers(self):
        server_file_path = f"vpn/vpn-servers.json"
        try:
            with open(server_file_path, "r") as vpn_servers_file:
                servers = json.load(vpn_servers_file)
        except FileNotFoundError:
            console.print(
                "[bold red] failed: Couldn't find available VPN servers, check if the vpn-servers.json file exists."
            )
            raise VPNServersNotFoundError

        return servers

    def get_vpn_path(self):
        vpn_exists = os.path.isfile(self.vpn_path)
        if vpn_exists:
            return "c:/Program Files/Windscribe/windscribe-cli.exe"
        else:
            raise VPNNotFoundError

    def connect(self, server_nickname):
        disconnect_command = f'"c:/Program Files/Windscribe/windscribe-cli.exe" disconnect'
        connect_command = f'"c:/Program Files/Windscribe/windscribe-cli.exe" connect "{server_nickname}"'
        try:
            subprocess.run(disconnect_command, shell=True, text=True, capture_output=True)
            time.sleep(2)
            subprocess.run(connect_command, shell=True, text=True, capture_output=True)
        except Exception as e:
            print(e)

    def is_connected(self):
        command = f'"c:/Program Files/Windscribe/windscribe-cli.exe" status'
        connection_output = subprocess.run(command, shell=True, text=True, capture_output=True)

        return "Connect state: Connected" in connection_output.stdout

    def connect_random_server(self):
        if not self.servers:
            raise NoMoreAvailableServersError
        
        random_server = random.randrange(0, len(self.servers))
        server_details = self.servers.pop(random_server)
        nickname = server_details['nickname']
        console.print(f"[bold green]Connecting to {server_details['city']}({nickname})...")
        self.connect(nickname)
        time.sleep(8)
        if self.is_connected():
            console.print(f"[bold green]Successfully connected to VPN")


