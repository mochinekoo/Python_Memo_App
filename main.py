import sys
import tkinter
from tkinter import filedialog, Text
from tkinter import Button
from tkinter import Frame
from tkinter import messagebox

window = tkinter.Tk()

def openTextChooseDialog():
    """
    開くファイルを選ぶ関数
    :return: 選んだパス
    """

    fileSelectType = [("テキストファイル", ".txt")]
    filePath = tkinter.filedialog.askopenfilename(filetypes=fileSelectType)
    return filePath

def openTextSaveDialog():
    """
    ファイルを保存する場所を選ぶ関数
    :return: 選んだパス
    """

    fileSelectType = [("テキストファイル", ".txt")]
    savePath = tkinter.filedialog.asksaveasfilename(filetypes=fileSelectType)
    return savePath

def runOpenFileCommand():
    """
    ファイルを開く関数（メニュー用）
    """
    selectPath = openTextChooseDialog()
    if selectPath == "":
        print("何も選ばれませんでした")
    else:
        print(selectPath)

def runSaveCommand():
    """
    ファイルを保存する関数（メニュー用）
    """

    entryText = entry.get("1.0", "end")
    selectPath = openTextSaveDialog()
    if selectPath == "":
        tkinter.messagebox.showerror(title="エラー", message="ファイルが選ばれませんでした")
    else:
        file = open(selectPath, 'x', encoding="UTF-8")
        file.write(entryText)
        tkinter.messagebox.showinfo(title="成功", message="正常にファイルが保存されました")

def runExitCommand():
    """
    アプリを終了する関数（メニュー用）
    """
    sys.exit(0)

def windowInit():
    """
    ウインドウを設定する関数
    :return: 成功した場合はTrueを返す
    """

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
    return True

if __name__ == "__main__":
    windowInit()
    window.mainloop()