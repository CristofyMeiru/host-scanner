class Scanner:
    def __init__(self, network_address: str):
        self.network_address = network_address

    def get_network_prefix(self) -> str:
        result: list[str] = self.network_address.split(".")[:3]
        if len(result) != 3:
            raise ValueError(
                f"Invalid network address: {self.network_address}\nExpected 3 valid octets."
            )

        return ".".join(result)

    def scan(self):
        address = self.get_network_prefix()
        for i in range(0, 255):
            self.check_host(f"{address}.{i}")

    def check_host(self, ip_address: str):
        print(ip_address)


if __name__ == "__main__":
    scanner = Scanner(network_address="192.168.1.0")
    scanner.scan()
