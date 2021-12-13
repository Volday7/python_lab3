from Sort import validator
from Sort import Lab_3
import pickle
from tqdm import tqdm
import argparse
import json
import logging


class File(object):
    data: str

    def __init__(self, f: str):
        with open(f, "r") as file:
            self.data = json.load(file)

    def data(self):
        return self.data


def choice() -> str:
    print("Сортировка по:\n"
          "1 - Весу\n"
          "2 - СНИЛСу\n"
          "3 - Серии паспорта\n"
          "4 - Опыту работы\n")
    ch = int(input())
    while ch != 1 or ch != 2 or ch != 3 or ch != 4:
        if ch == 1:
            return "weight"
        elif ch == 2:
            return "snils"
        elif ch == 3:
            return "passport_series"
        elif ch == 4:
            return "work_experience"
        else:
            print("Сортировка по:\n"
                  "1 - Весу\n"
                  "2 - СНИЛСу\n"
                  "3 - Серии паспорта\n"
                  "4 - Опыту работы\n")
            ch = input()


parser = argparse.ArgumentParser(description='Lab 3 python')
parser.add_argument('-input', type=str,
                    help='Input file for reading', dest="f_in")
parser.add_argument('-output', type=str,
                    help='Output file for writing correct data', dest="f_out")
args = parser.parse_args()
input_file = File(args.f_in)
#output_file = open(args.f_out, 'w')
dict_error = {"email": 0, "weight": 0, "snils": 0, "passport_series": 0, "occupation": 0,
              "work_experience": 0, "political_views": 0, "worldview": 0, "address": 0, "True": 0}
counter = 0
for i in input_file.data:
    counter += 1
counter_false = 0
result = []
for i in tqdm(input_file.data):
    f = validator.Validator(i)
    dict_error[f.check()] += 1
    if f.check() == "True":
        result.append(i)
        '''output_file.write("email: " + i["email"] + "\n")
        output_file.write("weight: " + str(i["weight"]) + "\n")
        output_file.write("snils: " + str(i["snils"]) + "\n")
        output_file.write("passport_series: " +
                          str(i["passport_series"]) + "\n")
        output_file.write("occupation: " + i["occupation"] + "\n")
        output_file.write("work_experience: " +
                          str(i["work_experience"]) + "\n")
        output_file.write("political_views: " + i["political_views"] + "\n")
        output_file.write("worldview: " + i["worldview"] + "\n")
        output_file.write("address: " + i["address"] + "\n")'''

    else:
        counter_false += 1
with open(args.f_out, "w") as output_file:
    json.dump(result, output_file, ensure_ascii=False, indent=1)

print("Всего пользователей: " + str(counter) + "\n")
print("Кол-во ошибок: " + str(counter_false) + "\n")
print("Кол-во корректных записей: " + str(counter - counter_false) + "\n")
for i in dict_error:
    print(i + ": " + str(dict_error[i]))
#output_file.close()
#data_to_sort = File(args.f_out)
#with open("D:\\for_lab_3.txt", "r") as f:
    #data_to_sort = json.load(f)
with open("D:\\for_lab_3_1.txt", "r") as f:
    data_to_sort = json.load(f)
#sorted_data = [int(i) for i in data_to_sort]
Lab_3.heapsort(data_to_sort)
with open("D:\\sorted_lab_3.txt", "wb") as f:
    pickle.dump(data_to_sort, f)
print("\nГотово!\n")
with open("D:\\sorted_lab_3.txt", "rb") as f:
    res = pickle.load(f)
#print(logging.info(f"Serialization is correct:{data_to_sort == res}"))
#print(res)
for i in range(1, 5):
    print(res[i])

