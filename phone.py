import numpy as np
import pandas as pd
from tkinter import *
from tkinter import scrolledtext

df = pd.DataFrame(columns =['Name','Telephone','Note'])

#очистка полей ввода
def del_field():
    txt.delete(0,END)
    txt1.delete(0,END)
    txt2.delete(0,END)
#Запись в csv файл и в Датафрейм поля
def write():
    t_book.delete(1.0, END)
    data_list = [txt.get(),txt1.get(),txt2.get()]
    #DataFrame
    df2 = pd.DataFrame([data_list],columns = ['Name','Telephone','Note'])
    print(df2)
    df = pd.read_csv(r'tel.csv')
    print(df)
    df = df.append(df2,ignore_index = True)
    # Возможность использовать русские буквы в csv
    #df.to_csv(r'tel.csv',header = ['Name','Telephone','Note'], index = False,mode='w',encoding = 'cp1251')
    #df.to_csv('file.csv',encoding='utf-8-sig')
    df.to_csv(r'tel.csv', header = False,index = False,mode='a')
    print(df)
    t_book.insert(INSERT,df) 
    del_field()
# Очистка экрана GUI и создание пустого датафрейма с столбцами
def clear():
    t_book.delete(1.0, END)
    df = pd.DataFrame(columns =['Name','Telephone','Note'])
    df.to_csv(r'tel.csv',header = ['Name','Telephone','Note'],sep =',',  mode='w',index = False)
   
#Work with Tkinter GUI 
window = Tk()  
window.title('Телефонная книга абонентов')
window.geometry('550x250')
#Текстовые надписи
text1 = Label(window, text="Имя абонента", font=("Arial", 10))
text1.grid(column=0, row=0)

text2 = Label(window,text = "Контактный телефон", font=("Arial", 10))
text2.grid(column = 1, row =0)

text3 = Label(window,text = "Примечание", font=("Arial", 10))
text3.grid(column = 2, row =0)
#Поле ввода текста
txt = Entry(window,width=15)  
txt.grid(column=0, row=1)
txt.focus()

txt1 = Entry(window,width=15)  
txt1.grid(column=1, row=1)

txt2 = Entry(window,width=15)  
txt2.grid(column=2, row=1)
#Кнопка запись
btn_r = Button(window, text="Записать!",command =lambda: write())  
btn_r.grid(column=2, row=3)
#Кнопка для очистки датафрейма
btn_c = Button(window, text="Очистить!",command =lambda: clear())  
btn_c.grid(column=2, row=5)
#Большое текстовое поле
t_book = scrolledtext.ScrolledText(window,width = 40,height = 2)
t_book.grid(column = 1, row = 5)

window.mainloop()

