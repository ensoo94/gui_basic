import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()

root.title("Python GUI Test") # 창 제목
root.geometry("640x480")

# 일괄 주석 처리 단축키 : 범위 선택 후 Ctrl + /
#progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # indeterminate - 왔다갔다
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # determinate - 차오름 
# progressbar.start(10) # 10ms마다 움직임 
# progressbar.pack()

# def btncmd(): 
#     progressbar.stop() # 작동 중지 

# btn =  Button(root, text="중지", command=btncmd) # 버튼에 동작 삽입
# btn.pack()

p_var2 = DoubleVar() # %는 항상 정수가 아니기 때문 
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2(): 
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기
        
        p_var2.set(i) # progress bar 값 설정
        progressbar2.update() # ui 업데이트 
        print(p_var2.get())

btn =  Button(root, text="시작", command=btncmd2) # 버튼에 동작 삽입
btn.pack()

root.mainloop() # 창이 닫히지 않도록 하는 역할
