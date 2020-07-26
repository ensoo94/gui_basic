from tkinter import *

# 1. Create Frame
root = Tk()

root.title("Python GUI Test") # 창 제목
#root.geometry("640x480+400+200") # 창 크기 : 가로 * 세로 + x 위치 + y 위치
root.geometry("640x480")
root.resizable(False, False) # 창 크기 조절 여부 : x(너비), y(높이) 값 변경 불가


root.mainloop() # 창이 닫히지 않도록 하는 역할

