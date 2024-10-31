#First Part of my task
my_dict = {"Год рождения" : 2003,
    "Месяц рождения" : 9,
    "День рождения" : 24}
print(my_dict)
print(my_dict.get("Год рождения"))
my_dict.update({"Город" : "Одесса"})
print(my_dict.get("Город"))
my_dict.update( {"Имя" : "Дима",
            "Отчество" : "Сергеевич"})
Sicret = my_dict.pop("Отчество")
print(Sicret)
print(my_dict)
#Second part
my_set = { 1,2,3,4,4,3,2,1, "Плотва"}
print(my_set)
my_set.update({5,6,7,7,6,5})
my_set.remove(1)
print(my_set)











    