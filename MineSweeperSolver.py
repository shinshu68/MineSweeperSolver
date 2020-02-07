
##PyAutoGUIのモジュール
import pyautogui

##プロセスを制御するためにOS周りのモジュール
import re
import os
import subprocess
import sys
import time
import array

##Win32のUI情報と制御用モジュール
# import win32api
import win32gui
import win32con


#以下、メインルーチン
if __name__ == "__main__":
    #実行前の待機(秒)
    time.sleep(1)
    #画面サイズの取得
    screen_x,screen_y = pyautogui.size()

    #マウスを(1,1)に移動しておく
    pyautogui.moveTo(1, 1, duration=1)

    #win32guiを使ってウインドウタイトルを探す
    #Windowのハンドル取得('クラス名','タイトルの一部')で検索クラスがわからなかったらNoneにする
    #有名どころで('#32770',"名前を付けて保存")かな
    parent_handle = win32gui.FindWindow(None, "Mine2000")

    #ハンドルIDが取れなかったら、電卓を起動する
    if parent_handle == 0 :
        cmd = 'C:\Program Files (x86)\mine2000 project\mine2000 ver2.2.1\mine2000.exe'
        # cmd = ['start', 'C:\Program Files (x86)\mine2000 project\mine2000 ver2.2.1\mine2000.exe']
        subprocess.Popen(cmd, shell=True)
        time.sleep(3)
        parent_handle = win32gui.FindWindow(None, "Mine2000")

    if parent_handle == 0 :
        print(u"アプリの起動に失敗したみたい、中断します")
        sys.exit()

    #ハンドルが取れたら、ウインドウの左上と右下の座標と画面のアクティブ化
    #ちなみに、アプリ内のボタンとか入力窓も頑張ればとれるけど、win32guiでやると複雑になりすぎる
    #おとなしく、アプリの座標とトップレベルウインドウの情報だけ使う
    if parent_handle > 0 :
        win_x1,win_y1,win_x2,win_y2 = win32gui.GetWindowRect(parent_handle)
        print(u"アプリの座標:"+str(win_x1)+"/"+str(win_y1))
        apw_x = win_x2 - win_x1
        apw_y = win_y2 - win_y1
        print(u"アプリの画面サイズ:"+str(apw_x)+"/"+str(apw_y))
        print(u"アプリを最前面に持ってくるよ")
        win32gui.SetForegroundWindow(parent_handle)
        #ウインドウの完全な情報を取ってくる、FindWindowで部分一致だったりした場合の補完用
        titlebar = win32gui.GetWindowText(parent_handle)
        classname = win32gui.GetClassName(parent_handle)


    #Drag/Drop関数があるけれど、実はmouseDownとmoveToを使ったほうがいい
    #アプリのマウスオーバー挙動はD&Dでは反応しない(逆に反応させないように使う場合はdragTo/dragRelがいい)
