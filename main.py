from models.klasy import generate_classes
from models.uczniowie import generate_students
from models.nauczyciele import generate_nauczyciele

LAB1 = [generate_students, generate_classes, generate_nauczyciele]


def generateTables(generators_list):
    for generator in generators_list:
        obj = generator().__next__()

        table_name = type(obj).__name__
        generated_data = [f"{row}\n" for row in generator()]

        with open(f"{table_name}.csv", 'w+', encoding="utf-8") as f:
            f.write(f"{obj.headers}\n")
            f.writelines(generated_data)


if __name__ == "__main__":
    generateTables(LAB1)
