import factory
from factory import Faker, Factory

from . import Stringify


class Miasta(Stringify):
    def __init__(self, IdM, NazwaM):
        self.IdM = IdM
        self.NazwaM = NazwaM

    @property
    def headers(self):
        return "IdM;NazwaM"


@factory.Faker.override_default_locale('pl_PL')
class CitiesFactory(Factory):
    class Meta:
        model = Miasta

    IdM = 0
    NazwaM = Faker('city')


def generate_cities(rows_num=12):
    for i in range(rows_num):
        yield CitiesFactory(IdM=i + 1)


if __name__ == "__main__":
    print(CitiesFactory().headers)
    for row in generate_cities(10):
        print(row)
