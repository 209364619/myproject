# coding=utf-8

import filetype

'''
使用pythonfiletype对基本文件类型进行简单分类判断
通过二进制读取文件，而不是使用简单的后缀名进行判断。
'''


def get_file_type(filepath):
    '''
    filetype返回文件类型
    该工具通过将文件转化为二进制流，截取文件的二进制的前2或者4字节进行判断文件格式。
    :param filepath:
    :return: str 文件类型 若非支持文件类型，返回None
    '''
    file_type = filetype.guess_extension(filepath)
    return file_type


def get_file_kind(filepath):
    '''
    获取文件类型(简单文件分类)
    :param filepath:
    :return: 支持文件类型返回文件类型 image,video,audio, application
    '''
    file_mine = filetype.guess_mime(filepath)
    index = file_mine.find('/')
    if index != -1:
        file_kind = file_mine[0:index]
        return file_kind


if __name__ == '__main__':
    # print get_file_type('1')
    print get_file_kind('1')
'''
filetype 支持类型 

图片 

• jpg  –  image/jpeg 
• png  –  image/png 
• gif  –  image/gif 
• webp  –  image/webp 
• cr2  –  image/x-canon-cr2 
• tif  –  image/tiff 
• bmp  –  image/bmp 
• jxr  –  image/vnd.ms-photo 
• psd  –  image/vnd.adobe.photoshop 
• ico  –  image/x-icon

视频 


• mp4  –  video/mp4 
• m4v  –  video/x-m4v 
• mkv  –  video/x-matroska 
• webm  –  video/webm 
• mov  –  video/quicktime 
• avi  –  video/x-msvideo 
• wmv  –  video/x-ms-wmv 
• mpg  –  video/mpeg 
• flv  –  video/x-flv

音频 


• mid  –  audio/midi 
• mp3  –  audio/mpeg 
• m4a  –  audio/m4a 
• ogg  –  audio/ogg 
• flac  –  audio/x-flac 
• wav  –  audio/x-wav 
• amr  –  audio/amr

资料库 


• epub  –  application/epub+zip 
• zip  –  application/zip 
• tar  –  application/x-tar 
• rar  –  application/x-rar-compressed 
• gz  –  application/gzip 
• bz2  –  application/x-bzip2 
• 7z  –  application/x-7z-compressed 
• xz  –  application/x-xz 
• pdf  –  application/pdf 
• exe  –  application/x-msdownload 
• swf  –  application/x-shockwave-flash 
• rtf  –  application/rtf 
• eot  –  application/octet-stream 
• ps  –  application/postscript 
• sqlite  –  application/x-sqlite3 
• nes  –  application/x-nintendo-nes-rom 
• crx  –  application/x-google-chrome-extension 
• cab  –  application/vnd.ms-cab-compressed 
• deb  –  application/x-deb 
• ar  –  application/x-unix-archive 
• Z  –  application/x-compress 
• lz  –  application/x-lzip

字体 


• woff  –  application/font-woff 
• woff2  –  application/font-woff 
• ttf  –  application/font-sfnt 
• otf  –  application/font-sfnt

'''
