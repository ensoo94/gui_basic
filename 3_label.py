from tkinter import *

root = Tk()
root.title("Python GUI Test") # 창 제목
root.geometry("400x200")

label1 = Label(root, text="안녕하세요") # 동작 없이 내용만 가지고 있음
label1.pack()

photo = PhotoImage(file="btn_img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요") # 속성 바꿔주는 함수
    global photo2 # 전역변수로 선언 : 하지 않으면 garbage 처리되어 사라짐
    photo2 = PhotoImage(file="min_banner.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop() # 창이 닫히지 않도록 하는 역할

