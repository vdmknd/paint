from tkinter import *
from tkinter import colorchooser
from random import *

WIDTH = 700
HEIGHT = 700
window = Tk()
window.config(width=WIDTH,height=HEIGHT)

spray = PhotoImage(file='spray.png')
pen = PhotoImage(file='pen.png')
pencil = PhotoImage(file='pencil.png')
bucket = PhotoImage(file='bucket.png')
rubber = PhotoImage(file='rubber.png')
gradient = PhotoImage(file='gradient.png')

tools = {'pen':0,'pencil':0,'spray':0,'line':0,'bg':0,'clear_all':0,'rubber':0,'gradient':0}
colors = ['white','black','yellow','green','red','pink','blue','orange','brown','gray']
print(tools)

color = 'black'
bgcolor = 'white'
current_tool = ''

def mouse_draw(event):
    global tools,current_tool,color,bgcolor
    x = event.x-1
    y = event.y-1
    if current_tool=='pen':
        Graphic.create_oval(x,y,x+5,y+5,fill=color,outline=color)
    elif current_tool=='pencil':
        Graphic.create_oval(x,y,x+2,y+2,fill=color,outline=color)
    elif current_tool=='spray':
        Graphic.create_oval(x,y,x+1,y+1,fill=color,outline=color)
        for i in range(3):
            Graphic.create_oval(x,y,x+randint(-10,10),y+randint(-10,10),fill=color,outline=color)
    elif current_tool=='bg':
        Graphic["bg"] = color
        bgcolor = color
    elif current_tool=='rubber':
        Graphic.create_oval(x,y,x+20,y+20,fill=bgcolor,outline=bgcolor)
        
def choose_color():
    global color
    color = colorchooser.askcolor()[1]
    btn_color = Label(window,text=' ',bg=color)
    btn_color.place(width=100,height=100,x=0,y=600)

def change_tools(a):
    global tools, current_tool
    for i in tools:
        tools[i] = 0
    tools[a] = 1
    current_tool = a
    
Graphic = Canvas(window,width=WIDTH,height=HEIGHT,bg='white')
Graphic.bind("<B1-Motion>",mouse_draw)
Graphic.pack()

pen1 = Button(window,text='pen',image=pen,command=lambda:change_tools('pen'))
pen1.place(width=100,height=100,x=0,y=100)
pencil1 = Button(window,text='pencil',image=pencil,command=lambda:change_tools('pencil'))
pencil1.place(width=100,height=100,x=0,y=200)
spray1= Button(window,text='spray',image=spray,command=lambda:change_tools('spray'))
spray1.place(width=100,height=100,x=0,y=300)
paint_bg = Button(window,text='bg',image=bucket,command=lambda:change_tools('bg'))
paint_bg.place(width=100,height=100,x=0,y=400)
rubber1 = Button(window,text='rubber',image=rubber,command=lambda:change_tools('rubber'))
rubber1.place(width=100,height=100,x=0,y=500)
gradient1 = Button(window,text=' ',image=gradient,command=choose_color)
gradient1.place(width=100,height=100,x=0,y=0)

window.mainloop()