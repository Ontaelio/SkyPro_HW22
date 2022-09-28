# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

class Unit:
    unit_movement = {
        'flyer': 1.2,
        'crawler': 0.5
    }

    move_directions = {
        'UP': {'x': 0, 'y': -1},
        'DOWN': {'x': 0, 'y': 1},
        'LEFT': {'x': -1, 'y': 0},
        'RIGHT': {'x': 1, 'y': 0},
    }

    def __init__(self, movement, x, y):
        if movement not in self.unit_movement:
            raise ValueError
        self.movement_type = movement
        self.pos_x = x
        self.pos_y = y

    def __str__(self):
        return f"{self.movement_type} at {self.pos_x}, {self.pos_y}."

    def move(self, direction):
        if direction not in self.move_directions:
            raise ValueError
        self.pos_x += self.move_directions[direction]['x'] * self.unit_movement[self.movement_type]
        self.pos_y += self.move_directions[direction]['y'] * self.unit_movement[self.movement_type]


class BadUnit:
    def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed=1):

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed

            field.set_unit(x=new_x, y=new_y, unit=self)


baba = Unit('flyer', 1, 1)
dada = Unit('crawler', 2, 2)

print(baba)
print(dada)

baba.move('UP')
dada.move('UP')

print(baba)
print(dada)