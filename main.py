import sys
import tkinter
from tkinter import filedialog, Text
from tkinter import Button
from tkinter import Frame
from tkinter import messagebox
from tkinter import font
from tkinter import simpledialog

import FontDialog

class Main:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.window = tkinter.Tk()
        return cls._instance

    def openTextChooseDialog(self):
        """
        開くファイルを選ぶ関数
        :return: 選んだパス
        """

        fileSelectType = [("テキストファイル", ".txt")]
        filePath = tkinter.filedialog.askopenfilename(filetypes=fileSelectType)
        return filePath

    def openTextSaveDialog(self):
        """
        ファイルを保存する場所を選ぶ関数
        :return: 選んだパス
        """

        fileSelectType = [("テキストファイル", ".txt")]
        savePath = tkinter.filedialog.asksaveasfilename(filetypes=fileSelectType)
        return savePath

    def runOpenFileCommand(self):
        """
        ファイルを開く関数（メニュー用）
        """
        selectPath = self.openTextChooseDialog()
        if selectPath == "":
            print("何も選ばれませんでした")
        else:
            print(selectPath)

    def runSaveCommand(self):
        """
        ファイルを保存する関数（メニュー用）
        """

        entryText = self.entry.get("1.0", "end")
        selectPath = self.openTextSaveDialog()
        if selectPath == "":
            tkinter.messagebox.showerror(title="エラー", message="ファイルが選ばれませんでした")
        else:
            file = open(selectPath, 'x', encoding="UTF-8")
            file.write(entryText)
            tkinter.messagebox.showinfo(title="成功", message="正常にファイルが保存されました")

    def runChangeFontCommand(self):
        """
        テキストの表示形式を変える関数
        """
        FontDialog.FontDialog(self.window, self)

    def runExitCommand(self):
        """
        アプリを終了する関数（メニュー用）
        """
        sys.exit(0)

    def windowInit(self):
        """
        ウインドウを設定する関数
        :return: 成功した場合はTrueを返す
        """

        self.window.wm_title("メモ帳")
        self.window.wm_geometry("1280x720")

        menu = tkinter.Menu(self.window, tearoff=0)
        self.window.config(menu=menu)
        file_menu = tkinter.Menu(menu, tearoff=0)
        file_menu.add_command(label="開く", command=self.runOpenFileCommand)
        file_menu.add_command(label="保存する", command=self.runSaveCommand)
        file_menu.add_command(label="終了する", command=self.runExitCommand)

        view_menu = tkinter.Menu(menu, tearoff=0)
        view_menu.add_command(label="フォント", command=self.runChangeFontCommand)

        menu.add_cascade(label="ファイル", menu=file_menu)
        menu.add_cascade(label="表示", menu=view_menu)

        frame_1 = Frame(self.window, borderwidth=4)
        frame_1.pack(side="left", fill="both", expand=True)
        self.entry = tkinter.Text(frame_1)
        self.entry.pack(side="left", fill="both", anchor="nw", expand=True)
        return True


if __name__ == "__main__":
    main = Main()
    main.windowInit()
    main.window.mainloop()
