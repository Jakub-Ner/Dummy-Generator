from faker import Faker

fake = Faker("pl_PL")

woman_names = [fake.first_name_female() for _ in range(100)]
man_names = [fake.first_name_male() for _ in range(100)]


def get_name(obj):
    if obj.Plec == "K":
        return fake.word(ext_word_list=woman_names)
    if obj.Plec == "M":
        return fake.word(ext_word_list=man_names)
    else:
        raise ValueError("Plec must be 'K' or 'M'")
