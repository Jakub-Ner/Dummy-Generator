from factory import Faker, Factory

from . import Stringify


class Oceny(Stringify):
    def __init__(self, IdO, Ocena, DataO):
        self.IdO = IdO
        self.Ocena = Ocena
        self.DataO = DataO

    @property
    def headers(self):
        return "IdO;Ocena;DataO"


class GradesGenerator(Factory):
    class Meta:
        model = Oceny

    IdO = 0
    Ocena = Faker("word", ext_word_list=["2", "3", "3.5", "4", "4.5", "5"])
    DataO = Faker("date_of_birth", maximum_age=3)


def generate_grades(rows_num=30):
    for i in range(rows_num):
        yield GradesGenerator(IdO=i + 1)


if __name__ == "__main__":
    print(GradesGenerator().headers)
    for row in generate_grades():
        print(row)
