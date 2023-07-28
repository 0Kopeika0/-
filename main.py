import random
from slova import WORDS

class Words:    
    def __repr__(self):
        return 'Класс для хранения слов'
    
    words = WORDS
    
    def load_random_word(self):
        return random.sample(self.words, len(self.words))

class BasicWord(Words): 
    def __repr__(self):
        return 'Проверка на соответствие введенного слова действительности'
       
    def __init__(self, subword):
        self.subword = subword
    
    def check(self, word):
        if word in self.subword:
            self.subword.remove(word)
            return True
        else:
            return False
    
    def count(self, word, count):
        zn = self.check(word)
        if zn:
            count+=1
        return count, zn
    
while True:
    name = input('Введите имя игрока ')
    if name=='stop': break
    
    znach = Words()
    massiv = znach.load_random_word()
    
    for i in range(len(massiv)):
        count = 0
        print(f'Составьте {len(massiv[i]["subword"])} слов из слова {massiv[i]["word"].upper()}', 'Слова должны быть не короче 3 букв', 'Чтобы закончить игру, угадайте все слова или напишите "stop"\nПоехали, ваше слово?','', sep = '\n')
        dl = BasicWord(massiv[i]['subword'])
        while True:
            word_people = input('Пользователь: ').lower()
            if word_people == 'stop' or count==len(massiv[i]["subword"])-1: 
                print(f'Игра завершена, вы угадали слов: {count}\n')
                break       
            znachen = dl.count(word_people, count)
            count = znachen[0]
            if znachen[1]:
                print('Компьютер: верно\n')
            else:
                print('Компьютер: неверно\n')