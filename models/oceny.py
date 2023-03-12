from factory import Faker, Factory

from . import Stringify
from .uczniowie import STUDENTS_NUM
from .przedmioty import SUBJECTS_NUM

GRADES_NUM = 30


class Oceny(Stringify):
    def __init__(self, IdU, IdP, Ocena, DataO):
        self.IdU = IdU
        self.IdP = IdP
        self.Ocena = Ocena
        self.DataO = DataO.strftime("%d-%m-%Y")

    @property
    def headers(self):
        return "IdU;IdP;Ocena;DataO"


class GradesGenerator(Factory):
    class Meta:
        model = Oceny

    IdU = Faker("pyint", min_value=1, max_value=STUDENTS_NUM)
    IdP = Faker("pyint", min_value=1, max_value=SUBJECTS_NUM)
    Ocena = Faker("word", ext_word_list=["2", "3", "3.5", "4", "4.5", "5"])
    DataO = Faker("date_of_birth", maximum_age=3)


def generate_grades(rows_num=GRADES_NUM):
    for i in range(rows_num):
        yield GradesGenerator()


if __name__ == "__main__":
    print(GradesGenerator().headers)
    for row in generate_grades():
        print(row)
