o = []
with open('coefficients.txt') as f:
    for line in f:
        o.append(float(line))
k = o[0]
c = o[1]

# a - Цифровое начение, полученное с АЦП; p - давление [мм рт. ст.]
a = float(input()) # Это заменить на импортирование значения измерений из текстового файла
p = (a - c) / k
print(p)