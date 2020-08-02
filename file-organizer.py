import os
import datetime

path1 = 'C:/Users/mhasa/Desktop/'
path2 = 'C:/Users/mhasa/Downloads/'
path3 = 'C:/Users/mhasa/Desktop/projects/New folder/'
path4 = 'D:/'


def duplicateRename(path, fileName, folderName):
    #print(fileName)
    splitted = fileName.split('.')
    theTime = str(datetime.datetime.now())
    theTime = theTime.replace(' ', '-')
    theTime = theTime.replace(':', '-')
    newName = splitted[0] + theTime + '.' + splitted[1]
    return os.rename(path + fileName, path + folderName + '/' + newName)


def sprucer(path):
    os.chdir(path)
    directoryDoc = path + 'Documents/'
    directoryImg = path + 'img/'
    directoryZip = path + 'Compressed/'
    directoryPs = path + 'ps/'
    directoryAi = path + 'ai/'


    for file in os.listdir():
        if file.endswith('.doc') or file.endswith('.docx') or file.endswith('.pdf') or file.endswith('.csv') or file.endswith('.ppt') or file.endswith('.pptx') or file.endswith('.xlsx'):
            if not os.path.exists(directoryDoc):
                os.mkdir(directoryDoc)
            try:
                os.rename(path + file, path + 'Documents/' + file)
            except FileExistsError:
                duplicateRename(path, file, 'Documents')

        elif file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.jfif'):
            if not os.path.exists(directoryImg):
                os.mkdir(directoryImg)
            try:
                os.rename(path + file, path + 'img/' + file)
            except FileExistsError:
                duplicateRename(path, file, 'img')

        elif file.endswith('.ai'):
            if not os.path.exists(directoryAi):
                os.mkdir(directoryAi)
            try:
                os.rename(path + file, path + 'ai/' + file)
            except FileExistsError:
                duplicateRename(path, file, 'ai')

        elif file.endswith('.psd'):
            if not os.path.exists(directoryPs):
                os.mkdir(directoryPs)
            try:
                os.rename(path + file, path + 'ps/' + file)
            except FileExistsError:
                duplicateRename(path, file, 'ps')

        elif file.endswith('.zip') or file.endswith('.rar'):
            if not os.path.exists(directoryZip):
                os.mkdir(directoryZip)
            try:
                os.rename(path + file, path + 'Compressed/' + file)
            except FileExistsError:
                duplicateRename(path, file, 'Compressed')


sprucer(path1)
sprucer(path4)
