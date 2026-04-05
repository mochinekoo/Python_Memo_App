import sys
import tkinter
from tkinter import filedialog

window = tkinter.Tk()
window.wm_title("メモ帳")

def openTextChooseDialog():
    fileSelectType = [("テキストファイル", ".txt")]
    filePath = tkinter.filedialog.askopenfilename(filetypes=fileSelectType)
    return filePath

def runOpenFileCommand():
    selectFile = openTextChooseDialog()
    if selectFile == "":
        print("何も選ばれませんでした")
    else:
        print(selectFile)

def runSaveCommand():
    pass

def runExitCommand():
    sys.exit(0)

menu = tkinter.Menu(window, tearoff=0)
window.config(menu=menu)
file_menu = tkinter.Menu(menu, tearoff=0)
file_menu.add_command(label="開く", command=runOpenFileCommand)
file_menu.add_command(label="保存する", command=runSaveCommand)
file_menu.add_command(label="終了する", command=runExitCommand)

menu.add_cascade(label="ファイル", menu=file_menu)


window.mainloop()