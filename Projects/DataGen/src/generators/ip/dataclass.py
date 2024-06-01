class Ip:
    """
    Class for ip address
    """

    def __init__(self, ip):
        self.ip = ip
        self.type = "ipv4" if "." in ip else "ipv6"

    def valid(self):
        """
        Check if ip is valid
        """
        try:
            if self.type == "ipv4":
                return all(0 <= int(i) <= 255 for i in self.ip.split("."))
            else:
                return all(0 <= int(i, 16) <= 65535 for i in self.ip.split(":"))
        except ValueError:
            return False

    def __str__(self):
        return self.ip

    def __repr__(self):
        return f"Ip({self.ip})"