"""
    This module contains a class describing the standard Internet tariff.
"""

class InternetTariff:
    def __init__(self, name: str, channels, speed: int, price: int):
        """
            :param name: Tariff name.
            :param channels: Number of channels.
            :param speed: Internet speed in Mbps.
            :param price: Tariff cost in rubles per month.
        """

        self._name = name
        self._channels = self._validate_channels(channels)
        self._speed = self._validate_speed(speed)
        self._price = self._validate_price(price)

    @staticmethod
    def _validate_channels(channels):
        if channels not in ['null'] and (not isinstance(channels, int) or channels < 0):
            raise ValueError("The number of channels must be a non-negative number.")
        return channels

    @staticmethod
    def _validate_speed(speed):
        if not isinstance(speed, (int, float)) or speed <= 0:
            raise ValueError("Internet speed must be a positive number")
        return speed

    @staticmethod
    def _validate_price(price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("The tariff price must be a non-negative number.")
        return price

    def get_list_view(self):
        return [self._name, self._channels, self._speed, self._price]

    def __str__(self):
        return f"Name: {self._name}, Channels: {self._channels}, Speed: {self._speed} Mbps, Price: {self._price} rubles per month"

    def __repr__(self):
        return f"InternetTariff('name={self._name}', channels={self._channels}, speed={self._speed}, price={self._price})"

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def channels(self):
        return self._channels
    @channels.setter
    def channels(self, value):
        self._channels = self._validate_channels(value)

    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, value):
        self._speed = self._validate_speed(value)

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = self._validate_price(value)