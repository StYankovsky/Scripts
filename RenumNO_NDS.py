# Скрипт перенумеровывает строки в налоговой декларации (когда, например, свели из нескольких файлов)
import re                                                  # импорт библиотеки для регулярных выражений
path = './svod.xml'                               # Путь к исходному файлу
num = 0                                                    # Счётчик для выражения замены
searchStr = 'НомерПор=\"\d{,3}\"'      # Выражение для замены НомерПор="<цифра>[<цифра><цифра>]"
with open (path, "rt", encoding="cp1251") as fin , open("shablon_new.txt", "wt", encoding="cp1251") as fout:
    content = fin.readlines()                      #Читаем построчно в список
#    content = [x.strip() for x in content] # Эта штука удаляет все непечатаемые символы в строке, 
#                                                              # но нам надо оставить красивую структуру документа (знаки табуляции),
#                                                              # так что здесь это не применяем :)
    for row in range(len(content)) :
        line = str (content[row])                  # Формируем строку из элемента списка
        if len (re.findall (searchStr,  line)) : # Если скомое в строке найдено
            num = num + 1
            changeStr = 'НомерПор="'+ str (num)+'"'      # Формируем замещающее выражение 
            lineWrite = re.sub (searchStr , changeStr , line) # Заменяем искомое на сформированную строку
            print (lineWrite[:-1],  file=fout)                          # Пишем в выводной файл с удалением лишнего перевода строки
        else :
            print (line[:-1],  file=fout) # Либо пишем строку AsIs
