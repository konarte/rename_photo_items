import os
import sys
import inspect
from os.path import join, getsize
#mport pathlib - заменить os.path в части слешей
from pathlib import Path


import copy
import shutil
import datetime

from colorama import init
from colorama import Fore, Back, Style


def rename(f_path, new_name):
    #print('06 = ',root, nameinfile03)
    filelist = os.listdir(f_path)
    count = 0
 
    for file in filelist:
        oldname = f_path + filelist[count]
        ext = (oldname[(len(oldname)-4):len(oldname)])
        f = Path(oldname)
        if ext == '.ini':
            print(Fore.RED + 'Is ini extension! ===> ' + Fore.WHITE + oldname)
            os.remove(oldname)
            print(Fore.RED + 'DELETED!')
            return
        
        if (ext == '.jpg') or (ext == '.png'):
            newnum = '_'+str('%02d'%(count + 1))
            newname = f_path + new_name + newnum + ext
            if oldname == newname:
                print(Fore.WHITE +'deja-rename!')
                print(Fore.MAGENTA + 'old=> ', oldname)
                print(Fore.MAGENTA + 'new=> ', newname)
                continue
            #os.rename(oldname, newname)
            try:
                f.rename(newname)
            except:
                print(OSError)
            print(Fore.GREEN)
            print(' _______________________________________________________________ ')
            print(Fore.YELLOW + 'old => ', oldname)
            print(Fore.GREEN + 'new => ', newname)
            print(' _______________________________________________________________ ')
            count += 1
            
        

init()
#print(Fore.GREEN + 'green text')
#print(Back.YELLOW + 'yellow back')
#print(Style.BRIGHT + 'bright' + Style.RESET_ALL)
#print('default')

path = sys.path[0]
for root, dirs, files in os.walk(path):
    #print(root, "consumes", end=" ")
    root = root.replace('/', '\\')+'\\'
    #print('00 = ', path, root)
    
    if '#' in root:
        #nameinfile = root[int(root.find('#'))+1:len(root)]

        nameinfile01 = root[::-1]
        nameinfile01 = nameinfile01[int(nameinfile01.find('#')):]
        nameinfile01 = nameinfile01[int(nameinfile01.find('#')+1):int(nameinfile01.find('\\'))]
        nameinfile01 = nameinfile01[::-1]

        #nameinfile01 = root[0:int(root.find('#'))+1]
        #print('01 = ',nameinfile01)
        #for i in range(len(nameinfile01),0,-1):
        #    if string.startswith('o', i)


        #nameinfile01 = nameinfile01[int(nameinfile01.find('#')+1):int(nameinfile01.find('\\'))]
        #nameinfile01 = root[int(root.find('\\')+1):int(root.find('#'))]
        #print('01 = ',nameinfile01)

    if '_' in root:
        nameinfile02 = root[int(root.find('_')+1):(len(root)-1)]
            #print('02 = ', nameinfile02)

        nameinfile03= nameinfile01 + '_' + nameinfile02
            #print('03 = ', nameinfile03)
            #print('041 = ', root)
            #root = root.replace('/', '\\')+'\\'
            #root = root.replace('\\', '/')+'/'
            #print('042 = ', root)
            

        rename(root, nameinfile03)
        #else:
            #continue
    

    #print(sum(getsize(join(root, name)) for name in files), end=" ")
    #print("bytes in", len(files), "non-directory files")
print(Style.BRIGHT + 'ALL OK!!!' + Style.RESET_ALL)
    


