# -*- coding: utf-8 -*-
"""
Created on Wed May 24 18:16:44 2023

@author: Колецкий Д.К.
"""
import tkinter as tk
from tkinter import ttk
from math import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os
from tkinter import messagebox


# Создаем новый объект Tk
root = tk.Tk()

# Задаем заголовок окна
root.title("Калькулятор химика - технолога.")

# Установим размер окна
root.geometry("1000x500")

# Получим ширину и высоту экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Вычисляем координаты окна приложения
window_width = 500
window_height = 500
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Добавим всплывающее окно 1
def click():
    window1 = tk.Tk()
    window1.title("Рассчет реакции")
    window1.geometry("1000x500")
    
# Настроим всплывающее окно 1
    screen_width = window1.winfo_screenwidth()
    screen_height = window1.winfo_screenheight()
    window_width = 500
    window_height = 500
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window1.geometry(f"{window_width}x{window_height}+{x}+{y}")
    window1.attributes("-topmost",True)
    
# Добавим всплывающее окно 2

    def click2():
        window2 = tk.Tk()
        window2.title("Информация по производству")
        window2.geometry("800x300")
        screen_width = window2.winfo_screenwidth()
        screen_height = window2.winfo_screenheight()
        window_width = 300
        window_height = 300
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        window2.geometry(f"{window_width}x{window_height}+{x}+{y}")
        window2.attributes("-topmost",True)
        
# #Добавим вводные данные
        label21=tk.Label(window2, text="Рассчет сделан с условием выхода реакции 95%.")
        label21.pack()
        label22=tk.Label(window2, text=" и получением серной кислоты с концентрацией 98%.")
        label22.pack()
        
# Добавим всплывающее окно 3
    def click3():
        window3 = tk.Tk()
        window3.title("Рассчет загрузки")
        window3.geometry("800x300")
        screen_width = window3.winfo_screenwidth()
        screen_height = window3.winfo_screenheight()
        window_width = 500
        window_height = 500
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        window3.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
# Добавляем поля ввоода в окно рассчета загрузки
        frame = tk.Frame(window3)
        frame.pack(expand=True)

        label31 = tk.Label(frame, text="Cколько продукта нужно получить(кг):")
        label31.grid(row=0, column=0)

        entry31 = tk.Entry(frame)
        entry31.grid(row=0, column=1)
        
        
 # Добавляем калькулятор рассчета по введенному значению       
        def calculate_a(): 
           kg = int(entry31.get())
           a = 0.342857*kg
           a = round(a, 0)
           if a > 0:
               messagebox.showinfo('Загрузка серы', f'S(кг)= {a} ')
        def calculate_b():
           kg = int(entry31.get()) 
           b = 0.196793*kg
           b = round(b, 0)
           if b > 0:
               messagebox.showinfo('Загрузка воды', f'H2O(кг) = {b} ')
        def calculate_c():
           kg = int(entry31.get())
           c = 2.219388*kg
           c = round(c, 0)
           if c > 0:
               messagebox.showinfo('Загрузка воздуха', f'Воздух(кг) = {c} ')
# Кнопка запуска рассчета
        button31 = tk.Button(frame, text="Рассчитать СЕРУ", command=calculate_a)
        button31.grid(row=2, column=1)
        button32 = tk.Button(frame, text="Рассчитать ВОДУ", command=calculate_b)
        button32.grid(row=3, column=1)
        button33 = tk.Button(frame, text="Рассчитать ВОЗДУХ", command=calculate_c)
        button33.grid(row=4, column=1)
                      
        window3.update_idletasks()
        width = window3.winfo_width()
        height = window3.winfo_height()
        x = (window3.winfo_screenwidth() // 2) - (width // 2)
        y = (window3.winfo_screenheight() // 2) - (height // 2)
        window3.geometry('{}x{}+{}+{}'.format(width, height, x, y))
                    
# Добавим надписи во всплывающем окне 1
    label2=ttk.Label(window1, text="Химическая  схема.")
    label3=ttk.Label(window1, text="S2+2O2=2SO2")
    label4=ttk.Label(window1, text="SO2+0,5О2=SO3")
    label5=ttk.Label(window1, text="SO3+H2O= H2SO4")
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()
    button2 = ttk.Button(window1, text="Информация по производству", command=click2)
    button2.pack()
    funcA2 = click3
    funcB2 = window1.destroy
    button3 = ttk.Button(window1, text="Рассчитать загрузку", command=lambda:[funcA2(),funcB2()])
    button3.pack()
    

# Добавим кнопку и привяжем к ней функцию вызова всплывающего окна
label1 = tk.Label(root, text="Выберете производство.")
label1.pack()
funcA = click
funcB = root.destroy

button1 = tk.Button(root, text="СЕРНАЯ КИСЛОТА", command=lambda:[funcA(),funcB()])
button1.pack()
root.attributes("-topmost",True)

# Запускаем основной цикл
root.mainloop()


