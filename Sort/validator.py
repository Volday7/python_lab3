import re
import json
from tqdm import tqdm
import argparse
import autopep8


class Validator:
    email: str
    weight: str
    snils: str
    passport_series: str
    occupation: str
    work_experience: str
    political_views: str
    worldview: str
    address: str

    def __init__(self, d: dict):
        self.email = d['email']
        self.weight = d['weight']
        self.snils = d['snils']
        self.passport_series = d['passport_series']
        self.occupation = d['occupation']
        self.work_experience = d['work_experience']
        self.political_views = d['political_views']
        self.worldview = d['worldview']
        self.address = d['address']

    def check(self):
        pattern = "^[^\\s@]+@([^\\s@.,]+\\.)+[^\\s@.,]{2,}$"
        if re.match(pattern, str(self.email)) is None:
            return 'email'
        pattern = "^\\d{1,3}"
        if re.match(pattern, str(self.weight)) is None:
            #if int(self.weight) < 40 and int(self.weight) > 150:
            return 'weight'
        if int(self.weight) < 40 or int(self.weight) > 150:
            return 'weight'
        pattern = "\\d{11}"
        if re.match(pattern, str(self.snils)) is None:
            return 'snils'
        pattern = "\\d\\d\\s\\d\\d"
        if re.match(pattern, str(self.passport_series)) is None:
            return 'passport_series'
        pattern = "[А-яа-я ]{1,}"
        if re.match(pattern, str(self.occupation)) is None:
            return 'occupation'
        pattern = "(^\\d{1,2})"
        if re.match(pattern, str(self.work_experience)) is None:
            return 'work_experience'
        pattern = ['(Либеральные)', '(Умеренные)', '(Индифферентные)', '(Коммунистические)', '(Социалистические)',
                   '(Анархистские)', '(Консервативные)', '(Либертарианские)', '(Анархистские)']
        count = 0
        for i in pattern:
            if re.match(i, str(self.political_views)) is None:
                count += 1
        if count == 9:
            return 'political_views'
        count = 0
        pattern = ['(Деизм)', '(Католицизм)', '(Пантеизм)', '(Буддизм)', '(Секулярный гуманизм)', '(Конфуцианство)',
                   '(Иудаизм)', '(Атеизм)', '(Агностицизм)']
        for i in pattern:
            if re.match(i, str(self.worldview)) is None:
                count += 1
        if count == 9:
            return 'worldview'
        pattern = "[А-Яа-я \\-.0-9]{1,}\\ [а-яА-Я0-9]{1,}"
        if re.match(pattern, str(self.address)) is None:
            return 'address'
        return 'True'

'''
class File(object):
    data: str

    def __init__(self, f: str):
        self.data = json.load(open(f, encoding='windows-1251'))

    def data(self):
        return self.data


parser = argparse.ArgumentParser(description='Lab 2 python')
parser.add_argument('-input', type=str,
                    help='Input file for reading', dest="f_in")
parser.add_argument('-output', type=str,
                    help='Output file for writing correct data', dest="f_out")
args = parser.parse_args()
input_file = File(args.f_in)
output_file = open(args.f_out, 'w')
dict_error = {"email": 0, "weight": 0, "snils": 0, "passport_series": 0, "occupation": 0,
              "work_experience": 0, "political_views": 0, "worldview": 0, "address": 0, "True": 0}
counter = 0
for i in input_file.data:
    counter += 1
counter_false = 0
for i in tqdm(input_file.data):
    f = Validator(i)
    dict_error[f.check()] += 1
    if f.check() == "True":
        output_file.write("email: " + i["email"] + "\n")
        output_file.write("weight: " + str(i["weight"]) + "\n")
        output_file.write("snils: " + str(i["snils"]) + "\n")
        output_file.write("passport_series: " +
                          str(i["passport_series"]) + "\n")
        output_file.write("occupation: " + i["occupation"] + "\n")
        output_file.write("work_experience: " +
                          str(i["work_experience"]) + "\n")
        output_file.write("political_views: " + i["political_views"] + "\n")
        output_file.write("worldview: " + i["worldview"] + "\n")
        output_file.write("address: " + i["address"] + "\n")
        output_file.write("\n\n")
    else:
        counter_false += 1

print("Всего пользователей: " + str(counter) + "\n")
print("Кол-во ошибок: " + str(counter_false) + "\n")
print("Кол-во корректных записей: " + str(counter - counter_false) + "\n")
for i in dict_error:
    print(i + ": " + str(dict_error[i]))
output_file.close()
'''