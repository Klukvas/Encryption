chars = '''
а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п,
р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я
        '''

chars = chars.split(',')
# Создание массива из строки, где каждый символ - отдельный элемент

charst = [char.replace(',', '').replace(
    ' ', '').replace('\n', '') for char in chars]
#Очищаем список от лишних запятых  и от знаков переноста строки
 
 
 
def coder_step1(string):
    string = string.replace(' ', '')
    #Убираем все пробелы
    first_code = []
    for ch in string:
        index = charst.index(ch)
        #Находим индекс каждой буквы
        first_code.append(index)
        #Добавляем в массив
    return first_code
    
def coder_step2(list, key1, key2_simp):
    second_code = []
    for item in list:
        formula = key2_simp*item + key1
        #Формула первой шифровки
        second_code.append(formula)
    return second_code
             
def coder_step3(list):
    third_code = []
    for item in list:
        formula = item % 33
        third_code.append(formula)
    return third_code

def coder_step4(list):
    fourth_code = ''
    for item in list:
        ciphertext = charst[item]
        #НАходим букву по шифрованному числу
        fourth_code = fourth_code + ciphertext
        
    return fourth_code

 
def decoder_step1(string):
    ciphertext = string.replace(' ', '').strip()
    first_decode = []
    for ch in ciphertext:
        index = charst.index(ch)
        first_decode.append(index)
    return first_decode

def decoder_step2(list, key2_simp, key1):
    second_code = []
    for ch in list:
        num = key2_simp*(int(ch) + 33 - key1)
        second_code.append(num)
    return second_code
# def decoder_step2(list):
#     variant_sh1 = []
#     variant_sh2 = []
#     variant_sh3 = []
#     second_code = []
#     for a in range(100):
#         for b in range(100):
#             for ch in list:
#                 if a not in [11,3,33]:
#                     num = a*(int(ch) + 33 - b)
#                     variant_sh1.append(num)
#             variant_sh2.append(variant_sh1)
#         variant_sh3.append(variant_sh2)
#     second_code.append(variant_sh3)
#     return second_code
def decoder_step3(list):
    third_code = []
    for ch in list:
        num = ch % 33
        third_code.append(num)
    return third_code      
            
def decoder_step4(list):
    fourth_code = ''
    for item in list:
        ciphertext = charst[item]
        #НАходим букву по шифрованному числу
        fourth_code = fourth_code + ciphertext
    return fourth_code 
 
 
        
def main():
    variant = input('Для дешифровки введите 1 для шифровки 2: ').strip()
    string = str(input('Ur string: ')).lower()
    if variant == '2':
        key1 = int(input('key №1: '))
        key2_simp = int(input('key №2 (not 3,11,33): '))
        code_string = coder_step4(
            coder_step3(
            coder_step2(
            coder_step1(string), key1, key2_simp)))
        print(f'code_string: {code_string}')
    elif variant == '1':
        key1 = int(input('key №1: '))
        key2_simp = int(input('key №2 (not 3,11,33): '))
        decode_string = decoder_step4(
            decoder_step3(
            decoder_step2(
            decoder_step1(string),key1, key2_simp)))
        print(f'decode_string: {decode_string}')
    else:
        print(f'Вы ввели {variant} а нужно 1 или 2')
        main()
    
if __name__ == '__main__':
    while True:
        main()