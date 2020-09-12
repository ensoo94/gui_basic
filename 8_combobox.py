import tkinter.ttk as ttk
from tkinter import *

root = Tk()

root.title("Python GUI Test") # 창 제목
root.geometry("640x480")

values = [str(x) + "일" for x in range(1, 32)] # 1 ~ 31
combobox = ttk.Combobox(root, height=5, values= values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정(초기값 설정도 가능)

readonly_combobox = ttk.Combobox(root, height=10, values= values, state="readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 선택 
readonly_combobox.pack()


def btncmd(): 
    print(combobox.get())

btn =  Button(root, text="선택", command=btncmd) # 버튼에 동작 삽입
btn.pack()


root.mainloop() # 창이 닫히지 않도록 하는 역할
