from tkinter import *

root = Tk()

root.title("Python GUI Test") # 창 제목
root.geometry("640x480")

# selectmode : extended(중복 선택) single(하나만 선택)
# height : 0이면 전부 표시, 숫자면 해당 인덱스까지만
listbox = Listbox(root, selectmode="extended", height=0) 
# insert : index와 내용 지정하여 추가, END의 경우 가장 끝에 추가
listbox.insert(0, "Apple")
listbox.insert(1, "Strawberry")
listbox.insert(2, "Banana")
listbox.insert(END, "Watermelon")
listbox.insert(END, "Grape")
listbox.pack()

def btncmd(): 
    # 삭제
    # listbox.delete(END) # 가장 마지막 항목 삭제
    # listbox.delete(0) # 가장 앞 항목 삭제

    # 갯수 확인
    # print("리스트에는 ", listbox.size(), "개가 있어요.")

    # 항목 확인 : listbox.get(시작 인덱스, 끝 인덱스)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 : index 반환 
    print("선택된 항목 : ", listbox.curselection())

btn =  Button(root, text="Run", command=btncmd) # 버튼에 동작 삽입
btn.pack()


root.mainloop() # 창이 닫히지 않도록 하는 역할
