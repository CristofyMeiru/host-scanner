class Scanner:
    def __init__(self, network_address: str):
        self.network_address = network_address

    def extract_network_address(self) -> str:
        result = self.network_address.split(".")
        if len(result) > 4:
            raise ValueError(f"Invalid network address: {self.network_address}")

        return result

    