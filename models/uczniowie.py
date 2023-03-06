import factory
from factory import Faker, Factory, SubFactory


class Uczniowie:
    def __init__(self, Nazwisko, Imie, DUr):
        self.Nazwisko = Nazwisko
        self.Imie = Imie
        self.DUr = DUr

        # self.KlasaU = KlasaU
        # self.Miasto = Miasto

    @property
    def headers(self):
        return "Nazwisko;Imie;DUr" # ;KlasaU;Miasto

    def __str__(self):
        return f"{self.Nazwisko};{self.Imie};{self.DUr}" # {self.IdU}; ;{self.KlasaU};{self.Miasto}


@factory.Faker.override_default_locale('pl_PL')
class GeneratorUczniow(Factory):
    class Meta:
        model = Uczniowie

    Nazwisko = Faker('last_name')
    Imie = Faker('first_name')
    DUr = Faker('date_of_birth', minimum_age=5, maximum_age=65)

    # KlasaU = SubFactory(GeneratorKlas)
    # Miasto = Faker('city')

def generate_students(rows_num):
    for _ in range(rows_num):
        yield GeneratorUczniow()

if __name__ == "__main__":
    print(GeneratorUczniow().headers)
    for row in generate_students(10):
        print(row)
