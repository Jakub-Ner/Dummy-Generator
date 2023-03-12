from factory import Faker, Factory

from . import Stringify
from .nauczyciele import TEACHERS_NUM
from .przedmioty import SUBJECTS_NUM

TEACHES_NUM = 30


class Uczy(Stringify):
    def __init__(self, IdN, IdP, IleGodz):
        # self.IdO = IdO
        self.IdN = IdN
        self.IdP = IdP
        self.IleGodz = IleGodz

    @property
    def headers(self):
        return "IdN;IdP;IleGodz"


class TeachesGenerator(Factory):
    class Meta:
        model = Uczy

    IdN = Faker('pyint', min_value=1, max_value=TEACHERS_NUM)
    IdP = Faker('pyint', min_value=1, max_value=SUBJECTS_NUM)
    IleGodz = Faker('pyint', min_value=1, max_value=30)


def generate_teaches(rows_num=TEACHES_NUM):
    for i in range(rows_num):
        yield TeachesGenerator()


if __name__ == "__main__":
    print(TeachesGenerator().headers)
    for row in generate_teaches():
        print(row)
