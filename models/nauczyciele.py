from datetime import timedelta

import factory
from factory import Faker, Factory

from . import Stringify
from .utils.names import get_name

TEACHERS_NUM = 20


class Nauczyciele(Stringify):
    def __init__(self, Nazwisko, Imie, DZatr, DUr, Plec, Pensja, Pensum, Telefon, working_offset):
        # self.IdN = IdN
        self.Nazwisko = Nazwisko
        self.Imie = Imie
        self.DZatr = DZatr.strftime("%d-%m-%Y")
        self.DUr = DUr.strftime("%d-%m-%Y")
        self.Plec = Plec
        self.Pensja = Pensja
        self.Pensum = Pensum
        self.Telefon = Telefon

        self.working_offset = working_offset

    @property
    def headers(self):
        return "Nazwisko;Imie;DZatr;DUr;Plec;Pensja;Pensum;Telefon"


@factory.Faker.override_default_locale('pl_PL')
class TeachersFactory(Factory):
    class Meta:
        model = Nauczyciele

    working_offset = Faker('random_int', min=25, max=27)

    # IdN = 0
    Nazwisko = Faker('last_name')
    Imie = factory.lazy_attribute(get_name)
    DZatr = factory.lazy_attribute(lambda o: o.DUr + timedelta(days=380 * o.working_offset))  # 380 for uneven dates
    DUr = Faker('date_of_birth', minimum_age=27, maximum_age=60)
    Plec = Faker('random_element', elements=('M', 'K'))
    Pensja = Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    Pensum = Faker("pyint", min_value=10, max_value=40)
    Telefon = Faker('phone_number')


def generate_teachers(rows_num=TEACHERS_NUM):
    for i in range(rows_num):
        yield TeachersFactory()


if __name__ == "__main__":
    print(TeachersFactory().headers)
    for row in generate_teachers(10):
        print(row)
