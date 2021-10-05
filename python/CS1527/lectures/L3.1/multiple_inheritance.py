# Author: Zsolt Kébel
# Date: 10/02/2021

class Car:
    __doc__ = 'Car Class'

    """Class attribute to hold list of Cars created."""
    all_cars = []

    def __init__(self, ma, mo, yr, **kwargs):
        super().__init__(**kwargs)
        self._make = ma
        self._model = mo
        self._year = yr
        """_odometer_reading should only be 
        accessed/modified via internal methods"""
        self.__odometer_reading = 0
        Car.all_cars.append(self)


class Boat:
    __doc__ = 'Simple Boat Class'

    """Represent boat characteristics."""

    def __init__(self, dis, blst, **kwargs):
        super().__init__(**kwargs)
        self._displacement = dis
        self._ballast = blst


class AmphibiousVehicle(Car, Boat):
    __doc__ = 'Amphibious Vehicle Class'

    """Represent amphibious vehicle – using multiple inh."""

    def __init__(self, fp, **kwargs):
        """Initialize attributes of the parent classes."""
        super().__init__(**kwargs)
        """Initialize attrs specific to an amphibious vehicle."""
        self._snorkel = False
        self._folding_prop = fp

    def convert(self):
        """Convert the vehicle for travel in water."""
        if self._folding_prop:
            print('Waiting for propeller ...')
        print('Preparing to sail ...')


car1 = Car(ma='Audi', mo='Q7', yr=2004)
boat1 = Boat(dis=200, blst=True)
amph1 = AmphibiousVehicle(ma='VW', mo='Schwimmwagen', yr=1944, fp=True, dis=900, blst=True)

print(AmphibiousVehicle.mro())  # Method Resolution Order (mro)
