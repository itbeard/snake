class Snake:
    def __init__(self):
        self.body = [(10, 10)]
        self.direction = 'UP'

    def move(self):
        # Copy the head
        new_head = list(self.body[0])

        if self.direction == 'UP':
            new_head[1] -= 1
        elif self.direction == 'DOWN':
            new_head[1] += 1
        elif self.direction == 'LEFT':
            new_head[0] -= 1
        elif self.direction == 'RIGHT':
            new_head[0] += 1

        self.body.insert(0, tuple(new_head))
        self.body.pop()

    def change_direction(self, new_direction):
        # Avoid moving in the opposite direction
        opposites = [('UP', 'DOWN'), ('DOWN', 'UP'), ('LEFT', 'RIGHT'), ('RIGHT', 'LEFT')]
        if (self.direction, new_direction) not in opposites:
            self.direction = new_direction

    def check_collision(self):
        return len(self.body) != len(set(self.body))

    def eat(self, food):
        if self.body[0] == food.position:
            return True
        return False

    def grow(self):
        self.body.append(self.body[-1])