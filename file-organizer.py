import os
import datetime

path1 = 'C:/Users/mhasa/Desktop/'
path2 = 'C:/Users/mhasa/Downloads/'
path3 = 'C:/Users/mhasa/Desktop/projects/New folder/'


def duplicateRename(path, fileName, folderName):
    #print(fileName)
    splitted = fileName.split('.')
    theTime = datetime.datetime.now()    
    newName = splitted[0] + theTime + f'.{splitted[1]}'
    return os.rename(path + fileName, path + folderName + '/' + newName)


def sprucer(path):
    os.chdir(path)

    directoryDoc = path + 'Documents/'
    directoryImg = path + 'img/'
    if not os.path.exists(directoryDoc):
        os.mkdir(directoryDoc)

    if not os.path.exists(directoryImg):
        os.mkdir(directoryImg)


    for file in os.listdir():
        if file.endswith('.doc') or file.endswith('.docx') or file.endswith('.pdf') or file.endswith('.csv') or file.endswith('.ppt') or file.endswith('.pptx') or file.endswith('.xlsx'):
            try:
                os.rename(path + file, path + 'Documents/' + file)
            except FileExistsError:
                duplicateRename(path, file, 'Documents')

        elif file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.jfif'):
            try:
                os.rename(path + file, path + 'img/' + file)
            except FileExistsError:
                duplicateRename(path, file, 'img')

        elif file.endswith('.ai'):
            try:
                os.rename(path + file, path + 'ai/' + file)
            except FileExistsError:
                duplicateRename(path, file, 'ai')

        elif file.endswith('.psd'):
            try:
                os.rename(path + file, path + 'ps/' + file)
            except FileExistsError:
                duplicateRename(path, file, 'ps')


sprucer(path1)
sprucer(path2)
# path = f'{path2}/'
# os.chdir(path)
# print(os.listdir())

#print([file.endswith('.docx') for file in os.listdir()])
