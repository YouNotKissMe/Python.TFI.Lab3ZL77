import os
from tabulate import tabulate


class lz77:
    def __init__(self, path):
        self.q = path
        self.path = open(path, 'r', encoding='utf-16').read()
        self.massivBukav = []
        for i in self.path:
            if i not in self.massivBukav:
                self.massivBukav.append(i)
        self.a = None
        self.potok = []
        self.tabuletions = [['размер исходного файла', 'размер после сжатия', 'len(исходного файла)',
                             'len(сжатого)', 'кф.сжатия']]

    def algoritm(self):
        for i in self.path:
            if self.a:
                if self.a in self.massivBukav:
                    self.a += i
                else:
                    self.massivBukav.append(self.a)
                    self.potok.append(self.massivBukav.index(self.a[:-1]))
                    self.a = self.a[-1] + i
            else:
                self.a = i
        if len(self.path) > 1:
            if self.a in self.massivBukav:
                self.potok.append(self.massivBukav.index(self.a))
            else:
                self.massivBukav.append(self.a)
                self.potok.append(self.massivBukav.index(self.a))
        self.a = None

    def reverseee(self):
        self.a = ''
        for i in self.potok:
            self.a += self.massivBukav[i]
        antiRLEtext = open('testing/file3.txt', 'w',encoding='utf-16')
        antiRLEtext.write(self.a)
        self.a = ''
        for i in self.potok:
            self.a += str(chr(i))
        RLEtext = open('testing/file2.txt', 'w',encoding='utf-16')
        RLEtext.write(self.a)
        size1, size2 = os.stat(self.q).st_size, os.stat('testing/file2.txt').st_size
        qqq = size1 / size2
        self.tabuletions.append([f'{size1} байт', f'{size2} байт', len(self.path),
                                 len(self.massivBukav), qqq])
        return print(tabulate(self.tabuletions, tablefmt='pipe', stralign='center',
                              headers='firstrow'))


if __name__ == '__main__':
    a = 'testing/file1.txt'
    q = lz77(a)
    q.algoritm()
    q.reverseee()

