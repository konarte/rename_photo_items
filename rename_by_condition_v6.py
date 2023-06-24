import os
from fs import open_fs

#Получить текущую директорию, где запущен скрипт
#dir = os.path.abspath(os.curdir)
#Получить текущую директорию, где расположен скрипт
#os.path.abspath(__file__)

#Скрипт переименовывает файлы в зависимости от требуемых условий
#состоит из трех функций:
#1обход древа и получение ссылок на файлы
#2создание списка для переименования по условию
#3переименование файлов


def move_files(data):
    # на вход словарь - старый путь: новый путь
    #Source file path source = 'data.csv'
    # destination file path dest = 'app/data.csv'
    # filename, dirname+'\\'+path2dir+'\\'+filename
    # try renaming the source path
    # to destination path
    # using os.rename() method
    if len(data)< 1:
        print ('Нечего копировать!')
        return

    data_items = data.items()

    for key, value in data_items:
        print('Обнаружен   : ', key)
        print('Переименован: ', value)
         
        try:
            os.rename(key, value)
            print("File is moved successfully")
 
        # If Source is a file
        # but destination is a directory
        except IsADirectoryError:
            print("Source is a file but destination is a directory.")
 
        # If source is a directory
        # but destination is a file
        except NotADirectoryError:
            print("Source is a directory but destination is a file.")
 
        # For permission related errors
        except PermissionError:
            print("Operation not permitted.")
 
        # For other errors
        except OSError as error:
            print(error)
        print('==================================')
    
         

def dir_contents(path):
    paths = []
    home_fs = open_fs(path)
    for path in home_fs.walk.files(filter=['*.jpg','*.png']):
        paths.append(path)
    return paths

def file_name_trans(path):
    count = 1 # с какого номера начинаем нумирацию если файлов в каталоге
    item_new = '' # новый путь для переименования
    
    pathfile_old ='' # старый путь к файлу для проверки   на серии файлов в одной директории
    #path_dictionary = {} 
    for item in path:
        #print(item)
        if item.find('#') != -1:

            #Получаем путь до файла
            pathfile = str(item.rsplit('/',1)[0])+'/'

            #проверяем - если путь одинаковый то увеличиваем счётчик файлов
            if pathfile_old == pathfile:
                count += 1
            else:
                count = 1 # с какого номера начинаем нумирацию если файлов в каталоге
            pathfile_old = pathfile 
            
            #Получаем расширение
            ext = (item[(len(item)-4):len(item)])

            #Получаем индекс
            #из /Kiepe/429000001#49904/photo_detail/429000001_detail_01.jpg
            #в  429000001
            #path.rsplit('/')[0])
            nameindex = (item.rsplit('#')[0]).rsplit('/',1)[1]
            # удаляем один ,два и три  и четыре пробела подряд в индексе
            nameindex = nameindex.replace('    ', '')
            nameindex = nameindex.replace('   ', '')
            nameindex = nameindex.replace('  ', '')
            nameindex = nameindex.replace(' ', '')
            

            if item.find('detail') != -1:
                #собираем путь обратно
                #print(pathfile + nameindex + '_detail' + str('%02d'%count)+ ext)
                #print('pathfile',pathfile)
                #print('nameindex',nameindex)
                #print('_detail')
                #print('str(%01d%count)',str('%01d'%count))
                #print('ext',ext)
                item_new = pathfile + nameindex + '_detail' + str('%01d'%count)+ ext
                translator(directory, item, item_new)
                #path_dictionary.update({directory+item : directory+item_new})

            elif item.find('mobile') != -1:
                #собираем путь обратно
                #print(pathfile + nameindex + '_mobile' + str('%02d'%count)+ ext)
                #print('pathfile',pathfile)
                #print('nameindex',nameindex)
                #print('_detail')
                #print('str(%01d%count)',str('%01d'%count))
                #print('ext',ext)
                item_new = pathfile + nameindex + '_mobile' + str('%01d'%count)+ ext
                translator(directory, item, item_new)
                #path_dictionary.update({directory+item : directory+item_new})
                
            elif item.find('web_1') != -1:
                #собираем путь обратно
                #print(pathfile + nameindex + '_web1' + str('%02d'%count)+ ext)
                item_new = pathfile + nameindex + '_web1_' + str('%01d'%count)+ ext
                translator(directory, item, item_new)
                
            elif item.find('web_2') != -1:
                #собираем путь обратно
                #print(pathfile + nameindex + '_web2' + str('%02d'%count)+ ext)
                item_new = pathfile + nameindex + '_web2_' + str('%01d'%count)+ ext
                translator(directory, item, item_new)
                
            else:
                print('____________not fileng')
        item_old = item # запоминаем прошлый путь
                
    return dic_path

def translator(rootpath, path_old, path_new):
    #тут корректируем пути для переноса
    #можно добавить различные путив зависимости от системы
    path_old = (directory + path_old).replace('/', '\\')
    # удаляем два и три  и четыре пробела подряд - создать отдельную процедуру которая генерит новый адрес и создает каталоги
    #path_new = path_new.replace('    ', '')
    #path_new = path_new.replace('   ', '')
    #path_new = path_new.replace('  ', '')
    path_new = (directory + path_new).replace('/', '\\')
    #если  пути не совпадают, тогда пишем в словарь для копирования
    if path_old != path_new:
        #работает с глобальным словарем
        dic_path.update({path_old : path_new})

    return dic_path

            
            
dic_path ={}   # словарь в который будем писать старый путь и новый путь     
    
directory = os.path.abspath(os.curdir) # директория в которой находится скрипт

files_old = dir_contents(directory)

dic_path = file_name_trans(files_old)

move_files(dic_path)

print('Переименование завершено!')


