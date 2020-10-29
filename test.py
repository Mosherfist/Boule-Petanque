from collections import namedtuple
Point = namedtuple('Point', 'a b c d e')
pt1= Point[(1, 'Haus', 'house', 'f', 'f', 'f'), (2, 'Uhr', 'watch', 'f', 'f', 'f'), (3, 'Auto', 'CAR', 'f', 'f', 'f')]
Point=
#pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
print(pt1.a)
print(pt1[0])