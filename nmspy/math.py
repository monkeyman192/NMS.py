from typing import Union

class Vector3f:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Vector3f"):
        return Vector3f(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3f"):
        return Vector3f(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: Union[float, int]):
        if isinstance(other, Vector3f):
            raise NotImplementedError("To multiply two vectors, use a @ b to compute the dot product")
        return Vector3f(other * self.x, other * self.y, other * self.z)

    def __rmul__(self, other: Union[float, int]):
        return self * other

    def __matmul__(self, other: "Vector3f") -> float:
        """ Dot product """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __neg__(self):
        return Vector3f(-self.x, -self.y, -self.z)

    def __repr__(self):
        return f"Vector3f({self.x}, {self.y}, {self.z})"


if __name__ == "__main__":
    v = Vector3f(1,2,3)
    k = 3 * v
    print(v)
    print(k)
    print(v * 6)
    print(v @ k)
