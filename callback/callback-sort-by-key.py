data = ["apple", "banana", "pear"]
print(data)
data.sort(key=len, reverse = True)
print(data)
data.sort(key=len, reverse = False)
print(data)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    # 将排序规则写死在类中，可以直接调用sort()方法
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

points = [
    Point(2, 3),
    Point(1, 5),
    Point(2, 1),
    Point(1, 2),
    Point(3, 0),
    Point(3, 4),
    Point(3, 3)
]

print("original:")
print(points)

print("points.sort():")
points.sort()
print(points)

points.sort(key=lambda p: (p.x, p.y))
print("\nsort by x asc, y asc:")
print(points)

points.sort(key=lambda p: (p.y, p.x))
print("\nsort by y asc, x asc:")
print(points)

points.sort(key=lambda p: (p.x, p.y), reverse=True)
print("\nsort by x desc, y desc:")
print(points)