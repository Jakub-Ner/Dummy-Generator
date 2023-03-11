from models.klasy import generate_classes
from models.miasta import generate_cities
from models.nauczyciele import generate_teachers
from models.uczniowie import generate_students
from models.przedmioty import generate_subjects
from models.oceny import generate_grades

LAB1 = [generate_students, generate_classes, generate_teachers, generate_cities, generate_subjects, generate_grades]


def generateTables(generators_list):
    for generator in generators_list:
        obj = generator().__next__()

        table_name = type(obj).__name__
        generated_data = [f"{row}\n" for row in generator()]

        with open(f"./lab1_generated_tables/{table_name}.csv", 'w+', encoding="utf-8") as f:
            f.write(f"{obj.headers}\n")
            f.writelines(generated_data)


if __name__ == "__main__":
    generateTables(LAB1)
