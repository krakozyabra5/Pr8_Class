import os
import pickle
import tempfile

while True:
    N = input("Введите номер задания (1-7) или 'q' для выхода: ")
    if N.lower() == 'q':
        break
    if N == '1':
        class Soda:
            def __init__(self, supplement = None):
                self.supplement = supplement

            def show_my_drink(self):
                if self.supplement:
                    print(f"Газировка и {self.supplement}.")
                else:
                    print("Обычная газировка.")

        print("Задание №1")
        my_soda = Soda(input("Введите добавку: "))
        my_soda.show_my_drink() 

    elif N == '2':
        class TriangleChecker:
            def __init__(self, a, b, c):
                self.a = a
                self.b = b
                self.c = c

            def is_triangle(self):
                if self.a > 0 and self.b > 0 and self.c > 0:
                    if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
                        return "Ура, можно построить треугольник!"
                    else:
                        return "Жаль, но из этого треугольник не сделать."
                else:
                    return "С отрицательными числами ничего не выйдет!"

        print("\nЗадание №2")
        try:
            a = float(input("Длина 1-ой стороны треугольника: "))
            b = float(input("Длина 2-ой стороны треугольника: "))
            c = float(input("Длина 3-ей стороны треугольника: "))

            tc = TriangleChecker(a, b, c)
            result = tc.is_triangle()
            print(result)

        except:
            print("Нужно вводить только числа!")

    elif N == '3':
        class KgToPounds:
            def __init__(self, kg):
                self.__kg = kg

            @property
            def kg(self):
                return self.__kg

            @kg.setter
            def kg(self, new_kg):
                if isinstance(new_kg, (int, float)):
                    self.__kg = new_kg
                else:
                    raise ValueError("Килограммы задаются только числами.")

            def to_pounds(self):
                return self.__kg * 2.205
        
        print("\nЗадание №3")
        kg_input = float(input("Введите вес в килограммах: "))
        obj = KgToPounds(kg_input)
        print("Текущий вес в килограммах:", obj.kg)
        new_kg_input = float(input("Введите новый вес в килограммах: "))
        obj.kg = new_kg_input
        print("Новый вес в килограммах: ", obj.kg)
        print("Вес в фунтах: ", obj.to_pounds())

    elif N == '4':
        class Nikola:
            def __init__(self, name, age):
                self.__name = self.__process_name(name)
                self.__age = age

            def __process_name(self, name):
                if name != "Николай":
                    return "Я не " + name + ", а Николай."
                return name

            def __getattr__(self, name):
                raise AttributeError("Этот атрибут или метод не предусмотрен.")

            def __dir__(self):
                return ['_Nikola__name', '_Nikola__age']

            def get_name(self):
                return self.__name

            def get_age(self):
                return self.__age

        print("\nЗадание №4")
        name = input("Введите имя: ")
        age = int(input("Введите возраст: "))

        nikola = Nikola(name, age)

        print(nikola.get_name())
        print(nikola.get_age())

    elif N == '5':
        class RealString:
            def __init__(self, string):
                self.string = string

            def __len__(self):
                return len(self.string)

            def comparison(self, obj):
                if isinstance (obj, RealString):
                    local_string = obj.string
                else:
            	    local_string = obj

                if len(self) < len(obj):
                    print("Строка", self.string, "меньше, чем строка", local_string)
                elif len(self) > len(obj):
                    print("Строка", self.string, "больше, чем строка", local_string)
                else:
                    print("Строка", self.string, "равна в длине строке", local_string)
            
        print("\nЗадание №5")
        user_input = input("Введите текст: ")
        real_string = RealString(user_input)
        other_input = input("Введите новый текст: ")
        real_string.comparison(other_input)

    elif N == '6' or N == '7':
        class Transaction:
            def __init__(self, amount, date, currency = 'USD', description = None):
                self.__amount = amount
                self.__date = date
                self.__currency = currency
                self.__description = description

            @property
            def amount(self):
                return self.__amount

            @property
            def date(self):
                return self.__date

            @property
            def currency(self):
                return self.__currency

            @property
            def description(self):
                return self.__description

        class Account:
            def __init__(self, account_number, account_name):
                self.__account_number = account_number
                self.__account_name = account_name
                self.__transactions = []

            @property
            def account_number(self):
                return self.__account_number

            @property
            def account_name(self):
                return self.__account_name

            @account_name.setter
            def account_name(self, name):
                if len(name) >= 4:
                    self.__account_name = name
                else:
                    raise ValueError("Имя счёта должно состоять из четырёх символов и больше.")

            def __len__(self):
                return len(self.__transactions)

            def add_transaction(self, transaction):
                self.__transactions.append(transaction)

            @property
            def balance(self):
                usd_transactions = [t for t in self.__transactions if t.currency == "USD"]
                return sum(t.amount for t in usd_transactions)

            @property
            def all_usd(self):
                return all(t.currency == "USD" for t in self.__transactions)

            def save(self, filename):
                data = {
                    "account_number": self.__account_number,
                    "account_name": self.__account_name,
                    "transactions": self.__transactions,
                }
                file_name = filename

                file = open(filename, "w")
                while True:
                    line = input("> ")
                    if line == "":
                        break
                    file.write(line + "\n")

                print("The file is recorded.")
                file.close()

                with open(file_name, "wb") as file:
                    pickle.dump(data, file)

            def load(self, filename):
                file_name = filename
                if os.path.exists(file_name):
                    with open(file_name, "rb") as file:
                        data = pickle.load(file)
                        self.__account_number = data["account_number"]
                        self.__account_name = data["account_name"]
                        self.__transactions = data["transactions"]

            def get_save_file_name(self):
                return r"G:\Python\Class\{}.acc".format(self.__account_number)

        print("\nЗадания №6 и №7")

        account = Account(account_number = "123456", account_name = "My account")

        while True:
            choice = input("Добавить трансакцию? (y/n): ")
            if choice.lower() == "y":
                amount = float(input("Введите сумму трансакции: "))
                date = input("Введите дату трансакции (год-месяц-день): ")
                currency = input("Введите валюту трансакции: ")
                description = input("Введите описание трансакции (опционально): ")
                transaction = Transaction(amount, date, currency, description)
                account.add_transaction(transaction)
            else:
                break

        account.save(account.get_save_file_name)

        print(f"Номер аакаунта: {account.account_number}")
        print(f"Имя счёта: {account.account_name}")
        print(f"Число трансакций: {len(account)}")
        print(f"Баланс: ${account.balance}")
        print(f"Все трансакции выполнены в USD: {account.all_usd}")
    else:
        print("\nЗадания с таким номером нет.\n")
