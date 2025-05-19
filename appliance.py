from abc import ABC, abstractmethod
class Calculatable(ABC):
    """
    Абстрактный базовый класс для объектов, которые могут быть рассчитаны.
    """
    @abstractmethod
    def calculate_energy_consumption(self):
        """Абстрактный метод для вычисления потребления энергии."""
        pass

    @abstractmethod
    def calculate_cost(self):
        """Абстрактный метод для вычисления стоимости."""
        pass

class Appliance(Calculatable):
    """
    Класс, представляющий бытовой прибор и его потребление энергии.
    """
    def __init__(self, power, hours, days, rate):
        self._power = power
        self._hours = hours
        self._days = days
        self._rate = rate
        self._energy_consumption = None  
        self._cost = None  

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        if value > 0:
            self._power = value
            self._energy_consumption = None 
            self._cost = None
        else:
            raise ValueError("Мощность должна быть больше нуля.")

    @property
    def energy_consumption(self):
        if self._energy_consumption is None:
            self._energy_consumption = self.calculate_energy_consumption()
        return self._energy_consumption

    @property
    def cost(self):
        if self._cost is None:
            self._cost = self.calculate_cost()
        return self._cost

    def calculate_energy_consumption(self):
        """Вычисляет потребление энергии прибора в кВт*ч."""
        return (self.power * self._hours * self._days) / 1000

    def calculate_cost(self):
        """Вычисляет стоимость потребленной энергии."""
        return self.energy_consumption * self._rate

    def __str__(self):
        return f"Прибор: Мощность={self.power} Вт, Потребление={self.energy_consumption:.2f} кВт*ч, Стоимость={self.cost:.2f} руб."

    def __repr__(self):
         return f"Appliance(power={self.power}, hours={self._hours}, days={self._days}, rate={self._rate})"