from factory import Faker, Factory

from . import Stringify


class Oceny(Stringify):
    def __init__(self, Ocena, DataO):
        # self.IdO = IdO
        self.Ocena = Ocena
        self.DataO = DataO.strftime("%d-%m-%Y")

    @property
    def headers(self):
        return "Ocena;DataO"


class GradesGenerator(Factory):
    class Meta:
        model = Oceny

    # IdO = 0
    Ocena = Faker("word", ext_word_list=["2", "3", "3.5", "4", "4.5", "5"])
    DataO = Faker("date_of_birth", maximum_age=3)


def generate_grades(rows_num=30):
    for i in range(rows_num):
        yield GradesGenerator()


if __name__ == "__main__":
    print(GradesGenerator().headers)
    for row in generate_grades():
        print(row)
