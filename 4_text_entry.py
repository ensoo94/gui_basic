from tkinter import *

root = Tk()

root.title("Python GUI Test") # 창 제목
root.geometry("440x280")

txt = Text(root, width=30, height=5) # Textarea 생성
txt.pack()

txt.insert(END, "글자를 입력하세요") # Placeholder

e = Entry(root, width=30) # Text와 차이점 : 줄바꿈 불가능!
e.pack()
e.insert(0, "한 줄만 입력하세용!") # 0 대신 END 입력해도 같음. Placeholder

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # Line 1, Column 0부터 txt의 값을 가져온다
    print(e.get()) # entry는 get만 해주면 됨!!

    # 내용 삭제
    txt.delete("1.0", END) # 내용 모두 삭제
    e.delete(0, END) # 0부터 끝까지 삭제

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록 하는 역할

