import sys
import tkinter
from tkinter import filedialog, Text
from tkinter import Button
from tkinter import Frame
from tkinter import messagebox

window = tkinter.Tk()

def openTextChooseDialog():
    fileSelectType = [("テキストファイル", ".txt")]
    filePath = tkinter.filedialog.askopenfilename(filetypes=fileSelectType)
    return filePath

def openTextSaveDialog():
    fileSelectType = [("テキストファイル", ".txt")]
    savePath = tkinter.filedialog.asksaveasfilename(filetypes=fileSelectType)
    return savePath

def runOpenFileCommand():
    selectPath = openTextChooseDialog()
    if selectPath == "":
        print("何も選ばれませんでした")
    else:
        print(selectPath)

def runSaveCommand():
    entryText = entry.get("1.0", "end")
    selectPath = openTextSaveDialog()
    if selectPath == "":
        tkinter.messagebox.showerror(title="エラー", message="ファイルが選ばれませんでした")
    else:
        file = open(selectPath, 'x', encoding="UTF-8")
        file.write(entryText)
        tkinter.messagebox.showinfo(title="成功", message="正常にファイルが保存されました")

def runExitCommand():
    sys.exit(0)

def windowInit():
    global entry
    window.wm_title("メモ帳")
    window.wm_geometry("1280x720")

    menu = tkinter.Menu(window, tearoff=0)
    window.config(menu=menu)
    file_menu = tkinter.Menu(menu, tearoff=0)
    file_menu.add_command(label="開く", command=runOpenFileCommand)
    file_menu.add_command(label="保存する", command=runSaveCommand)
    file_menu.add_command(label="終了する", command=runExitCommand)
    menu.add_cascade(label="ファイル", menu=file_menu)

    frame_1 = Frame(window, borderwidth=4)
    frame_1.pack(side="left", fill="both", expand=True)
    entry = tkinter.Text(frame_1)
    entry.pack(side="left", fill="both", anchor="nw", expand=True)

if __name__ == "__main__":
    windowInit()
    window.mainloop()