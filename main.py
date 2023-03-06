from models.klasy import GeneratorKlas
from models.uczniowie import GeneratorUczniow

ROWS_NUM = 20

LAB1 = [GeneratorUczniow, GeneratorKlas]


def generateTables(generators_list):
    for generator in generators_list:
        table_name = type(generator()).__name__
        generated_data = [f"{generator()}\n" for _ in range(ROWS_NUM)]

        with open(f"{table_name}.csv", 'w+') as f:
            f.write(f"{generator().headers}\n")
            f.writelines(generated_data)


if __name__ == "__main__":
    generateTables(LAB1)
