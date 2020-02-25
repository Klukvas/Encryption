import re
chars = '''
а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п,
р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я
        '''
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
#16, 27, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
# ЧИСЛА В ЦЕЗАРЕ НЕ ПЕРЕВОДЯТСЯ
chars = chars.split(',')
# Создание массива из строки, где каждый символ - отдельный элемент

charst = [char.replace(',', '').replace(
    ' ', '').replace('\n', '') for char in chars]
#Очищаем список от лишних запятых  и от знаков переноста строки

def decoder(string):
    string_out = ''
    key = int(input('Key: '))
    for char in string:

        index = charst.index(char)
        # Находим индекс символа в нашем алфавите

        index += key
        # Находим искомый индекс

        if index > len(charst) - 1:
            # Если индекс больше чес общая длинна алфавита

            move = int(len(charst)) - index
            # Узнаем на скольно нужно подвинуть начиная с первого символа

            string_out += charst[-move]
        else:
            string_out += charst[index]

    return string_out

def if_digit(all_numers, string_val):
    indexes = []
    for item in all_numers:
        indexes.append(string_val.index(item))
        #Записываем на каких местах стоят числа
    string = re.sub('\d+', '', string_val)
    #Удаляем числа со строки
    string_out = decoder(string)
    #ПОлучаем собранную строку
    for num, it in enumerate(indexes):
        #enumerate - нумерация цикла(начинается с 1); Перебираем индексы, на которых были числа
        for numb, i in enumerate(string):
            #Перебираем собранную строку
            if numb-1 == num-1:
                #При нахождении нужного индекса, в котором должно быть число
                if num == len(string_out):
                #Если число было в конце
                    string_out = string_out + str(all_numers[numb])
                else:
                    string_out = string_out[:it] + str(all_numers[numb]) + string_out[it:]
                #Возвращаем на нужные места числа
    print(f'string: {string_out}')
    return string


while True:
    # decoder('замъскйиазоюожъан')
    string_val = str(input('Ur string: ')).lower()
    #Вводим строку для дешифровки
    all_numers = re.findall('\d+', string_val)
    #Ищем есть ли в ней числа
    if len(all_numers):
        #Если числа присутствуют
        if_digit(all_numers, string_val)
    else:
        decoder(string_val)
