import os # 파일 열기
from tkinter import *

root = Tk()

root.title("제목 없음 - Windows 메모장") # 창 제목
root.geometry("640x480")

# 열기, 저장 
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장

menu = Menu(root) 

# File 메뉴
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file) 
menu_file.add_command(label="끝내기", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)

# 메뉴 (빈 값)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 입력창
txt = Text(root, yscrollcommand=scrollbar.set) # Textarea 생성
txt.pack(fill="both", expand=True) # 꽉 찬 입력창 생성

# 스크롤바와 입력창 맵핑
scrollbar.config(command=txt.yview)


root.config(menu = menu) 
root.mainloop() # 창이 닫히지 않도록 하는 역할