import pyautogui as pg
import time
import pygetwindow as gw
from text_db import *

def get_active_window() -> bool:
    window = gw.getActiveWindowTitle()
    return window == "한컴 타자연습"

def hancom_typing(texts:str) -> None:
    time.sleep(2)
    
    i = 0
    while i < len(texts):
        if get_active_window():
            print(texts[i])
            ii = 0
            text_split = list(texts[i])
            while ii < len(text_split):
                if get_active_window():
                    pg.write(text_split[ii], interval=0)
                    ii += 1
                    time.sleep(0.05)
                else:
                    print("액티브 윈도우 창 확인 - 2")
                    time.sleep(2)

            i += 1
        
        else:
            print("액티브 윈도우 창 확인 - 1")
            time.sleep(2)


hancom_typing(en_texts)