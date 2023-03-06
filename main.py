from models.klasy import generate_classes
from models.uczniowie import generate_students

ROWS_NUM = 20

LAB1 = [generate_students, generate_classes]


def generateTables(generators_list):
    for generator in generators_list:
        obj = generator(ROWS_NUM).__next__()

        table_name = type(obj).__name__
        generated_data = [f"{row}\n" for row in generator(ROWS_NUM)]

        with open(f"{table_name}.csv", 'w+') as f:
            f.write(f"{obj.headers}\n")
            f.writelines(generated_data)


if __name__ == "__main__":
    generateTables(LAB1)
