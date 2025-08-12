# Using the Faker module, create a list containing 4 dictionaries with personal information about individuals.

from faker import Faker

fake = Faker()
info_list = []
for i in range(4):
    info_dic = {}
    info_dic["User_name"] = fake.user_name()
    info_dic["E-mail"] = f"{info_dic["User_name"]}@gmail.com"
    info_dic["Birthday"] = fake.date()
    info_dic["Address"] = fake.address()
    info_list.append(info_dic)
print(info_list)
