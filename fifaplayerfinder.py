import pandas as pd
import tkinter as tk 
from tkinter import ttk 
from prop import * 

class GUI:
    def __init__(self,type,text,row_num,col_num,varname,pad_x,pad_y,command,sticky):
        self.type=type
        self.varname=varname
        pos_list=["GK","RWB","RB","CB","LB","LWB","CDM","CM","CAM","RM","RW","LM","LW","RF","CF","LF","ST"]
        if self.type=="label":
            self.label=tk.Label(window,text=text)
            self.label.grid(row=row_num,column=col_num,padx=pad_x,pady=pad_y)
            self.label.config(font=("Courier", 14))

        if self.type=="entry":
            self.entry=tk.Entry(window,textvariable=varname, font=('calibre',8, 'bold'))
            self.entry.grid(row=row_num,column=col_num)
        
        if self.type=="button":
            self.button=tk.Button(window,text=text,command=command)
            self.button.grid(row=row_num,column=col_num,padx=pad_x,pady=pad_y,sticky=sticky)

        if self.type=="combobox":
            self.combobox=ttk.Combobox(window,textvariable=position_var,sticky=sticky)
            self.combobox["values"]=pos_list
            self.combobox.grid(row=row_num,column=col_num,padx=pad_x,pady=pad_y)
    



window=tk.Tk()
window.geometry("900x640")
window.grid()

window.columnconfigure((0,1,2,3),weight=1)
window.rowconfigure((0,1),weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)

age_var=tk.IntVar()
value_var=tk.IntVar()
position_var=tk.StringVar()
overall_var=tk.IntVar() 

pressed=False
 
def process():
    
    textbox.delete('1.0', tk.END)
    global age,overall,value,position ,pressed,pos_list,playerlist
    age=age_var.get()
    overall=overall_var.get()
    value=value_var.get()
    position=position_var.get()
    pressed=True
    data=pd.read_csv("sources/fifa22.csv")

    pos_list=["GK","RWB","RB","CB","LB","LWB","CDM","CM","CAM","RM","RW","LM","LW","RF","CF","LF","ST"]

 
    user_choice=position
    minoverall=overall
    minvalue=value
    maxage=age

    
    indexlist=data.index[data["player_positions"]==user_choice].tolist()  # istenilen pozisyonda olan oyuncuların index list'i
    playernamelist=[]
    num=0
    def player(indexlist,minoverall,minvalue,maxage,num):
        for id in indexlist:
            if data.iloc[id]["overall"]>minoverall and data.iloc[id]["value_eur"]/1000000>minvalue and data.iloc[id]["age"]<maxage:
                num+=1
                
                playernamelist.append([data.iloc[id]["short_name"],data.iloc[id]["overall"],data.iloc[id]["value_eur"]/1000000,data.iloc[id]["age"]])
                
    
    
    if num==0:
        print("no player")
             

    player(indexlist,minoverall,minvalue,maxage,num)

    textbox.insert(tk.END,"Name" +"\t" +"\t"+ "overall" +"\t" +"\t"+ "value"+"\t"+"\t"+ "age" +"\n")
    textbox.insert(tk.END,"\n")

    if len(playernamelist)>0:
        for player in playernamelist:
            textbox.insert(tk.END,player[0] +"\t" +"\t"+ str(player[1]) +"\t" +"\t"+ str(player[2])+"m euro"+"\t"+"\t"+ str(player[3]) +"\n")



label1=GUI("label","Maximum Age",0,0,None,(40,75),(0,0),None,None)
entry1=GUI("entry",None,1,0,age_var,(10,30),(0,0),None,sticky=tk.N)


label2=GUI("label","Minimum Value",0,1,None,(40,75),(0,0),None,None)
entry2=GUI("entry",None,1,1,value_var,(10,30),(0,0),None,sticky=tk.N)


label3=GUI("label","Position",0,2,None,(20,75),(0,0),None,None)
combobox=GUI("combobox",None,1,2,position_var,(0,0),(0,0),None, None)

label4=GUI("label","Minimum Overall ",0,3,None,(10,25),(0,0),None,None)
entry4=GUI("entry",None,1,3,overall_var,(0,0),(0,0),None,sticky=tk.N)

button1=GUI("button","Let me cook",2,1,None,(175,0),(0,0),process,sticky=tk.N)
 
textbox=tk.Text(window)
textbox.grid(row=3,column=0,columnspan=4)


window.mainloop()


