from tkinter import *
from PIL import Image,ImageTk
from functools import partial
from tkinter import messagebox
import datetime 
import time

def open1():
    name1=[]
    price1=[]
    def btn_clicked():
        for widgets in root1.winfo_children():
          widgets.destroy()
    def bill(name,price,name0):
        
        bill = Tk()
        bill.title("srikart")
        bill.geometry("550x500")
        bill.configure(bg = "#4799E9")
        s=sum(price)
        a0=Label(bill,text="STAR WATCH",font=(50),bg = "#4799E9")
        a0.place(x=180,y=0)
        a2=Label(bill,text="WATCH NAME",font=(50),bg = "#4799E9")
        a2.place(x=9,y=55)
        a4=Label(bill,text="PRICE",font=(50),bg="#4799E9")
        a4.place(x=400,y=55)
        q=9
        w=55+30
        for i in name:
            a=Label(bill,text=i,font=(50),bg = "#4799E9")
            a.place(x=q,y=w)
            w=w+30
        v=55+30
        for p in price:
            b=Label(bill,text="Rs."+str(p),font=(50),bg = "#4799E9")
            b.place(x=400,y=v)
            v=v+30
        a40=Label(bill,text="-"*70,font=(50),bg="#4799E9")
        a40.place(x=9,y=v)
        a4=Label(bill,text="TOTAL PRICE",font=(50),bg = "#4799E9")
        a4.place(x=q,y=v+20)
        a4=Label(bill,text="Rs."+str(s),font=(50),bg = "#4799E9")
        a4.place(x=400,y=v+20)
        a4=Label(bill,text="Delivery      : Tomorrow,",font=(50),bg = "#4799E9")
        a4.place(x=q,y=w+55)
        a5=Label(bill,text=tomorrow,font=(50),bg = "#4799E9")
        a5.place(x=230,y=v+55)
        a6=Label(bill,text="HEY "+str(name0)+"!",font=(50),bg = "#4799E9")
        a6.place(x=q,y=w+90)
        a7=Label(bill,text="THANKS FOR SHOPPING WITH US!" ,font=(50),bg = "#4799E9")
        a7.place(x=q+60,y=w+130)




        
        '''a1=Label(bill,text=name,font=(50),bg = "#4799E9")
        a1.place(x=130,y=55)
        a4=Label(bill,text="Price           :",font=(50),bg="#4799E9")
        a4.place(x=9,y=80)
        a3=Label(bill,text="Rs."+str(price),font=(50),bg = "#4799E9")
        a3.place(x=130,y=80)
        a4=Label(bill,text="Delivery      : Tomorrow,",font=(50),bg = "#4799E9")
        a4.place(x=10,y=107)
        a5=Label(bill,text=tomorrow,font=(50),bg = "#4799E9")
        a5.place(x=235,y=107)
        a6=Label(bill,text="Customer name  :",font=(50),bg = "#4799E9")
        a6.place(x=9,y=135)
        a7=Label(bill,text=name1,font=(50),bg = "#4799E9")
        a7.place(x=180,y=135)'''
    def ask(name,price):
        print(price)
        a=messagebox.askyesno("Confirm","Are you sure to buy?")
        
        if a is True:
            root.destroy()
            def printInput():
                inp1 = e3.get(1.0, "end-1c")
                inp2 = e2.get(1.0, "end-1c")
                inp3 = e1.get(1.0, "end-1c")
                inp4 = e4.get(1.0, "end-1c")
        
                print(inp1)  
                print(inp2)
                print(inp3)
                print(inp4)
                inp0=inp1+".txt"
                q=open(inp0,"a+")
                q.write("Name: "+inp1+"\n")
                q.write("Email id: "+inp2+"\n")
                q.write("Phone no: "+inp3+"\n")
                q.write("Address: "+inp4+"\n")
                q.write("Watches: ")
                for x in name:
                    q.write(x)
                q.write("\n"+"Date: "+today1)
                    
                q.close()

                bill(name,price,inp1)
        

            window = Tk()

            window.geometry("1280x720")
            window.configure(bg = "#FFFFFF")
            canvas = Canvas(
                window,
                bg = "#FFFFFF",
                height = 720,
                width = 1280,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
            canvas.place(x = 0, y = 0)

            background_img = PhotoImage(file = f"background.png")
            background = canvas.create_image(
                675.5, 480.5,
                image=background_img)




            e1=Text(window,height=3,width=50)
            e1.place(x=825,y=374)

            e2=Text(window,height=3,width=50)
            e2.place(x=825,y=230)

            e3=Text(window,height=3,width=50)
            e3.place(x=825,y=90)

            e4=Text(window,height=5,width=50)
            e4.place(x=825,y=500)

            canvas.create_text(
                876.5, 61.5,
                text = "Name:",
                fill = "#000000",
                font = ("None", int(24.0)))

            canvas.create_text(
                888.5, 478.0,
                text = "Address:",
                fill = "#000000",
                font = ("None", int(24.0)))

            canvas.create_text(
                925.0, 344.5,
                text = "Phone Number:",
                fill = "#000000",
                font = ("None", int(24.0)))

            canvas.create_text(
                877.5, 205.0,
                text = "E-mail:",
                fill = "#000000",
                font = ("None", int(24.0)))

            img0 = PhotoImage(file = f"billnow.png")
            b0 = Button(
                image = img0,
                borderwidth = 0,
                highlightthickness = 0,
                command = printInput,
                relief = "flat")

            b0.place(
                x = 1009, y = 653,
                width = 232,
                height = 40)
            window.resizable(False, False)
            window.mainloop()

            '''bill = Tk()
            bill.title("srikart")
            bill.geometry("550x200")
            bill.configure(bg = "#4799E9")
            a0=Label(bill,text="STAR WATCH",font=(50),bg = "#4799E9")
            a0.place(x=180,y=0)
            a2=Label(bill,text="Watch name:",font=(50),bg = "#4799E9")
            a2.place(x=9,y=55)
            a1=Label(bill,text=name,font=(50),bg = "#4799E9")
            a1.place(x=130,y=55)
            a4=Label(bill,text="Price           :",font=(50),bg="#4799E9")
            a4.place(x=9,y=80)
            a3=Label(bill,text="Rs."+str(price),font=(50),bg = "#4799E9")
            a3.place(x=130,y=80)
            a4=Label(bill,text="Delivery      : Tomorrow,",font=(50),bg = "#4799E9")
            a4.place(x=10,y=107)
            a5=Label(bill,text=tomorrow,font=(50),bg = "#4799E9")
            a5.place(x=235,y=107)'''

    def branch1():
        #z.destroy()
        a=Label(root1,image=img51)
        a.place(x=0,y=45)
        p1=1000
        p=Label(root1,text="PRICE :"+str(p1))
        p.place(x=800,y=125)
        B=Button(root1,text="BUY NOW",bg="light green",command= partial(add,name,p1))
        B.place(x=800,y=200)
    def branch(b52):
        global z
        #b.destroy()
        z=Label(root1,image=b52)
        z.place(x=0,y=45)
        p1=1000
        p=Label(root1,text="PRICE :"+str(p1))
        p.place(x=800,y=125)
        B=Button(root1,text="ADD TO CART",bg="light green",command=partial(add,name,p1))
        B.place(x=800,y=200)

    def b61(img):
        name="Noise ColorFit Pulse"
        for widgets in root1.winfo_children():
          widgets.destroy()
        p1=1999
        T1=Label(root1,text="Noise ColorFit Pulse ",height=2,width=22,bg="#f8f8f8")
        T1.place(x=0,y=5)
        global b
        b= Label(root1,image = img)
        b.place(x=0,y=45)
        T = Text(root1,height = 7, width = 52,bg="#f8f8f8")
        T.place(x=330,y=45)
        
        for i in range(7):
            T.insert(END,eval("txt2"+str(i+1)))
        T.config(state=DISABLED)
        Tc=Label(root1,text="colour")
        Tc.place(x=800,y=45)
        b1=Button(root1,text="Teal green")
        b1.place(x=800,y=75)
        
        
        b2=Button(root1,text="Royal blue")
        b2.place(x=870,y=75)
        p=Label(root1,text="PRICE :"+str(p1))
        p.place(x=800,y=125)
        B=Button(root1,text="ADD TO CART",bg="light green",command=partial(add,name,p1))
        B.place(x=800,y=200)

    def b71(img):
        name="Fire-Boltt Ninja 2"
        for widgets in root1.winfo_children():
          widgets.destroy()
        p1=1999
        T1=Label(root1,text="Fire-Boltt Ninja 2",height=2,width=22,bg="#f8f8f8")
        T1.place(x=0,y=5)
        global b
        b= Label(root1,image = img)
        b.place(x=0,y=45)
        T = Text(root1,height = 7, width = 52,bg="#f8f8f8")
        T.place(x=330,y=45)
        
        for i in range(6):
            T.insert(END,eval("txt1"+str(i+1)))
        T.config(state=DISABLED)
        Tc=Label(root1,text="colour")
        Tc.place(x=800,y=45)
        b1=Button(root1,text="Green")
        b1.place(x=800,y=75)
        
        
        b2=Button(root1,text="BLACK")
        b2.place(x=850,y=75)
        p=Label(root1,text="PRICE :"+str(p1))
        p.place(x=800,y=125)
        B=Button(root1,text="ADD TO CART",bg="light green",command=partial(add,name,p1))
        B.place(x=800,y=200)
    def b51(img,b52):
        name="Symbol Silicone Analog"
        for widgets in root1.winfo_children():
          widgets.destroy()
        global p1
        p1=1500
        T1=Label(root1,text="Symbol Silicone Analog",height=2,width=22,bg="#f8f8f8")
        T1.place(x=0,y=5)
        global b
        b= Label(root1,image = img)
        b.place(x=0,y=45)
        T = Text(root1,height = 7, width = 52,bg="#f8f8f8")
        T.place(x=330,y=45)
        
        for i in range(7):
            T.insert(END,eval("txt"+str(i+1)))
        T.config(state=DISABLED)
        Tc=Label(root1,text="colour")
        Tc.place(x=800,y=45)
        b1=Button(root1,text="NAVY",command=branch1)
        b1.place(x=800,y=75)
        
        
        b2=Button(root1,text="BLACK",command=partial(branch,b52))
        b2.place(x=850,y=75)
        p=Label(root1,text="PRICE :"+str(p1))
        p.place(x=800,y=125)
        B=Button(root1,text="ADD TO CART",bg="light green",command=partial(add,name,p1))
        B.place(x=800,y=200)


    def b100(img):
        name="Symbol Silicone Analog"
        for widgets in root1.winfo_children():
          widgets.destroy()
        global p1
        p1=1000
        T1=Label(root1,text="Symbol Silicone Analog",height=2,width=22,bg="#f8f8f8")
        T1.place(x=0,y=5)
        global b
        b= Label(root1,image = img)
        b.place(x=0,y=45)
        T = Text(root1,height = 7, width = 52,bg="#f8f8f8")
        T.place(x=330,y=45)
        
        for i in range(5):
            T.insert(END,eval("txt3"+str(i+1)))
        T.config(state=DISABLED)
        Tc=Label(root1,text="colour")
        Tc.place(x=800,y=45)
        b1=Button(root1,text="Dark Green")
        b1.place(x=800,y=75)

        p=Label(root1,text="PRICE :"+str(p1))
        p.place(x=800,y=125)
        B=Button(root1,text="ADD TO CART",bg="light green",command=partial(add,name,p1))
        B.place(x=800,y=200)

    def b101(img):
        name="Teal By Chumbak Leafy Branches"
        for widgets in root1.winfo_children():
          widgets.destroy()
        global p1
        p1=1499
        T1=Label(root1,text="Teal By Chumbak Leafy Branches",height=2,width=32,bg="#f8f8f8")
        T1.place(x=0,y=5)
        global b
        b= Label(root1,image = img)
        b.place(x=0,y=45)
        T = Text(root1,height = 7, width = 52,bg="#f8f8f8")
        T.place(x=330,y=45)
        
        for i in range(4):
            T.insert(END,eval("txt4"+str(i+1)))
        T.config(state=DISABLED)
        Tc=Label(root1,text="colour")
        Tc.place(x=800,y=45)
        b1=Button(root1,text="Blue")
        b1.place(x=800,y=75)

        p=Label(root1,text="PRICE :"+str(p1))
        p.place(x=800,y=125)
        B=Button(root1,text="ADD TO CART",bg="light green",command=partial(add,name,p1))
        B.place(x=800,y=200)

    def b102(img):
        name="Teal By Chumbak Leafy Branches"
        for widgets in root1.winfo_children():
          widgets.destroy()
        global p1
        p1=1499
        T1=Label(root1,text="Teal By Chumbak Leafy Branches",height=2,width=32,bg="#f8f8f8")
        T1.place(x=0,y=5)
        global b
        b= Label(root1,image = img)
        b.place(x=0,y=45)
        T = Text(root1,height = 7, width = 52,bg="#f8f8f8")
        T.place(x=330,y=45)
        
        for i in range(4):
            T.insert(END,eval("txt5"+str(i+1)))
        T.config(state=DISABLED)
        Tc=Label(root1,text="colour")
        Tc.place(x=800,y=45)
        b1=Button(root1,text="Blue")
        b1.place(x=800,y=75)

        p=Label(root1,text="PRICE :"+str(p1))
        p.place(x=800,y=125)
        B=Button(root1,text="ADD TO CART",bg="light green",command=partial(add,name,p1))
        B.place(x=800,y=200)

    def carty():
        fram=LabelFrame(root,width=200,height=390)
        fram.place(x=1200,y=100)
        pex=Label(fram,image=pexels)
        pex.place(x=1,y=1)
        
        close1=Button(fram,image=close,command=fram.destroy)
        close1.place(x=150,y=1)
        
        b=40
        for i in name1:
        
                    
            a=Label(fram,text=i)
            a.place(x=5,y=b)
            b+=30
        d=Button(fram,text="BUY NOW",command=partial(ask,name1,price1))
        d.place(x=125,y=350)
                

    def remove1(n,p):
        t=Label(root,text=n+" removed from cart.",height=2,width=42,bg="#f8f8f8")
        t.place(x=600,y=450)
        name1.remove(n)
        price1.remove(p)
        print(name1)
        
        

    def add(name,price):
        #global name1,price1
        t=Label(root,text=name+" added to cart.",height=1,width=42,bg="#f8f8f8")
        t.place(x=600,y=470)
        root.after(5000,t.destroy)
        name1.append(name)
        price1.append(price)
        print(name1)
        r=Button(root1,text="Remove from cart",command=partial(remove1,name,price))
        r.place(x=900,y=200)


    def b103(img):
        name="TITAN Womens Green"
        for widgets in root1.winfo_children():
          widgets.destroy()
        global p1
        p1=1799
        T1=Label(root1,text="TITAN Womens Green Dial Stainless Steel",height=2,width=32,bg="#f8f8f8")
        T1.place(x=0,y=5)
        global b
        b= Label(root1,image = img)
        b.place(x=0,y=45)
        T = Text(root1,height = 7, width = 52,bg="#f8f8f8")
        T.place(x=330,y=45)
        
        for i in range(6):
            T.insert(END,eval("txt6"+str(i+1)))
        T.config(state=DISABLED)
        Tc=Label(root1,text="colour")
        Tc.place(x=800,y=45)
        b1=Button(root1,text="Green")
        b1.place(x=800,y=75)

        p=Label(root1,text="PRICE :"+str(p1))
        p.place(x=800,y=125)
        B=Button(root1,text="ADD TO CART",bg="light green",command=partial(add,name,p1))
        B.place(x=800,y=200)

    def b104(img):
        name="Ball official standrad"
        for widgets in root1.winfo_children():
          widgets.destroy()
        global p1
        p1=2999
        T1=Label(root1,text="Ball official standrad",height=2,width=32,bg="#f8f8f8")
        T1.place(x=0,y=5)
        global b
        b= Label(root1,image = img)
        b.place(x=0,y=45)
        T = Text(root1,height = 7, width = 52,bg="#f8f8f8")
        T.place(x=330,y=45)
        
        for i in range(5):
            T.insert(END,eval("txt7"+str(i+1)))
        T.config(state=DISABLED)
        Tc=Label(root1,text="colour")
        Tc.place(x=800,y=45)
        b1=Button(root1,text="multicoloured")
        b1.place(x=800,y=75)

        p=Label(root1,text="PRICE :"+str(p1))
        p.place(x=800,y=125)
        B=Button(root1,text="ADD TO CART",bg="light green",command=partial(add,name,p1))
        B.place(x=800,y=200)   
        
    def w():
        for widgets in root1.winfo_children():
          widgets.destroy()
        texty=Label(root1,text="LOOK COOL ",fg="green",font = ("None",int(30.0)))
        texty1=Label(root1,text="AND ",fg="black",font = ("None",int(30.0)))
        texty2=Label(root1,text="FASHIONABLE!",fg="#4799E9",font = ("None",int(30.0)))
        texty.place(x=380,y=100)
        texty1.place(x=630,y=100)
        texty2.place(x=730,y=100)
        global b10
        global b11
        global b12
        global b13
        b10 = Button(
        image = img10,
        borderwidth = 0,
        highlightthickness = 0,
        command = partial(b100,img100),
        relief = "flat")

        b10.place(
        x = 291, y = 176,
        width = 296,
        height = 247)

        
        b11 = Button(
        image = img11,
        borderwidth = 0,
        highlightthickness = 0,
        command =  partial(b101,img101),
        relief = "flat")

        b11.place(
        x = 621, y = 181,
        width = 282,
        height = 242)

       
        b12 = Button(
        image = img12,
        borderwidth = 0,
        highlightthickness = 0,
        command =partial(b102,img102),
        relief = "flat")

        b12.place(
        x = 937, y = 181,
        width = 259,
        height = 242)

        
        b13 = Button(
        image = img13,
        borderwidth = 0,
        highlightthickness = 0,
        command = partial(b103,img103),
        relief = "flat")

        b13.place(
        x = 1230, y = 185,
        width = 177,
        height = 242)

    def m():
        for widgets in root1.winfo_children():
          widgets.destroy()
        texty=Label(root1,text="LOOK COOL ",fg="green",font = ("None",int(30.0)))
        texty1=Label(root1,text="AND ",fg="black",font = ("None",int(30.0)))
        texty2=Label(root1,text="FASHIONABLE!",fg="#4799E9",font = ("None",int(30.0)))
        texty.place(x=380,y=100)
        texty1.place(x=630,y=100)
        texty2.place(x=730,y=100)
        b10.destroy()
        b11.destroy()
        b12.destroy()
        b13.destroy()
        b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = partial(b104,img104),
        relief = "flat")

        b4.place(
        x = 1230, y = 185,
        width = 147,
        height = 220)
        
        b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = partial(b51,img51,b52),
        relief = "flat")

        b5.place(
        x = 937, y = 181,
        width = 259,
        height = 224)

        
        b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = partial(b61,img6),
        relief = "raised")

        b6.place(
        x = 291, y = 176,
        width = 296,
        height = 247
        )

        b7 = Button(
        image = img7,
        borderwidth = 0,
        highlightthickness = 0,
        command = partial(b71,img71),
        relief = "flat")

        b7.place(
        x = 621, y = 181,
        width = 282,
        height = 242)



    root = Tk()
    root.title("srikart")
    root.geometry("1440x1024")
    root.configure(bg = "#f8f8f8")
    canvas = Canvas(
        root,
        bg = "#f8f8f8",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    canvas.create_text(
        704.5, 57.5,
        text = "STAR WATCH",
        fill = "#000000",
        font = ("None", int(48.0)))


            
        

    cart=Button(root,text="GO TO CART",bg="orange",command=carty)
    cart.place(x=1250,y=60)

    def shift():
        x1,y1,x2,y2 = canvas.bbox("marquee")
        if(x2<0 or y1<0): 
            x1 = canvas.winfo_width()
            y1=450
            canvas.coords("marquee",x1,y1)
        else:
            canvas.move("marquee", -2, 0)
        canvas.after(1000//fps,shift)

    #canvas=Canvas(root)
    canvas.pack( fill=BOTH,expand=1)
    text_var="FREE DELIVERY!                                                                                                                                               2 YEARS WARRANTY!"
    text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',18,'bold'),fill='black',tags=("marquee",),anchor='w')
    x1,y1,x2,y2 = canvas.bbox("marquee")
    width = x2-x1
    height = y2-y1
    canvas['width']=width
    canvas['height']=height
    fps=70    #Change the fps to make the animation faster/slower
    shift()

    global txt1,txt2,txt3,txt4,txt5,txt6,txt7
    txt1= "Dial Color: Navy , Case Shape: Round ,\n"
    txt2="Dial Glass Material: Mineral\n"
    txt3="Band Color: Navy, Band Material: Silicon\n"
    txt4='Watch Movement Type:Quartz,\n'
    txt5='Watch Display Type: Analog-Digital\n'           
    txt6='Case Material: Plastic, Case Diameter: 55MM\n'  
    txt7='1 Year Manufacturer Warranty'

    global txt11,txt12,txt13,txt14,txt15,txt16
    txt11="Brand:Fire-Boltt\n"
    txt12="Colour:Dark Green\n"
    txt13="Special Feature:	Stopwatch, camera control, music control\n,"
    txt14="full font language, Blood oxygen saturation measurement\n"
    txt15="Compatible Devices:Tablet,Smartphone\n"
    txt16="Screen Size: 1.5 Inches"

    global txt21,txt22,txt23,txt24,txt25,txt26,txt27
    txt21="Brand:‎Noise\n"
    txt22="Manufacturer:TSL, Fulongfuhe Road, Dongguan city - 523025\n"
    txt23="Model:‎Wrb-sw-colorfitpulse-std-teal_teal\n"
    txt24="Model Name:‎ColorFit Pulse\n"
    txt25="Product Dimensions:‎4.1 x 3.7 x 1 cm; 40 Grams\n"
    txt26="Resolution:‎240 x 240\n"
    txt27="Special Features:Heart Rate Monitor, Sleep & Step Tracking\n"

    global txt31,txt32,txt33,txt34,txt35
    txt31="Made from PU strap & Brass dial\n"
    txt32="One Year Warranty on the mechanism.\n"
    txt33="Watch comes citizen 2035 movement.\n"
    txt34="Care- Wipe with a dry cloth to clean.\n"
    txt35="A Wrist Watch with Chumbak Watch Tin."

    global txt41,txt42,txt43,txt44
    txt41="Made from PU strap & Brass dial\n"
    txt42="One Year Warranty on the mechanism. No warranty on the strap, dial and case.\n"
    txt43="Strap Length: 24 cms & Dail width: 3.5 cms\n"
    txt44="Box Content- 1 Wrist Watch with Chumbak Watch Tin\n"

    global txt51,txt52,txt53,txt54,txt55,txt56
    txt51="Dial Color: Black, Case Shape: Round, Dial Glass Material: Glass\n"
    txt52="Band Color: Multi-Colour, Band Material: Synthetic\n"
    txt53="Watch Movement Type: Quartz, Watch Display Type: Analog\n"
    txt54="Case Material: Metal, Case Diameter: 85 millimeters\n"
    txt55="Water Resistance Depth: 30 meters, Buckle Clasp\n"
    txt56="1 year warranty"

    global txt61,txt62,txt63,txt64,txt65,txt66
    txt61="Country of Origin:India\n"
    txt62="Case Thickness:9.55 mm\n"
    txt63="Band Material:Stainless Steel\n"
    txt64="Water Resistant Depth:50 Meters\n"
    txt65="Battery Composition:Lithium\n"
    txt66="1 year warranty"

    global txt71,txt72,txt73,txt74,txt75
    txt71="Automatic caliber BALL RR1103-C\n"
    txt72="multi-colored micro gas tubes on hour, minute, second hands and dial for night reading capability\n"
    txt73="Shock resistance:5,000Gs\n"
    txt74="Titanium with TiC Titanium carbide coating\n"
    txt75="Nubuck leather strap with standard buckle\n"

    '''img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 29, y = 383,
        width = 198,
        height = 45)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 29, y = 314,
        width = 198,
        height = 45)'''

    img2 = PhotoImage(file = f"img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = w,
        relief = "flat")

    b2.place(
        x = 29, y = 314,
        width = 198,
        height = 45)

    img3 = PhotoImage(file = f"img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = m,
        relief = "flat")

    b3.place(
        x = 29, y = 245,
        width = 198,
        height = 45)

    img4 = PhotoImage(file=f"img4.png")
    img104=PhotoImage(file = f"img104.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = partial(b104,img104),
        relief = "flat")

    b4.place(
        x = 1230, y = 185,
        width = 147,
        height = 220)
    img51=PhotoImage(file = f"img51.png")
    b52=PhotoImage(file =f"img52.png")
    img5 = PhotoImage(file=f"img5.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = partial(b51,img51,b52),
        relief = "flat")

    b5.place(
        x = 937, y = 181,
        width = 259,
        height = 224)

    img6 = PhotoImage(file = f"img61.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = partial(b61,img6),
        relief = "raised")

    b6.place(
        x = 291, y = 176,
        width = 296,
        height = 247
        )
    img71=PhotoImage(file=f"img71.png")
    img7 = PhotoImage(file = f"img7.png")
    b7 = Button(
        image = img7,
        borderwidth = 0,
        highlightthickness = 0,
        command =partial(b71,img71),
        relief = "flat")

    b7.place(
        x = 621, y = 181,
        width = 282,
        height = 242)

    '''img106=PhotoImage(file=f"img106.png")
    b106=Label(image=img106)
    b106.place(x=100,y=57)'''



    root1=Frame(root,width=1300,height=280)
    root1.place(x=45,y=500)
    
    texty=Label(root1,text="LOOK COOL ",fg="green",font = ("None",int(30.0)))
    texty.place(x=380,y=100)

    
    texty1=Label(root1,text="AND ",fg="black",font = ("None",int(30.0)))
    texty1.place(x=630,y=100)
    texty2=Label(root1,text="FASHIONABLE!",fg="#4799E9",font = ("None",int(30.0)))
    texty2.place(x=730,y=100)
    



    img100=PhotoImage(file = f"img100.png")
    img101=PhotoImage(file = f"img101.png")
    img102=PhotoImage(file = f"img102.png")
    img103=PhotoImage(file = f"img103.png")
    img104=PhotoImage(file = f"img104.png")
    img10 = PhotoImage(file = f"img10.png")
    img11 = PhotoImage(file = f"img11.png")
    img12 = PhotoImage(file = f"img12.png")
    img13 = PhotoImage(file = f"img131.png")
    close=PhotoImage(file = f"close.png")
    pexels=PhotoImage(file = f"pexels.png")

    
    
    today = datetime.date.today()
    today1=today
    today1=str(today1)
    tomorrow = today + datetime.timedelta(days = 1) 


    '''img8 = PhotoImage(file = f"img8.png")
    b8 = Button(
        image = img8,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b8.place(
        x = 1268, y = 120,
        width = 104,
        height = 36)'''

    '''def remove1(f,i):
        f.destroy()
        name1.remove(i)
        print(name1)

    def carty():
        fram=LabelFrame(root,width=200,height=390)
        fram.place(x=1200,y=100)
        close1=Button(fram,image=close,command=fram.destroy)
        close1.place(x=150,y=1)
        b=40
        da={}
        dc={}
        
        for i in name1:
        
                    
            da[i]=Label(fram,text=i)
            da[i].place(x=5,y=b)
            dc[i]=Button(fram,text="-",bg="red",command= lambda : [remove1(da[i],i),dc[i].place_forget()])
            dc[i].place(x=170,y=b)
            b+=30
        d=Button(fram,text="BUY NOW")
        d.place(x=125,y=350)'''
    #root.resizable(False, False)
    root.mainloop()

def des():
    rooty.destroy()
    open1()

rooty = Tk()
rooty.title("sri")
rooty.geometry("1598x799")
rooty.configure(bg = "#f8f8f8")



img=PhotoImage(file=f"screen1.png")
i1=Label(rooty,image=img)
i1.place(x=-10,y=0)

img0=PhotoImage(file=f"img001.png")
i2=Button(rooty,image=img0,bg= "#FEA150",command=des)
i2.place(x=1080,y=580)


'''rooty = Tk()
rooty.title("sri")
rooty.geometry("1930x832")
rooty.configure(bg = "#f8f8f8")



img=PhotoImage(file=f"capture.png")
i1=Label(rooty,image=img)
i1.place(x=-10,y=0)

img0=PhotoImage(file=f"img000.png")
i2=Button(rooty,image=img0,bg= "#FEA150",command=des)
i2.place(x=950,y=630)'''

rooty.mainloop()
#reference srini cse and 
