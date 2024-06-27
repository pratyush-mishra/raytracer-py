from vector import Vec3

class Ray:

    def __init__(self, origin: Vec3, direction: Vec3):
        self.orig = origin
        self.dir = direction

    def at(self, t: float):
        return self.orig + self.dir*t