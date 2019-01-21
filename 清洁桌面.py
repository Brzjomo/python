#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
from enum import Enum


class dirStruct(Enum):
    DirNone = 1     #直接拷贝到指定的目录
    DirExt = 2      #按后缀名新建文件夹，将相同的文件拷贝到指定的目录
    DirOrigin = 3   #按照原来目录来新建目录并且拷贝文件


def moveextfile(srcpath, dstpath, ext, dirstrut):
    for root, _, files in os.walk(srcpath):
        if dirstrut is dirStruct.DirOrigin:
            newpath = root.replace(srcpath, dstpath)
            if not os.path.exists(newpath):
                os.mkdir(newpath)
            for filename in files:
                if os.path.splitext(filename)[1] in ext:
                    filepath = os.path.join(root, filename)
                    shutil.move(filepath, newpath)

        if dirstrut is dirStruct.DirExt:
            for dirext in ext:
                dirpath = os.path.join(dstpath, dirext.lstrip('.'))
                if not os.path.exists(dirpath):
                    os.mkdir(dirpath)
            for filename in files:
                extname = os.path.splitext(filename)[1]
                if extname in ext:
                    filepath = os.path.join(root, filename)
                    newfilepath = os.path.join(dstpath, extname.lstrip('.'))
                    shutil.move(filepath, newfilepath)

        if dirstrut is dirStruct.DirNone:
            for filename in files:
                if os.path.splitext(filename)[1] in ext:
                    filepath = os.path.join(root, filename)
                    shutil.move(filepath, dstpath)


if __name__ == "__main__":
    srcpath = r'C:\Users\Lenovo\Desktop'
    #桌面文件夹路径
    dstpath = r'C:\Users\Lenovo\桌面收纳'
    #储存文件夹路径
    moveextfile(srcpath, dstpath, ['.txt', '.html', '.htm', '.css', '.js', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.php', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.mp4', '.avi', '.mkv', '.flv', '.lua', '.mp3', '.iso', '.rar', '.zip', '.7z', '.exe', '.pdf', '.bmp', '.tif', '.wav', '.aac', '.flac', '.swf', '.ini', '.dll', '.obj', '.c4d', '.3ds', '.bat', '.ai', '.dwg', '.aps', '.asp', '.bin', '.chm', '.chr', '.class', '.crt', '.fon', '.ico', '.mid', '.msi', '.py', '.psd', '.raw', '.reg', '.tga', '.ttf', '.wav', '.fbx', '.max', '.mtl', '.sbsar', '.lnk', '.pyc', '.fbp', '.tga', '.tbscene', '.3b', '.toc', '.spp', '.zpr', '.bip', '.html', '.html', '.html'], dirStruct.DirOrigin)
    #删除路径文件夹下的所有东西（用来删除空文件夹，如果有上方没有定义的文件类型，此步骤也会导致未定义文件的永久删除）。新增文件类型时，记得同时在两个脚本中添加。
    shutil.rmtree(srcpath)
    #原理是将桌面文件夹中的所有已定义的文件类型，剪切到储存文件夹中。然后删除所有未定义的文件类型和空文件夹。
    #脚本运行后桌面剩余的文件，一律都在公共文件夹中，需要手动剪切到储存文件夹。第二次就不需要手动处理了。
