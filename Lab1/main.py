import sys
import math

class EquationSolver:
    def __init__(self):
        self.a = self.getCoef(1)
        self.b = self.getCoef(2)
        self.c = self.getCoef(3)
        self.roots = set()

    def getCoef(self, pos):
        try:
            coef = float(sys.argv[pos])
        except Exception:
            flag = True
            while flag:
                print(f'Введите коэффициент {chr(ord('A') + pos - 1)}: ', end='')
                try:
                    coef = float(input())
                except ValueError:
                    print('Неверный коэффициент! Попробуйте ещё раз.')
                    continue
                flag = False
        return coef

    def calculateRoots(self):
        if self.a == self.b == self.c == 0:
            return


        if self.a == 0:
            if self.b == 0:
                return

            if self.c * self.b > 0:
                return

            self.roots.add(math.sqrt(abs(self.c / self.b)))
            self.roots.add(-math.sqrt(abs(self.c / self.b)))
            return

        D = self.b * self.b - 4 * self.a * self.c
        if D >= 0:
            t1, t2 = (-self.b + math.sqrt(D)) / 2 / self.a, (-self.b - math.sqrt(D)) / 2 / self.a

            if t1 >= 0:
                self.roots.add(math.sqrt(t1))
                self.roots.add(-math.sqrt(t1))

            if t2 >= 0:
                self.roots.add(math.sqrt(t2))
                self.roots.add(-math.sqrt(t2))

    def printRoots(self):
        if len(self.roots) == 0:
            if self.a == self.b == self.c == 0:
                print('Бесконечное количество решений!')
                return

            print('Нет действительных корней!')
            return

        for i, x in enumerate(sorted(self.roots)):
            print(f'x{i} = {x}')




if __name__ == '__main__':
    eqsolver = EquationSolver()
    eqsolver.calculateRoots()
    eqsolver.printRoots()
