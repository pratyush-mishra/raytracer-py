import math
class vec3(list):

    def __init__(self, e0, e1, e2):
        self.append(float(e0))
        self.append(float(e1))
        self.append(float(e2))

        #x,y,z coordinates
        self.x = e0
        self.y = e1
        self.z = e2

        #r,g,b coordinates
        self.r = e0
        self.g = e1
        self.b = e2

        self.length = math.sqrt(e0*e0 + e1*e1 + e2*e2)
        self.length_squared = e0*e0 + e1*e1 + e2*e2

    def x(self):
        return self[0]

    def y(self):
        return self[1]
    
    def z(self):
        return self[2]
    
    def __add__(self, vector):
        return vec3(self[0] + vector[0], self[1] + vector[1], self[2] + vector[2])

    def __sub__(self, vector):
        return vec3(self[0] - vector[0], self[1] - vector[1], self[2] - vector[2])

    def __mul__(self, scalar):
        return vec3(self[0] * scalar, self[1] * scalar, self[2] * scalar)
    
    def __truediv__(self, scalar):
        return vec3(self[0] / scalar, self[1] / scalar, self[2] / scalar)

    def multiply(self, vector):
        return vec3(self[0] * vector[0], self[1] * vector[1], self[2] * vector[2])
    

    def print_vector(self):
        return self

def unit_vector(vector: vec3) -> vec3:
    return vector / vector.length

def dot(u: vec3, v:vec3) -> float:
    return u[0] * v[0] + u[1] * u[1] + u[2] * v[2]

def cross(u: vec3, v:vec3) -> vec3:
    return vec3(u[1]*v[2] - u[2]*v[1], u[0]*v[2] - u[2]*v[0], u[0]*v[1] - u[1]*v[0])
