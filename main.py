import statistics as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from matplotlib import cm
import pandas as pd

print('Добро пожаловать в решатель математических задач. 📓 \n'
      )
print('Условные обозначения типов задач: \n'
      '\tуравнения - ur \n'
      '\tупрощение выражений - uv \n'
      '\tпроизводная - pr \n'
      '\tфакторизация - dk \n'
      '\tраскрытие скобок - rs \n'
      '\tкомбинирование логарифмических выражений - kl \n'
      '\tупрощение тригонометрических выражений - ut \n'
      '\tфункции - fu \n'
      '\tгеометрия - gm \n'
      '\tстатистика и комбинаторика - st \n'
      '\tпрогрессии - prg \n')


def equations():
    a = input('Введи 1-е уравнение: ')
    b = input('Введи 2-е уравнение \n'
              '(если его нет - нажать Enter.): ')
    c = input('Введи 3-е уравнение \n'
              '(если его нет - нажать Enter.): ')
    print('Введи переменные относительно которых решается уравнение. Если её нет - нажать Enter.')
    p1 = input('Переменная №1 = ')
    p2 = input('Переменная №2 = ')
    p3 = input('Переменная №3 = ')
    if p3 != '' and p2 != '':
        d1 = sym.symbols(p1)
        d2 = sym.symbols(p2)
        d3 = sym.symbols(p3)
    elif p3 == '' and p2 != '':
        d1 = sym.symbols(p1)
        d2 = sym.symbols(p2)
    elif p3 == '' and p2 == '':
        d1 = sym.symbols(p1)
    if c == '' and b == '':
        ur = sym.solveset(a, d1)
        print(d1, '=', *ur)
    elif a != '' and c == '':
        ur = sym.solve((a, b), (d1, d2))
        print(d1, '=', ur[d1], d2, '=', ur[d2])
    elif a != '' and b != '' and c != '':
        ur = sym.solve((a, b, c), (d1, d2, d3))
        print(d1, '=', ur[d1], d2, '=', ur[d2], d3, '=', ur[d3])


def factorization():
    a = input('Введи уравнение для факторизации: ')
    print(sym.factor(a))


def derivative():
    x = sym.symbols(input())
    y = eval(input('Введи функцию: '))
    a = y.diff(x)
    print('f’=', a)


def combining_logarithmic_expressions():
    a = input('Введи логарифмическое выражение: \n')
    print(sym.logcombine(a))


def simplification_of_trigonometric_expressions():
    a = input('Введи тригонометрическое выражение: ')
    print(sym.trigsimp(a))


def expression_simplification():
    a = input('Введи выражение для упрощёния: \n')
    print(sym.simplify(a))

