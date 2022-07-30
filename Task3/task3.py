# Винни-Пух и ритм стихов
text = str(input("Введите ваш стих: "))
vocals = ['а','у','о','ю','ы','я','е','ё','э']
lines = text.split()
lst = [sum(i in vocals for i in line) for line in lines]
if len(set(lst)) == 1:
    res = 'парам пам-пам'
else: res = 'пам парам'

print(res)