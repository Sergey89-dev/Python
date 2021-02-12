class Data:
    def __init__(self, day_r):
        self.day_r = day_r

    @classmethod
    def take_d(cls, day_r):

        test_date = []

        for i in day_r.split():
            if i != '-' : 
                test_date.append(i)
        return int(test_date[0]), int(test_date[1]), int(test_date[2])

    @staticmethod
    def move(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Данные корректны'
                else: 
                    return f"Ошибка"

    def __str__(self):
        return f"Нынешняя дата {Data.take_d(self.day_r)}"

present_time = Data("12 - 2 - 2021")
print(present_time)
print(Data.move(16, 8, 2030))
print(present_time.move(24, 5, 2012))