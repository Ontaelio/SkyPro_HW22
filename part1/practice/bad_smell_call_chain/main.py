# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
    def __init__(self, room, pop):
        self.room = room
        self.city_population = pop

    def get_person_room(self):
        return self.room

    def get_city_population(self):
        return self.city_population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

a = Person(42, 100000)
print(a.get_person_room())
print(a.get_city_population())