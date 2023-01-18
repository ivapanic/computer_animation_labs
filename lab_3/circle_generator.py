import random


class CircleGenerator:
    def __init__(self, quantity=100, velocity=0.8, max_x=1920, max_y=1080):
        self.quantity = quantity
        self.velocity = [velocity, velocity]
        self.max_x = max_x
        self.max_y = max_y
        self.circles = self.create_all_circles()

    def create_a_circle(self):
        x = random.randint(0, self.max_x)
        y = random.randint(0, self.max_y)

        velocity_x = random.uniform(-self.velocity[0], self.velocity[0])
        velocity_y = random.uniform(-self.velocity[1], self.velocity[1])

        return [x, y, velocity_x, velocity_y]

    def create_all_circles(self):
        circles = []
        for i in range(self.quantity):
            circles.append(self.create_a_circle())
        return circles

    def update(self):
        for circle in self.circles:
            circle[0] += circle[2]     # x += velocity_x
            circle[1] += circle[3]     # y += velocity_y

            if not 0 < circle[0] < self.max_x:
                circle[2] *= -1

            if not 0 < circle[1] < self.max_y:
                circle[3] *= -1

    def connect_circles(self):
        self.lines = []
        for p0 in range(self.quantity - 1):
            for p1 in range(p0 + 1, self.quantity):
                self.lines.append([self.circles[p0][:2], self.circles[p1][:2]])

        return self.lines
