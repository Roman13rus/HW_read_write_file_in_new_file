def reader(list_files): #в качестве аргумента принимаем список файлов
    text_dict = {}
    for i, file in enumerate(list_files):
        with open(file,'r',encoding='utf-8') as firstfile:# открываем для чтения всех файлов и посчета количествыа строк.
            text = firstfile.readlines()
            text_dict[int(len(text))] = list_files[i]
            text_sort_tuple = sorted(text_dict.items(), key=lambda x: x[0]) #сортируем словарь по ключам(количеству строк)
            text_dict = dict(text_sort_tuple)
    #print(text_dict) # для проверки
    for count, name in text_dict.items(): 
        with open('new.txt','a',encoding='utf-8') as doc: #открываем файл для перезаписи в новый файл
            doc.write(name)
            doc.write('\n')
            doc.write(str(count))
            doc.write('\n')
            with open(name,'r',encoding='utf-8') as file:
                content = file.read()
                doc.write(content)
                doc.write('\n')

print(reader(['1.txt', '2.txt','3.txt'])) #для проверки 
