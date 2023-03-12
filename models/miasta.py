import factory
from factory import Faker, Factory

from . import Stringify

CITIES_NUM = 12


class Miasta(Stringify):
    def __init__(self, NazwaM):
        # self.IdM = IdM
        self.NazwaM = NazwaM

    @property
    def headers(self):
        return "NazwaM"


@factory.Faker.override_default_locale('pl_PL')
class CitiesFactory(Factory):
    class Meta:
        model = Miasta

    # IdM = 0
    NazwaM = Faker('city')


def generate_cities(rows_num=CITIES_NUM):
    for i in range(rows_num):
        yield CitiesFactory()


if __name__ == "__main__":
    print(CitiesFactory().headers)
    for row in generate_cities(10):
        print(row)
