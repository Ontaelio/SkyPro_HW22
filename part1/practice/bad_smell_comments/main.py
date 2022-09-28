
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

    def _move(self, direction):
        if direction not in self.move_directions:
            raise ValueError
        self.pos_x += self.move_directions[direction]['x'] * self.unit_movement[self.movement_type]
        self.pos_y += self.move_directions[direction]['y'] * self.unit_movement[self.movement_type]

    def move(self, field, coord_x, coord_y, direction, flyer, crawler, speed):
        if flyer and crawler:
            raise ValueError('Рожденный ползать летать не должен!')
        self.pos_x = coord_x
        self.pos_y = coord_y
        self._move(direction)
        field.set_unit(x=self.pos_x, y=self.pos_y, unit=self)


