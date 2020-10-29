from collections import namedtuple
from random import shuffle, choice

Vokabel = namedtuple('Vokabel', ['deutsch', 'english'])


def read_vokabel_file(fname):
    with open(fname, 'r') as f:
        for line in f.readlines():
            words = line.split(',')
            _ = Vokabel(deutsch=words[0].strip(), english=words[1].strip())
            vokabeln.append(_)
        return vokabeln


def test_deutsch_english(vokabeln):
    score = 0
    for i in vokabeln:
        test = input(f'Was heißt {i.deutsch} auf englisch?: ')
        if test == i.english:
            score += 1
            print('Correct')
        else:
            print(f'Wrong the answer was {i.english}')
    return score


if __name__ == '__main__':
    vokabeln = []
    fname = input('Vokabelfile?')
    vokabeln = read_vokabel_file(fname)
    score = test_deutsch_english(vokabeln)
    print(f'Your final score is {score}!')