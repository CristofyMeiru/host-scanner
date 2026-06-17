import platform
import subprocess
from subprocess import CompletedProcess

PING_PARAM: str = "-n" if platform.system().lower() == "windows" else "-c"


class Scanner:

    def __init__(self, network_address: str) -> None:
        self.network_address = network_address
        self.available_hosts = 0

    def get_network_prefix(self) -> str:
        result: list[str] = self.network_address.split(".")[:3]
        if len(result) != 3:
            raise ValueError(
                f"Invalid network address: {self.network_address}\nExpected 3 valid octets."
            )

        return ".".join(result)

    def scan(self) -> None:
        address = self.get_network_prefix()

        print(f"Scanning network {address}.0/24...")

        for i in range(1, 255):
            self.check_host(f"{address}.{i}")

        print(f"{self.available_hosts} available hosts in local network.")
        return

    def check_host(self, ip_address: str):
        result: CompletedProcess[str] = subprocess.run(
            ["ping", PING_PARAM, "1", ip_address], capture_output=True, text=True
        )
        first = result.stdout.split("\n")[:2]
        if result.returncode == 0:
            self.available_hosts += 1
            print(f"{first}\n")


if __name__ == "__main__":
    scanner = Scanner(network_address="192.168.1.0")
    scanner.scan()
