from tkinter import *

root = Tk()

root.title("Python GUI Test") # 창 제목
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar() # int형으로 값을 저장한다
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable = burger_var)
btn_burger1.select() # default 선택 
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable = burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable = burger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar() # String형으로 값을 저장한다
btn_drint1 = Radiobutton(root, text="콜라", value="콜라", variable = drink_var)
btn_drint1.select()
btn_drint2 = Radiobutton(root, text="사이다", value="사이다", variable = drink_var)
btn_drint3 = Radiobutton(root, text="쥬스", value="쥬스", variable = drink_var)
btn_drint1.pack()
btn_drint2.pack()
btn_drint3.pack()


def btncmd(): 
    print(burger_var.get()) # 선택된 라디오 항목의 값(value)
    print(drink_var.get())

btn =  Button(root, text="주문", command=btncmd) # 버튼에 동작 삽입
btn.pack()


root.mainloop() # 창이 닫히지 않도록 하는 역할