try:
    type = input('Введи тип задачи: \n')
    if type == 'ur':
        equations()
    elif type == 'dk':
        factorization()
    elif type.lower() == 'pr':
        derivative()
    elif type == 'kl':
        combining_logarithmic_expressions()
    elif type == 'ut':
        simplification_of_trigonometric_expressions()
    elif type == 'uv':
        expression_simplification()
    elif type == 'rs':
        a = input('Введи выражение в котором надо раскрыть скобки: \n')
        print(sym.expand(a))
    elif type == 'st':
        ts = input('Введи раздел \n'
                   '  - cтатистика - st \n'
                   '  - вероятности - vs \n'
                   '  - комбинаторика - kb \n'
                   '  - диаграммы и графики - dg \n'
                   '  - отношение 2-х введённых данных - of \n')
        if ts == 'st':
            sp = input('Введи набор чисел через пробел. Будут выведены все данные из этого раздела: \n').split(' ')
            sp = list(map(lambda x: float(eval(x)), sp))
            sp = sorted(sp)
            print('Ср. арифметическое =', st.fmean(sp))
            print('Ср. геометрическое =', st.geometric_mean(sp))
            print('Ср. гармоническое =', st.harmonic_mean(sp))
            print('Медиана =', st.median(sp))
            print('Низшая медиана =', st.median_low(sp))
            print('Высшая медиана =', st.median_high(sp))
            print('Групп. медиана =', st.median_grouped(sp))
            print('Мода =', st.mode(sp))
            print('Мультимода =', st.multimode(sp))
            print('Интервалы равной вероятности =', st.quantiles(sp))
            print('Стандартное отклонение =', st.pstdev(sp))
            print('Популяционная дисперсия =', st.pvariance(sp))
            print('Выборочное стандартное отклонение =', st.stdev(sp))
            print('Выборочная дисперсия =', st.variance(sp))
        elif ts == 'vs':
            n = int(input('Всего предметов N: '))
            na = int(input('Искомое кол-во N(A): '))
            nb = int(input('Искомое кол-во N(B) *для объединения и пересеченя событий: '))
            print('P(A) =', sym.Rational(na, n))
            print('P(B) =', sym.Rational(nb, n))
            print('P(A∩B) =', sym.Rational(na, n) * sym.Rational(nb, n))
            print('P(A⋃B) =', sym.Rational(na, n) + sym.Rational(nb, n) - (sym.Rational(na, n)) * sym.Rational(nb, n))
        elif ts == 'of':
            sp = input('Введи первый набор чисел через пробел. Будут выведены все данные из этого раздела: \n').split(
                ' ')
            sp = list(map(lambda x: float(eval(x)), sp))
            sp = sorted(sp)
            sp2 = input('Введи второй набор чисел через пробел. Будут выведены все данные из этого раздела: \n').split(
                ' ')
            print('Kовариация данных =', st.covariance(sp, sp2))
            print('Kорреляция Пирсона =', st.correlation(sp, sp2))
            print('Линейная регрессия =', st.linear_regression(sp, sp2))
            sp2 = list(map(lambda x: float(eval(x)), sp2))
            sp2 = sorted(sp2)
        elif ts == 'dg':
            tg = input('Выбери тип графика/диаграммы:\n'
                       '  - столбчатая диаграмма - sd\n'
                       '  - круговая диаграмма - kd\n'
                       '  - oблако рассеивания - or\n')
            if tg == 'sd':
                ts = input('Введи тип данных:\n'
                           'CSV-файл - csv\n'
                           'Вручную - mt\n')
                if ts.lower() == 'mt':
                    n = int(input('Введи число предметов:\n'))
                    an = []
                    for i in range(1, n + 1):
                        an.append(i)
                    sp = []
                    print('Вводи значения для числа предметов соответственно. После каждого нажимать Enter:')
                    for i in range(n):
                        a = input()
                        sp.append(a)
                    sp = list(map(lambda x: int(eval(x)), sp))
                    fig = plt.figure()
                    plt.bar(an, sp, color='r')
                    plt.grid(True)
                    plt.show()
                elif ts.lower() == 'csv':
                    road = input('Введи путь файла. Должно оканчиваться на .csv:\n')
                    data = pd.read_csv(road)
                    df = pd.DataFrame(data)
                    X = list(df.iloc[:, 0])
                    Y = list(df.iloc[:, 1])
                    plt.grid(True)
                    plt.show()
                elif tg == 'or':
                    name = input('Введи путл файла .csv:\n')
            elif tg == 'kd':
                sp = input('Введи наименования данных через пробел:\n')
                x = [10, 26]
                fig = plt.figure()
                plt.pie(x, labels=sp)
                plt.show()
    elif type == 'fu':
        tf = input('Выбери тип графика:\n'
                   '  - 2D\n'
                   '  - 3D\n'
                   '  - Параметральная 2D - p2\n'
                   '  - Параметральная 3D - p3\n')
        if tf == '3D' or tf == '3d':
            a = input('Введи функцию с «F(z)»: \n')
            x = sym.symbols('x')
            y = sym.symbols('y')
            f = lambda x, y: eval(a)
            fig = plt.figure(figsize=(50, 50))
            ax = fig.add_subplot(1, 1, 1, projection='3d')
            x1, x2 = float(input('Введи предел x1 (рекомендуется отрицательное значение):\n')), float(
                input('Введи предел x2:\n'))
            y1, y2 = float(input('Введи предел y1 (рекомендуется отрицательное значение):\n')), float(
                input('Введи предел y2:\n'))
            xval = np.linspace(x1, x2, 100)
            yval = np.linspace(y1, y2, 100)
            x, y = np.meshgrid(xval, yval)
            z = f(x, y)
            surf = ax.plot_surface(
                x, y, z,
                rstride=1,
                cstride=1,
                cmap=cm.viridis)
            plt.grid(True)
            plt.show()
        elif tf == '2D' or tf == '2d':
            a = input('Введи функцию F(x) = ')
            x = sym.symbols('x')
            y = lambda x: eval(a)
            fig = plt.subplots()
            x = np.linspace(-10, 10, 100)
            plt.plot(x, y(x), color='r')
            plt.grid(True)
            plt.show()
    elif type == 'prg':
        tp = input('Введи тип: \n'
                   '  - арифметическая - ap, \n'
                   '  - геометрическая - gp \n')
        if tp == 'ap':
            print('Введи исходные данные: \n')
            anach = eval(input('a₁ = '))
            alast = eval(input('aₙ = '))
            d = eval(input('d = '))
            sp = []
            for i in range(anach, alast + 1, d):
                sp.append(i)
            print('Сумма всех членов =', ((2 * anach + d * (len(sp) - 1)) / 2) * len(sp))
            x = input('Проверка принадлежит ли число прогрессии:\n')
            if x in sp:
                print('Пренадлежит')
            else:
                print('Не пренадлежит')
        # elif tp == 'gp':
    elif type == 'gm':
        print('Типы данных и величин:\n'
              '\tПланиметрические:\n'
              '\t\tквадрат -  cu\n'
              '\t\tромб - rb\n'
              '\t\tокружность - cr\n'
              '\t\tкруг - kr\n'
              '\t\tпараллелограмм - pg\n'
              '\t\tпрямоугольник - pu\n'
              '\t\tтрапеция - tp\n'
              '\t\tтреугольник - tg\n'
              '\t\tправильный n-угольник - nu\n'
              'Стереометрические:\n'
              '\tПризмы:\n'
              '\t\tПроизвольная n-угольная - rnp\n'
              '\t\tПрямая n-угольная - pnp \n'
              '\t\tПравильная n-угольная - inp\n'
              '\tПирамиды:\n'
              '\t\tПроизвольная - rsp\n'
              '\t\tПрямая - psp\n'
              '\t\tПравильная - isp\n'
              '\tТела вращения:\n'
              '\t\tЦилиндр - sci\n'
              '\t\tШар - sph\n'
              '\t\tКонус - scs\n'
              '')
        a = input('Введи фигуру:\n')

except Exception as e:
    print(e)
