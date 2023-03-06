import factory
from factory import Faker, Factory, SubFactory


class Uczniowie:
    def __init__(self, Nazwisko, Imie, DUr):
        # self.IdU = IdU
        self.Nazwisko = Nazwisko
        self.Imie = Imie
        self.DUr = DUr

        # self.KlasaU = KlasaU
        # self.Miasto = Miasto

    @property
    def headers(self):
        return "IdU;Nazwisko;Imie;DUr" # ;KlasaU;Miasto

    def __str__(self):
        return f"{self.Nazwisko};{self.Imie};{self.DUr}" # {self.IdU}; ;{self.KlasaU};{self.Miasto}


@factory.Faker.override_default_locale('pl_PL')
class GeneratorUczniow(Factory):
    class Meta:
        model = Uczniowie

    # IdU = 0
    Nazwisko = Faker('last_name')
    Imie = Faker('first_name')
    DUr = Faker('date_of_birth', minimum_age=5, maximum_age=65)

    # KlasaU = SubFactory(GeneratorKlas)
    # Miasto = Faker('city')


if __name__ == "__main__":
    print(GeneratorUczniow().headers)
    print(GeneratorUczniow())
