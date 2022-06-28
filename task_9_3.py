class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income =  {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):

        return ' '.join([self.name, self.surname])

    def get_total_income(self):

        return sum(self._income.values())


z = Position('Manap', 'Shymyr', 'IT', 5000, 100)
name = z.get_full_name()
salary = z.get_total_income()
postion = z.position
print(name)

print(salary)
print(postion)