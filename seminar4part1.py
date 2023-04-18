# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So
# if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

a = "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890"

a = a.split()

b = []

for i in a:
    b.append(i[0:2])
c = dict().fromkeys(b, list())

for i in a:
    c[i[0:2]].append(i)

print(c)