from tkinter import *

root = Tk()
root.title("Python GUI Test") # 창 제목
root.geometry("400x250")

btn1 = Button(root, text="버튼1") # 버튼 내용 지정
btn1.pack() # 버튼 표출 : 프로그램에 포함시키는 역할

btn2 = Button(root, padx=5, pady=10, text="버튼2") # padx = 버튼 가로, pady = 버튼 세로 여백 설정(text에 크기 영향 받음)
btn2.pack()

btn3 = Button(root, width=10, height=3, text="버튼3") # width = 버튼 가로, height = 버튼 세로 크기 설정(text 영향 없음)
btn3.pack()

btn4 = Button(root, fg="red", bg="yellow", text="버튼4") # fg = 폰트 색, bg = 배경 색
btn4.pack()

photo = PhotoImage(file="btn_img.png") # 사진 불러오기
btn5 = Button(root, image=photo) # 이미지를 이용한 버튼
btn5.pack()

def btncmd(): # 버튼 클릭시 실행
    print("버튼이 클릭되었어요.")

btn6 =  Button(root, text="Run", command=btncmd) # 버튼에 동작 삽입
btn6.pack()

root.mainloop() # 창이 닫히지 않도록 하는 역할

