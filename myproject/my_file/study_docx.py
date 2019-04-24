# coding=utf-8
from docx import Document
from win32com import client as wc


def read_docx(filepath):
    try:
        document = Document(filepath)
    except:
        return {"status": "faild", "msg": "can't open file"}
    text = ""
    for paragraph in document.paragraphs:
        print paragraph.text
        text += paragraph.text
    print text


def docToDocx():
    word = wc.Dispatch('Word.Application')
    word.Visible = 1
    doc = word.Documents.Open('F:\python workspace\myproject\myproject\my_file\doc.doc')  # 目标路径下的文件
    doc.SaveAs('doc.docx', 12)  # 转化后路径下的文件
    doc.Close()
    word.Quit()


if __name__ == '__main__':
    docToDocx()
