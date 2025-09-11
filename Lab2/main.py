import requests

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

N = 21

def main():
    r = Rectangle(N, N, "синего")
    c = Circle(N, "зеленого")
    s = Square(N, "красного")
    print(r)
    print(c)
    print(s)

    r = requests.get('https://bmstu.ru/')
    print(r.status_code)

if __name__ == "__main__":
    main()
