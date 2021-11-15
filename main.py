import os


class Lz77:
    def __init__(self, path, creat=None):
        self.path = path
        self.text = open(path, 'r').read()
        if creat != None:
            self.revtext = open(creat, 'w')
        self.textcoda = open('testing/file2.txt', 'w')
        self.textcoda2 = open('testing/file3.txt', 'w')
        self.lampa = []  # массив с букавами
        self.chisla = []  # массив с индаксами букав
        self.flag = -1
        self.a = ''

    def print(self):
        return print(self.text)

    def algoritm(self):
        for i in range(len(self.text)): # не видит цепочки повторений больше 2, исправить
            if self.flag != -1:
                self.lampa.append(self.text[i])
                self.chisla.append(self.flag+1)
                self.flag = None
            else:
                if self.text[i] in self.lampa:
                    self.flag = self.lampa.index(self.text[i])
                else:
                    self.lampa.append(self.text[i])
                    self.chisla.append(0)
        for i in range(len(self.lampa)):
            self.a += f'{self.chisla[i]}{self.lampa[i]}'
        self.textcoda.write(self.a)
        self.textcoda.close()
        self.a = ''

    def reverseAlgorithm(self):
        for i in range(len(self.chisla)):
            if self.chisla[i] != 0:
                self.a += self.lampa[self.chisla[i]-1]
                self.a += self.lampa[i]
            else:
                self.a += self.lampa[i]
        self.textcoda2.write(self.a)
        self.textcoda2.close()
        self.a = ''

a = 'testing/file1.txt'
abc = Lz77(a)
abc.algoritm()
abc.reverseAlgorithm()
# b = 'testing/file2.txt'
size1 = os.stat(a).st_size
print(f'исходный размер файла {size1} байт\n')
size2 = os.stat('testing/file2.txt').st_size
print(f'получившийся после RLE размер файла {size2}')
# qqq = size1 / size2
# print(f'кф сжатия {qqq}')
