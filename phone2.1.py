import numpy as np
import pandas as pd
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton

df = pd.DataFrame(columns =['Group','Name','Telephone','Note'])
# Запись пустого Датафрейма в файл.Использовать 1 раз
#остальную часть закомментить
#df.to_csv(r'abonents.csv',header = ['Group','Name','Telephone','Note'],sep =',',  mode='w',index = False)
##print(df)

#очистка полей ввода
def del_field():
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)  

#Запись в csv файл и в Датафрейм поля
def write():
    #Очистка текстового поля 
    t_book.delete(1.0, END)
    #Список из полученных при вводе данных
    data_list = [combo.get(),txt1.get(),txt2.get(),txt3.get()]
    #DataFrame, добавляемый к исходному
    df2 = pd.DataFrame([data_list],columns = ['Group','Name','Telephone','Note'])
    #Чтение датафрейма из файла и добавление к нему введенных данных
    df = pd.read_csv(r'abonents.csv',dtype = str)
    df = df.append(df2,ignore_index = True)
    #Запись всего в csv файл и очистка полей
    df.to_csv(r'abonents.csv',header = ['Group','Name','Telephone','Note'], index = False,mode='w')
    t_book.insert(INSERT,df)
    del_field()

# Очистка экрана GUI и создание пустого датафрейма с столбцами
def clear():
    #Проверка Чекбокса на необходимость удаления всех данных
    if chk_state.get() == False:
        t_book.delete(1.0, END)
    elif chk_state.get() == True:
        t_book.delete(1.0, END)
        df = pd.DataFrame(columns =['Group','Name','Telephone','Note'])
        df.to_csv(r'abonents.csv',header = ['Group','Name','Telephone','Note'],sep =',',  mode='w',index = False)

#Поиск значений по датафрейму
def find():
   #Очистка текстового поля
    t_book.delete(1.0, END)
    #Чтение датафрейма из файла
    df = pd.read_csv(r'abonents.csv',dtype = str)
    #index -> номер столбца для поиска
    index = selected.get()
    #pd.Series,содержащая выбранный столбец
    find_series = df.iloc[:,index]
    #Условие для отбора строк в датафрейме,содержащий введенный текст
    find_condition = find_series.str.contains(txt_find.get(),regex = False,na = False)
    #Датафрейм с результатом поиска и вставка его в поле ввода
    find_res = df[find_condition]
    t_book.insert(INSERT,find_res)
   

#Work with Tkinter GUI 
window = Tk()  
window.title('Телефонная книга абонентов')
window.geometry('550x250')

#Список категории абонента
combo = Combobox(window)
combo['values'] = ("Family", "Friends", "Colleagues", "Relatives", "Classmates", "Others")
combo.current(1)    #Текущее значение "Friends"
combo.grid(column=0, row=1)

#Текстовые надписи
text = Label(window,text="Группа абонента", font=("Arial", 10)) 
text.grid(column=0, row=0)

text1 = Label(window, text="Имя абонента", font=("Arial", 10))
text1.grid(column=1, row=0)

text2 = Label(window,text = "Контактный телефон", font=("Arial", 10))
text2.grid(column = 2, row =0)

text3 = Label(window,text = "Примечание", font=("Arial", 10))
text3.grid(column = 3, row =0)

#Поле ввода текста
txt1 = Entry(window,width=15)  
txt1.grid(column=1, row=1)
txt1.focus()

txt2 = Entry(window,width=15)  
txt2.grid(column=2, row=1)

txt3 = Entry(window,width=15)  
txt3.grid(column=3, row=1)

#Кнопка запись
btn_r = Button(window, text="Записать!",command =lambda: write())  
btn_r.grid(column=2, row=3)
#Кнопка для очистки датафрейма
btn_c = Button(window, text="Очистить!",command =lambda: clear())  
btn_c.grid(column=2, row=4)

#Чекбокс
chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(window,text = 'Удалить всю\n книгу',var = chk_state)
chk.grid(column=3, row=3)

#Большое текстовое поле
t_book = scrolledtext.ScrolledText(window,width = 35,height = 5)
t_book.grid(column = 0, row = 4,columnspan = 2,rowspan = 2)

#Кнопка Найти
but_f = Button(window,text = 'Искать',command=find)
but_f.grid(column = 2, row = 8)

#Текстовое поле для кнопки Найти
txt_find = Entry(window,width =20)
txt_find.grid(column = 0,row = 8)

#Радиокнопки
selected = IntVar()
point1 = Radiobutton(window,text='Имя', value=1, variable=selected)  
point2 = Radiobutton(window,text='Номер телефона', value=2, variable=selected)  
point3 = Radiobutton(window,text='Примечание', value=3, variable=selected)

point1.grid(column = 0,row = 9)
point1.focus()
point2.grid(column = 1,row = 9)
point3.grid(column = 2,row = 9)

window.mainloop()

