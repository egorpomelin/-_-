from tkinter import *
import sqlite3

with sqlite3.connect('галерея.db') as db:
    cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS художник(художник_id integer PRIMARY KEY, имя_художника text NOT NULL, адрес text NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS картина(id_картины integer PRIMARY KEY, имя_художника text NOT NULL, название text NOT NULL, цена integer NOT NULL)''')

cursor.execute('''SELECT художник.художник_id, художник.имя_художника, художник.адрес FROM художник, картина WHERE художник.имя_художника=картина.имя_художника''')


def cler(a):
    a.delete(0, END)


def VivodHud():
    cler2()

    frame2 = Frame(relief=RAISED)
    frame2.place(x = 0, y = 100, width=800, height= 900)

    Label1 = Label(text='ID художника')
    Label1.place(x =50, y = 100, width= 100, height= 25)

    Label2 = Label(text='ФИО')
    Label2.place(x =300, y = 100, width= 100, height= 25)

    Label3 = Label(text='адрес')
    Label3.place(x =550, y = 100, width= 100, height= 25)



    mesege = Listbox()
    mesege.place(x = 50, y = 125, width=250, height=800)

    mesege1 = Listbox()
    mesege1.place(x = 300, y = 125, width=250, height=800)

    mesege2 = Listbox()
    mesege2.place(x = 550, y = 125, width=250, height=800)


    cursor.execute('SELECT * FROM художник')
    vs = cursor.fetchall()
    # ID = 'ID художника'
    # Name = 'ФИО'
    # adres = 'адрес'
    # prob = '                     '
    # mesege.insert(END,(ID, prob, Name, prob, adres))
    b =1
    for i in vs:
        mesege.insert(END,(b, '.', i[0]))
        mesege1.insert(END,(b, '.', i[1]))
        mesege2.insert(END,(b, '.', i[2]))
        b += 1


def VivodKart():
    cler2()

    frame2 = Frame(relief=RAISED)
    frame2.place(x = 0, y = 100, width=800, height= 900)

    Label1 = Label(text='ID картины')
    Label1.place(x =50, y = 100, width= 100, height= 25)

    Label2 = Label(text='имя художника')
    Label2.place(x =150, y = 100, width= 100, height= 25)

    Label3 = Label(text='название картины')
    Label3.place(x =350, y = 100, width= 100, height= 25)

    Label4 = Label(text='цена')
    Label4.place(x =550, y = 100, width= 100, height= 25)

    mesege = Listbox()
    mesege.place(x = 50, y = 125, width=100, height=800)

    mesege1 = Listbox()
    mesege1.place(x = 150, y = 125, width=200, height=800)

    mesege2 = Listbox()
    mesege2.place(x = 350, y = 125, width=200, height=800)

    mesege3 = Listbox()
    mesege3.place(x = 550, y = 125, width=250, height=800)

    cursor.execute('SELECT * FROM картина')
    vs = cursor.fetchall()
    # ID = 'ID художника'
    # Name = 'ФИО'
    # adres = 'адрес'
    # prob = '                     '
    # mesege.insert(END,(ID, prob, Name, prob, adres))
    b =1
    for i in vs:
        mesege.insert(END,(b, '.',i[0]))
        mesege1.insert(END,(b, '.',i[1]))
        mesege2.insert(END,(b, '.',i[2]))
        mesege3.insert(END,(b, '.', i[3]))
        b += 1

def DabHud():
    # cler(frame)

    def DabHud1():
        idd = ID.get()
        name = Name.get()
        price = Price.get()
        cursor.execute('''INSERT INTO художник(художник_id, имя_художника, адрес) VALUES(?, ?, ?)''', (idd, name, price))
        db.commit()
        cler(ID)
        cler(Name)
        cler(Price)

    cler1()
    
    frame = Frame(relief=RAISED)
    frame.place(x = 800, y = 100, width=790, height= 900)

    Label1 = Label(master= frame, text='ID')
    Label1.place(x =50, y = 0, width= 100, height= 25)
    

    ID = Entry(master= frame, text='')
    ID.place(x =50, y = 25, width= 300, height= 25)
    

    Label2 = Label(master= frame, text='ФИО')
    Label2.place(x =50, y = 50, width= 50, height= 25)
    
    Name = Entry(master= frame, text='')
    Name.place(x = 50, y = 75, width= 300, height= 25)
    

    Label3 = Label(master= frame, text='адрес')
    Label3.place(x =50, y = 100, width= 50, height= 25)
    
    Price = Entry(master= frame, text='')
    Price.place(x =50, y = 125, width= 300, height= 25)
    

    DabButton = Button(master= frame, text='добавить', command=DabHud1, relief=RAISED)
    DabButton.place(x = 50, y = 160, width=300, height=25 )
    
    DabButton['bg'] = 'green'

    


def DabKart():
    # cler(frame)
    def DabKart1():
        idd = IDx.get()
        name = Namex.get()
        name2 = Name2x.get()
        price = Pricex.get()
        cursor.execute('''INSERT INTO картина(id_картины, имя_художника, название, цена) VALUES(?, ?, ?, ?)''', (idd, name, name2, price))
        db.commit()
        cler(IDx)
        cler(Namex)
        cler(Name2x)
        cler(Pricex)
    
    cler1()
    
    frame = Frame(relief=RAISED)
    frame.place(x = 800, y = 100, width=790, height= 900)

    Label1 = Label(master= frame, text='ID картины')
    Label1.place(x =50, y = 0, width= 100, height= 25)

    IDx = Entry(master= frame, text='')
    IDx.place(x =50, y = 25, width= 300, height= 25)

    Label2 = Label(master= frame, text='ФИО художника')
    Label2.place(x =50, y = 50, width= 100, height= 25)
    Namex = Entry(master= frame, text='')
    Namex.place(x = 50, y = 75, width= 300, height= 25)

    Label3 = Label(master= frame, text='название картины')
    Label3.place(x =50, y = 100, width= 100, height= 25)
    Name2x = Entry(master= frame, text='')
    Name2x.place(x = 50, y = 125, width= 300, height= 25)

    Label4 = Label(master= frame, text='цена')
    Label4.place(x =50, y = 150, width= 50, height= 25)
    Pricex = Entry(master= frame, text='')
    Pricex.place(x = 50, y = 175, width= 300, height= 25)

    DabButton = Button(master= frame, text='добавить', command=DabKart1)
    DabButton.place(x = 50, y = 210, width=300, height=25 )
    DabButton['bg'] = 'green'


def DeletKart():
    cler1()

    def DeletKart1():
        file = open('проданные.txt', 'a')
        dele= IDx.get()
        cursor.execute('''SELECT * FROM картина WHERE название= ?''', [dele])
        vs = cursor.fetchall()
        for i in vs:
            nev = str(i) + '\n'
            file.write(nev)
        file.close()
        cursor.execute('DELETE FROM картина WHERE название= ?', [dele])
        db.commit()
        cler(IDx)

    frame = Frame(relief=RAISED)
    frame.place(x = 800, y = 100, width=790, height= 900)

    Label0 = Label(master= frame, text='название картины')
    Label0.place(x =50, y = 0, width= 100, height= 25)

    IDx = Entry(master= frame, text='')
    IDx.place(x =50, y = 25, width= 300, height= 25)

    DabButton = Button(master= frame, text='удалить', command=DeletKart1)
    DabButton.place(x = 50, y = 60, width=300, height=25 )
    DabButton['bg'] = 'green'

def Delethud():
    cler1()

    def DeletHud1():
        dele= IDx.get()
        cursor.execute('DELETE FROM художник WHERE имя_художника = ?', [dele])
        db.commit()
        cler(IDx)

    frame = Frame(relief=RAISED)
    frame.place(x = 800, y = 100, width=790, height= 900)

    Label0 = Label(master= frame, text='имя художника')
    Label0.place(x =50, y = 0, width= 100, height= 25)

    IDx = Entry(master= frame, text='')
    IDx.place(x =50, y = 25, width= 300, height= 25)

    DabButton = Button(master= frame, text='удалить', command=DeletHud1)
    DabButton.place(x = 50, y = 60, width=300, height=25 )
    DabButton['bg'] = 'green'

def PoiskHud():

    cler2()

    frame2 = Frame(relief=RAISED)
    frame2.place(x = 0, y = 100, width=800, height= 900)

    Label1 = Label(text='ID картины')
    Label1.place(x =50, y = 100, width= 100, height= 25)

    Label2 = Label(text='ФИО художника')
    Label2.place(x =150, y = 100, width= 100, height= 25)

    Label3 = Label(text='название картины')
    Label3.place(x =350, y = 100, width= 100, height= 25)

    Label4 = Label(text='цена')
    Label4.place(x =550, y = 100, width= 100, height= 25)

    mesege = Listbox()
    mesege.place(x = 50, y = 125, width=100, height=800)

    mesege1 = Listbox()
    mesege1.place(x = 150, y = 125, width=200, height=800)

    mesege2 = Listbox()
    mesege2.place(x = 350, y = 125, width=200, height=800)

    mesege3 = Listbox()
    mesege3.place(x = 550, y = 125, width=250, height=800)

    hud = Poisk.get()
    cursor.execute('''SELECT * FROM картина WHERE имя_художника =?''', [hud])
    # cursor.execute('''SELECT * FROM художник WHERE имя= ?''', [hud])

    vs = cursor.fetchall()
    b =1
    for i in vs:
        mesege.insert(END,(b, '.',i[0]))
        mesege1.insert(END,(b, '.',i[1]))
        mesege2.insert(END,(b, '.',i[2]))
        mesege3.insert(END,(b, '.', i[3]))
        b += 1
    
    cler(Poisk)

def PoiskName():
    cler2()

    frame2 = Frame(relief=RAISED)
    frame2.place(x = 0, y = 100, width=800, height= 900)

    Label1 = Label(text='ID картины')
    Label1.place(x =50, y = 100, width= 100, height= 25)

    Label2 = Label(text='ФИО художника')
    Label2.place(x =150, y = 100, width= 100, height= 25)

    Label3 = Label(text='название картины')
    Label3.place(x =350, y = 100, width= 100, height= 25)

    Label4 = Label(text='цена')
    Label4.place(x =550, y = 100, width= 100, height= 25)

    mesege = Listbox()
    mesege.place(x = 50, y = 125, width=100, height=800)

    mesege1 = Listbox()
    mesege1.place(x = 150, y = 125, width=200, height=800)

    mesege2 = Listbox()
    mesege2.place(x = 350, y = 125, width=200, height=800)

    mesege3 = Listbox()
    mesege3.place(x = 550, y = 125, width=250, height=800)

    hud = Poisk.get()
    cursor.execute('''SELECT * FROM картина WHERE название= ?''', [hud])
    vs = cursor.fetchall()
    b =1
    for i in vs:
        mesege.insert(END,(b, '.',i[0]))
        mesege1.insert(END,(b, '.',i[1]))
        mesege2.insert(END,(b, '.',i[2]))
        mesege3.insert(END,(b, '.', i[3]))
        b += 1
    
    cler(Poisk)

def cler1():
    frame.destroy()

def cler2():
    frame2.destroy()

#графический интерфейс

windoow = Tk()
windoow.title('галерея')
windoow.geometry('1600x800')

MenuButton1 = Button(text='добавить художника', command=DabHud, relief= GROOVE)
MenuButton1.place(x = 50, y = 30, width=130, height=25 )
MenuButton1['bg'] = 'green'

MenuButton2 = Button(text='добавить картину', command=DabKart, relief= RIDGE)
MenuButton2.place(x = 190, y = 30, width=130, height=25 )
MenuButton2['bg'] = 'green'

MenuButton3 = Button(text='удалить художника', command=Delethud)
MenuButton3.place(x = 330, y = 30, width=130, height=25 )
MenuButton3['bg'] = 'green'

MenuButton4 = Button(text='удалить картину', command=DeletKart)
MenuButton4.place(x = 470, y = 30, width=130, height=25 )
MenuButton4['bg'] = 'green'

MenuButton5 = Button(text='все художники', command=VivodHud)
MenuButton5.place(x = 610, y = 30, width=130, height=25 )
MenuButton5['bg'] = 'green'

MenuButton6 = Button(text='все картины', command=VivodKart)
MenuButton6.place(x = 750, y = 30, width=130, height=25 )
MenuButton6['bg'] = 'green'

Poisk = Entry(text='')
Poisk.place(x = 50, y = 70, width= 300, height= 25)

PoiskButton = Button(text='поиск по художнику', command=PoiskHud)
PoiskButton.place(x = 360, y = 70, width=150, height=25 )
PoiskButton['bg'] = 'green'

PoiskButton2 = Button(text='поиск по названию', command=PoiskName)
PoiskButton2.place(x = 520, y = 70, width=150, height=25 )
PoiskButton2['bg'] = 'green'

frame2 = Frame(relief=RAISED)
frame2.place(x = 0, y = 100, width=800, height= 900)


frame = Frame(relief=RAISED)
frame.place(x = 800, y = 100, width=790, height= 900)
    



windoow.mainloop()
db.close()