import factory
from factory import Factory

from . import Stringify

SUBJECTS = ["matematyka", "fizyka", "chemia", "biologia", "geografia", "historia", "język polski", "język angielski",
            "język niemiecki", "religia"]


class Przedmioty(Stringify):
    def __init__(self, NazwaP):
        # self.IdP = IdP
        self.NazwaP = NazwaP

    @property
    def headers(self):
        return "NazwaP"


@factory.Faker.override_default_locale('pl_PL')
class SubjectsFactory(Factory):
    class Meta:
        model = Przedmioty

    # IdP = 0
    NazwaP = ""


def generate_subjects(rows_num=10):
    for i in range(rows_num):
        yield SubjectsFactory(NazwaP=SUBJECTS[i])


if __name__ == "__main__":
    print(SubjectsFactory().headers)
    for row in generate_subjects(10):
        print(row)
