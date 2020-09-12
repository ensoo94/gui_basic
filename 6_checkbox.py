from tkinter import *

root = Tk()

root.title("Python GUI Test") # 창 제목
root.geometry("640x480")

chkvar = IntVar() #chkvar에 int형으로 값을 저장한다
chkbox =  Checkbutton(root, text = "오늘 하루 보지 않기", variable = chkvar)
#chkbox.select() # 자동 선택 처리
#chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable = chkvar2)
chkbox2.pack()

def btncmd(): 
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn =  Button(root, text="Run", command=btncmd) # 버튼에 동작 삽입
btn.pack()


root.mainloop() # 창이 닫히지 않도록 하는 역할
