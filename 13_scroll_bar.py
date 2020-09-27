from tkinter import *

root = Tk()

root.title("Python GUI Test") # 창 제목
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32): # 1 ~ 31일
    listbox.insert(END, str(i) + "일")

listbox.pack(side="left")

# listbox와 scrollbar 서로 맵핑
scrollbar.config(command=listbox.yview)

root.mainloop() # 창이 닫히지 않도록 하는 역할
