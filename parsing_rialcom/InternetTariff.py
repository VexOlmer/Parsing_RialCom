class InternetTariff:
    def __init__(self, name, channels, speed, price):
        self.name = name
        self.channels = channels
        self.speed = speed
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Channels: {self.channels}, Speed: {self.speed} Mbps, Price: {self.price} rubles per month"

    def __repr__(self):
        return f"InternetTariff('name={self.name}', channels={self.channels}, speed={self.speed}, price={self.price})"