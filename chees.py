# from Saurabh import IQ

#  13,330 Line

from tkinter import *
#import tkMessageBox

enter = None

wrong_move = "Sorry wrong move\nThis is wrong move moved by this unit "
no_move = "This unit have no place to move ! "
wrong_player = "Wrong player is playing ! " 

root=Tk()

pl_1_ch = 0
pl_2_ch = 0
pl_1_tc = 2
pl_2_tc = 2

cheat_move_sol = 0
cheat_move_unit = 0
cheat_l = []
to_nut = [] 

p_row = None
p_column = None
type_of_unit = None

unit = ["f","w"]
state = [1,1]

row_0 = ['wall','wall','wall','wall','wall','wall','wall','wall''wall','wall']
row_1 = ['wall','b_ele','b_hor','b_cam','b_que','b_king','b_cam','b_hor','b_ele','wall',]
row_2 = ['wall','b_sol','b_sol','b_sol','b_sol','b_sol','b_sol','b_sol','b_sol','wall',]
row_3 = ['wall','plate','plate','plate','plate','plate','plate','plate','plate','wall',]
row_4 = ['wall','plate','plate','plate','plate','plate','plate','plate','plate','wall',]
row_5 = ['wall','plate','plate','plate','plate','plate','plate','plate','plate','wall',]
row_6 = ['wall','plate','plate','plate','plate','plate','plate','plate','plate','wall',]
row_7 = ['wall','w_sol','w_sol','w_sol','w_sol','w_sol','w_sol','w_sol','w_sol','wall',]
row_8 = ['wall','w_ele','w_hor','w_cam','w_que','w_king','w_cam','w_hor','w_ele','wall',]
row_9 = ['wall','wall','wall','wall','wall','wall','wall','wall''wall','wall']

main_dic = { 11:"b_ele",12:"b_hor",13:'b_cam',14:'b_que',15:"b_king",16:"b_cam",17:"b_hor",18:"b_ele",
             21:"b_sol",22:"b_sol",23:"b_sol",24:"b_sol",25:"b_sol",26:"b_sol",27:"b_sol",28:"b_sol",
            31:"plate",32:"plate",33:"plate",34:"plate",35:"plate",36:"plate",37:"plate",38:"plate",
            41:"plate",42:"plate",43:"plate",44:"plate",45:"plate",46:"plate",47:"plate",48:"plate",
            51:"plate",52:"plate",53:"plate",54:"plate",55:"plate",56:"plate",57:"plate",58:"plate",
            61:"plate",62:"plate",63:"plate",64:"plate",65:"plate",66:"plate",67:"plate",68:"plate",
            71:"w_ele",72:"w_hor",73:'w_cam',74:'w_que',75:"w_king",76:"w_cam",77:"w_hor",78:"w_ele",
            81:"w_ele",82:"w_hor",83:'w_cam',84:'w_que',85:"w_king",86:"w_cam",87:"w_hor",88:"w_ele"}

whole_match = {}
            

def basic():
    global r1c1
    global r1c2
    global r1c3
    global r1c4
    global r1c5
    global r1c6
    global r1c7
    global r1c8
    global r2c1
    global r2c2
    global r2c3
    global r2c4
    global r2c5
    global r2c6
    global r2c7
    global r2c8
    global r3c1
    global r3c2
    global r3c3
    global r3c4
    global r3c5
    global r3c6
    global r3c7
    global r3c8
    global r4c1
    global r4c2
    global r4c3
    global r4c4
    global r4c5
    global r4c6
    global r4c7
    global r4c8
    global r5c1
    global r5c2
    global r5c3
    global r5c4
    global r5c5
    global r5c6
    global r5c7
    global r5c8
    global r6c1
    global r6c2
    global r6c3
    global r6c4
    global r6c5
    global r6c6
    global r6c7
    global r6c8
    global r7c1
    global r7c2
    global r7c3
    global r7c4
    global r7c5
    global r7c6
    global r7c7
    global r7c8
    global r8c1
    global r8c2
    global r8c3
    global r8c4
    global r8c5
    global r8c6
    global r8c7
    global r8c8
    global player_1
    global player_2
    global player_1_ch
    global player_2_ch
    global player_1_tc
    global player_2_tc
    global player
    global player_1_ch_rep
    global player_2_ch_rep
    global player_1_tc_rep
    global player_2_tc_rep
    global boundry

    m1.destroy()
    m2.destroy()
    m3.destroy()
    m4.destroy()
    m5.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    l.destroy()

    m = Label(root,text = "         	    	    	",bg="orange")
    m.grid(row=0,column=0)
    
    r1c1 = Button(root,height=55,width=55,command = r1c1_move)
    r1c1.grid(row=1,column=1)
    r1c2 = Button(root,height=55,width=55,command = r1c2_move)
    r1c2.grid(row=1,column=2)
    r1c3 = Button(root,height=55,width=55,command = r1c3_move)
    r1c3.grid(row=1,column=3)
    r1c4 = Button(root,height=55,width=55,command = r1c4_move)
    r1c4.grid(row=1,column=4)
    r1c5 = Button(root,height=55,width=55,command = r1c5_move)
    r1c5.grid(row=1,column=5)
    r1c6 = Button(root,height=55,width=55,command = r1c6_move)
    r1c6.grid(row=1,column=6)
    r1c7 = Button(root,height=55,width=55,command = r1c7_move)
    r1c7.grid(row=1,column=7)
    r1c8 = Button(root,height=55,width=55,command = r1c8_move)
    r1c8.grid(row=1,column=8)
    
    r1c1.config(image=b_ele_w)
    r1c2.config(image=b_hor_b)
    r1c3.config(image=b_cam_w)
    r1c4.config(image=b_que_b)
    r1c5.config(image=b_king_w)
    r1c6.config(image=b_cam_b)
    r1c7.config(image=b_hor_w)
    r1c8.config(image=b_ele_b)

    r2c1 = Button(root,height=55,width=55,command = r2c1_move)
    r2c1.grid(row=2,column=1)
    r2c2 = Button(root,height=55,width=55,command = r2c2_move)
    r2c2.grid(row=2,column=2)
    r2c3 = Button(root,height=55,width=55,command = r2c3_move)
    r2c3.grid(row=2,column=3)
    r2c4 = Button(root,height=55,width=55,command = r2c4_move)
    r2c4.grid(row=2,column=4)
    r2c5 = Button(root,height=55,width=55,command = r2c5_move)
    r2c5.grid(row=2,column=5)
    r2c6 = Button(root,height=55,width=55,command = r2c6_move)
    r2c6.grid(row=2,column=6)
    r2c7 = Button(root,height=55,width=55,command = r2c7_move)
    r2c7.grid(row=2,column=7)
    r2c8 = Button(root,height=55,width=55,command = r2c8_move)
    r2c8.grid(row=2,column=8)
    
    r2c1.config(image=b_sol_b)
    r2c2.config(image=b_sol_w)
    r2c3.config(image=b_sol_b)
    r2c4.config(image=b_sol_w)
    r2c5.config(image=b_sol_b)
    r2c6.config(image=b_sol_w)
    r2c7.config(image=b_sol_b)
    r2c8.config(image=b_sol_w)

    r3c1 = Button(root,height=55,width=55,command = r3c1_move)
    r3c1.grid(row=3,column=1)
    r3c2 = Button(root,height=55,width=55,command = r3c2_move)
    r3c2.grid(row=3,column=2)
    r3c3 = Button(root,height=55,width=55,command = r3c3_move)
    r3c3.grid(row=3,column=3)
    r3c4 = Button(root,height=55,width=55,command = r3c4_move)
    r3c4.grid(row=3,column=4)
    r3c5 = Button(root,height=55,width=55,command = r3c5_move)
    r3c5.grid(row=3,column=5)
    r3c6 = Button(root,height=55,width=55,command = r3c6_move)
    r3c6.grid(row=3,column=6)
    r3c7 = Button(root,height=55,width=55,command = r3c7_move)
    r3c7.grid(row=3,column=7)
    r3c8 = Button(root,height=55,width=55,command = r3c8_move)
    r3c8.grid(row=3,column=8)
    
    r3c1.config(image=w_plate)
    r3c2.config(image=b_plate)
    r3c3.config(image=w_plate)
    r3c4.config(image=b_plate)
    r3c5.config(image=w_plate)
    r3c6.config(image=b_plate)
    r3c7.config(image=w_plate)
    r3c8.config(image=b_plate)

    r4c1 = Button(root,height=55,width=55,command = r4c1_move)
    r4c1.grid(row=4,column=1)
    r4c2 = Button(root,height=55,width=55,command = r4c2_move)
    r4c2.grid(row=4,column=2)
    r4c3 = Button(root,height=55,width=55,command = r4c3_move)
    r4c3.grid(row=4,column=3)
    r4c4 = Button(root,height=55,width=55,command = r4c4_move)
    r4c4.grid(row=4,column=4)
    r4c5 = Button(root,height=55,width=55,command = r4c5_move)
    r4c5.grid(row=4,column=5)
    r4c6 = Button(root,height=55,width=55,command = r4c6_move)
    r4c6.grid(row=4,column=6)
    r4c7 = Button(root,height=55,width=55,command = r4c7_move)
    r4c7.grid(row=4,column=7)
    r4c8 = Button(root,height=55,width=55,command = r4c8_move)
    r4c8.grid(row=4,column=8)
    
    r4c1.config(image=b_plate)
    r4c2.config(image=w_plate)
    r4c3.config(image=b_plate)
    r4c4.config(image=w_plate)
    r4c5.config(image=b_plate)
    r4c6.config(image=w_plate)
    r4c7.config(image=b_plate)
    r4c8.config(image=w_plate)


    r5c1 = Button(root,height=55,width=55,command = r5c1_move)
    r5c1.grid(row=5,column=1)
    r5c2 = Button(root,height=55,width=55,command = r5c2_move)
    r5c2.grid(row=5,column=2)
    r5c3 = Button(root,height=55,width=55,command = r5c3_move)
    r5c3.grid(row=5,column=3)
    r5c4 = Button(root,height=55,width=55,command = r5c4_move)
    r5c4.grid(row=5,column=4)
    r5c5 = Button(root,height=55,width=55,command = r5c5_move)
    r5c5.grid(row=5,column=5)
    r5c6 = Button(root,height=55,width=55,command = r5c6_move)
    r5c6.grid(row=5,column=6)
    r5c7 = Button(root,height=55,width=55,command = r5c7_move)
    r5c7.grid(row=5,column=7)
    r5c8 = Button(root,height=55,width=55,command = r5c8_move)
    r5c8.grid(row=5,column=8)
    
    r5c1.config(image=w_plate)
    r5c2.config(image=b_plate)
    r5c3.config(image=w_plate)
    r5c4.config(image=b_plate)
    r5c5.config(image=w_plate)
    r5c6.config(image=b_plate)
    r5c7.config(image=w_plate)
    r5c8.config(image=b_plate)

    r6c1 = Button(root,height=55,width=55,command = r6c1_move)
    r6c1.grid(row=6,column=1)
    r6c2 = Button(root,height=55,width=55,command = r6c2_move)
    r6c2.grid(row=6,column=2)
    r6c3 = Button(root,height=55,width=55,command = r6c3_move)
    r6c3.grid(row=6,column=3)
    r6c4 = Button(root,height=55,width=55,command = r6c4_move)
    r6c4.grid(row=6,column=4)
    r6c5 = Button(root,height=55,width=55,command = r6c5_move)
    r6c5.grid(row=6,column=5)
    r6c6 = Button(root,height=55,width=55,command = r6c6_move)
    r6c6.grid(row=6,column=6)
    r6c7 = Button(root,height=55,width=55,command = r6c7_move)
    r6c7.grid(row=6,column=7)
    r6c8 = Button(root,height=55,width=55,command = r6c8_move)
    r6c8.grid(row=6,column=8)
    
    r6c1.config(image=b_plate)
    r6c2.config(image=w_plate)
    r6c3.config(image=b_plate)
    r6c4.config(image=w_plate)
    r6c5.config(image=b_plate)
    r6c6.config(image=w_plate)
    r6c7.config(image=b_plate)
    r6c8.config(image=w_plate)

    r7c1 = Button(root,height=55,width=55,command = r7c1_move)
    r7c1.grid(row=7,column=1)
    r7c2 = Button(root,height=55,width=55,command = r7c2_move)
    r7c2.grid(row=7,column=2)
    r7c3 = Button(root,height=55,width=55,command = r7c3_move)
    r7c3.grid(row=7,column=3)
    r7c4 = Button(root,height=55,width=55,command = r7c4_move)
    r7c4.grid(row=7,column=4)
    r7c5 = Button(root,height=55,width=55,command = r7c5_move)
    r7c5.grid(row=7,column=5)
    r7c6 = Button(root,height=55,width=55,command = r7c6_move)
    r7c6.grid(row=7,column=6)
    r7c7 = Button(root,height=55,width=55,command = r7c7_move)
    r7c7.grid(row=7,column=7)
    r7c8 = Button(root,height=55,width=55,command = r7c8_move)
    r7c8.grid(row=7,column=8)
    
    r7c1.config(image=w_sol_w)
    r7c2.config(image=w_sol_b)
    r7c3.config(image=w_sol_w)
    r7c4.config(image=w_sol_b)
    r7c5.config(image=w_sol_w)
    r7c6.config(image=w_sol_b)
    r7c7.config(image=w_sol_w)
    r7c8.config(image=w_sol_b)

    r8c1 = Button(root,height=55,width=55,command = r8c1_move)
    r8c1.grid(row=8,column=1)
    r8c2 = Button(root,height=55,width=55,command = r8c2_move)
    r8c2.grid(row=8,column=2)
    r8c3 = Button(root,height=55,width=55,command = r8c3_move)
    r8c3.grid(row=8,column=3)
    r8c4 = Button(root,height=55,width=55,command = r8c4_move)
    r8c4.grid(row=8,column=4)
    r8c5 = Button(root,height=55,width=55,command = r8c5_move)
    r8c5.grid(row=8,column=5)
    r8c6 = Button(root,height=55,width=55,command = r8c6_move)
    r8c6.grid(row=8,column=6)
    r8c7 = Button(root,height=55,width=55,command = r8c7_move)
    r8c7.grid(row=8,column=7)
    r8c8 = Button(root,height=55,width=55,command = r8c8_move)
    r8c8.grid(row=8,column=8)

    r8c1.config(image=w_ele_b)
    r8c2.config(image=w_hor_w)
    r8c3.config(image=w_cam_b)
    r8c4.config(image=w_que_w)
    r8c5.config(image=w_king_b)
    r8c6.config(image=w_cam_w)
    r8c7.config(image=w_hor_b)
    r8c8.config(image=w_ele_w)

    m = Label(root,text = "\t  \t",bg="orange")
    m.grid(row=9,column=1)

    player = Label(root,text = "",font="99")
    player.grid(row=4,column=0)
    player.config(text = "Player : 1 \n White",bg="white",fg="Dark Blue")

#########################################################################################

    player_1 = Label(root,text = "      player 1",font="99",bg="orange")
    player_1.grid(row=5,column=9)

    player_1_ch = Label(root,text = " No. of cheat : ",font="39",bg="orange")
    player_1_ch.grid(row=6,column=9)

    player_1_tc = Label(root,text = " unit to kill : ",font="39",bg="orange")
    player_1_tc.grid(row=7,column=9)

    player_1_ch_rep = Label(root,font="39",bg="orange")
    player_1_ch_rep.grid(row=6,column=10)

    player_1_tc_rep = Label(root,font="39",bg="orange")
    player_1_tc_rep.grid(row=7,column=10)

    player_1_ch_rep.config(text = str(pl_1_ch))
    player_1_tc_rep.config(text = str(pl_1_tc))

    player_2 = Label(root,text = "      player 2",font="99",bg="orange")
    player_2.grid(row=1,column=9)

    player_2_ch = Label(root,text = " No. of cheat : ",font="39",bg="orange")
    player_2_ch.grid(row=2,column=9)

    player_2_tc = Label(root,text = " unit to kill : ",font="39",bg="orange")
    player_2_tc.grid(row=3,column=9)

    player_2_ch_rep = Label(root,font="39",bg="orange")
    player_2_ch_rep.grid(row=2,column=10)

    player_2_tc_rep = Label(root,font="39",bg="orange")
    player_2_tc_rep.grid(row=3,column=10)

    player_2_ch_rep.config(text = str(pl_2_ch))
    player_2_tc_rep.config(text = str(pl_2_tc))

    boundry = Label(root,text = "*****************",font="39",bg="orange")
    boundry.grid(row=4,column=9)
#############################################################################################

    root.bind('<Escape>',clear)
    r1c1.bind("<Button-3>",r1c1_cheat)
    r1c2.bind("<Button-3>",r1c2_cheat)
    r1c3.bind("<Button-3>",r1c3_cheat)
    r1c4.bind("<Button-3>",r1c4_cheat)
    r1c5.bind("<Button-3>",r1c5_cheat)
    r1c6.bind("<Button-3>",r1c6_cheat)
    r1c7.bind("<Button-3>",r1c7_cheat)
    r1c8.bind("<Button-3>",r1c8_cheat)
    r2c1.bind("<Button-3>",r2c1_cheat)
    r2c2.bind("<Button-3>",r2c2_cheat)
    r2c3.bind("<Button-3>",r2c3_cheat)
    r2c4.bind("<Button-3>",r2c4_cheat)
    r2c5.bind("<Button-3>",r2c5_cheat)
    r2c6.bind("<Button-3>",r2c6_cheat)
    r2c7.bind("<Button-3>",r2c7_cheat)
    r2c8.bind("<Button-3>",r2c8_cheat)
    r3c1.bind("<Button-3>",r3c1_cheat)
    r3c2.bind("<Button-3>",r3c2_cheat)
    r3c3.bind("<Button-3>",r3c3_cheat)
    r3c4.bind("<Button-3>",r3c4_cheat)
    r3c5.bind("<Button-3>",r3c5_cheat)
    r3c6.bind("<Button-3>",r3c6_cheat)
    r3c7.bind("<Button-3>",r3c7_cheat)
    r3c8.bind("<Button-3>",r3c8_cheat)
    r4c1.bind("<Button-3>",r4c1_cheat)
    r4c2.bind("<Button-3>",r4c2_cheat)
    r4c3.bind("<Button-3>",r4c3_cheat)
    r4c4.bind("<Button-3>",r4c4_cheat)
    r4c5.bind("<Button-3>",r4c5_cheat)
    r4c6.bind("<Button-3>",r4c6_cheat)
    r4c7.bind("<Button-3>",r4c7_cheat)
    r4c8.bind("<Button-3>",r4c8_cheat)
    r5c1.bind("<Button-3>",r5c1_cheat)
    r5c2.bind("<Button-3>",r5c2_cheat)
    r5c3.bind("<Button-3>",r5c3_cheat)
    r5c4.bind("<Button-3>",r5c4_cheat)
    r5c5.bind("<Button-3>",r5c5_cheat)
    r5c6.bind("<Button-3>",r5c6_cheat)
    r5c7.bind("<Button-3>",r5c7_cheat)
    r5c8.bind("<Button-3>",r5c8_cheat)
    r6c1.bind("<Button-3>",r6c1_cheat)
    r6c2.bind("<Button-3>",r6c2_cheat)
    r6c3.bind("<Button-3>",r6c3_cheat)
    r6c4.bind("<Button-3>",r6c4_cheat)
    r6c5.bind("<Button-3>",r6c5_cheat)
    r6c6.bind("<Button-3>",r6c6_cheat)
    r6c7.bind("<Button-3>",r6c7_cheat)
    r6c8.bind("<Button-3>",r6c8_cheat)
    r7c1.bind("<Button-3>",r7c1_cheat)
    r7c2.bind("<Button-3>",r7c2_cheat)
    r7c3.bind("<Button-3>",r7c3_cheat)
    r7c4.bind("<Button-3>",r7c4_cheat)
    r7c5.bind("<Button-3>",r7c5_cheat)
    r7c6.bind("<Button-3>",r7c6_cheat)
    r7c7.bind("<Button-3>",r7c7_cheat)
    r7c8.bind("<Button-3>",r7c8_cheat)
    r8c1.bind("<Button-3>",r8c1_cheat)
    r8c2.bind("<Button-3>",r8c2_cheat)
    r8c3.bind("<Button-3>",r8c3_cheat)
    r8c4.bind("<Button-3>",r8c4_cheat)
    r8c5.bind("<Button-3>",r8c5_cheat)
    r8c6.bind("<Button-3>",r8c6_cheat)
    r8c7.bind("<Button-3>",r8c7_cheat)
    r8c8.bind("<Button-3>",r8c8_cheat)

def clear(event):
    global unit
    global cheat_l
    global cheat_move_sol
    global cheat_move_unit
    global to_nut
    do(None)
    if to_nut != []:
        boundry.config(text = "*****************")
        i=0
        l=len(to_nut)
        while i<l:
            unit[0] = str(to_nut[i])
            normal()
            i=i+1
        to_nut = []
        cheat_l = []
        cheat_move_sol = 0
        cheat_move_unit = 0
    unit = ['n','n']
    
def clicked_unit_clr():
    
            global r1c1
            global r1c2
            global r1c3
            global r1c4
            global r1c5
            global r1c6
            global r1c7
            global r1c8
            global r2c1
            global r2c2
            global r2c3
            global r2c4
            global r2c5
            global r2c6
            global r2c7
            global r2c8
            global r3c1
            global r3c2
            global r3c3
            global r3c4
            global r3c5
            global r3c6
            global r3c7
            global r3c8
            global r4c1
            global r4c2
            global r4c3
            global r4c4
            global r4c5
            global r4c6
            global r4c7
            global r4c8
            global r5c1
            global r5c2
            global r5c3
            global r5c4
            global r5c5
            global r5c6
            global r5c7
            global r5c8
            global r6c1
            global r6c2
            global r6c3
            global r6c4
            global r6c5
            global r6c6
            global r6c7
            global r6c8
            global r7c1
            global r7c2
            global r7c3
            global r7c4
            global r7c5
            global r7c6
            global r7c7
            global r7c8
            global r8c1
            global r8c2
            global r8c3
            global r8c4
            global r8c5
            global r8c6
            global r8c7
            global r8c8
            x = p_row*10+p_column
            if x  == 11 :
                u = unit[1]
                if u == "b_sol":
                    r1c1.config(image=clicked_b_sol)
                if u == "w_sol":
                    r1c1.config(image=clicked_w_sol)
                if u == "b_ele":
                    r1c1.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r1c1.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r1c1.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r1c1.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r1c1.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r1c1.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r1c1.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r1c1.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r1c1.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r1c1.config(image=clicked_w_que)
                    

            if x  == 12 :
                u = unit[1]
                if u == "b_sol":
                    r1c2.config(image=clicked_b_sol)
                if u == "w_sol":
                    r1c2.config(image=clicked_w_sol)
                if u == "b_ele":
                    r1c2.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r1c2.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r1c2.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r1c2.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r1c2.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r1c2.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r1c2.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r1c2.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r1c2.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r1c2.config(image=clicked_w_que)
                    

            if x  == 13 :
                u = unit[1]
                if u == "b_sol":
                    r1c3.config(image=clicked_b_sol)
                if u == "w_sol":
                    r1c3.config(image=clicked_w_sol)
                if u == "b_ele":
                    r1c3.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r1c3.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r1c3.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r1c3.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r1c3.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r1c3.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r1c3.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r1c3.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r1c3.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r1c3.config(image=clicked_w_que)
                    

            if x  == 14 :
                u = unit[1]
                if u == "b_sol":
                    r1c4.config(image=clicked_b_sol)
                if u == "w_sol":
                    r1c4.config(image=clicked_w_sol)
                if u == "b_ele":
                    r1c4.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r1c4.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r1c4.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r1c4.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r1c4.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r1c4.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r1c4.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r1c4.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r1c4.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r1c4.config(image=clicked_w_que)
                    

            if x  == 15 :
                u = unit[1]
                if u == "b_sol":
                    r1c5.config(image=clicked_b_sol)
                if u == "w_sol":
                    r1c5.config(image=clicked_w_sol)
                if u == "b_ele":
                    r1c5.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r1c5.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r1c5.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r1c5.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r1c5.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r1c5.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r1c5.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r1c5.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r1c5.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r1c5.config(image=clicked_w_que)
                    
            if x  == 16 :
                u = unit[1]
                if u == "b_sol":
                    r1c6.config(image=clicked_b_sol)
                if u == "w_sol":
                    r1c6.config(image=clicked_w_sol)
                if u == "b_ele":
                    r1c6.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r1c6.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r1c6.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r1c6.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r1c6.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r1c6.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r1c6.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r1c6.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r1c6.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r1c6.config(image=clicked_w_que)
                    
            if x  == 17 :
                u = unit[1]
                if u == "b_sol":
                    r1c7.config(image=clicked_b_sol)
                if u == "w_sol":
                    r1c7.config(image=clicked_w_sol)
                if u == "b_ele":
                    r1c7.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r1c7.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r1c7.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r1c7.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r1c7.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r1c7.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r1c7.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r1c7.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r1c7.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r1c7.config(image=clicked_w_que)
                    
            if x  == 18 :
                u = unit[1]
                if u == "b_sol":
                    r1c8.config(image=clicked_b_sol)
                if u == "w_sol":
                    r1c8.config(image=clicked_w_sol)
                if u == "b_ele":
                    r1c8.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r1c8.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r1c8.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r1c8.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r1c8.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r1c8.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r1c8.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r1c8.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r1c8.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r1c8.config(image=clicked_w_que)
                    
            if x  == 21 :
                u = unit[1]
                if u == "b_sol":
                    r2c1.config(image=clicked_b_sol)
                if u == "w_sol":
                    r2c1.config(image=clicked_w_sol)
                if u == "b_ele":
                    r2c1.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r2c1.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r2c1.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r2c1.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r2c1.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r2c1.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r2c1.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r2c1.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r2c1.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r2c1.config(image=clicked_w_que)
                    
            if x  == 22 :
                u = unit[1]
                if u == "b_sol":
                    r2c2.config(image=clicked_b_sol)
                if u == "w_sol":
                    r2c2.config(image=clicked_w_sol)
                if u == "b_ele":
                    r2c2.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r2c2.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r2c2.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r2c2.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r2c2.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r2c2.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r2c2.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r2c2.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r2c2.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r2c2.config(image=clicked_w_que)
                    
            if x  == 23 :
                u = unit[1]
                if u == "b_sol":
                    r2c3.config(image=clicked_b_sol)
                if u == "w_sol":
                    r2c3.config(image=clicked_w_sol)
                if u == "b_ele":
                    r2c3.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r2c3.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r2c3.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r2c3.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r2c3.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r2c3.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r2c3.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r2c3.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r2c3.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r2c3.config(image=clicked_w_que)
                    
            if x  == 24 :
                u = unit[1]
                if u == "b_sol":
                    r2c4.config(image=clicked_b_sol)
                if u == "w_sol":
                    r2c4.config(image=clicked_w_sol)
                if u == "b_ele":
                    r2c4.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r2c4.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r2c4.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r2c4.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r2c4.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r2c4.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r2c4.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r2c4.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r2c4.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r2c4.config(image=clicked_w_que)
                    
            if x  == 25 :
                u = unit[1]
                if u == "b_sol":
                    r2c5.config(image=clicked_b_sol)
                if u == "w_sol":
                    r2c5.config(image=clicked_w_sol)
                if u == "b_ele":
                    r2c5.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r2c5.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r2c5.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r2c5.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r2c5.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r2c5.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r2c5.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r2c5.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r2c5.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r2c5.config(image=clicked_w_que)
                    
            if x  == 26 :
                u = unit[1]
                if u == "b_sol":
                    r2c6.config(image=clicked_b_sol)
                if u == "w_sol":
                    r2c6.config(image=clicked_w_sol)
                if u == "b_ele":
                    r2c6.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r2c6.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r2c6.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r2c6.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r2c6.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r2c6.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r2c6.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r2c6.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r2c6.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r2c6.config(image=clicked_w_que)
                    
            if x  == 27 :
                u = unit[1]
                if u == "b_sol":
                    r2c7.config(image=clicked_b_sol)
                if u == "w_sol":
                    r2c7.config(image=clicked_w_sol)
                if u == "b_ele":
                    r2c7.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r2c7.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r2c7.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r2c7.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r2c7.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r2c7.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r2c7.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r2c7.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r2c7.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r2c7.config(image=clicked_w_que)
                    
            if x  == 28 :
                u = unit[1]
                if u == "b_sol":
                    r2c8.config(image=clicked_b_sol)
                if u == "w_sol":
                    r2c8.config(image=clicked_w_sol)
                if u == "b_ele":
                    r2c8.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r2c8.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r2c8.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r2c8.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r2c8.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r2c8.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r2c8.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r2c8.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r2c8.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r2c8.config(image=clicked_w_que)
                    
            if x  == 31 :
                u = unit[1]
                if u == "b_sol":
                    r3c1.config(image=clicked_b_sol)
                if u == "w_sol":
                    r3c1.config(image=clicked_w_sol)
                if u == "b_ele":
                    r3c1.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r3c1.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r3c1.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r3c1.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r3c1.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r3c1.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r3c1.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r3c1.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r3c1.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r3c1.config(image=clicked_w_que)
                    
            if x  == 32 :
                u = unit[1]
                if u == "b_sol":
                    r3c2.config(image=clicked_b_sol)
                if u == "w_sol":
                    r3c2.config(image=clicked_w_sol)
                if u == "b_ele":
                    r3c2.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r3c2.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r3c2.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r3c2.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r3c2.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r3c2.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r3c2.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r3c2.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r3c2.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r3c2.config(image=clicked_w_que)
                    
            if x  == 33 :
                u = unit[1]
                if u == "b_sol":
                    r3c3.config(image=clicked_b_sol)
                if u == "w_sol":
                    r3c3.config(image=clicked_w_sol)
                if u == "b_ele":
                    r3c3.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r3c3.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r3c3.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r3c3.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r3c3.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r3c3.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r3c3.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r3c3.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r3c3.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r3c3.config(image=clicked_w_que)
                    
            if x  == 34 :
                u = unit[1]
                if u == "b_sol":
                    r3c4.config(image=clicked_b_sol)
                if u == "w_sol":
                    r3c4.config(image=clicked_w_sol)
                if u == "b_ele":
                    r3c4.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r3c4.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r3c4.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r3c4.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r3c4.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r3c4.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r3c4.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r3c4.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r3c4.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r3c4.config(image=clicked_w_que)
                    
            if x  == 35 :
                u = unit[1]
                if u == "b_sol":
                    r3c5.config(image=clicked_b_sol)
                if u == "w_sol":
                    r3c5.config(image=clicked_w_sol)
                if u == "b_ele":
                    r3c5.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r3c5.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r3c5.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r3c5.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r3c5.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r3c5.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r3c5.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r3c5.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r3c5.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r3c5.config(image=clicked_w_que)
                    
            if x  == 36 :
                u = unit[1]
                if u == "b_sol":
                    r3c6.config(image=clicked_b_sol)
                if u == "w_sol":
                    r3c6.config(image=clicked_w_sol)
                if u == "b_ele":
                    r3c6.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r3c6.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r3c6.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r3c6.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r3c6.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r3c6.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r3c6.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r3c6.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r3c6.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r3c6.config(image=clicked_w_que)
                    
            if x  == 37 :
                u = unit[1]
                if u == "b_sol":
                    r3c7.config(image=clicked_b_sol)
                if u == "w_sol":
                    r3c7.config(image=clicked_w_sol)
                if u == "b_ele":
                    r3c7.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r3c7.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r3c7.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r3c7.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r3c7.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r3c7.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r3c7.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r3c7.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r3c7.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r3c7.config(image=clicked_w_que)
                    
            if x  == 38 :
                u = unit[1]
                if u == "b_sol":
                    r3c8.config(image=clicked_b_sol)
                if u == "w_sol":
                    r3c8.config(image=clicked_w_sol)
                if u == "b_ele":
                    r3c8.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r3c8.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r3c8.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r3c8.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r3c8.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r3c8.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r3c8.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r3c8.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r3c8.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r3c8.config(image=clicked_w_que)
                    
            if x  == 41 :
                u = unit[1]
                if u == "b_sol":
                    r4c1.config(image=clicked_b_sol)
                if u == "w_sol":
                    r4c1.config(image=clicked_w_sol)
                if u == "b_ele":
                    r4c1.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r4c1.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r4c1.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r4c1.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r4c1.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r4c1.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r4c1.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r4c1.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r4c1.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r4c1.config(image=clicked_w_que)
                    
            if x  == 42 :
                u = unit[1]
                if u == "b_sol":
                    r4c2.config(image=clicked_b_sol)
                if u == "w_sol":
                    r4c2.config(image=clicked_w_sol)
                if u == "b_ele":
                    r4c2.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r4c2.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r4c2.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r4c2.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r4c2.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r4c2.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r4c2.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r4c2.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r4c2.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r4c2.config(image=clicked_w_que)
                    
            if x  == 43 :
                u = unit[1]
                if u == "b_sol":
                    r4c3.config(image=clicked_b_sol)
                if u == "w_sol":
                    r4c3.config(image=clicked_w_sol)
                if u == "b_ele":
                    r4c3.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r4c3.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r4c3.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r4c3.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r4c3.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r4c3.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r4c3.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r4c3.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r4c3.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r4c3.config(image=clicked_w_que)
                    
            if x  == 44 :
                u = unit[1]
                if u == "b_sol":
                    r4c4.config(image=clicked_b_sol)
                if u == "w_sol":
                    r4c4.config(image=clicked_w_sol)
                if u == "b_ele":
                    r4c4.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r4c4.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r4c4.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r4c4.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r4c4.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r4c4.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r4c4.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r4c4.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r4c4.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r4c4.config(image=clicked_w_que)
                    
            if x  == 45 :
                u = unit[1]
                if u == "b_sol":
                    r4c5.config(image=clicked_b_sol)
                if u == "w_sol":
                    r4c5.config(image=clicked_w_sol)
                if u == "b_ele":
                    r4c5.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r4c5.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r4c5.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r4c5.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r4c5.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r4c5.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r4c5.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r4c5.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r4c5.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r4c5.config(image=clicked_w_que)
                    
            if x  == 46 :
                u = unit[1]
                if u == "b_sol":
                    r4c6.config(image=clicked_b_sol)
                if u == "w_sol":
                    r4c6.config(image=clicked_w_sol)
                if u == "b_ele":
                    r4c6.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r4c6.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r4c6.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r4c6.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r4c6.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r4c6.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r4c6.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r4c6.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r4c6.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r4c6.config(image=clicked_w_que)
                    
            if x  == 47 :
                u = unit[1]
                if u == "b_sol":
                    r4c7.config(image=clicked_b_sol)
                if u == "w_sol":
                    r4c7.config(image=clicked_w_sol)
                if u == "b_ele":
                    r4c7.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r4c7.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r4c7.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r4c7.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r4c7.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r4c7.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r4c7.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r4c7.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r4c7.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r4c7.config(image=clicked_w_que)
                    
            if x  == 48 :
                u = unit[1]
                if u == "b_sol":
                    r4c8.config(image=clicked_b_sol)
                if u == "w_sol":
                    r4c8.config(image=clicked_w_sol)
                if u == "b_ele":
                    r4c8.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r4c8.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r4c8.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r4c8.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r4c8.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r4c8.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r4c8.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r4c8.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r4c8.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r4c8.config(image=clicked_w_que)
                    
            if x  == 51 :
                u = unit[1]
                if u == "b_sol":
                    r5c1.config(image=clicked_b_sol)
                if u == "w_sol":
                    r5c1.config(image=clicked_w_sol)
                if u == "b_ele":
                    r5c1.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r5c1.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r5c1.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r5c1.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r5c1.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r5c1.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r5c1.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r5c1.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r5c1.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r5c1.config(image=clicked_w_que)
                    
            if x  == 52 :
                u = unit[1]
                if u == "b_sol":
                    r5c2.config(image=clicked_b_sol)
                if u == "w_sol":
                    r5c2.config(image=clicked_w_sol)
                if u == "b_ele":
                    r5c2.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r5c2.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r5c2.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r5c2.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r5c2.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r5c2.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r5c2.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r5c2.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r5c2.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r5c2.config(image=clicked_w_que)
                    
            if x  == 53 :
                u = unit[1]
                if u == "b_sol":
                    r5c3.config(image=clicked_b_sol)
                if u == "w_sol":
                    r5c3.config(image=clicked_w_sol)
                if u == "b_ele":
                    r5c3.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r5c3.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r5c3.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r5c3.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r5c3.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r5c3.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r5c3.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r5c3.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r5c3.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r5c3.config(image=clicked_w_que)
                    
            if x  == 54 :
                u = unit[1]
                if u == "b_sol":
                    r5c4.config(image=clicked_b_sol)
                if u == "w_sol":
                    r5c4.config(image=clicked_w_sol)
                if u == "b_ele":
                    r5c4.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r5c4.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r5c4.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r5c4.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r5c4.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r5c4.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r5c4.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r5c4.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r5c4.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r5c4.config(image=clicked_w_que)
                    
            if x  == 55 :
                u = unit[1]
                if u == "b_sol":
                    r5c5.config(image=clicked_b_sol)
                if u == "w_sol":
                    r5c5.config(image=clicked_w_sol)
                if u == "b_ele":
                    r5c5.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r5c5.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r5c5.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r5c5.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r5c5.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r5c5.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r5c5.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r5c5.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r5c5.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r5c5.config(image=clicked_w_que)
                    
            if x  == 56 :
                u = unit[1]
                if u == "b_sol":
                    r5c6.config(image=clicked_b_sol)
                if u == "w_sol":
                    r5c6.config(image=clicked_w_sol)
                if u == "b_ele":
                    r5c6.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r5c6.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r5c6.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r5c6.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r5c6.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r5c6.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r5c6.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r5c6.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r5c6.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r5c6.config(image=clicked_w_que)
                    
            if x  == 57 :
                u = unit[1]
                if u == "b_sol":
                    r5c7.config(image=clicked_b_sol)
                if u == "w_sol":
                    r5c7.config(image=clicked_w_sol)
                if u == "b_ele":
                    r5c7.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r5c7.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r5c7.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r5c7.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r5c7.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r5c7.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r5c7.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r5c7.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r5c7.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r5c7.config(image=clicked_w_que)
                    
            if x  == 58 :
                u = unit[1]
                if u == "b_sol":
                    r5c8.config(image=clicked_b_sol)
                if u == "w_sol":
                    r5c8.config(image=clicked_w_sol)
                if u == "b_ele":
                    r5c8.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r5c8.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r5c8.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r5c8.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r5c8.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r5c8.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r5c8.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r5c8.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r5c8.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r5c8.config(image=clicked_w_que)
                    
            if x  == 61 :
                u = unit[1]
                if u == "b_sol":
                    r6c1.config(image=clicked_b_sol)
                if u == "w_sol":
                    r6c1.config(image=clicked_w_sol)
                if u == "b_ele":
                    r6c1.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r6c1.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r6c1.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r6c1.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r6c1.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r6c1.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r6c1.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r6c1.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r6c1.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r6c1.config(image=clicked_w_que)
                    
            if x  == 62 :
                u = unit[1]
                if u == "b_sol":
                    r6c2.config(image=clicked_b_sol)
                if u == "w_sol":
                    r6c2.config(image=clicked_w_sol)
                if u == "b_ele":
                    r6c2.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r6c2.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r6c2.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r6c2.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r6c2.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r6c2.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r6c2.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r6c2.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r6c2.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r6c2.config(image=clicked_w_que)
                    
            if x  == 63 :
                u = unit[1]
                if u == "b_sol":
                    r6c3.config(image=clicked_b_sol)
                if u == "w_sol":
                    r6c3.config(image=clicked_w_sol)
                if u == "b_ele":
                    r6c3.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r6c3.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r6c3.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r6c3.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r6c3.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r6c3.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r6c3.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r6c3.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r6c3.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r6c3.config(image=clicked_w_que)
                    
            if x  == 64 :
                u = unit[1]
                if u == "b_sol":
                    r6c4.config(image=clicked_b_sol)
                if u == "w_sol":
                    r6c4.config(image=clicked_w_sol)
                if u == "b_ele":
                    r6c4.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r6c4.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r6c4.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r6c4.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r6c4.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r6c4.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r6c4.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r6c4.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r6c4.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r6c4.config(image=clicked_w_que)
                    
            if x  == 65 :
                u = unit[1]
                if u == "b_sol":
                    r6c5.config(image=clicked_b_sol)
                if u == "w_sol":
                    r6c5.config(image=clicked_w_sol)
                if u == "b_ele":
                    r6c5.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r6c5.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r6c5.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r6c5.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r6c5.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r6c5.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r6c5.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r6c5.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r6c5.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r6c5.config(image=clicked_w_que)
                    
            if x  == 66 :
                u = unit[1]
                if u == "b_sol":
                    r6c6.config(image=clicked_b_sol)
                if u == "w_sol":
                    r6c6.config(image=clicked_w_sol)
                if u == "b_ele":
                    r6c6.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r6c6.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r6c6.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r6c6.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r6c6.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r6c6.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r6c6.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r6c6.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r6c6.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r6c6.config(image=clicked_w_que)
                    
            if x  == 67 :
                u = unit[1]
                if u == "b_sol":
                    r6c7.config(image=clicked_b_sol)
                if u == "w_sol":
                    r6c7.config(image=clicked_w_sol)
                if u == "b_ele":
                    r6c7.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r6c7.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r6c7.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r6c7.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r6c7.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r6c7.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r6c7.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r6c7.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r6c7.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r6c7.config(image=clicked_w_que)
                    
            if x  == 68 :
                u = unit[1]
                if u == "b_sol":
                    r6c8.config(image=clicked_b_sol)
                if u == "w_sol":
                    r6c8.config(image=clicked_w_sol)
                if u == "b_ele":
                    r6c8.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r6c8.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r6c8.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r6c8.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r6c8.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r6c8.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r6c8.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r6c8.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r6c8.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r6c8.config(image=clicked_w_que)
                    
            if x  == 71 :
                u = unit[1]
                if u == "b_sol":
                    r7c1.config(image=clicked_b_sol)
                if u == "w_sol":
                    r7c1.config(image=clicked_w_sol)
                if u == "b_ele":
                    r7c1.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r7c1.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r7c1.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r7c1.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r7c1.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r7c1.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r7c1.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r7c1.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r7c1.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r7c1.config(image=clicked_w_que)
                    
            if x  == 72 :
                u = unit[1]
                if u == "b_sol":
                    r7c2.config(image=clicked_b_sol)
                if u == "w_sol":
                    r7c2.config(image=clicked_w_sol)
                if u == "b_ele":
                    r7c2.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r7c2.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r7c2.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r7c2.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r7c2.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r7c2.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r7c2.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r7c2.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r7c2.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r7c2.config(image=clicked_w_que)
                    
            if x  == 73 :
                u = unit[1]
                if u == "b_sol":
                    r7c3.config(image=clicked_b_sol)
                if u == "w_sol":
                    r7c3.config(image=clicked_w_sol)
                if u == "b_ele":
                    r7c3.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r7c3.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r7c3.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r7c3.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r7c3.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r7c3.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r7c3.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r7c3.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r7c3.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r7c3.config(image=clicked_w_que)
                    
            if x  == 74 :
                u = unit[1]
                if u == "b_sol":
                    r7c4.config(image=clicked_b_sol)
                if u == "w_sol":
                    r7c4.config(image=clicked_w_sol)
                if u == "b_ele":
                    r7c4.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r7c4.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r7c4.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r7c4.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r7c4.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r7c4.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r7c4.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r7c4.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r7c4.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r7c4.config(image=clicked_w_que)
                    
            if x  == 75 :
                u = unit[1]
                if u == "b_sol":
                    r7c5.config(image=clicked_b_sol)
                if u == "w_sol":
                    r7c5.config(image=clicked_w_sol)
                if u == "b_ele":
                    r7c5.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r7c5.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r7c5.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r7c5.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r7c5.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r7c5.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r7c5.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r7c5.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r7c5.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r7c5.config(image=clicked_w_que)
                    
            if x  == 76 :
                u = unit[1]
                if u == "b_sol":
                    r7c6.config(image=clicked_b_sol)
                if u == "w_sol":
                    r7c6.config(image=clicked_w_sol)
                if u == "b_ele":
                    r7c6.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r7c6.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r7c6.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r7c6.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r7c6.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r7c6.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r7c6.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r7c6.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r7c6.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r7c6.config(image=clicked_w_que)
                    
            if x  == 77 :
                u = unit[1]
                if u == "b_sol":
                    r7c7.config(image=clicked_b_sol)
                if u == "w_sol":
                    r7c7.config(image=clicked_w_sol)
                if u == "b_ele":
                    r7c7.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r7c7.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r7c7.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r7c7.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r7c7.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r7c7.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r7c7.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r7c7.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r7c7.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r7c7.config(image=clicked_w_que)
                    
            if x  == 78 :
                u = unit[1]
                if u == "b_sol":
                    r7c8.config(image=clicked_b_sol)
                if u == "w_sol":
                    r7c8.config(image=clicked_w_sol)
                if u == "b_ele":
                    r7c8.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r7c8.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r7c8.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r7c8.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r7c8.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r7c8.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r7c8.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r7c8.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r7c8.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r7c8.config(image=clicked_w_que)
                    
            if x  == 81 :
                u = unit[1]
                if u == "b_sol":
                    r8c1.config(image=clicked_b_sol)
                if u == "w_sol":
                    r8c1.config(image=clicked_w_sol)
                if u == "b_ele":
                    r8c1.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r8c1.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r8c1.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r8c1.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r8c1.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r8c1.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r8c1.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r8c1.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r8c1.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r8c1.config(image=clicked_w_que)
                    
            if x  == 82 :
                u = unit[1]
                if u == "b_sol":
                    r8c2.config(image=clicked_b_sol)
                if u == "w_sol":
                    r8c2.config(image=clicked_w_sol)
                if u == "b_ele":
                    r8c2.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r8c2.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r8c2.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r8c2.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r8c2.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r8c2.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r8c2.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r8c2.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r8c2.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r8c2.config(image=clicked_w_que)
                    
            if x  == 83 :
                u = unit[1]
                if u == "b_sol":
                    r8c3.config(image=clicked_b_sol)
                if u == "w_sol":
                    r8c3.config(image=clicked_w_sol)
                if u == "b_ele":
                    r8c3.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r8c3.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r8c3.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r8c3.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r8c3.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r8c3.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r8c3.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r8c3.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r8c3.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r8c3.config(image=clicked_w_que)
                    
            if x  == 84 :
                u = unit[1]
                if u == "b_sol":
                    r8c4.config(image=clicked_b_sol)
                if u == "w_sol":
                    r8c4.config(image=clicked_w_sol)
                if u == "b_ele":
                    r8c4.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r8c4.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r8c4.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r8c4.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r8c4.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r8c4.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r8c4.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r8c4.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r8c4.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r8c4.config(image=clicked_w_que)
                    
            if x  == 85 :
                u = unit[1]
                if u == "b_sol":
                    r8c5.config(image=clicked_b_sol)
                if u == "w_sol":
                    r8c5.config(image=clicked_w_sol)
                if u == "b_ele":
                    r8c5.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r8c5.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r8c5.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r8c5.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r8c5.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r8c5.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r8c5.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r8c5.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r8c5.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r8c5.config(image=clicked_w_que)
                    
            if x  == 86 :
                u = unit[1]
                if u == "b_sol":
                    r8c6.config(image=clicked_b_sol)
                if u == "w_sol":
                    r8c6.config(image=clicked_w_sol)
                if u == "b_ele":
                    r8c6.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r8c6.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r8c6.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r8c6.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r8c6.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r8c6.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r8c6.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r8c6.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r8c6.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r8c6.config(image=clicked_w_que)
                    
            if x  == 87 :
                u = unit[1]
                if u == "b_sol":
                    r8c7.config(image=clicked_b_sol)
                if u == "w_sol":
                    r8c7.config(image=clicked_w_sol)
                if u == "b_ele":
                    r8c7.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r8c7.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r8c7.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r8c7.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r8c7.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r8c7.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r8c7.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r8c7.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r8c7.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r8c7.config(image=clicked_w_que)
                    
            if x  == 88 :
                u = unit[1]
                if u == "b_sol":
                    r8c8.config(image=clicked_b_sol)
                if u == "w_sol":
                    r8c8.config(image=clicked_w_sol)
                if u == "b_ele":
                    r8c8.config(image=clicked_b_ele)
                    
                if u == "w_ele":
                    r8c8.config(image=clicked_w_ele)
                    
                if u == "b_hor":
                    r8c8.config(image=clicked_b_hor)
                    
                if u == "w_hor":
                    r8c8.config(image=clicked_w_hor)
                    
                if u == "b_cam":
                    r8c8.config(image=clicked_b_cam)
                    
                if u == "w_cam":
                    r8c8.config(image=clicked_w_cam)
                    
                if u == "b_king":
                    r8c8.config(image=clicked_b_king)
                    
                if u == "w_king":
                    r8c8.config(image=clicked_w_king)
                    
                if u == "b_que":
                    r8c8.config(image=clicked_b_que)
                    
                if u == "w_que":
                    r8c8.config(image=clicked_w_que)
                    
                     


def check_move():                                               #  BRAIN
    global move_able
    
    place = unit[0]
    pic = unit[1]

    x = place[0]
    y = place[1]
    
    move_able = []
    u_row = None
    row = None
    d_row = None

    if place[0] == "1":
        u_row = row_0
        row = row_1
        d_row = row_2
    if place[0] == "2":
        u_row = row_1
        row = row_2
        d_row = row_3
    if place[0] == "3" :
        u_row = row_2
        row = row_3
        d_row = row_4
    if place[0] == "4":
        u_row = row_3
        row = row_4
        d_row = row_5
    if place[0] == "5" :
        u_row = row_4
        row = row_5
        d_row = row_6
    if place[0] == "6" :
        u_row = row_5
        row = row_6
        d_row = row_7
    if place[0] == "7" :
        u_row = row_6
        row = row_7
        d_row = row_8
    if place[0] == "8" :
        u_row = row_7
        row = row_8
        l_row = row_9

    if pic == "w_sol" or pic == "b_sol":
        if pic == "w_sol":
            if y=="1" or y=="8":
                if y=="1":
                    right_rough = u_row[int(y)+1]
                    if right_rough[0] == "b":                           # 63 64 65
                        move_able.append(int(place)-9)                  # 73 74 75
                    rough = u_row[int(y)]
                    if rough == "plate":
                        move_able.append(int(place)-10)
                    
                if y=="8":
                    left_rough = u_row[int(y)-1]
                    if left_rough[0] == "b":
                        move_able.append(int(place)-11)
                    rough = u_row[int(y)]
                    if rough == "plate":
                        move_able.append(int(place)-10)
                        
            else:
                right_rough = rough = u_row[int(y)+1]
                if right_rough[0] == "b":
                    move_able.append(int(place)-9)
                left_rough = rough = u_row[int(y)-1]
                if left_rough[0] == "b":
                    move_able.append(int(place)-11)
                rough = u_row[int(y)]
                if rough == "plate":
                    move_able.append(int(place)-10)
                
                
               
                
        if pic == "b_sol":
            if y=="1" or y=="8":
                if y=="1":
                    right_rough = d_row[int(y)+1]
                    if right_rough[0] == "w":                           # 63 64 65  [BLACK]
                        move_able.append(int(place)+11)                 # 73 74 75  [WHITE}
                    rough = d_row[int(y)]
                    if rough == "plate":
                        move_able.append(int(place)+10)
                if y=="8":
                    left_rough = d_row[int(y)-1]
                    if left_rough[0] == "w":
                        move_able.append(int(place)+9)
                    rough = d_row[int(y)]
                    if rough == "plate":
                        move_able.append(int(place)+10)
            else:
                right_rough = rough = d_row[int(y)+1]
                if right_rough[0] == "w":
                    move_able.append(int(place)+11)
                left_rough = rough = d_row[int(y)-1]
                if left_rough[0] == "w":
                    move_able.append(int(place)+9)
                rough = d_row[int(y)]
                if rough == "plate":
                    move_able.append(int(place)+10)

            
            
    if pic == "w_ele" or pic == "b_ele":
        if pic == "w_ele":
            
            
            y=int(place[1])
        
            clm = [row_9[y],row_8[y],row_7[y],row_6[y],row_5[y],row_4[y],row_3[y],row_2[y],row_1[y],row_0[y]]
    
            reached_plate = 9-int(place[0])
            on_plate = int(place)
            while True:
                reached_plate = reached_plate + 1
                if clm[reached_plate] == "wall" or clm[reached_plate][0] == "w":
                    break
                else:
                    on_plate = on_plate-10
                    move_able.append(on_plate)
                    if clm[reached_plate][0] == "b":
                        break
            reached_plate = 9-int(place[0])
            on_plate = int(place)
            while True:
                reached_plate = reached_plate - 1
                if clm[reached_plate] == "wall" or clm[reached_plate][0] == "w":
                    break
                else:
                    on_plate = on_plate+10
                    move_able.append(on_plate)
                    if clm[reached_plate][0] == "b":
                        break

            reached_plate = y
            on_plate = int(place)
            while True:
                reached_plate = reached_plate + 1
                if row[reached_plate] == "wall" or row[reached_plate][0] == "w":
                    break
                else:
                    on_plate = on_plate+1
                    move_able.append(on_plate)
                    if row[reached_plate][0] == "b":
                        break

            reached_plate = y
            on_plate = int(place)
            while True:
                reached_plate = reached_plate - 1
                if row[reached_plate] == "wall" or row[reached_plate][0] == "w":
                    break
                else:
                    on_plate = on_plate-1
                    move_able.append(on_plate)
                    if row[reached_plate][0] == "b":
                        break
                    
      
                        
        if pic == "b_ele":

            y=int(place[1])
        
            clm = [row_9[y],row_8[y],row_7[y],row_6[y],row_5[y],row_4[y],row_3[y],row_2[y],row_1[y],row_0[y]]
    
            reached_plate = 9-int(place[0])
            on_plate = int(place)
            while True:
                reached_plate = reached_plate + 1
                if clm[reached_plate] == "wall" or clm[reached_plate][0] == "b":
                    break
                else:
                    on_plate = on_plate-10
                    10
                    move_able.append(on_plate)
                    if clm[reached_plate][0] == "w":
                        break
            reached_plate = 9-int(place[0])
            on_plate = int(place)
            while True:
                reached_plate = reached_plate - 1
                if clm[reached_plate] == "wall" or clm[reached_plate][0] == "b":
                    break
                else:
                    on_plate = on_plate+10
                    move_able.append(on_plate)
                    if clm[reached_plate][0] == "w":
                        break

            reached_plate = y
            on_plate = int(place)
            while True:
                reached_plate = reached_plate + 1
                if row[reached_plate] == "wall" or row[reached_plate][0] == "b":
                    break
                else:
                    on_plate = on_plate+1
                    move_able.append(on_plate)
                    if row[reached_plate][0] == "w":
                        break

            reached_plate = y
            on_plate = int(place)
            while True:
                reached_plate = reached_plate - 1
                if row[reached_plate] == "wall" or row[reached_plate][0] == "b":
                    break
                else:
                    on_plate = on_plate-1
                    move_able.append(on_plate)
                    if row[reached_plate][0] == "w":
                        break
                

    if pic == "w_cam" or pic == "b_cam":
        if pic == "w_cam":
            
            y=int(place)
            x=y
            can = []
        
            while True:
                x = x-9
                s = str(x)
                if len(s)==1:
                    s="0"+s

                if int(s[0])>=9 or int(s[1])>=9 or int(s[0])<=0 or int(s[1])<=0:
                    break
                else:
                    can.append(s)

            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1


            y=int(place)
            x=y
            can = []
        
            while True:
                x = x-11
                s = str(x)
                if len(s)==1:
                    s="0"+s
        
                if int(s[0])>=9 or int(s[1])>=9 or int(s[0])<=0 or int(s[1])<=0:            #2
                    break
                else:
                    can.append(s)
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1    


            y=int(place)
            x=y
            can = []
        
            while True:
                x = x+9
                s = str(x)
                if len(s)==1:
                    s="0"+s
                if int(s[0])>=9 or int(s[1])>=9 or int(s[0])<=0 or int(s[1])<=0:
                    break
                else:
                    can.append(s)
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1


            y=int(place)
            x=y
            can = []
        
            while True:
                x = x+11
                s = str(x)
                if len(s)==1:
                    s="0"+s
        
                if int(s[0])>=9 or int(s[1])>=9 or int(s[0])<=0 or int(s[1])<=0:
                    break
                else:
                    can.append(s)
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1    
            

        if pic == "b_cam":

            y=int(place)
            x=y
            can = []
        
            while True:
                x = x-9
                s = str(x)
                if len(s)==1:
                    s="0"+s

                if int(s[0])>=9 or int(s[1])>=9 or int(s[0])<=0 or int(s[1])<=0:
                    break
                else:
                    can.append(s)

            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1


            y=int(place)
            x=y
            can = []
        
            while True:
                x = x-11
                s = str(x)
                if len(s)==1:
                    s="0"+s
        
                if int(s[0])>=9 or int(s[1])>=9 or int(s[0])<=0 or int(s[1])<=0:            #2
                    break
                else:
                    can.append(s)
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1    


            y=int(place)
            x=y
            can = []
        
            while True:
                x = x+9
                s = str(x)
                if len(s)==1:
                    s="0"+s
                if int(s[0])>=9 or int(s[1])>=9 or int(s[0])<=0 or int(s[1])<=0:
                    break
                else:
                    can.append(s)
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1


            y=int(place)
            x=y
            can = []
        
            while True:
                x = x+11
                s = str(x)
                if len(s)==1:
                    s="0"+s
        
                if int(s[0])>=9 or int(s[1])>=9 or int(s[0])<=0 or int(s[1])<=0:
                    break
                else:
                    can.append(s)
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1    
            

    if pic == "w_hor" or pic == "b_hor":
        if pic == "w_hor":
            x=int(place)
            can = [str(x-19),str(x-21),str(x-12),str(x+8),str(x+19),str(x+21),str(x+12),str(x-8)]  #82
             
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
          
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos[0]=="w":
                    can.remove(can[i])
                    i=i-1
                else:
                    move_able.append(int(can[i]))
                l = len(can)
                i=i+1     
            

        if pic == "b_hor":
            x=int(place)
            can = [str(x-19),str(x-21),str(x-12),str(x+8),str(x+19),str(x+21),str(x+12),str(x-8)]  #82
           
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                 
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
           
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos[0]=="b":
                    can.remove(can[i])
                    i=i-1
                else:
                    move_able.append(int(can[i]))
                l = len(can)
                i=i+1     
            
                        
    if pic == "w_que" or pic == "b_que":
        if pic == "w_que":
            x=int(place)
            can = [str(x+10),str(x+20),str(x+30),str(x+40),str(x+60),str(x+70),str(x+80)]
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1    


            can =[str(x-10),str(x-20),str(x-30),str(x-40),str(x-60),str(x-70),str(x-80)]

            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1    
            can =[str(x+11),str(x+22),str(x+33),str(x+44),str(x+55),str(x+66),str(x+77)]
            
            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1
            can =[str(x-11),str(x-22),str(x-33),str(x-44),str(x-55),str(x-66),str(x-77)]

            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1
            can =[str(x+9) ,str(x+18),str(x+27),str(x+36),str(x+45),str(x+54),str(x+63)]
            
            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1
            can =[str(x-9) ,str(x-18),str(x-27),str(x-36),str(x-45),str(x-54),str(x-63)]
            
            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1


            can =[str(x-1) ,str(x-2),str(x-3),str(x-4),str(x-5),str(x-6),str(x-7)]
            
            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1

            can =[str(x+1) ,str(x+2),str(x+3),str(x+4),str(x+5),str(x+6),str(x+7)]
            
            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="w":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="b":
                        break

                i=i+1

        if pic == "b_que":
            x=int(place)
            can = [str(x+10),str(x+20),str(x+30),str(x+40),str(x+60),str(x+70),str(x+80)]
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1    


            can =[str(x-10),str(x-20),str(x-30),str(x-40),str(x-60),str(x-70),str(x-80)]

            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1    
            can =[str(x+11),str(x+22),str(x+33),str(x+44),str(x+55),str(x+66),str(x+77)]
            
            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1
            can =[str(x-11),str(x-22),str(x-33),str(x-44),str(x-55),str(x-66),str(x-77)]

            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1
            can =[str(x+9) ,str(x+18),str(x+27),str(x+36),str(x+45),str(x+54),str(x+63)]
            
            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1
            can =[str(x-9) ,str(x-18),str(x-27),str(x-36),str(x-45),str(x-54),str(x-63)]
            
            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1


            can =[str(x-1) ,str(x-2),str(x-3),str(x-4),str(x-5),str(x-6),str(x-7)]
            
            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1

            can =[str(x+1) ,str(x+2),str(x+3),str(x+4),str(x+5),str(x+6),str(x+7)]
            
            x=int(place)
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
    
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos == "wall" or pos[0]=="b":
                    break
                else:
                    move_able.append(int(can[i]))
                    if pos[0]=="w":
                        break

                i=i+1


    if pic == "w_king" or pic == "b_king":
        if pic == "w_king":
            x = int(place)
            can = [str(x+10),str(x-10),str(x+1),str(x-1),str(x+11),str(x+9),str(x-11),str(x-9)]
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos[0]=="w":
                    can.remove(can[i])
                    i=i-1
                else:
                    move_able.append(int(can[i]))
                l = len(can)
                i=i+1     
            

        if pic == "b_king":
            x = int(place)
            can = [str(x+10),str(x-10),str(x+1),str(x-1),str(x+11),str(x+9),str(x-11),str(x-9)]
            i=0
            l=len(can)
            while i<l:
                s = can[i]      #                        ['63', '61', '74', '70', '103', '101', '94', '74']
                if int(s)>=89 or int(s)<=10:            #['63', '61', '74', '70', '101', '94', '74']
                    can.remove(s)
                    i=i-1
                l = len(can)
                i=i+1
            i=0
            l=len(can)
            while i<l:
                if can[i][0] == "1":
                    row = row_1
                if can[i][0] == "2":
                    row = row_2
                   
                if can[i][0] == "3" :
                    row = row_3
                  
                if can[i][0] == "4":
                    row = row_4
                    
                if can[i][0] == "5" :
                    row = row_5
                 
                if can[i][0] == "6" :
                    row = row_6
        
                if can[i][0] == "7" :
                    row = row_7
             
                if can[i][0] == "8" :
                    row = row_8

                pos = row[int(can[i][1])]

                if pos[0]=="b":
                    can.remove(can[i])
                    i=i-1
                else:
                    move_able.append(int(can[i]))
                l = len(can)
                i=i+1        
            
    if move_able != []:
        clicked_unit_clr()
    else:
        state[1] = 1
        tkMessageBox.showinfo("No place",no_move)

def GAME_END():
    r1c1.destroy()
    r1c2.destroy()
    r1c3.destroy()
    r1c4.destroy()
    r1c5.destroy()
    r1c6.destroy()
    r1c7.destroy()
    r1c8.destroy()
    r2c1.destroy()
    r2c2.destroy()
    r2c3.destroy()
    r2c4.destroy()
    r2c5.destroy()
    r2c6.destroy()
    r2c7.destroy()
    r2c8.destroy()
    r3c1.destroy()
    r3c2.destroy()
    r3c3.destroy()
    r3c4.destroy()
    r3c5.destroy()
    r3c6.destroy()
    r3c7.destroy()
    r3c8.destroy()
    r4c1.destroy()
    r4c2.destroy()
    r4c3.destroy()
    r4c4.destroy()
    r4c5.destroy()
    r4c6.destroy()
    r4c7.destroy()
    r4c8.destroy()
    r5c1.destroy()
    r5c2.destroy()
    r5c3.destroy()
    r5c4.destroy()
    r5c5.destroy()
    r5c6.destroy()
    r5c7.destroy()
    r5c8.destroy()
    r6c1.destroy()
    r6c2.destroy()
    r6c3.destroy()
    r6c4.destroy()
    r6c5.destroy()
    r6c6.destroy()
    r6c7.destroy()
    r6c8.destroy()
    r7c1.destroy()
    r7c2.destroy()
    r7c3.destroy()
    r7c4.destroy()
    r7c5.destroy()
    r7c6.destroy()
    r7c7.destroy()
    r7c8.destroy()
    r8c1.destroy()
    r8c2.destroy()
    r8c3.destroy()
    r8c4.destroy()
    r8c5.destroy()
    r8c6.destroy()
    r8c7.destroy()
    r8c8.destroy()
    player.destroy()
    player_1.destroy()
    player_1_ch.destroy()
    player_1_tc.destroy()
    player_1_ch_rep.destroy()
    player_1_tc_rep.destroy()
    player_2.destroy()
    player_2_ch.destroy()
    player_2_tc.destroy()
    player_2_ch_rep.destroy()
    player_2_tc_rep.destroy()
    boundry.destroy()
    


def king_died(place):
    place = str(place)
    if int(place[0]) == 1:
        row=row_1
    if int(place[0]) == 2:
        row=row_2
    if int(place[0]) == 3:
        row=row_3
    if int(place[0]) == 4:
        row=row_4
    if int(place[0]) == 5:
        row=row_5
    if int(place[0]) == 6:
        row=row_6
    if int(place[0]) == 7:
        row=row_7
    if int(place[0]) == 8:
        row=row_8

    if row[int(place[1])] == "b_king":
        GAME_END()
        l = Label(root,text="\n \n \n\n\n\n\nNICE GAME PLAYED BY \n\n PLAYER 1 \n\n MST KHELE BHAI .... ", bg= "orange",fg="purple",font="99")
        l.grid(row=2,column=2)
        return False

    elif  row[int(place[1])] == "w_king":
        GAME_END()
        l = Label(root,text="\n \n \n\n\n\n\nNICE GAME PLAYED BY \n \nPLAYER 2 \n\n MST KHELE BHAI .... ", bg= "orange",fg="purple",font="99")
        l.grid(row=2,column=2)
        return False

    else:
        return True
    

            
def main_move(): # 3120
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    global click
    global move_able
    global cheat_l
    global cheat_move_sol
    global cheat_move_unit
    global to_nut
    global whole_match
    global main_dic

    if p_row == 1:
        info = row_1[p_column]
    if p_row == 2:
        info = row_2[p_column]
    if p_row == 3:
        info = row_3[p_column]
    if p_row == 4:
        info = row_4[p_column]
    if p_row == 5:
        info = row_5[p_column]
    if p_row == 6:
        info = row_6[p_column]
    if p_row == 7:
        info = row_7[p_column]
    if p_row == 8:
        info = row_8[p_column]


    player = state[0]
    click = state[1]
  
    if click == 1:
        if cheat_l != []:
            i=0
            l=len(to_nut)
            while i<l:
                unit[0] = to_nut[i]
                normal()
                i=i+1
            
        if info == 'b_ele' or info ==  'b_hor' or info == 'b_cam' or info == 'b_que' or info == 'b_king' or info == 'w_ele' or info == 'w_hor' or info == 'w_cam' or info == 'w_que' or info == 'w_king' or info == 'b_sol' or info == 'w_sol' :
            if player == 1:
                if info == 'w_ele' or info == 'w_hor' or info == 'w_cam' or info == 'w_que' or info == 'w_king' or info == 'w_sol' :
                    state[1]=2
                    x = p_row*10+p_column
                    unit[0] = str(x)
                    unit[1] = info
                    check_move()
                            
                else:
                    if to_nut != []:
                        boundry.config(text = "*****************")
                        i=0
                        l=len(to_nut)
                        while i<l:
                            unit[0] = to_nut[i]
                            normal()
                            i=i+1
                        to_nut = []
                        cheat_l = []
                        cheat_move_sol = 0
                        cheat_move_unit = 0
                        unit = ['n','n']
                    tkMessageBox.showinfo("Wrong Player",wrong_player)
                    unit = ['n','n']
            if player == 2:
                if info == 'b_ele' or info == 'b_hor' or info == 'b_cam' or info == 'b_que' or info == 'b_king' or info == 'b_sol' :
                    state[1]=2
                    x = p_row*10+p_column
                    unit[0] = str(x)
                    unit[1] = info
                    check_move()
                else:
                    if to_nut != []:
                        boundry.config(text = "*****************")
                        i=0
                        l=len(to_nut)
                        while i<l:
                            unit[0] = to_nut[i]
                            normal()
                            i=i+1
                        to_nut = []
                        cheat_l = []
                        cheat_move_sol = 0
                        cheat_move_unit = 0
                    tkMessageBox.showinfo("Wrong Player",wrong_player)
                    unit = ['n','n']
    if click == 2 :
        place = p_row*10+p_column
        if place in move_able:
            if king_died(place):
                cheat_count()
                normal()
                state[1] = 1
                l = len(whole_match.keys())
                main_dic[unit[0]]="plate"
                main_dic[place]=unit[1]
                new_dic_game= {l+1:main_dic}
                whole_match.update(new_dic_game)
                if place == 11 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c1.config(image=b_sol_w)
                        row_1[1] = u
                    if u == "w_sol":
                        r1c1.config(image=w_sol_w)
                        row_1[1] = u
                    if u == "b_ele":
                        r1c1.config(image=b_ele_w)
                        row_1[1] = u
                    if u == "w_ele":
                        r1c1.config(image=w_ele_w)
                        row_1[1] = u
                    if u == "b_hor":
                        r1c1.config(image=b_hor_w)
                        row_1[1] = u
                    if u == "w_hor":
                        r1c1.config(image=w_hor_w)
                        row_1[1] = u
                    if u == "b_cam":
                        r1c1.config(image=b_cam_w)
                        row_1[1] = u
                    if u == "w_cam":
                        r1c1.config(image=w_cam_w)
                        row_1[1] = u
                    if u == "b_king":
                        r1c1.config(image=b_king_w)
                        row_1[1] = u
                    if u == "w_king":
                        r1c1.config(image=w_king_w)
                        row_1[1] = u
                    if u == "b_que":
                        r1c1.config(image=b_que_w)
                        row_1[1] = u
                    if u == "w_que":
                        r1c1.config(image=w_que_w)
                        row_1[1] = u
        ######################################################################
                        
                if place == 13 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c3.config(image=b_sol_w)
                        row_1[3] = u
                    if u == "w_sol":
                        r1c3.config(image=w_sol_w)
                        row_1[3] = u
                    if u == "b_ele":
                        r1c3.config(image=b_ele_w)
                        row_1[3] = u
                    if u == "w_ele":
                        r1c3.config(image=w_ele_w)
                        row_1[3] = u
                    if u == "b_hor":
                        r1c3.config(image=b_hor_w)
                        row_1[3] = u
                    if u == "w_hor":
                        r1c3.config(image=w_hor_w)
                        row_1[3] = u
                    if u == "b_cam":
                        r1c3.config(image=b_cam_w)
                        row_1[3] = u
                    if u == "w_cam":
                        r1c3.config(image=w_cam_w)
                        row_1[3] = u
                    if u == "b_king":
                        r1c3.config(image=b_king_w)
                        row_1[3] = u
                    if u == "w_king":
                        r1c3.config(image=w_king_w)
                        row_1[3] = u
                    if u == "b_que":
                        r1c3.config(image=b_que_w)
                        row_1[3] = u
                    if u == "w_que":
                        r1c3.config(image=w_que_w)
                        row_1[3] = u
        ##############################################################################################
                if place == 15 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c5.config(image=b_sol_w)
                        row_1[5] = u
                    if u == "w_sol":
                        r1c5.config(image=w_sol_w)
                        row_1[5] = u
                    if u == "b_ele":
                        r1c5.config(image=b_ele_w)
                        row_1[5] = u
                    if u == "w_ele":
                        r1c5.config(image=w_ele_w)
                        row_1[5] = u
                    if u == "b_hor":
                        r1c5.config(image=b_hor_w)
                        row_1[5] = u
                    if u == "w_hor":
                        r1c5.config(image=w_hor_w)
                        row_1[5] = u
                    if u == "b_cam":
                        r1c5.config(image=b_cam_w)
                        row_1[5] = u
                    if u == "w_cam":
                        r1c5.config(image=w_cam_w)
                        row_1[5] = u
                    if u == "b_king":
                        r1c5.config(image=b_king_w)
                        row_1[5] = u
                    if u == "w_king":
                        r1c5.config(image=w_king_w)
                        row_1[5] = u
                    if u == "b_que":
                        r1c5.config(image=b_que_w)
                        row_1[5] = u
                    if u == "w_que":
                        r1c5.config(image=w_que_w)
                        row_1[5] = u
        ######################################################################################
                if place == 17 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c7.config(image=b_sol_w)
                        row_1[7] = u
                    if u == "w_sol":
                        r1c7.config(image=w_sol_w)
                        row_1[7] = u
                    if u == "b_ele":
                        r1c7.config(image=b_ele_w)
                        row_1[7] = u
                    if u == "w_ele":
                        r1c7.config(image=w_ele_w)
                        row_1[7] = u
                    if u == "b_hor":
                        r1c7.config(image=b_hor_w)
                        row_1[7] = u
                    if u == "w_hor":
                        r1c7.config(image=w_hor_w)
                        row_1[7] = u
                    if u == "b_cam":
                        r1c7.config(image=b_cam_w)
                        row_1[7] = u
                    if u == "w_cam":
                        r1c7.config(image=w_cam_w)
                        row_1[7] = u
                    if u == "b_king":
                        r1c7.config(image=b_king_w)
                        row_1[7] = u
                    if u == "w_king":
                        r1c7.config(image=w_king_w)
                        row_1[7] = u
                    if u == "b_que":
                        r1c7.config(image=b_que_w)
                        row_1[7] = u
                    if u == "w_que":
                        r1c7.config(image=w_que_w)
                        row_1[7] = u
        ######################################################################################
                if place == 21 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c1.config(image=b_sol_b)
                        row_2[1] = u
                    if u == "w_sol":
                        r2c1.config(image=w_sol_b)
                        row_2[1] = u
                    if u == "b_ele":
                        r2c1.config(image=b_ele_b)
                        row_2[1] = u
                    if u == "w_ele":
                        r2c1.config(image=w_ele_b)
                        row_2[1] = u
                    if u == "b_hor":
                        r2c1.config(image=b_hor_b)
                        row_2[1] = u
                    if u == "w_hor":
                        r2c1.config(image=w_hor_b)
                        row_2[1] = u
                    if u == "b_cam":
                        r2c1.config(image=b_cam_b)
                        row_2[1] = u
                    if u == "w_cam":
                        r2c1.config(image=w_cam_b)
                        row_2[1] = u
                    if u == "b_king":
                        r2c1.config(image=b_king_b)
                        row_2[1] = u
                    if u == "w_king":
                        r2c1.config(image=w_king_b)
                        row_2[1] = u
                    if u == "b_que":
                        r2c1.config(image=b_que_b)
                        row_2[1] = u
                    if u == "w_que":
                        r2c1.config(image=w_que_b)
                        row_2[1] = u
        ######################################################################################
                if place == 23 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c3.config(image=b_sol_b)
                        row_2[3] = u
                    if u == "w_sol":
                        r2c3.config(image=w_sol_b)
                        row_2[3] = u
                    if u == "b_ele":
                        r2c3.config(image=b_ele_b)
                        row_2[3] = u
                    if u == "w_ele":
                        r2c3.config(image=w_ele_b)
                        row_2[3] = u
                    if u == "b_hor":
                        r2c3.config(image=b_hor_b)
                        row_2[3] = u
                    if u == "w_hor":
                        r2c3.config(image=w_hor_b)
                        row_2[3] = u
                    if u == "b_cam":
                        r2c3.config(image=b_cam_b)
                        row_2[3] = u
                    if u == "w_cam":
                        r2c3.config(image=w_cam_b)
                        row_2[3] = u
                    if u == "b_king":
                        r2c3.config(image=b_king_b)
                        row_2[3] = u
                    if u == "w_king":
                        r2c3.config(image=w_king_b)
                        row_2[3] = u
                    if u == "b_que":
                        r2c3.config(image=b_que_b)
                        row_2[3] = u
                    if u == "w_que":
                        r2c3.config(image=w_que_b)
                        row_2[3] = u
        ######################################################################################
                if place == 25 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c5.config(image=b_sol_b)
                        row_2[5] = u
                    if u == "w_sol":
                        r2c5.config(image=w_sol_b)
                        row_2[5] = u
                    if u == "b_ele":
                        r2c5.config(image=b_ele_b)
                        row_2[5] = u
                    if u == "w_ele":
                        r2c5.config(image=w_ele_b)
                        row_2[5] = u
                    if u == "b_hor":
                        r2c5.config(image=b_hor_b)
                        row_2[5] = u
                    if u == "w_hor":
                        r2c5.config(image=w_hor_b)
                        row_2[5] = u
                    if u == "b_cam":
                        r2c5.config(image=b_cam_b)
                        row_2[5] = u
                    if u == "w_cam":
                        r2c5.config(image=w_cam_b)
                        row_2[5] = u
                    if u == "b_king":
                        r2c5.config(image=b_king_b)
                        row_2[5] = u
                    if u == "w_king":
                        r2c5.config(image=w_king_b)
                        row_2[5] = u
                    if u == "b_que":
                        r2c5.config(image=b_que_b)
                        row_2[5] = u
                    if u == "w_que":
                        r2c5.config(image=w_que_b)
                        row_2[5] = u
        ######################################################################################
                if place == 27 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c7.config(image=b_sol_b)
                        row_2[7] = u
                    if u == "w_sol":
                        r2c7.config(image=w_sol_b)
                        row_2[7] = u
                    if u == "b_ele":
                        r2c7.config(image=b_ele_b)
                        row_2[7] = u
                    if u == "w_ele":
                        r2c7.config(image=w_ele_b)
                        row_2[7] = u
                    if u == "b_hor":
                        r2c7.config(image=b_hor_b)
                        row_2[7] = u
                    if u == "w_hor":
                        r2c7.config(image=w_hor_b)
                        row_2[7] = u
                    if u == "b_cam":
                        r2c7.config(image=b_cam_b)
                        row_2[7] = u
                    if u == "w_cam":
                        r2c7.config(image=w_cam_b)
                        row_2[7] = u
                    if u == "b_king":
                        r2c7.config(image=b_king_b)
                        row_2[7] = u
                    if u == "w_king":
                        r2c7.config(image=w_king_b)
                        row_2[7] = u
                    if u == "b_que":
                        r2c7.config(image=b_que_b)
                        row_2[7] = u
                    if u == "w_que":
                        r2c7.config(image=w_que_b)
                        row_2[7] = u
        ######################################################################################
                if place == 31 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c1.config(image=b_sol_w)
                        row_3[1] = u
                    if u == "w_sol":
                        r3c1.config(image=w_sol_w)
                        row_3[1] = u
                    if u == "b_ele":
                        r3c1.config(image=b_ele_w)
                        row_3[1] = u
                    if u == "w_ele":
                        r3c1.config(image=w_ele_w)
                        row_3[1] = u
                    if u == "b_hor":
                        r3c1.config(image=b_hor_w)
                        row_3[1] = u
                    if u == "w_hor":
                        r3c1.config(image=w_hor_w)
                        row_3[1] = u
                    if u == "b_cam":
                        r3c1.config(image=b_cam_w)
                        row_3[1] = u
                    if u == "w_cam":
                        r3c1.config(image=w_cam_w)
                        row_3[1] = u
                    if u == "b_king":
                        r3c1.config(image=b_king_w)
                        row_3[1] = u
                    if u == "w_king":
                        r3c1.config(image=w_king_w)
                        row_3[1] = u
                    if u == "b_que":
                        r3c1.config(image=b_que_w)
                        row_3[1] = u
                    if u == "w_que":
                        r3c1.config(image=w_que_w)
                        row_3[1] = u
        ######################################################################################
                if place == 33 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c3.config(image=b_sol_w)
                        row_3[3] = u
                    if u == "w_sol":
                        r3c3.config(image=w_sol_w)
                        row_3[3] = u
                    if u == "b_ele":
                        r3c3.config(image=b_ele_w)
                        row_3[3] = u
                    if u == "w_ele":
                        r3c3.config(image=w_ele_w)
                        row_3[3] = u
                    if u == "b_hor":
                        r3c3.config(image=b_hor_w)
                        row_3[3] = u
                    if u == "w_hor":
                        r3c3.config(image=w_hor_w)
                        row_3[3] = u
                    if u == "b_cam":
                        r3c3.config(image=b_cam_w)
                        row_3[3] = u
                    if u == "w_cam":
                        r3c3.config(image=w_cam_w)
                        row_3[3] = u
                    if u == "b_king":
                        r3c3.config(image=b_king_w)
                        row_3[3] = u
                    if u == "w_king":
                        r3c3.config(image=w_king_w)
                        row_3[3] = u
                    if u == "b_que":
                        r3c3.config(image=b_que_w)
                        row_3[3] = u
                    if u == "w_que":
                        r3c3.config(image=w_que_w)
                        row_3[3] = u
        ######################################################################################
                if place == 35 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c5.config(image=b_sol_w)
                        row_3[5] = u
                    if u == "w_sol":
                        r3c5.config(image=w_sol_w)
                        row_3[5] = u
                    if u == "b_ele":
                        r3c5.config(image=b_ele_w)
                        row_3[5] = u
                    if u == "w_ele":
                        r3c5.config(image=w_ele_w)
                        row_3[5] = u
                    if u == "b_hor":
                        r3c5.config(image=b_hor_w)
                        row_3[5] = u
                    if u == "w_hor":
                        r3c5.config(image=w_hor_w)
                        row_3[5] = u
                    if u == "b_cam":
                        r3c5.config(image=b_cam_w)
                        row_3[5] = u
                    if u == "w_cam":
                        r3c5.config(image=w_cam_w)
                        row_3[5] = u
                    if u == "b_king":
                        r3c5.config(image=b_king_w)
                        row_3[5] = u
                    if u == "w_king":
                        r3c5.config(image=w_king_w)
                        row_3[5] = u
                    if u == "b_que":
                        r3c5.config(image=b_que_w)
                        row_3[5] = u
                    if u == "w_que":
                        r3c5.config(image=w_que_w)
                        row_3[5] = u
        ######################################################################################
                if place == 37 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c7.config(image=b_sol_w)
                        row_3[7] = u
                    if u == "w_sol":
                        r3c7.config(image=w_sol_w)
                        row_3[7] = u
                    if u == "b_ele":
                        r3c7.config(image=b_ele_w)
                        row_3[7] = u
                    if u == "w_ele":
                        r3c7.config(image=w_ele_w)
                        row_3[7] = u
                    if u == "b_hor":
                        r3c7.config(image=b_hor_w)
                        row_3[7] = u
                    if u == "w_hor":
                        r3c7.config(image=w_hor_w)
                        row_3[7] = u
                    if u == "b_cam":
                        r3c7.config(image=b_cam_w)
                        row_3[7] = u
                    if u == "w_cam":
                        r3c7.config(image=w_cam_w)
                        row_3[7] = u
                    if u == "b_king":
                        r3c7.config(image=b_king_w)
                        row_3[7] = u
                    if u == "w_king":
                        r3c7.config(image=w_king_w)
                        row_3[7] = u
                    if u == "b_que":
                        r3c7.config(image=b_que_w)
                        row_3[7] = u
                    if u == "w_que":
                        r3c7.config(image=w_que_w)
                        row_3[7] = u
        ######################################################################################
                if place == 41 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c1.config(image=b_sol_b)
                        row_4[1] = u
                    if u == "w_sol":
                        r4c1.config(image=w_sol_b)
                        row_4[1] = u
                    if u == "b_ele":
                        r4c1.config(image=b_ele_b)
                        row_4[1] = u
                    if u == "w_ele":
                        r4c1.config(image=w_ele_b)
                        row_4[1] = u
                    if u == "b_hor":
                        r4c1.config(image=b_hor_b)
                        row_4[1] = u
                    if u == "w_hor":
                        r4c1.config(image=w_hor_b)
                        row_4[1] = u
                    if u == "b_cam":
                        r4c1.config(image=b_cam_b)
                        row_4[1] = u
                    if u == "w_cam":
                        r4c1.config(image=w_cam_b)
                        row_4[1] = u
                    if u == "b_king":
                        r4c1.config(image=b_king_b)
                        row_4[1] = u
                    if u == "w_king":
                        r4c1.config(image=w_king_b)
                        row_4[1] = u
                    if u == "b_que":
                        r4c1.config(image=b_que_b)
                        row_4[1] = u
                    if u == "w_que":
                        r4c1.config(image=w_que_b)
                        row_4[1] = u
        ######################################################################################
                if place == 43 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c3.config(image=b_sol_b)
                        row_4[3] = u
                    if u == "w_sol":
                        r4c3.config(image=w_sol_b)
                        row_4[3] = u
                    if u == "b_ele":
                        r4c3.config(image=b_ele_b)
                        row_4[3] = u
                    if u == "w_ele":
                        r4c3.config(image=w_ele_b)
                        row_4[3] = u
                    if u == "b_hor":
                        r4c3.config(image=b_hor_b)
                        row_4[3] = u
                    if u == "w_hor":
                        r4c3.config(image=w_hor_b)
                        row_4[3] = u
                    if u == "b_cam":
                        r4c3.config(image=b_cam_b)
                        row_4[3] = u
                    if u == "w_cam":
                        r4c3.config(image=w_cam_b)
                        row_4[3] = u
                    if u == "b_king":
                        r4c3.config(image=b_king_b)
                        row_4[3] = u
                    if u == "w_king":
                        r4c3.config(image=w_king_b)
                        row_4[3] = u
                    if u == "b_que":
                        r4c3.config(image=b_que_b)
                        row_4[3] = u
                    if u == "w_que":
                        r4c3.config(image=w_que_b)
                        row_4[3] = u
        ######################################################################################
                if place == 45 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c5.config(image=b_sol_b)
                        row_4[5] = u
                    if u == "w_sol":
                        r4c5.config(image=w_sol_b)
                        row_4[5] = u
                    if u == "b_ele":
                        r4c5.config(image=b_ele_b)
                        row_4[5] = u
                    if u == "w_ele":
                        r4c5.config(image=w_ele_b)
                        row_4[5] = u
                    if u == "b_hor":
                        r4c5.config(image=b_hor_b)
                        row_4[5] = u
                    if u == "w_hor":
                        r4c5.config(image=w_hor_b)
                        row_4[5] = u
                    if u == "b_cam":
                        r4c5.config(image=b_cam_b)
                        row_4[5] = u
                    if u == "w_cam":
                        r4c5.config(image=w_cam_b)
                        row_4[5] = u
                    if u == "b_king":
                        r4c5.config(image=b_king_b)
                        row_4[5] = u
                    if u == "w_king":
                        r4c5.config(image=w_king_b)
                        row_4[5] = u
                    if u == "b_que":
                        r4c5.config(image=b_que_b)
                        row_4[5] = u
                    if u == "w_que":
                        r4c5.config(image=w_que_b)
                        row_4[5] = u
        ######################################################################################
                if place == 47 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c7.config(image=b_sol_b)
                        row_4[7] = u
                    if u == "w_sol":
                        r4c7.config(image=w_sol_b)
                        row_4[7] = u
                    if u == "b_ele":
                        r4c7.config(image=b_ele_b)
                        row_4[7] = u
                    if u == "w_ele":
                        r4c7.config(image=w_ele_b)
                        row_4[7] = u
                    if u == "b_hor":
                        r4c7.config(image=b_hor_b)
                        row_4[7] = u
                    if u == "w_hor":
                        r4c7.config(image=w_hor_b)
                        row_4[7] = u
                    if u == "b_cam":
                        r4c7.config(image=b_cam_b)
                        row_4[7] = u
                    if u == "w_cam":
                        r4c7.config(image=w_cam_b)
                        row_4[7] = u
                    if u == "b_king":
                        r4c7.config(image=b_king_b)
                        row_4[7] = u
                    if u == "w_king":
                        r4c7.config(image=w_king_b)
                        row_4[7] = u
                    if u == "b_que":
                        r4c7.config(image=b_que_b)
                        row_4[7] = u
                    if u == "w_que":
                        r4c7.config(image=w_que_b)
                        row_4[7] = u
        ######################################################################################
                if place == 51 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c1.config(image=b_sol_w)
                        row_5[1] = u
                    if u == "w_sol":
                        r5c1.config(image=w_sol_w)
                        row_5[1] = u
                    if u == "b_ele":
                        r5c1.config(image=b_ele_w)
                        row_5[1] = u
                    if u == "w_ele":
                        r5c1.config(image=w_ele_w)
                        row_5[1] = u
                    if u == "b_hor":
                        r5c1.config(image=b_hor_w)
                        row_5[1] = u
                    if u == "w_hor":
                        r5c1.config(image=w_hor_w)
                        row_5[1] = u
                    if u == "b_cam":
                        r5c1.config(image=b_cam_w)
                        row_5[1] = u
                    if u == "w_cam":
                        r5c1.config(image=w_cam_w)
                        row_5[1] = u
                    if u == "b_king":
                        r5c1.config(image=b_king_w)
                        row_5[1] = u
                    if u == "w_king":
                        r5c1.config(image=w_king_w)
                        row_5[1] = u
                    if u == "b_que":
                        r5c1.config(image=b_que_w)
                        row_5[1] = u
                    if u == "w_que":
                        r5c1.config(image=w_que_w)
                        row_5[1] = u
        ######################################################################################
                if place == 53 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c3.config(image=b_sol_w)
                        row_5[3] = u
                    if u == "w_sol":
                        r5c3.config(image=w_sol_w)
                        row_5[3] = u
                    if u == "b_ele":
                        r5c3.config(image=b_ele_w)
                        row_5[3] = u
                    if u == "w_ele":
                        r5c3.config(image=w_ele_w)
                        row_5[3] = u
                    if u == "b_hor":
                        r5c3.config(image=b_hor_w)
                        row_5[3] = u
                    if u == "w_hor":
                        r5c3.config(image=w_hor_w)
                        row_5[3] = u
                    if u == "b_cam":
                        r5c3.config(image=b_cam_w)
                        row_5[3] = u
                    if u == "w_cam":
                        r5c3.config(image=w_cam_w)
                        row_5[3] = u
                    if u == "b_king":
                        r5c3.config(image=b_king_w)
                        row_5[3] = u
                    if u == "w_king":
                        r5c3.config(image=w_king_w)
                        row_5[3] = u
                    if u == "b_que":
                        r5c3.config(image=b_que_w)
                        row_5[3] = u
                    if u == "w_que":
                        r5c3.config(image=w_que_w)
                        row_5[3] = u
        ######################################################################################
                if place == 55 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c5.config(image=b_sol_w)
                        row_5[5] = u
                    if u == "w_sol":
                        r5c5.config(image=w_sol_w)
                        row_5[5] = u
                    if u == "b_ele":
                        r5c5.config(image=b_ele_w)
                        row_5[5] = u
                    if u == "w_ele":
                        r5c5.config(image=w_ele_w)
                        row_5[5] = u
                    if u == "b_hor":
                        r5c5.config(image=b_hor_w)
                        row_5[5] = u
                    if u == "w_hor":
                        r5c5.config(image=w_hor_w)
                        row_5[5] = u
                    if u == "b_cam":
                        r5c5.config(image=b_cam_w)
                        row_5[5] = u
                    if u == "w_cam":
                        r5c5.config(image=w_cam_w)
                        row_5[5] = u
                    if u == "b_king":
                        r5c5.config(image=b_king_w)
                        row_5[5] = u
                    if u == "w_king":
                        r5c5.config(image=w_king_w)
                        row_5[5] = u
                    if u == "b_que":
                        r5c5.config(image=b_que_w)
                        row_5[5] = u
                    if u == "w_que":
                        r5c5.config(image=w_que_w)
                        row_5[5] = u
        ######################################################################################
                if place == 57 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c7.config(image=b_sol_w)
                        row_5[7] = u
                    if u == "w_sol":
                        r5c7.config(image=w_sol_w)
                        row_5[7] = u
                    if u == "b_ele":
                        r5c7.config(image=b_ele_w)
                        row_5[7] = u
                    if u == "w_ele":
                        r5c7.config(image=w_ele_w)
                        row_5[7] = u
                    if u == "b_hor":
                        r5c7.config(image=b_hor_w)
                        row_5[7] = u
                    if u == "w_hor":
                        r5c7.config(image=w_hor_w)
                        row_5[7] = u
                    if u == "b_cam":
                        r5c7.config(image=b_cam_w)
                        row_5[7] = u
                    if u == "w_cam":
                        r5c7.config(image=w_cam_w)
                        row_5[7] = u
                    if u == "b_king":
                        r5c7.config(image=b_king_w)
                        row_5[7] = u
                    if u == "w_king":
                        r5c7.config(image=w_king_w)
                        row_5[7] = u
                    if u == "b_que":
                        r5c7.config(image=b_que_w)
                        row_5[7] = u
                    if u == "w_que":
                        r5c7.config(image=w_que_w)
                        row_5[7] = u
        ################################
                        #######################
                if place == 61 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c1.config(image=b_sol_b)
                        row_6[1] = u
                    if u == "w_sol":
                        r6c1.config(image=w_sol_b)
                        row_6[1] = u
                    if u == "b_ele":
                        r6c1.config(image=b_ele_b)
                        row_6[1] = u
                    if u == "w_ele":
                        r6c1.config(image=w_ele_b)
                        row_6[1] = u
                    if u == "b_hor":
                        r6c1.config(image=b_hor_b)
                        row_6[1] = u
                    if u == "w_hor":
                        r6c1.config(image=w_hor_b)
                        row_6[1] = u
                    if u == "b_cam":
                        r6c1.config(image=b_cam_b)
                        row_6[1] = u
                    if u == "w_cam":
                        r6c1.config(image=w_cam_b)
                        row_6[1] = u
                    if u == "b_king":
                        r6c1.config(image=b_king_b)
                        row_6[1] = u
                    if u == "w_king":
                        r6c1.config(image=w_king_b)
                        row_6[1] = u
                    if u == "b_que":
                        r6c1.config(image=b_que_b) 
                        row_6[1] = u
                    if u == "w_que":
                        r6c1.config(image=w_que_b)
                        row_6[1] = u
        ######################################################################################
                if place == 63 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c3.config(image=b_sol_b)
                        row_6[3] = u
                    if u == "w_sol":
                        r6c3.config(image=w_sol_b)
                        row_6[3] = u
                    if u == "b_ele":
                        r6c3.config(image=b_ele_b)
                        row_6[3] = u
                    if u == "w_ele":
                        r6c3.config(image=w_ele_b)
                        row_6[3] = u
                    if u == "b_hor":
                        r6c3.config(image=b_hor_b)
                        row_6[3] = u
                    if u == "w_hor":
                        r6c3.config(image=w_hor_b)
                        row_6[3] = u
                    if u == "b_cam":
                        r6c3.config(image=b_cam_b)
                        row_6[3] = u
                    if u == "w_cam":
                        r6c3.config(image=w_cam_b)
                        row_6[3] = u
                    if u == "b_king":
                        r6c3.config(image=b_king_b)
                        row_6[3] = u
                    if u == "w_king":
                        r6c3.config(image=w_king_b)
                        row_6[3] = u
                    if u == "b_que":
                        r6c3.config(image=b_que_b)
                        row_6[3] = u
                    if u == "w_que":
                        r6c3.config(image=w_que_b)
                        row_6[3] = u
        ######################################################################################
                if place == 65 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c5.config(image=b_sol_b)
                        row_6[5] = u
                    if u == "w_sol":
                        r6c5.config(image=w_sol_b)
                        row_6[5] = u
                    if u == "b_ele":
                        r6c5.config(image=b_ele_b)
                        row_6[5] = u
                    if u == "w_ele":
                        r6c5.config(image=w_ele_b)
                        row_6[5] = u
                    if u == "b_hor":
                        r6c5.config(image=b_hor_b)
                        row_6[5] = u
                    if u == "w_hor":
                        r6c5.config(image=w_hor_b)
                        row_6[5] = u
                    if u == "b_cam":
                        r6c5.config(image=b_cam_b)
                        row_6[5] = u
                    if u == "w_cam":
                        r6c5.config(image=w_cam_b)
                        row_6[5] = u
                    if u == "b_king":
                        r6c5.config(image=b_king_b)
                        row_6[5] = u
                    if u == "w_king":
                        r6c5.config(image=w_king_b)
                        row_6[5] = u
                    if u == "b_que":
                        r6c5.config(image=b_que_b)
                        row_6[5] = u
                    if u == "w_que":
                        r6c5.config(image=w_que_b)
                        row_6[5] = u
        ######################################################################################
                if place == 67 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c7.config(image=b_sol_b)
                        row_6[7] = u
                    if u == "w_sol":
                        r6c7.config(image=w_sol_b)
                        row_6[7] = u
                    if u == "b_ele":
                        r6c7.config(image=b_ele_b)
                        row_6[7] = u
                    if u == "w_ele":
                        r6c7.config(image=w_ele_b)
                        row_6[7] = u
                    if u == "b_hor":
                        r6c7.config(image=b_hor_b)
                        row_6[7] = u
                    if u == "w_hor":
                        r6c7.config(image=w_hor_b)
                        row_6[7] = u
                    if u == "b_cam":
                        r6c7.config(image=b_cam_b)
                        row_6[7] = u
                    if u == "w_cam":
                        r6c7.config(image=w_cam_b)
                        row_6[7] = u
                    if u == "b_king":
                        r6c7.config(image=b_king_b)
                        row_6[7] = u
                    if u == "w_king":
                        r6c7.config(image=w_king_b)
                        row_6[7] = u
                    if u == "b_que":
                        r6c7.config(image=b_que_b)
                        row_6[7] = u
                    if u == "w_que":
                        r6c7.config(image=w_que_b)
                        row_6[7] = u
        ######################################################################################
                if place == 71 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c1.config(image=b_sol_w)
                        row_7[1] = u
                    if u == "w_sol":
                        r7c1.config(image=w_sol_w)
                        row_7[1] = u
                    if u == "b_ele":
                        r7c1.config(image=b_ele_w)
                        row_7[1] = u
                    if u == "w_ele":
                        r7c1.config(image=w_ele_w)
                        row_7[1] = u
                    if u == "b_hor":
                        r7c1.config(image=b_hor_w)
                        row_7[1] = u
                    if u == "w_hor":
                        r7c1.config(image=w_hor_w)
                        row_7[1] = u
                    if u == "b_cam":
                        r7c1.config(image=b_cam_w)
                        row_7[1] = u
                    if u == "w_cam":
                        r7c1.config(image=w_cam_w)
                        row_7[1] = u
                    if u == "b_king":
                        r7c1.config(image=b_king_w)
                        row_7[1] = u
                    if u == "w_king":
                        r7c1.config(image=w_king_w)
                        row_7[1] = u
                    if u == "b_que":
                        r7c1.config(image=b_que_w)
                        row_7[1] = u
                    if u == "w_que":
                        r7c1.config(image=w_que_w)
                        row_7[1] = u
        ######################################################################################
                if place == 73 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c3.config(image=b_sol_w)
                        row_7[3] = u
                    if u == "w_sol":
                        r7c3.config(image=w_sol_w)
                        row_7[3] = u
                    if u == "b_ele":
                        r7c3.config(image=b_ele_w)
                        row_7[3] = u
                    if u == "w_ele":
                        r7c3.config(image=w_ele_w)
                        row_7[3] = u
                    if u == "b_hor":
                        r7c3.config(image=b_hor_w)
                        row_7[3] = u
                    if u == "w_hor":
                        r7c3.config(image=w_hor_w)
                        row_7[3] = u
                    if u == "b_cam":
                        r7c3.config(image=b_cam_w)
                        row_7[3] = u
                    if u == "w_cam":
                        r7c3.config(image=w_cam_w)
                        row_7[3] = u
                    if u == "b_king":
                        r7c3.config(image=b_king_w)
                        row_7[3] = u
                    if u == "w_king":
                        r7c3.config(image=w_king_w)
                        row_7[3] = u
                    if u == "b_que":
                        r7c3.config(image=b_que_w)
                        row_7[3] = u
                    if u == "w_que":
                        r7c3.config(image=w_que_w)
                        row_7[3] = u
        ######################################################################################
                if place == 75 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c5.config(image=b_sol_w)
                        row_7[5] = u
                    if u == "w_sol":
                        r7c5.config(image=w_sol_w)
                        row_7[5] = u
                    if u == "b_ele":
                        r7c5.config(image=b_ele_w)
                        row_7[5] = u
                    if u == "w_ele":
                        r7c5.config(image=w_ele_w)
                        row_7[5] = u
                    if u == "b_hor":
                        r7c5.config(image=b_hor_w)
                        row_7[5] = u
                    if u == "w_hor":
                        r7c5.config(image=w_hor_w)
                        row_7[5] = u
                    if u == "b_cam":
                        r7c5.config(image=b_cam_w)
                        row_7[5] = u
                    if u == "w_cam":
                        r7c5.config(image=w_cam_w)
                        row_7[5] = u
                    if u == "b_king":
                        r7c5.config(image=b_king_w)
                        row_7[5] = u
                    if u == "w_king":
                        r7c5.config(image=w_king_w)
                        row_7[5] = u
                    if u == "b_que":
                        r7c5.config(image=b_que_w)
                        row_7[5] = u
                    if u == "w_que":
                        r7c5.config(image=w_que_w)
                        row_7[5] = u
        ######################################################################################
                if place == 77 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c7.config(image=b_sol_w)
                        row_7[7] = u
                    if u == "w_sol":
                        r7c7.config(image=w_sol_w)
                        row_7[7] = u
                    if u == "b_ele":
                        r7c7.config(image=b_ele_w)
                        row_7[7] = u
                    if u == "w_ele":
                        r7c7.config(image=w_ele_w)
                        row_7[7] = u
                    if u == "b_hor":
                        r7c7.config(image=b_hor_w)
                        row_7[7] = u
                    if u == "w_hor":
                        r7c7.config(image=w_hor_w)
                        row_7[7] = u
                    if u == "b_cam":
                        r7c7.config(image=b_cam_w)
                        row_7[7] = u
                    if u == "w_cam":
                        r7c7.config(image=w_cam_w)
                        row_7[7] = u
                    if u == "b_king":
                        r7c7.config(image=b_king_w)
                        row_7[7] = u
                    if u == "w_king":
                        r7c7.config(image=w_king_w)
                        row_7[7] = u
                    if u == "b_que":
                        r7c7.config(image=b_que_w)
                        row_7[7] = u
                    if u == "w_que":
                        r7c7.config(image=w_que_w)
                        row_7[7] = u
        ######################################################################################
                if place == 81 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c1.config(image=b_sol_b)
                        row_8[1] = u
                    if u == "w_sol":
                        r8c1.config(image=w_sol_b)
                        row_8[1] = u
                    if u == "b_ele":
                        r8c1.config(image=b_ele_b)
                        row_8[1] = u
                    if u == "w_ele":
                        r8c1.config(image=w_ele_b)
                        row_8[1] = u
                    if u == "b_hor":
                        r8c1.config(image=b_hor_b)
                        row_8[1] = u
                    if u == "w_hor":
                        r8c1.config(image=w_hor_b)
                        row_8[1] = u
                    if u == "b_cam":
                        r8c1.config(image=b_cam_b)
                        row_8[1] = u
                    if u == "w_cam":
                        r8c1.config(image=w_cam_b)
                        row_8[1] = u
                    if u == "b_king":
                        r8c1.config(image=b_king_b)
                        row_8[1] = u
                    if u == "w_king":
                        r8c1.config(image=w_king_b)
                        row_8[1] = u
                    if u == "b_que":
                        r8c1.config(image=b_que_b)
                        row_8[1] = u
                    if u == "w_que":
                        r8c1.config(image=w_que_b)
                        row_8[1] = u
        ######################################################################################
                if place == 83 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c3.config(image=b_sol_b)
                        row_8[3] = u
                    if u == "w_sol":
                        r8c3.config(image=w_sol_b)
                        row_8[3] = u
                    if u == "b_ele":
                        r8c3.config(image=b_ele_b)
                        row_8[3] = u
                    if u == "w_ele":
                        r8c3.config(image=w_ele_b)
                        row_8[3] = u
                    if u == "b_hor":
                        r8c3.config(image=b_hor_b)
                        row_8[3] = u
                    if u == "w_hor":
                        r8c3.config(image=w_hor_b)
                        row_8[3] = u
                    if u == "b_cam":
                        r8c3.config(image=b_cam_b)
                        row_8[3] = u
                    if u == "w_cam":
                        r8c3.config(image=w_cam_b)
                        row_8[3] = u
                    if u == "b_king":
                        r8c3.config(image=b_king_b)
                        row_8[3] = u
                    if u == "w_king":
                        r8c3.config(image=w_king_b)
                        row_8[3] = u
                    if u == "b_que":
                        r8c3.config(image=b_que_b)
                        row_8[3] = u
                    if u == "w_que":
                        r8c3.config(image=w_que_b)
                        row_8[3] = u
        ######################################################################################
                if place == 85 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c5.config(image=b_sol_b)
                        row_8[5] = u
                    if u == "w_sol":
                        r8c5.config(image=w_sol_b)
                        row_8[5] = u
                    if u == "b_ele":
                        r8c5.config(image=b_ele_b)
                        row_8[5] = u
                    if u == "w_ele":
                        r8c5.config(image=w_ele_b)
                        row_8[5] = u
                    if u == "b_hor":
                        r8c5.config(image=b_hor_b)
                        row_8[5] = u
                    if u == "w_hor":
                        r8c5.config(image=w_hor_b)
                        row_8[5] = u
                    if u == "b_cam":
                        r8c5.config(image=b_cam_b)
                        row_8[5] = u
                    if u == "w_cam":
                        r8c5.config(image=w_cam_b)
                        row_8[5] = u
                    if u == "b_king":
                        r8c5.config(image=b_king_b)
                        row_8[5] = u
                    if u == "w_king":
                        r8c5.config(image=w_king_b)
                        row_8[5] = u
                    if u == "b_que":
                        r8c5.config(image=b_que_b)
                        row_8[5] = u
                    if u == "w_que":
                        r8c5.config(image=w_que_b)
                        row_8[5] = u
        ######################################################################################
                if place == 87 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c7.config(image=b_sol_b)
                        row_8[7] = u
                    if u == "w_sol":
                        r8c7.config(image=w_sol_b)
                        row_8[7] = u
                    if u == "b_ele":
                        r8c7.config(image=b_ele_b)
                        row_8[7] = u
                    if u == "w_ele":
                        r8c7.config(image=w_ele_b)
                        row_8[7] = u
                    if u == "b_hor":
                        r8c7.config(image=b_hor_b)
                        row_8[7] = u
                    if u == "w_hor":
                        r8c7.config(image=w_hor_b)
                        row_8[7] = u
                    if u == "b_cam":
                        r8c7.config(image=b_cam_b)
                        row_8[7] = u
                    if u == "w_cam":
                        r8c7.config(image=w_cam_b)
                        row_8[7] = u
                    if u == "b_king":
                        r8c7.config(image=b_king_b)
                        row_8[7] = u
                    if u == "w_king":
                        r8c7.config(image=w_king_b)
                        row_8[7] = u
                    if u == "b_que":
                        r8c7.config(image=b_que_b)
                        row_8[7] = u
                    if u == "w_que":
                        r8c7.config(image=w_que_b)
                        row_8[7] = u
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        
                if place == 12 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c2.config(image=b_sol_b)
                        row_1[2] = u
                    if u == "w_sol":
                        r1c2.config(image=w_sol_b)
                        row_1[2] = u
                    if u == "b_ele":
                        r1c2.config(image=b_ele_b)
                        row_1[2] = u
                    if u == "w_ele":
                        r1c2.config(image=w_ele_b)
                        row_1[2] = u
                    if u == "b_hor":
                        r1c2.config(image=b_hor_b)
                        row_1[2] = u
                    if u == "w_hor":
                        r1c2.config(image=w_hor_b)
                        row_1[2] = u
                    if u == "b_cam":
                        r1c2.config(image=b_cam_b)
                        row_1[2] = u
                    if u == "w_cam":
                        r1c2.config(image=w_cam_b)
                        row_1[2] = u
                    if u == "b_king":
                        r1c2.config(image=b_king_b)
                        row_1[2] = u
                    if u == "w_king":
                        r1c2.config(image=w_king_b)
                        row_1[2] = u
                    if u == "b_que":
                        r1c2.config(image=b_que_b)
                        row_1[2] = u
                    if u == "w_que":
                        r1c2.config(image=w_que_b)
                        row_1[2] = u


                if place == 14 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c4.config(image=b_sol_b)
                        row_1[4] = u
                    if u == "w_sol":
                        r1c4.config(image=w_sol_b)
                        row_1[4] = u
                    if u == "b_ele":
                        r1c4.config(image=b_ele_b)
                        row_1[4] = u
                    if u == "w_ele":
                        r1c4.config(image=w_ele_b)
                        row_1[4] = u
                    if u == "b_hor":
                        r1c4.config(image=b_hor_b)
                        row_1[4] = u
                    if u == "w_hor":
                        r1c4.config(image=w_hor_b)
                        row_1[4] = u
                    if u == "b_cam":
                        r1c4.config(image=b_cam_b)
                        row_1[4] = u
                    if u == "w_cam":
                        r1c4.config(image=w_cam_b)
                        row_1[4] = u
                    if u == "b_king":
                        r1c4.config(image=b_king_b)
                        row_1[4] = u
                    if u == "w_king":
                        r1c4.config(image=w_king_b)
                        row_1[4] = u
                    if u == "b_que":
                        r1c4.config(image=b_que_b)
                        row_1[4] = u
                    if u == "w_que":
                        r1c4.config(image=w_que_b)
                        row_1[4] = u

                if place == 16 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c6.config(image=b_sol_b)
                        row_1[6] = u
                    if u == "w_sol":
                        r1c6.config(image=w_sol_b)
                        row_1[6] = u
                    if u == "b_ele":
                        r1c6.config(image=b_ele_b)
                        row_1[6] = u
                    if u == "w_ele":
                        r1c6.config(image=w_ele_b)
                        row_1[6] = u
                    if u == "b_hor":
                        r1c6.config(image=b_hor_b)
                        row_1[6] = u
                    if u == "w_hor":
                        r1c6.config(image=w_hor_b)
                        row_1[6] = u
                    if u == "b_cam":
                        r1c6.config(image=b_cam_b)
                        row_1[6] = u
                    if u == "w_cam":
                        r1c6.config(image=w_cam_b)
                        row_1[6] = u
                    if u == "b_king":
                        r1c6.config(image=b_king_b)
                        row_1[6] = u
                    if u == "w_king":
                        r1c6.config(image=w_king_b)
                        row_1[6] = u
                    if u == "b_que":
                        r1c6.config(image=b_que_b)
                        row_1[6] = u
                    if u == "w_que":
                        r1c6.config(image=w_que_b)
                        row_1[6] = u


                if place == 18 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c8.config(image=b_sol_b)
                        row_1[8] = u
                    if u == "w_sol":
                        r1c8.config(image=w_sol_b)
                        row_1[8] = u
                    if u == "b_ele":
                        r1c8.config(image=b_ele_b)
                        row_1[8] = u
                    if u == "w_ele":
                        r1c8.config(image=w_ele_b)
                        row_1[8] = u
                    if u == "b_hor":
                        r1c8.config(image=b_hor_b)
                        row_1[8] = u
                    if u == "w_hor":
                        r1c8.config(image=w_hor_b)
                        row_1[8] = u
                    if u == "b_cam":
                        r1c8.config(image=b_cam_b)
                        row_1[8] = u
                    if u == "w_cam":
                        r1c8.config(image=w_cam_b)
                        row_1[8] = u
                    if u == "b_king":
                        r1c8.config(image=b_king_b)
                        row_1[8] = u
                    if u == "w_king":
                        r1c8.config(image=w_king_b)
                        row_1[8] = u
                    if u == "b_que":
                        r1c8.config(image=b_que_b)
                        row_1[8] = u
                    if u == "w_que":
                        r1c8.config(image=w_que_b)
                        row_1[8] = u

                if place == 32 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c2.config(image=b_sol_b)
                        row_3[2] = u
                    if u == "w_sol":
                        r3c2.config(image=w_sol_b)
                        row_3[2] = u
                    if u == "b_ele":
                        r3c2.config(image=b_ele_b)
                        row_3[2] = u
                    if u == "w_ele":
                        r3c2.config(image=w_ele_b)
                        row_3[2] = u
                    if u == "b_hor":
                        r3c2.config(image=b_hor_b)
                        row_3[2] = u
                    if u == "w_hor":
                        r3c2.config(image=w_hor_b)
                        row_3[2] = u
                    if u == "b_cam":
                        r3c2.config(image=b_cam_b)
                        row_3[2] = u
                    if u == "w_cam":
                        r3c2.config(image=w_cam_b)
                        row_3[2] = u
                    if u == "b_king":
                        r3c2.config(image=b_king_b)
                        row_3[2] = u
                    if u == "w_king":
                        r3c2.config(image=w_king_b)
                        row_3[2] = u
                    if u == "b_que":
                        r3c2.config(image=b_que_b)
                        row_3[2] = u
                    if u == "w_que":
                        r3c2.config(image=w_que_b)
                        row_3[2] = u


                if place == 34 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c4.config(image=b_sol_b)
                        row_3[4] = u
                    if u == "w_sol":
                        r3c4.config(image=w_sol_b)
                        row_3[4] = u
                    if u == "b_ele":
                        r3c4.config(image=b_ele_b)
                        row_3[4] = u
                    if u == "w_ele":
                        r3c4.config(image=w_ele_b)
                        row_3[4] = u
                    if u == "b_hor":
                        r3c4.config(image=b_hor_b)
                        row_3[4] = u
                    if u == "w_hor":
                        r3c4.config(image=w_hor_b)
                        row_3[4] = u
                    if u == "b_cam":
                        r3c4.config(image=b_cam_b)
                        row_3[4] = u
                    if u == "w_cam":
                        r3c4.config(image=w_cam_b)
                        row_3[4] = u
                    if u == "b_king":
                        r3c4.config(image=b_king_b)
                        row_3[4] = u
                    if u == "w_king":
                        r3c4.config(image=w_king_b)
                        row_3[4] = u
                    if u == "b_que":
                        r3c4.config(image=b_que_b)
                        row_3[4] = u
                    if u == "w_que":
                        r3c4.config(image=w_que_b)
                        row_3[4] = u

                if place == 36 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c6.config(image=b_sol_b)
                        row_3[6] = u
                    if u == "w_sol":
                        r3c6.config(image=w_sol_b)
                        row_3[6] = u
                    if u == "b_ele":
                        r3c6.config(image=b_ele_b)
                        row_3[6] = u
                    if u == "w_ele":
                        r3c6.config(image=w_ele_b)
                        row_3[6] = u
                    if u == "b_hor":
                        r3c6.config(image=b_hor_b)
                        row_3[6] = u
                    if u == "w_hor":
                        r3c6.config(image=w_hor_b)
                        row_3[6] = u
                    if u == "b_cam":
                        r3c6.config(image=b_cam_b)
                        row_3[6] = u
                    if u == "w_cam":
                        r3c6.config(image=w_cam_b)
                        row_3[6] = u
                    if u == "b_king":
                        r3c6.config(image=b_king_b)
                        row_3[6] = u
                    if u == "w_king":
                        r3c6.config(image=w_king_b)
                        row_3[6] = u
                    if u == "b_que":
                        r3c6.config(image=b_que_b)
                        row_3[6] = u
                    if u == "w_que":
                        r3c6.config(image=w_que_b)
                        row_3[6] = u


                if place == 38 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c8.config(image=b_sol_b)
                        row_3[8] = u
                    if u == "w_sol":
                        r3c8.config(image=w_sol_b)
                        row_3[8] = u
                    if u == "b_ele":
                        r3c8.config(image=b_ele_b)
                        row_3[8] = u
                    if u == "w_ele":
                        r3c8.config(image=w_ele_b)
                        row_3[8] = u
                    if u == "b_hor":
                        r3c8.config(image=b_hor_b)
                        row_3[8] = u
                    if u == "w_hor":
                        r3c8.config(image=w_hor_b)
                        row_3[8] = u
                    if u == "b_cam":
                        r3c8.config(image=b_cam_b)
                        row_3[8] = u
                    if u == "w_cam":
                        r3c8.config(image=w_cam_b)
                        row_3[8] = u
                    if u == "b_king":
                        r3c8.config(image=b_king_b)
                        row_3[8] = u
                    if u == "w_king":
                        r3c8.config(image=w_king_b)
                        row_3[8] = u
                    if u == "b_que":
                        r3c8.config(image=b_que_b)
                        row_3[8] = u
                    if u == "w_que":
                        r3c8.config(image=w_que_b)
                        row_3[8] = u        

                if place == 52 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c2.config(image=b_sol_b)
                        row_5[2] = u
                    if u == "w_sol":
                        r5c2.config(image=w_sol_b)
                        row_5[2] = u
                    if u == "b_ele":
                        r5c2.config(image=b_ele_b)
                        row_5[2] = u
                    if u == "w_ele":
                        r5c2.config(image=w_ele_b)
                        row_5[2] = u
                    if u == "b_hor":
                        r5c2.config(image=b_hor_b)
                        row_5[2] = u
                    if u == "w_hor":
                        r5c2.config(image=w_hor_b)
                        row_5[2] = u
                    if u == "b_cam":
                        r5c2.config(image=b_cam_b)
                        row_5[2] = u
                    if u == "w_cam":
                        r5c2.config(image=w_cam_b)
                        row_5[2] = u
                    if u == "b_king":
                        r5c2.config(image=b_king_b)
                        row_5[2] = u
                    if u == "w_king":
                        r5c2.config(image=w_king_b)
                        row_5[2] = u
                    if u == "b_que":
                        r5c2.config(image=b_que_b)
                        row_5[2] = u
                    if u == "w_que":
                        r5c2.config(image=w_que_b)
                        row_5[2] = u


                if place == 54 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c4.config(image=b_sol_b)
                        row_5[4] = u
                    if u == "w_sol":
                        r5c4.config(image=w_sol_b)
                        row_5[4] = u
                    if u == "b_ele":
                        r5c4.config(image=b_ele_b)
                        row_5[4] = u
                    if u == "w_ele":
                        r5c4.config(image=w_ele_b)
                        row_5[4] = u
                    if u == "b_hor":
                        r5c4.config(image=b_hor_b)
                        row_5[4] = u
                    if u == "w_hor":
                        r5c4.config(image=w_hor_b)
                        row_5[4] = u
                    if u == "b_cam":
                        r5c4.config(image=b_cam_b)
                        row_5[4] = u
                    if u == "w_cam":
                        r5c4.config(image=w_cam_b)
                        row_5[4] = u
                    if u == "b_king":
                        r5c4.config(image=b_king_b)
                        row_5[4] = u
                    if u == "w_king":
                        r5c4.config(image=w_king_b)
                        row_5[4] = u
                    if u == "b_que":
                        r5c4.config(image=b_que_b)
                        row_5[4] = u
                    if u == "w_que":
                        r5c4.config(image=w_que_b)
                        row_5[4] = u

                if place == 56 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c6.config(image=b_sol_b)
                        row_5[6] = u
                    if u == "w_sol":
                        r5c6.config(image=w_sol_b)
                        row_5[6] = u
                    if u == "b_ele":
                        r5c6.config(image=b_ele_b)
                        row_5[6] = u
                    if u == "w_ele":
                        r5c6.config(image=w_ele_b)
                        row_5[6] = u
                    if u == "b_hor":
                        r5c6.config(image=b_hor_b)
                        row_5[6] = u
                    if u == "w_hor":
                        r5c6.config(image=w_hor_b)
                        row_5[6] = u
                    if u == "b_cam":
                        r5c6.config(image=b_cam_b)
                        row_5[6] = u
                    if u == "w_cam":
                        r5c6.config(image=w_cam_b)
                        row_5[6] = u
                    if u == "b_king":
                        r5c6.config(image=b_king_b)
                        row_5[6] = u
                    if u == "w_king":
                        r5c6.config(image=w_king_b)
                        row_5[6] = u
                    if u == "b_que":
                        r5c6.config(image=b_que_b)
                        row_5[6] = u
                    if u == "w_que":
                        r5c6.config(image=w_que_b)
                        row_5[6] = u


                if place == 58 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c8.config(image=b_sol_b)
                        row_5[8] = u
                    if u == "w_sol":
                        r5c8.config(image=w_sol_b)
                        row_5[8] = u
                    if u == "b_ele":
                        r5c8.config(image=b_ele_b)
                        row_5[8] = u
                    if u == "w_ele":
                        r5c8.config(image=w_ele_b)
                        row_5[8] = u
                    if u == "b_hor":
                        r5c8.config(image=b_hor_b)
                        row_5[8] = u
                    if u == "w_hor":
                        r5c8.config(image=w_hor_b)
                        row_5[8] = u
                    if u == "b_cam":
                        r5c8.config(image=b_cam_b)
                        row_5[8] = u
                    if u == "w_cam":
                        r5c8.config(image=w_cam_b)
                        row_5[8] = u
                    if u == "b_king":
                        r5c8.config(image=b_king_b)
                        row_5[8] = u
                    if u == "w_king":
                        r5c8.config(image=w_king_b)
                        row_5[8] = u
                    if u == "b_que":
                        r5c8.config(image=b_que_b)
                        row_5[8] = u
                    if u == "w_que":
                        r5c8.config(image=w_que_b)
                        row_5[8] = u

                if place == 72 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c2.config(image=b_sol_b)
                        row_7[2] = u
                    if u == "w_sol":
                        r7c2.config(image=w_sol_b)
                        row_7[2] = u
                    if u == "b_ele":
                        r7c2.config(image=b_ele_b)
                        row_7[2] = u
                    if u == "w_ele":
                        r7c2.config(image=w_ele_b)
                        row_7[2] = u
                    if u == "b_hor":
                        r7c2.config(image=b_hor_b)
                        row_7[2] = u
                    if u == "w_hor":
                        r7c2.config(image=w_hor_b)
                        row_7[2] = u
                    if u == "b_cam":
                        r7c2.config(image=b_cam_b)
                        row_7[2] = u
                    if u == "w_cam":
                        r7c2.config(image=w_cam_b)
                        row_7[2] = u
                    if u == "b_king":
                        r7c2.config(image=b_king_b)
                        row_7[2] = u
                    if u == "w_king":
                        r7c2.config(image=w_king_b)
                        row_7[2] = u
                    if u == "b_que":
                        r7c2.config(image=b_que_b)
                        row_7[2] = u
                    if u == "w_que":
                        r7c2.config(image=w_que_b)
                        row_7[2] = u


                if place == 74 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c4.config(image=b_sol_b)
                        row_7[4] = u
                    if u == "w_sol":
                        r7c4.config(image=w_sol_b)
                        row_7[4] = u
                    if u == "b_ele":
                        r7c4.config(image=b_ele_b)
                        row_7[4] = u
                    if u == "w_ele":
                        r7c4.config(image=w_ele_b)
                        row_7[4] = u
                    if u == "b_hor":
                        r7c4.config(image=b_hor_b)
                        row_7[4] = u
                    if u == "w_hor":
                        r7c4.config(image=w_hor_b)
                        row_7[4] = u
                    if u == "b_cam":
                        r7c4.config(image=b_cam_b)
                        row_7[4] = u
                    if u == "w_cam":
                        r7c4.config(image=w_cam_b)
                        row_7[4] = u
                    if u == "b_king":
                        r7c4.config(image=b_king_b)
                        row_7[4] = u
                    if u == "w_king":
                        r7c4.config(image=w_king_b)
                        row_7[4] = u
                    if u == "b_que":
                        r7c4.config(image=b_que_b)
                        row_7[4] = u
                    if u == "w_que":
                        r7c4.config(image=w_que_b)
                        row_7[4] = u

                if place == 76 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c6.config(image=b_sol_b)
                        row_7[6] = u
                    if u == "w_sol":
                        r7c6.config(image=w_sol_b)
                        row_7[6] = u
                    if u == "b_ele":
                        r7c6.config(image=b_ele_b)
                        row_7[6] = u
                    if u == "w_ele":
                        r7c6.config(image=w_ele_b)
                        row_7[6] = u
                    if u == "b_hor":
                        r7c6.config(image=b_hor_b)
                        row_7[6] = u
                    if u == "w_hor":
                        r7c6.config(image=w_hor_b)
                        row_7[6] = u
                    if u == "b_cam":
                        r7c6.config(image=b_cam_b)
                        row_7[6] = u
                    if u == "w_cam":
                        r7c6.config(image=w_cam_b)
                        row_7[6] = u
                    if u == "b_king":
                        r7c6.config(image=b_king_b)
                        row_7[6] = u
                    if u == "w_king":
                        r7c6.config(image=w_king_b)
                        row_7[6] = u
                    if u == "b_que":
                        r7c6.config(image=b_que_b)
                        row_7[6] = u
                    if u == "w_que":
                        r7c6.config(image=w_que_b)
                        row_7[6] = u


                if place == 78 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c8.config(image=b_sol_b)
                        row_7[8] = u
                    if u == "w_sol":
                        r7c8.config(image=w_sol_b)
                        row_7[8] = u
                    if u == "b_ele":
                        r7c8.config(image=b_ele_b)
                        row_7[8] = u
                    if u == "w_ele":
                        r7c8.config(image=w_ele_b)
                        row_7[8] = u
                    if u == "b_hor":
                        r7c8.config(image=b_hor_b)
                        row_7[8] = u
                    if u == "w_hor":
                        r7c8.config(image=w_hor_b)
                        row_7[8] = u
                    if u == "b_cam":
                        r7c8.config(image=b_cam_b)
                        row_7[8] = u
                    if u == "w_cam":
                        r7c8.config(image=w_cam_b)
                        row_7[8] = u
                    if u == "b_king":
                        r7c8.config(image=b_king_b)
                        row_7[8] = u
                    if u == "w_king":
                        r7c8.config(image=w_king_b)
                        row_7[8] = u
                    if u == "b_que":
                        r7c8.config(image=b_que_b)
                        row_7[8] = u
                    if u == "w_que":
                        r7c8.config(image=w_que_b)
                        row_7[8] = u

                if place == 22 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c2.config(image=b_sol_w)
                        row_2[2] = u
                    if u == "w_sol":
                        r2c2.config(image=w_sol_w)
                        row_2[2] = u
                    if u == "b_ele":
                        r2c2.config(image=b_ele_w)
                        row_2[2] = u
                    if u == "w_ele":
                        r2c2.config(image=w_ele_w)
                        row_2[2] = u
                    if u == "b_hor":
                        r2c2.config(image=b_hor_w)
                        row_2[2] = u
                    if u == "w_hor":
                        r2c2.config(image=w_hor_w)
                        row_2[2] = u
                    if u == "b_cam":
                        r2c2.config(image=b_cam_w)
                        row_2[2] = u
                    if u == "w_cam":
                        r2c2.config(image=w_cam_w)
                        row_2[2] = u
                    if u == "b_king":
                        r2c2.config(image=b_king_w)
                        row_2[2] = u
                    if u == "w_king":
                        r2c2.config(image=w_king_w)
                        row_2[2] = u
                    if u == "b_que":
                        r2c2.config(image=b_que_w)
                        row_2[2] = u
                    if u == "w_que":
                        r2c2.config(image=w_que_w)
                        row_2[2] = u
        ######################################################################################
                if place == 24 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c4.config(image=b_sol_w)
                        row_2[4] = u
                    if u == "w_sol":
                        r2c4.config(image=w_sol_w)
                        row_2[4] = u
                    if u == "b_ele":
                        r2c4.config(image=b_ele_w)
                        row_2[4] = u
                    if u == "w_ele":
                        r2c4.config(image=w_ele_w)
                        row_2[4] = u
                    if u == "b_hor":
                        r2c4.config(image=b_hor_w)
                        row_2[4] = u
                    if u == "w_hor":
                        r2c4.config(image=w_hor_w)
                        row_2[4] = u
                    if u == "b_cam":
                        r2c4.config(image=b_cam_w)
                        row_2[4] = u
                    if u == "w_cam":
                        r2c4.config(image=w_cam_w)
                        row_2[4] = u
                    if u == "b_king":
                        r2c4.config(image=b_king_w)
                        row_2[4] = u
                    if u == "w_king":
                        r2c4.config(image=w_king_w)
                        row_2[4] = u
                    if u == "b_que":
                        r2c4.config(image=b_que_w)
                        row_2[4] = u
                    if u == "w_que":
                        r2c4.config(image=w_que_w)
                        row_2[4] = u
        ######################################################################################
                if place == 26 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c6.config(image=b_sol_w)
                        row_2[6] = u
                    if u == "w_sol":
                        r2c6.config(image=w_sol_w)
                        row_2[6] = u
                    if u == "b_ele":
                        r2c6.config(image=b_ele_w)
                        row_2[6] = u
                    if u == "w_ele":
                        r2c6.config(image=w_ele_w)
                        row_2[6] = u
                    if u == "b_hor":
                        r2c6.config(image=b_hor_w)
                        row_2[6] = u
                    if u == "w_hor":
                        r2c6.config(image=w_hor_w)
                        row_2[6] = u
                    if u == "b_cam":
                        r2c6.config(image=b_cam_w)
                        row_2[6] = u
                    if u == "w_cam":
                        r2c6.config(image=w_cam_w)
                        row_2[6] = u
                    if u == "b_king":
                        r2c6.config(image=b_king_w)
                        row_2[6] = u
                    if u == "w_king":
                        r2c6.config(image=w_king_w)
                        row_2[6] = u
                    if u == "b_que":
                        r2c6.config(image=b_que_w)
                        row_2[6] = u
                    if u == "w_que":
                        r2c6.config(image=w_que_w)
                        row_2[6] = u
        ######################################################################################
                if place == 28 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c8.config(image=b_sol_w)
                        row_2[8] = u
                    if u == "w_sol":
                        r2c8.config(image=w_sol_w)
                        row_2[8] = u
                    if u == "b_ele":
                        r2c8.config(image=b_ele_w)
                        row_2[8] = u
                    if u == "w_ele":
                        r2c8.config(image=w_ele_w)
                        row_2[8] = u
                    if u == "b_hor":
                        r2c8.config(image=b_hor_w)
                        row_2[8] = u
                    if u == "w_hor":
                        r2c8.config(image=w_hor_w)
                        row_2[8] = u
                    if u == "b_cam":
                        r2c8.config(image=b_cam_w)
                        row_2[8] = u
                    if u == "w_cam":
                        r2c8.config(image=w_cam_w)
                        row_2[8] = u
                    if u == "b_king":
                        r2c8.config(image=b_king_w)
                        row_2[8] = u
                    if u == "w_king":
                        r2c8.config(image=w_king_w)
                        row_2[8] = u
                    if u == "b_que":
                        r2c8.config(image=b_que_w)
                        row_2[8] = u
                    if u == "w_que":
                        r2c8.config(image=w_que_w)
                        row_2[8] = u

                if place == 42 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c2.config(image=b_sol_w)
                        row_4[2] = u
                    if u == "w_sol":
                        r4c2.config(image=w_sol_w)
                        row_4[2] = u
                    if u == "b_ele":
                        r4c2.config(image=b_ele_w)
                        row_4[2] = u
                    if u == "w_ele":
                        r4c2.config(image=w_ele_w)
                        row_4[2] = u
                    if u == "b_hor":
                        r4c2.config(image=b_hor_w)
                        row_4[2] = u
                    if u == "w_hor":
                        r4c2.config(image=w_hor_w)
                        row_4[2] = u
                    if u == "b_cam":
                        r4c2.config(image=b_cam_w)
                        row_4[2] = u
                    if u == "w_cam":
                        r4c2.config(image=w_cam_w)
                        row_4[2] = u
                    if u == "b_king":
                        r4c2.config(image=b_king_w)
                        row_4[2] = u
                    if u == "w_king":
                        r4c2.config(image=w_king_w)
                        row_4[2] = u
                    if u == "b_que":
                        r4c2.config(image=b_que_w)
                        row_4[2] = u
                    if u == "w_que":
                        r4c2.config(image=w_que_w)
                        row_4[2] = u
        ######################################################################################
                if place == 44 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c4.config(image=b_sol_w)
                        row_4[4] = u
                    if u == "w_sol":
                        r4c4.config(image=w_sol_w)
                        row_4[4] = u
                    if u == "b_ele":
                        r4c4.config(image=b_ele_w)
                        row_4[4] = u
                    if u == "w_ele":
                        r4c4.config(image=w_ele_w)
                        row_4[4] = u
                    if u == "b_hor":
                        r4c4.config(image=b_hor_w)
                        row_4[4] = u
                    if u == "w_hor":
                        r4c4.config(image=w_hor_w)
                        row_4[4] = u
                    if u == "b_cam":
                        r4c4.config(image=b_cam_w)
                        row_4[4] = u
                    if u == "w_cam":
                        r4c4.config(image=w_cam_w)
                        row_4[4] = u
                    if u == "b_king":
                        r4c4.config(image=b_king_w)
                        row_4[4] = u
                    if u == "w_king":
                        r4c4.config(image=w_king_w)
                        row_4[4] = u
                    if u == "b_que":
                        r4c4.config(image=b_que_w)
                        row_4[4] = u
                    if u == "w_que":
                        r4c4.config(image=w_que_w)
                        row_4[4] = u
        ######################################################################################
                if place == 46 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c6.config(image=b_sol_w)
                        row_4[6] = u
                    if u == "w_sol":
                        r4c6.config(image=w_sol_w)
                        row_4[6] = u
                    if u == "b_ele":
                        r4c6.config(image=b_ele_w)
                        row_4[6] = u
                    if u == "w_ele":
                        r4c6.config(image=w_ele_w)
                        row_4[6] = u
                    if u == "b_hor":
                        r4c6.config(image=b_hor_w)
                        row_4[6] = u
                    if u == "w_hor":
                        r4c6.config(image=w_hor_w)
                        row_4[6] = u
                    if u == "b_cam":
                        r4c6.config(image=b_cam_w)
                        row_4[6] = u
                    if u == "w_cam":
                        r4c6.config(image=w_cam_w)
                        row_4[6] = u
                    if u == "b_king":
                        r4c6.config(image=b_king_w)
                        row_4[6] = u
                    if u == "w_king":
                        r4c6.config(image=w_king_w)
                        row_4[6] = u
                    if u == "b_que":
                        r4c6.config(image=b_que_w)
                        row_4[6] = u
                    if u == "w_que":
                        r4c6.config(image=w_que_w)
                        row_4[6] = u
        ######################################################################################
                if place == 48 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c8.config(image=b_sol_w)
                        row_4[8] = u
                    if u == "w_sol":
                        r4c8.config(image=w_sol_w)
                        row_4[8] = u
                    if u == "b_ele":
                        r4c8.config(image=b_ele_w)
                        row_4[8] = u
                    if u == "w_ele":
                        r4c8.config(image=w_ele_w)
                        row_4[8] = u
                    if u == "b_hor":
                        r4c8.config(image=b_hor_w)
                        row_4[8] = u
                    if u == "w_hor":
                        r4c8.config(image=w_hor_w)
                        row_4[8] = u
                    if u == "b_cam":
                        r4c8.config(image=b_cam_w)
                        row_4[8] = u
                    if u == "w_cam":
                        r4c8.config(image=w_cam_w)
                        row_4[8] = u
                    if u == "b_king":
                        r4c8.config(image=b_king_w)
                        row_4[8] = u
                    if u == "w_king":
                        r4c8.config(image=w_king_w)
                        row_4[8] = u
                    if u == "b_que":
                        r4c8.config(image=b_que_w)
                        row_4[8] = u
                    if u == "w_que":
                        r4c8.config(image=w_que_w)
                        row_4[8] = u

                if place == 62 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c2.config(image=b_sol_w)
                        row_6[2] = u
                    if u == "w_sol":
                        r6c2.config(image=w_sol_w)
                        row_6[2] = u
                    if u == "b_ele":
                        r6c2.config(image=b_ele_w)
                        row_6[2] = u
                    if u == "w_ele":
                        r6c2.config(image=w_ele_w)
                        row_6[2] = u
                    if u == "b_hor":
                        r6c2.config(image=b_hor_w)
                        row_6[2] = u
                    if u == "w_hor":
                        r6c2.config(image=w_hor_w)
                        row_6[2] = u
                    if u == "b_cam":
                        r6c2.config(image=b_cam_w)
                        row_6[2] = u
                    if u == "w_cam":
                        r6c2.config(image=w_cam_w)
                        row_6[2] = u
                    if u == "b_king":
                        r6c2.config(image=b_king_w)
                        row_6[2] = u
                    if u == "w_king":
                        r6c2.config(image=w_king_w)
                        row_6[2] = u
                    if u == "b_que":
                        r6c2.config(image=b_que_w)
                        row_6[2] = u
                    if u == "w_que":
                        r6c2.config(image=w_que_w)
                        row_6[2] = u
        ######################################################################################
                if place == 64 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c4.config(image=b_sol_w)
                        row_6[4] = u
                    if u == "w_sol":
                        r6c4.config(image=w_sol_w)
                        row_6[4] = u
                    if u == "b_ele":
                        r6c4.config(image=b_ele_w)
                        row_6[4] = u
                    if u == "w_ele":
                        r6c4.config(image=w_ele_w)
                        row_6[4] = u
                    if u == "b_hor":
                        r6c4.config(image=b_hor_w)
                        row_6[4] = u
                    if u == "w_hor":
                        r6c4.config(image=w_hor_w)
                        row_6[4] = u
                    if u == "b_cam":
                        r6c4.config(image=b_cam_w)
                        row_6[4] = u
                    if u == "w_cam":
                        r6c4.config(image=w_cam_w)
                        row_6[4] = u
                    if u == "b_king":
                        r6c4.config(image=b_king_w)
                        row_6[4] = u
                    if u == "w_king":
                        r6c4.config(image=w_king_w)
                        row_6[4] = u
                    if u == "b_que":
                        r6c4.config(image=b_que_w)
                        row_6[4] = u
                    if u == "w_que":
                        r6c4.config(image=w_que_w)
                        row_6[4] = u
        ######################################################################################
                if place == 66 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c6.config(image=b_sol_w)
                        row_6[6] = u
                    if u == "w_sol":
                        r6c6.config(image=w_sol_w)
                        row_6[6] = u
                    if u == "b_ele":
                        r6c6.config(image=b_ele_w)
                        row_6[6] = u
                    if u == "w_ele":
                        r6c6.config(image=w_ele_w)
                        row_6[6] = u
                    if u == "b_hor":
                        r6c6.config(image=b_hor_w)
                        row_6[6] = u
                    if u == "w_hor":
                        r6c6.config(image=w_hor_w)
                        row_6[6] = u
                    if u == "b_cam":
                        r6c6.config(image=b_cam_w)
                        row_6[6] = u
                    if u == "w_cam":
                        r6c6.config(image=w_cam_w)
                        row_6[6] = u
                    if u == "b_king":
                        r6c6.config(image=b_king_w)
                        row_6[6] = u
                    if u == "w_king":
                        r6c6.config(image=w_king_w)
                        row_6[6] = u
                    if u == "b_que":
                        r6c6.config(image=b_que_w)
                        row_6[6] = u
                    if u == "w_que":
                        r6c6.config(image=w_que_w)
                        row_6[6] = u
        ######################################################################################
                if place == 68 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c8.config(image=b_sol_w)
                        row_6[8] = u
                    if u == "w_sol":
                        r6c8.config(image=w_sol_w)
                        row_6[8] = u
                    if u == "b_ele":
                        r6c8.config(image=b_ele_w)
                        row_6[8] = u
                    if u == "w_ele":
                        r6c8.config(image=w_ele_w)
                        row_6[8] = u
                    if u == "b_hor":
                        r6c8.config(image=b_hor_w)
                        row_6[8] = u
                    if u == "w_hor":
                        r6c8.config(image=w_hor_w)
                        row_6[8] = u
                    if u == "b_cam":
                        r6c8.config(image=b_cam_w)
                        row_6[8] = u
                    if u == "w_cam":
                        r6c8.config(image=w_cam_w)
                        row_6[8] = u
                    if u == "b_king":
                        r6c8.config(image=b_king_w)
                        row_6[8] = u
                    if u == "w_king":
                        r6c8.config(image=w_king_w)
                        row_6[8] = u
                    if u == "b_que":
                        r6c8.config(image=b_que_w)
                        row_6[8] = u
                    if u == "w_que":
                        r6c8.config(image=w_que_w)
                        row_6[8] = u

                if place == 82 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c2.config(image=b_sol_w)
                        row_8[2] = u
                    if u == "w_sol":
                        r8c2.config(image=w_sol_w)
                        row_8[2] = u
                    if u == "b_ele":
                        r8c2.config(image=b_ele_w)
                        row_8[2] = u
                    if u == "w_ele":
                        r8c2.config(image=w_ele_w)
                        row_8[2] = u
                    if u == "b_hor":
                        r8c2.config(image=b_hor_w)
                        row_8[2] = u
                    if u == "w_hor":
                        r8c2.config(image=w_hor_w)
                        row_8[2] = u
                    if u == "b_cam":
                        r8c2.config(image=b_cam_w)
                        row_8[2] = u
                    if u == "w_cam":
                        r8c2.config(image=w_cam_w)
                        row_8[2] = u
                    if u == "b_king":
                        r8c2.config(image=b_king_w)
                        row_8[2] = u
                    if u == "w_king":
                        r8c2.config(image=w_king_w)
                        row_8[2] = u
                    if u == "b_que":
                        r8c2.config(image=b_que_w)
                        row_8[2] = u
                    if u == "w_que":
                        r8c2.config(image=w_que_w)
                        row_8[2] = u
        ######################################################################################
                if place == 84 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c4.config(image=b_sol_w)
                        row_8[4] = u
                    if u == "w_sol":
                        r8c4.config(image=w_sol_w)
                        row_8[4] = u
                    if u == "b_ele":
                        r8c4.config(image=b_ele_w)
                        row_8[4] = u
                    if u == "w_ele":
                        r8c4.config(image=w_ele_w)
                        row_8[4] = u
                    if u == "b_hor":
                        r8c4.config(image=b_hor_w)
                        row_8[4] = u
                    if u == "w_hor":
                        r8c4.config(image=w_hor_w)
                        row_8[4] = u
                    if u == "b_cam":
                        r8c4.config(image=b_cam_w)
                        row_8[4] = u
                    if u == "w_cam":
                        r8c4.config(image=w_cam_w)
                        row_8[4] = u
                    if u == "b_king":
                        r8c4.config(image=b_king_w)
                        row_8[4] = u
                    if u == "w_king":
                        r8c4.config(image=w_king_w)
                        row_8[4] = u
                    if u == "b_que":
                        r8c4.config(image=b_que_w)
                        row_8[4] = u
                    if u == "w_que":
                        r8c4.config(image=w_que_w)
                        row_8[4] = u
        ######################################################################################
                if place == 86 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c6.config(image=b_sol_w)
                        row_8[6] = u
                    if u == "w_sol":
                        r8c6.config(image=w_sol_w)
                        row_8[6] = u
                    if u == "b_ele":
                        r8c6.config(image=b_ele_w)
                        row_8[6] = u
                    if u == "w_ele":
                        r8c6.config(image=w_ele_w)
                        row_8[6] = u
                    if u == "b_hor":
                        r8c6.config(image=b_hor_w)
                        row_8[6] = u
                    if u == "w_hor":
                        r8c6.config(image=w_hor_w)
                        row_8[6] = u
                    if u == "b_cam":
                        r8c6.config(image=b_cam_w)
                        row_8[6] = u
                    if u == "w_cam":
                        r8c6.config(image=w_cam_w)
                        row_8[6] = u
                    if u == "b_king":
                        r8c6.config(image=b_king_w)
                        row_8[6] = u
                    if u == "w_king":
                        r8c6.config(image=w_king_w)
                        row_8[6] = u
                    if u == "b_que":
                        r8c6.config(image=b_que_w)
                        row_8[6] = u
                    if u == "w_que":
                        r8c6.config(image=w_que_w)
                        row_8[6] = u
        ######################################################################################
                if place == 88 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c8.config(image=b_sol_w)
                        row_8[8] = u
                    if u == "w_sol":
                        r8c8.config(image=w_sol_w)
                        row_8[8] = u
                    if u == "b_ele":
                        r8c8.config(image=b_ele_w)
                        row_8[8] = u
                    if u == "w_ele":
                        r8c8.config(image=w_ele_w)
                        row_8[8] = u
                    if u == "b_hor":
                        r8c8.config(image=b_hor_w)
                        row_8[8] = u
                    if u == "w_hor":
                        r8c8.config(image=w_hor_w)
                        row_8[8] = u
                    if u == "b_cam":
                        r8c8.config(image=b_cam_w)
                        row_8[8] = u
                    if u == "w_cam":
                        r8c8.config(image=w_cam_w)
                        row_8[8] = u
                    if u == "b_king":
                        r8c8.config(image=b_king_w)
                        row_8[8] = u
                    if u == "w_king":
                        r8c8.config(image=w_king_w)
                        row_8[8] = u
                    if u == "b_que":
                        r8c8.config(image=b_que_w)
                        row_8[8] = u
                    if u == "w_que":
                        r8c8.config(image=w_que_w)
                        row_8[8] = u
                all_ok()
                move_able = []
                unit[0] = "n"
                unit[1] = "n"
                
            else:
                pass
        else:
            tkMessageBox.showinfo("Wrong Move",wrong_move)
    
    ###############################################################################################################
            

def cheat_count():
    global pl_1_tc
    global pl_1_ch
    global pl_2_tc
    global pl_2_ch
    if p_row == 1:
        info = row_1[p_column]
    if p_row == 2:
        info = row_2[p_column]
    if p_row == 3:
        info = row_3[p_column]
    if p_row == 4:
        info = row_4[p_column]
    if p_row == 5:
        info = row_5[p_column]
    if p_row == 6:
        info = row_6[p_column]
    if p_row == 7:
        info = row_7[p_column]
    if p_row == 8:
        info = row_8[p_column]

    if info == "b_ele" or info == "b_cam" or info == "b_hor" or info == "b_que" or info == "w_ele" or info == "w_cam" or info == "w_hor" or info == "w_que":
        if state[0]==1:
            if unit[1][2: ] == "sol":
                pl_1_tc = pl_1_tc - 1
                if pl_1_tc<1:
                    pl_1_tc = 2
                    pl_1_ch = pl_1_ch +1
                player_1_ch_rep.config(text = str(pl_1_ch))
                player_1_tc_rep.config(text = str(pl_1_tc))

        if state[0]==2:
            if unit[1][2: ] == "sol":
                pl_2_tc = pl_2_tc - 1
                if pl_2_tc<1:
                    pl_2_tc = 2
                    pl_2_ch = pl_2_ch +1
                player_2_ch_rep.config(text = str(pl_2_ch))
                player_2_tc_rep.config(text = str(pl_2_tc))

        
def cheat_move():
    if state[1] == 2:
        tkMessageBox.showinfo("unit clicked","Please press ESC button to exit move and \n then use cheat .")
    else:
        if state[0] == 1:
            if pl_1_ch >0:
                cheat_move1()
            else:
                tkMessageBox.showinfo("No cheat","You Dont have any cheat. \n Cut any higher degree opponent unit with a 'pyada'. ")

        if state[0] == 2:
            if pl_2_ch >0:
                cheat_move1()
            else:
                tkMessageBox.showinfo("No Cheat","You Dont have any cheat. \n Cut any higher degree opponent unit with a 'pyada'. ")
          
def cheat_move1():
    global cheat_move_sol
    global cheat_move_unit
    global cheat_l
    global to_nut
    global unit
    global p_row
    global p_column
    boundry.config(text = "CHEAT MODE")
    if True:
        if cheat_move_sol <4:
            while cheat_move_sol <4:
                row = p_row
                column = p_column
                if row == 1:
                    info = row_1[column]
                if row == 2:
                    info = row_2[column]
                if row == 3:
                    info = row_3[column]
                if row == 4:
                    info = row_4[column]
                if row == 5:
                    info = row_5[column]
                if row == 6:
                    info = row_6[column]
                if row == 7:
                    info = row_7[column]
                if row == 8:
                    info = row_8[column]
                if info == "plate":
                    cheat_l.append(p_row*10+p_column)
                    to_nut.append(str(p_row*10+p_column))
                    cheat_move_sol = cheat_move_sol +1
                    unit[0] = str(p_row*10+p_column)
                    blue_plating()
                    unit = ['n','n']
                    break
                else:
                    if to_nut != []:
                        boundry.config(text = "*****************")
                        i=0
                        l=len(to_nut)
                        while i<l:
                            unit[0] = str(to_nut[i])
                            normal()
                            i=i+1
                        to_nut = []
                        cheat_l = []
                        cheat_move_sol = 0
                        cheat_move_unit = 0
                    if p_row != None:
                        tkMessageBox.showinfo("No Plate","Choose only Plate")
                    p_row = None
                    p_column = None
                    break
            if cheat_move_sol == 4:
                cheat_move2()
        else:
            while cheat_move_unit <4:
                row = p_row
                column = p_column
                if row == 1:
                    info = row_1[column]
                if row == 2:
                    info = row_2[column]
                if row == 3:
                    info = row_3[column]
                if row == 4:
                    info = row_4[column]
                if row == 5:
                    info = row_5[column]
                if row == 6:
                    info = row_6[column]
                if row == 7:
                    info = row_7[column]
                if row == 8:
                    info = row_8[column]
                if info == "plate":
                    cheat_l.append(p_row*10+p_column)
                    to_nut.append(str(p_row*10+p_column))
                    cheat_move_unit = cheat_move_unit +1
                    unit[0] = str(p_row*10+p_column)
                    blue_plating()
                    unit = ['n','n']
                    break
                else:
                    if to_nut != []:
                        boundry.config(text = "*****************")
                        i=0
                        l=len(to_nut)
                        while i<l:
                            unit[0] = str(to_nut[i])
                            normal()
                            i=i+1
                        to_nut = []
                        cheat_l = []
                        cheat_move_sol = 0
                        cheat_move_unit = 0
                    if p_row != None:
                        tkMessageBox.showinfo("No Plate","Choose only Plate")
                    p_row = None
                    p_column = None
                    break
            if cheat_move_unit == 4:
                cheat_move4()

def cheat_move2():
    global cheat_l
    global sol_unit
    global to_nut
    global cheat_move_sol
    global cheat_move_unit

    cheat_l.sort()
    row = int(str(cheat_l[1])[0])
    column = int(str(cheat_l[0])[1])
    if row == 1:
        info = row_1[column]
    if row == 2:
        info = row_2[column]
    if row == 3:
        info = row_3[column]
    if row == 4:
        info = row_4[column]
    if row == 5:
        info = row_5[column]
    if row == 6:
        info = row_6[column]
    if row == 7:
        info = row_7[column]
    if row == 8:
        info = row_8[column]
    if state[0] == 1:
        if info[2: ] == "sol":
            if info == "w_sol":
                cheat_l = []
                sol_unit = row*10+column 
            else:
                boundry.config(text = "*****************")
                tkMessageBox.showinfo("Wrong Selection","Select Your own unit !")
                i=0
                while i<4:
                    unit[0] = to_nut[i]
                    normal()
                    i=i+1
                to_nut = []
                cheat_l = []
                cheat_move_sol = 0
                cheat_move_unit = 0
        else:
            boundry.config(text = "*****************")
            tkMessageBox.showinfo("Wrong Selection","Select 'pyada' to activate cheat !")
            i=0
            while i<4:
                unit[0] = to_nut[i]
                normal()
                i=i+1
            to_nut = []
            cheat_l = []
            cheat_move_sol = 0
            cheat_move_unit = 0
    if state[0] == 2:
        if info[2: ]=="sol":
            if info == "b_sol":
                cheat_l = []
                sol_unit = row*10+column 
            else:
                boundry.config(text = "*****************")
                tkMessageBox.showinfo("Wrong Selection","Select Your own unit !")
                i=0
                while i<4:
                    unit[0] = to_nut[i]
                    normal()
                    i=i+1
                to_nut = []
                cheat_l = []
                cheat_move_sol = 0

        else:
            boundry.config(text = "*****************")
            tkMessageBox.showinfo("Wrong Selection","Select 'pyada' to activate cheat !")
            i=0
            while i<4:
                unit[0] = to_nut[i]
                normal()
                i=i+1
            to_nut = []
            cheat_l = []
            cheat_move_sol = 0
            cheat_move_unit = 0

def cheat_move4():
    global cheat_l
    global unit
    global to_nut
    global cheat_move_sol
    global cheat_move_unit
    global pl_1_ch
    global pl_2_ch

    cheat_l.sort()
    i=0
    while i<8:
        unit[0] = to_nut[i]
        normal()
        i=i+1
    unit[0] = 'n'
    row = int(str(cheat_l[1])[0])
    column = int(str(cheat_l[0])[1])
    if row == 1:
        info = row_1[column]
    if row == 2:
        info = row_2[column]
    if row == 3:
        info = row_3[column]
    if row == 4:
        info = row_4[column]
    if row == 5:
        info = row_5[column]
    if row == 6:
        info = row_6[column]
    if row == 7:
        info = row_7[column]
    if row == 8:
        info = row_8[column]

    que_unit = row*10+column
    if state[0] == 1:
        if info != "w_sol":
            if info[2: ] == "king":
                boundry.config(text = "*****************")
                tkMessageBox.showinfo("Selection Error","Bhak \n matlab kuch bhi \n can't select king")
                to_nut = []
                cheat_l = []
                cheat_move_sol = 0
                cheat_move_unit = 0
                
            elif info[0] == "w":
                row = int(str(sol_unit)[0])
                column = int(str(sol_unit)[1])
                
                if row == 1:
                    row = row_1
                if row == 2:
                    row = row_2
                if row == 3:
                    row = row_3
                if row == 4:
                    row = row_4
                if row == 5:
                    row = row_5
                if row == 6:
                    row = row_6
                if row == 7:
                    row = row_7
                if row == 8:
                    row = row_8
                unit[0] = sol_unit
                unit[1] = info
                
                do(None)

                unit[0] = "n"
                unit[1] = "n"
                to_nut = []
                cheat_l = []
                cheat_move_sol = 0
                cheat_move_unit = 0
                pl_1_ch = pl_1_ch-1
                player_1_ch_rep.config(text = str(pl_1_ch))
                boundry.config(text = "*****************")

            
                

            else:
                boundry.config(text = "*****************")
                tkMessageBox.showinfo("Selection Error","Select your own team unit !")
                to_nut = []
                cheat_l = []
                cheat_move_sol = 0
                cheat_move_unit = 0

    if state[0] == 2:
        if info != "b_sol":
            if info[2: ] == "king":
                boundry.config(text = "*****************")
                tkMessageBox.showinfo("Selection Error","Bhak \n matlab kuch bhi \n can't select king")
                to_nut = []
                cheat_l = []
                cheat_move_sol = 0
                cheat_move_unit = 0
                
            elif info[0] == "b":

                row = int(str(sol_unit)[0])
                column = int(str(sol_unit)[1])
                
                if row == 1:
                    row = row_1
                if row == 2:
                    row = row_2
                if row == 3:
                    row = row_3
                if row == 4:
                    row = row_4
                if row == 5:
                    row = row_5
                if row == 6:
                    row = row_6
                if row == 7:
                    row = row_7
                if row == 8:
                    row = row_8
                unit[0] = sol_unit
                unit[1] = info
                
                do(None)

                to_nut = []
                cheat_l = []
                cheat_move_sol = 0
                cheat_move_unit = 0
                pl_2_ch = pl_2_ch-1
                player_1_ch_rep.config(text = str(pl_2_ch))
                boundry.config(text = "*****************")

                unit[0] = "n"
                unit[1] = "n"
            else:
                tkMessageBox.showinfo("Selection Error","Select your own team unit !")
                to_nut = []
                cheat_l = []
                cheat_move_sol = 0
                cheat_move_unit = 0
def all_ok():
    global root2
    global state
    if unit[1] == "w_sol":
        if unit[0][0]=="2":
            
            root2 = Tk()
            root2.config(bg="orange")

            que = Button(root2,text = "    QUEEN   ",command = ch_que_w)
            que.grid(row=2,column=2)

            ele = Button(root2,text = "    ELEPHANT   ",command = ch_ele_w)
            ele.grid(row=2,column=3)

            cam = Button(root2,text = "    CAMMEL   ",command = ch_cam_w)
            cam.grid(row=2,column=4)

            hor = Button(root2,text = "   HORSE   ",command = ch_hor_w)
            hor.grid(row=2,column=5)

    if unit[1] == "b_sol":
        if unit[0][0]=="7":
            
            root2 = Tk()
            root2.config(bg="orange")

            que = Button(root2,text = "    QUEEN   ",command = ch_que_b)
            que.grid(row=2,column=2)

            ele = Button(root2,text = "    ELEPHANT   ",command = ch_ele_b)
            ele.grid(row=2,column=3)

            cam = Button(root2,text = "    CAMMEL   ",command = ch_cam_b)
            cam.grid(row=2,column=4)

            hor = Button(root2,text = "   HORSE   ",command = ch_hor_b)
            hor.grid(row=2,column=5)
    
    if state[0] == 1:
        state[0] = 2
        player.config(text = "Player : 2 \n Black",bg="Black",fg="white")
    elif state[0] == 2:
        player.config(text = "Player : 1 \n White",bg="White",fg="black")
        state[0] = 1


def ch_que_w():
    global unit
    
    
    row = row_1
    i=0
    l=len(row)
    while i<l:
                x = row[i]
                if x == "w_sol":
                    get = i
                    break
                i=i+1

    pos = 10+get
    unit[0] = pos
    unit[1] = "w_que"
    do(None)
    root2.destroy()

def ch_cam_w():
    global unit
    row = row_1
    i=0
    l=len(row)
    while i<l:
                x = row[i]
                if x == "w_sol":
                    get = i
                    break
                i=i+1

    pos = 10+get
    unit[0] = pos
    unit[1] = "w_cam"

    do(None)
    root2.destroy()

def ch_hor_w():
    global unit
    row = row_1
    i=0
    l=len(row)
    while i<l:
                x = row[i]
                if x == "w_sol":
                    get = i
                    break
                i=i+1

    pos = 10+get
    unit[0] = pos
    unit[1] = "w_hor"
    do(None)
    root2.destroy()

def ch_ele_w():
    global unit
    row = row_1
    i=0
    l=len(row)
    while i<l:
                x = row[i]
                if x == "w_sol":
                    get = i
                    break
                i=i+1

    pos = 10+get
    unit[0] = pos
    unit[1] = "w_ele"
    do(None)
    root2.destroy()



##################

def ch_que_b():
    global unit
    row = row_8
    i=0
    l=len(row)
    while i<l:
                x = row[i]
                if x == "b_sol":
                    get = i
                    break
                i=i+1

    pos = 80+get
    unit[0] = pos
    unit[1] = "b_que"
    do(None)
    root2.destroy()

def ch_cam_b():
    global unit
    row = row_8
    i=0
    l=len(row)
    while i<l:
                x = row[i]
                if x == "b_sol":
                    get = i
                    break
                i=i+1

    pos = 80+get
    unit[0] = pos
    unit[1] = "b_cam"
    do(None)
    root2.destroy()

def ch_hor_b():
    global unit
    row = row_8
    i=0
    l=len(row)
    while i<l:
                x = row[i]
                if x == "b_sol":
                    get = i
                    break
                i=i+1

    pos = 80+get
    unit[0] = pos
    unit[1] = "b_hor"
    do(None)
    root2.destroy()

def ch_ele_b():
    global unit
    row = row_8
    i=0
    l=len(row)
    while i<l:
                x = row[i]
                if x == "b_sol":
                    get = i
                    break
                i=i+1

    pos = 80+get
    unit[0] = pos
    unit[1] = "b_ele"
    do(None)
    root2.destroy()

def blue_plating():
            if unit[0] == "11":
                    row_1[1] = "plate"
                    r1c1.config(image=blue_plate)
            if unit[0] == "12":
                    row_1[2] = "plate"
                    r1c2.config(image=blue_plate)
            if unit[0] == "13":
                    row_1[3] = "plate"
                    r1c3.config(image=blue_plate)

            if unit[0] == "14":
                    row_1[4] = "plate"
                    r1c4.config(image=blue_plate)
            if unit[0] == "15":
                    row_1[5] = "plate"
                    r1c5.config(image=blue_plate)
            if unit[0] == "16":
                    row_1[6] = "plate"
                    r1c6.config(image=blue_plate)
            if unit[0] == "17":
                    row_1[7] = "plate"
                    r1c7.config(image=blue_plate)
            if unit[0] == "18":
                    row_1[8] = "plate"
                    r1c8.config(image=blue_plate)
            if unit[0] == "21":
                    row_2[1] = "plate"
                    r2c1.config(image=blue_plate)
            if unit[0] == "22":
                    row_2[2] = "plate"
                    r2c2.config(image=blue_plate)
            if unit[0] == "23":
                    row_2[3] = "plate"
                    r2c3.config(image=blue_plate)
            if unit[0] == "24":
                    row_2[4] = "plate"
                    r2c4.config(image=blue_plate)
            if unit[0] == "25":
                    row_2[5] = "plate"
                    r2c5.config(image=blue_plate)
            if unit[0] == "26":
                    row_2[6] = "plate"
                    r2c6.config(image=blue_plate)
            if unit[0] == "27":
                    row_2[7] = "plate"
                    r2c7.config(image=blue_plate)
            if unit[0] == "28":
                    row_2[8] = "plate"
                    r2c8.config(image=blue_plate)
            if unit[0] == "31":
                    row_3[1] = "plate"
                    r3c1.config(image=blue_plate)
            if unit[0] == "32":
                    row_3[2] = "plate"
                    r3c2.config(image=blue_plate)
            if unit[0] == "33":
                    row_3[3] = "plate"
                    r3c3.config(image=blue_plate)
            if unit[0] == "34":
                    row_3[4] = "plate"
                    r3c4.config(image=blue_plate)
            if unit[0] == "35":
                    row_3[5] = "plate"
                    r3c5.config(image=blue_plate)
            if unit[0] == "36":
                    row_3[6] = "plate"
                    r3c6.config(image=blue_plate)
            if unit[0] == "37":
                    row_3[7] = "plate"
                    r3c7.config(image=blue_plate)
            if unit[0] == "38":
                    row_3[8] = "plate"
                    r3c8.config(image=blue_plate)
            if unit[0] == "41":
                    row_4[1] = "plate"
                    r4c1.config(image=blue_plate)
            if unit[0] == "42":
                    row_4[2] = "plate"
                    r4c2.config(image=blue_plate)
            if unit[0] == "43":
                    row_4[3] = "plate"
                    r4c3.config(image=blue_plate)
            if unit[0] == "44":
                    row_4[4] = "plate"
                    r4c4.config(image=blue_plate)
            if unit[0] == "45":
                    row_4[5] = "plate"
                    r4c5.config(image=blue_plate)
            if unit[0] == "46":
                    row_4[6] = "plate"
                    r4c6.config(image=blue_plate)
            if unit[0] == "47":
                    row_4[7] = "plate"
                    r4c7.config(image=blue_plate)
            if unit[0] == "48":
                    row_4[8] = "plate"
                    r4c8.config(image=blue_plate)
                    
            if unit[0] == "51":
                    row_5[1] = "plate"
                    r5c1.config(image=blue_plate)
            if unit[0] == "52":
                    row_5[2] = "plate"
                    r5c2.config(image=blue_plate)
            if unit[0] == "53":
                    row_5[3] = "plate"
                    r5c3.config(image=blue_plate)
            if unit[0] == "54":
                    row_5[4] = "plate"
                    r5c4.config(image=blue_plate)
            if unit[0] == "55":
                    row_5[5] = "plate"
                    r5c5.config(image=blue_plate)
            if unit[0] == "56":
                    row_5[6] = "plate"
                    r5c6.config(image=blue_plate)
            if unit[0] == "57":
                    row_5[7] = "plate"
                    r5c7.config(image=blue_plate)
            if unit[0] == "58":
                    row_5[8] = "plate"
                    r5c8.config(image=blue_plate)
            if unit[0] == "61": 
                    row_6[1] = "plate"
                    r6c1.config(image=blue_plate)
            if unit[0] == "62":
                    row_6[2] = "plate"
                    r6c2.config(image=blue_plate)
            if unit[0] == "63":
                    row_6[3] = "plate"
                    r6c3.config(image=blue_plate)
            if unit[0] == "64":
                    row_6[4] = "plate"
                    r6c4.config(image=blue_plate)
            if unit[0] == "65":
                    row_6[5] = "plate"
                    r6c5.config(image=blue_plate)
            if unit[0] == "66":
                    row_6[6] = "plate"
                    r6c6.config(image=blue_plate)
            if unit[0] == "67":
                    row_6[7] = "plate"
                    r6c7.config(image=blue_plate)
            if unit[0] == "68":
                    row_6[8] = "plate"
                    r6c8.config(image=blue_plate)
            if unit[0] == "71":
                    row_7[1] = "plate"
                    r7c1.config(image=blue_plate)
            if unit[0] == "72":
                    row_7[2] = "plate"
                    r7c2.config(image=blue_plate)
            if unit[0] == "73":
                    row_7[3] = "plate"
                    r7c3.config(image=blue_plate)
            if unit[0] == "74":
                    row_7[4] = "plate"
                    r7c4.config(image=blue_plate)
            if unit[0] == "75":
                    row_7[5] = "plate"
                    r7c5.config(image=blue_plate)
            if unit[0] == "76":
                    row_7[6] = "plate"
                    r7c6.config(image=blue_plate)
            if unit[0] == "77":
                    row_7[7] = "plate"
                    r7c7.config(image=blue_plate)
            if unit[0] == "78":
                    row_7[8] = "plate"
                    r7c8.config(image=blue_plate)
            if unit[0] == "81":
                    row_8[1] = "plate"
                    r8c1.config(image=blue_plate)
            if unit[0] == "82":
                    row_8[2] = "plate"
                    r8c2.config(image=blue_plate)
            if unit[0] == "83":
                    row_8[3] = "plate"
                    r8c3.config(image=blue_plate)
            if unit[0] == "84":
                    row_8[4] = "plate"
                    r8c4.config(image=blue_plate)
            if unit[0] == "85":
                    row_8[5] = "plate"
                    r8c5.config(image=blue_plate)
            if unit[0] == "86":
                    row_8[6] = "plate"
                    r8c6.config(image=blue_plate)
            if unit[0] == "87":
                    row_8[7] = "plate"
                    r8c7.config(image=blue_plate)
            if unit[0] == "88":
                    row_8[8] = "plate"
                    r8c8.config(image=blue_plate)

                    
def normal():
            
            if unit[0] == "11":
                    row_1[1] = "plate"
                    r1c1.config(image=w_plate)
            if unit[0] == "12":
                    row_1[2] = "plate"
                    r1c2.config(image=b_plate)
            if unit[0] == "13":
                    row_1[3] = "plate"
                    r1c3.config(image=w_plate)

            if unit[0] == "14":
                    row_1[4] = "plate"
                    r1c4.config(image=b_plate)
            if unit[0] == "15":
                    row_1[5] = "plate"
                    r1c5.config(image=w_plate)
            if unit[0] == "16":
                    row_1[6] = "plate"
                    r1c6.config(image=b_plate)
            if unit[0] == "17":
                    row_1[7] = "plate"
                    r1c7.config(image=w_plate)
            if unit[0] == "18":
                    row_1[8] = "plate"
                    r1c8.config(image=b_plate)
            if unit[0] == "21":
                    row_2[1] = "plate"
                    r2c1.config(image=b_plate)
            if unit[0] == "22":
                    row_2[2] = "plate"
                    r2c2.config(image=w_plate)
            if unit[0] == "23":
                    row_2[3] = "plate"
                    r2c3.config(image=b_plate)
            if unit[0] == "24":
                    row_2[4] = "plate"
                    r2c4.config(image=w_plate)
            if unit[0] == "25":
                    row_2[5] = "plate"
                    r2c5.config(image=b_plate)
            if unit[0] == "26":
                    row_2[6] = "plate"
                    r2c6.config(image=w_plate)
            if unit[0] == "27":
                    row_2[7] = "plate"
                    r2c7.config(image=b_plate)
            if unit[0] == "28":
                    row_2[8] = "plate"
                    r2c8.config(image=w_plate)
            if unit[0] == "31":
                    row_3[1] = "plate"
                    r3c1.config(image=w_plate)
            if unit[0] == "32":
                    row_3[2] = "plate"
                    r3c2.config(image=b_plate)
            if unit[0] == "33":
                    row_3[3] = "plate"
                    r3c3.config(image=w_plate)
            if unit[0] == "34":
                    row_3[4] = "plate"
                    r3c4.config(image=b_plate)
            if unit[0] == "35":
                    row_3[5] = "plate"
                    r3c5.config(image=w_plate)
            if unit[0] == "36":
                    row_3[6] = "plate"
                    r3c6.config(image=b_plate)
            if unit[0] == "37":
                    row_3[7] = "plate"
                    r3c7.config(image=w_plate)
            if unit[0] == "38":
                    row_3[8] = "plate"
                    r3c8.config(image=b_plate)
            if unit[0] == "41":
                    row_4[1] = "plate"
                    r4c1.config(image=b_plate)
            if unit[0] == "42":
                    row_4[2] = "plate"
                    r4c2.config(image=w_plate)
            if unit[0] == "43":
                    row_4[3] = "plate"
                    r4c3.config(image=b_plate)
            if unit[0] == "44":
                    row_4[4] = "plate"
                    r4c4.config(image=w_plate)
            if unit[0] == "45":
                    row_4[5] = "plate"
                    r4c5.config(image=b_plate)
            if unit[0] == "46":
                    row_4[6] = "plate"
                    r4c6.config(image=w_plate)
            if unit[0] == "47":
                    row_4[7] = "plate"
                    r4c7.config(image=b_plate)
            if unit[0] == "48":
                    row_4[8] = "plate"
                    r4c8.config(image=w_plate)
                    
            if unit[0] == "51":
                    row_5[1] = "plate"
                    r5c1.config(image=w_plate)
            if unit[0] == "52":
                    row_5[2] = "plate"
                    r5c2.config(image=b_plate)
            if unit[0] == "53":
                    row_5[3] = "plate"
                    r5c3.config(image=w_plate)
            if unit[0] == "54":
                    row_5[4] = "plate"
                    r5c4.config(image=b_plate)
            if unit[0] == "55":
                    row_5[5] = "plate"
                    r5c5.config(image=w_plate)
            if unit[0] == "56":
                    row_5[6] = "plate"
                    r5c6.config(image=b_plate)
            if unit[0] == "57":
                    row_5[7] = "plate"
                    r5c7.config(image=w_plate)
            if unit[0] == "58":
                    row_5[8] = "plate"
                    r5c8.config(image=b_plate)
            if unit[0] == "61":
                    row_6[1] = "plate"
                    r6c1.config(image=b_plate)
            if unit[0] == "62":
                    row_6[2] = "plate"
                    r6c2.config(image=w_plate)
            if unit[0] == "63":
                    row_6[3] = "plate"
                    r6c3.config(image=b_plate)
            if unit[0] == "64":
                    row_6[4] = "plate"
                    r6c4.config(image=w_plate)
            if unit[0] == "65":
                    row_6[5] = "plate"
                    r6c5.config(image=b_plate)
            if unit[0] == "66":
                    row_6[6] = "plate"
                    r6c6.config(image=w_plate)
            if unit[0] == "67":
                    row_6[7] = "plate"
                    r6c7.config(image=b_plate)
            if unit[0] == "68":
                    row_6[8] = "plate"
                    r6c8.config(image=w_plate)
            if unit[0] == "71":
                    row_7[1] = "plate"
                    r7c1.config(image=w_plate)
            if unit[0] == "72":
                    row_7[2] = "plate"
                    r7c2.config(image=b_plate)
            if unit[0] == "73":
                    row_7[3] = "plate"
                    r7c3.config(image=w_plate)
            if unit[0] == "74":
                    row_7[4] = "plate"
                    r7c4.config(image=b_plate)
            if unit[0] == "75":
                    row_7[5] = "plate"
                    r7c5.config(image=w_plate)
            if unit[0] == "76":
                    row_7[6] = "plate"
                    r7c6.config(image=b_plate)
            if unit[0] == "77":
                    row_7[7] = "plate"
                    r7c7.config(image=w_plate)
            if unit[0] == "78":
                    row_7[8] = "plate"
                    r7c8.config(image=b_plate)
            if unit[0] == "81":
                    row_8[1] = "plate"
                    r8c1.config(image=b_plate)
            if unit[0] == "82":
                    row_8[2] = "plate"
                    r8c2.config(image=w_plate)
            if unit[0] == "83":
                    row_8[3] = "plate"
                    r8c3.config(image=b_plate)
            if unit[0] == "84":
                    row_8[4] = "plate"
                    r8c4.config(image=w_plate)
            if unit[0] == "85":
                    row_8[5] = "plate"
                    r8c5.config(image=b_plate)
            if unit[0] == "86":
                    row_8[6] = "plate"
                    r8c6.config(image=w_plate)
            if unit[0] == "87":
                    row_8[7] = "plate"
                    r8c7.config(image=b_plate)
            if unit[0] == "88":
                    row_8[8] = "plate"
                    r8c8.config(image=w_plate)
            
def r1c1_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    
    p_row =1
    p_column=1
    main_move()
def r1c2_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=2
    main_move()
    
def r1c3_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=3
    main_move()
    
def r1c4_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=4
    main_move()
    
def r1c5_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=5
    main_move()
    
def r1c6_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=6
    main_move()
    
def r1c7_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=7
    main_move()
    
def r1c8_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=8
    main_move()
    
def r2c1_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    global state
    global unit

    p_row =2
    p_column=1

    main_move()

def r2c2_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit


    p_row =2
    p_column=2
    main_move()
    
def r2c3_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=3
    main_move()
    
def r2c4_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=4
    main_move()
    
def r2c5_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=5
    main_move()
    
def r2c6_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=6
    main_move()
    
def r2c7_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=7
    main_move()
    
def r2c8_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=8
    main_move()
    
def r3c1_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit

    p_row =3
    p_column=1
    
    main_move()

def r3c2_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=2
    main_move()

def r3c3_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=3
    main_move()

def r3c4_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=4
    main_move()
    
def r3c5_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=5
    main_move()
    
def r3c6_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=6
    main_move()
    
def r3c7_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=7
    main_move()
    
def r3c8_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=8
    main_move()
    
def r4c1_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=1
    main_move()
    
def r4c2_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=2
    main_move()
    
def r4c3_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=3
    main_move()
    
def r4c4_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=4
    main_move()
    
def r4c5_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=5
    main_move()
    
def r4c6_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=6
    main_move()
    
def r4c7_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=7
    main_move()
    
def r4c8_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=8
    main_move()
    
def r5c1_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=1
    main_move()
    
def r5c2_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=2
    main_move()

def r5c3_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=3
    main_move()
    
def r5c4_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=4
    main_move()
    
def r5c5_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=5
    main_move()
    

def r5c6_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=6
    main_move()
    

def r5c7_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=7
    main_move()
    

def r5c8_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=8
    main_move()
    

def r6c1_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=1
    main_move()
    

def r6c2_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=2
    main_move()
    

def r6c3_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=3
    main_move()
    

def r6c4_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=4
    main_move()
    

def r6c5_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=5
    main_move()
    
def r6c6_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=6
    main_move()
    

def r6c7_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=7
    main_move()
    

def r6c8_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=8
    main_move()
    

def r7c1_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=1
    main_move()
    

def r7c2_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=2
    main_move()
    

def r7c3_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=3
    main_move()
    

def r7c4_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=4
    main_move()
    

def r7c5_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=5
    main_move()
    

def r7c6_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=6
    main_move()
    

def r7c7_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=7
    main_move()
    

def r7c8_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=8
    main_move()
    

def r8c1_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=1
    main_move()
    

def r8c2_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=2
    main_move()
    

def r8c3_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=3
    main_move()
    

def r8c4_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=4
    main_move()
    

def r8c5_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=5
    main_move()
    

def r8c6_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=6
    main_move()
    

def r8c7_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=7
    main_move()
    

def r8c8_move():
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=8
    main_move()

def r1c1_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    
    p_row =1
    p_column=1
    cheat_move()
def r1c2_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=2
    cheat_move()
    
def r1c3_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=3
    cheat_move()
    
def r1c4_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=4
    cheat_move()
    
def r1c5_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=5
    cheat_move()
    
def r1c6_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=6
    cheat_move()
    
def r1c7_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=7
    cheat_move()
    
def r1c8_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =1
    p_column=8
    cheat_move()
    
def r2c1_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    global state
    global unit

    p_row =2
    p_column=1

    cheat_move()

def r2c2_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit


    p_row =2
    p_column=2
    cheat_move()
    
def r2c3_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=3
    cheat_move()
    
def r2c4_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=4
    cheat_move()
    
def r2c5_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=5
    cheat_move()
    
def r2c6_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=6
    cheat_move()
    
def r2c7_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=7
    cheat_move()
    
def r2c8_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =2
    p_column=8
    cheat_move()
    
def r3c1_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit

    p_row =3
    p_column=1
    
    cheat_move()

def r3c2_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=2
    cheat_move()

def r3c3_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=3
    cheat_move()

def r3c4_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=4
    cheat_move()
    
def r3c5_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=5
    cheat_move()
    
def r3c6_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=6
    cheat_move()
    
def r3c7_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=7
    cheat_move()
    
def r3c8_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =3
    p_column=8
    cheat_move()
    
def r4c1_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=1
    cheat_move()
    
def r4c2_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=2
    cheat_move()
    
def r4c3_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=3
    cheat_move()
    
def r4c4_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=4
    cheat_move()
    
def r4c5_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=5
    cheat_move()
    
def r4c6_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=6
    cheat_move()
    
def r4c7_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=7
    cheat_move()
    
def r4c8_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =4
    p_column=8
    cheat_move()
    
def r5c1_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=1
    cheat_move()
    
def r5c2_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=2
    cheat_move()

def r5c3_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=3
    cheat_move()
    
def r5c4_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=4
    cheat_move()
    
def r5c5_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=5
    cheat_move()
    

def r5c6_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=6
    cheat_move()
    

def r5c7_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=7
    cheat_move()
    

def r5c8_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =5
    p_column=8
    cheat_move()
    

def r6c1_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=1
    cheat_move()
    

def r6c2_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=2
    cheat_move()
    

def r6c3_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=3
    cheat_move()
    

def r6c4_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=4
    cheat_move()
    

def r6c5_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=5
    cheat_move()
    
def r6c6_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=6
    cheat_move()
    

def r6c7_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=7
    cheat_move()
    

def r6c8_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =6
    p_column=8
    cheat_move()
    

def r7c1_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=1
    cheat_move()
    

def r7c2_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=2
    cheat_move()
    

def r7c3_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=3
    cheat_move()
    

def r7c4_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=4
    cheat_move()
    

def r7c5_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=5
    cheat_move()
    

def r7c6_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=6
    cheat_move()
    

def r7c7_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=7
    cheat_move()
    

def r7c8_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =7
    p_column=8
    cheat_move()
    

def r8c1_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=1
    cheat_move()
    

def r8c2_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=2
    cheat_move()
    

def r8c3_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=3
    cheat_move()
    

def r8c4_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=4
    cheat_move()
    

def r8c5_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=5
    cheat_move()
    

def r8c6_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=6
    cheat_move()
    

def r8c7_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=7
    cheat_move()
    

def r8c8_cheat(event):
    global p_row
    global p_column
    global row_1
    global row_2
    global row_3
    global row_4
    global row_5
    global row_6
    global row_7
    global row_8
    global state
    global unit
    p_row =8
    p_column=8
    cheat_move()

def help_me():
    global main_ab
    global ba_btn
    global enter

    m1.destroy()
    m2.destroy()
    m3.destroy()
    m4.destroy()
    m5.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    l.destroy()
    
    main_ab = Label(root,text = "Chess \n \n  This is simply a chess game with some interesting feature . \n In this you can use CHEAT  \n\n Yes! cheat.... You have to kill two upper  \n Order unit [horse,camel,queen,elephant] by Soldier \n It will give you a cheat \n\n \t \t For feedback please write us  email on : dimension@working.com \n We will take care our your demands and feedback \n Thankyou \n \n  \n                                                            Saurabh Agrawal \n                                                               CEO \n                                                               Dimesion corp. ",bg="orange",font="99")
    main_ab.grid(row=4,column=4)

    ba_btn = Button(root,text = "BACK",command = ask)
    ba_btn.grid(row=3,column=5)

    enter = "about"


def about():
    global main_ab
    global ba_btn
    global enter

    m1.destroy()
    m2.destroy()
    m3.destroy()
    m4.destroy()
    m5.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    l.destroy()
    
    main_ab = Label(root,text = "Chess \n \n \t\t This is CHESS game developed by Dimension corp. \n \t\t In this we have tried to make our game more user friendly,\n Interesting,attractive \n\n  We have tried to fullfill every need of a player \n We are trying to connect it with LAN \n So that you can enjoy this\n With some one near your\n house... \n\n\n For feedback please write us  email on : dimension@working.com \n We will take care our your demands and feedback \n Thankyou \n \n  \n                                                            Saurabh Agrawal \n                                                               CEO \n                                                               Dimesion corp. ",bg="orange",font="99")
    main_ab.grid(row=4,column=4)

    ba_btn = Button(root,text = "BACK",command = ask)
    ba_btn.grid(row=3,column=5)

    enter = "about"

def ask():
    global l
    global m1
    global m2
    global m3
    global m4
    global m5
    global b1
    global b2
    global b3
    global b4
    global b5
    global enter

    if enter == "about":
        main_ab.destroy()
        ba_btn.destroy()
        enter= None

    if enter == "setting":
        main_ab.destroy()
        ba_btn.destroy()
        ch1.destroy()
        ch2.destroy()
        enter= None

    m1 = Label(root,text = "\n\n\n\t\t\n\n\n\t\t\t\t\t\t\t\t\t\t",bg="orange",fg="blue",font="99")
    m1.grid(row=3,column=3)
    l=Label(root,text = "Dimension chess  ",bg="orange",fg="blue",font="99")
    l.grid(row=3,column=3)

    b1 = Button(root,text = "   Start game      ",command =basic)
    b1.grid(row=4,column=3)
    m2 = Label(root,text = "\n\n",bg="orange",fg="blue",font="99")
    m2.grid(row=5,column=3)
    b5 = Button(root,text = "   Setting      ",command =setting)
    b5.grid(row=6,column=3)
    m5 = Label(root,text = "\n",bg="orange",fg="blue",font="99")
    m5.grid(row=7,column=3)
    b4 = Button(root,text = "   HELP      ",command =help_me)
    b4.grid(row=8,column=3)
    m3 = Label(root,text = "\n",bg="orange",fg="blue",font="99")
    m3.grid(row=9,column=3)
    b2 = Button(root,text = "   About      ",command =about)
    b2.grid(row=10,column=3)
    m4 = Label(root,text = "\n",bg="orange",fg="blue",font="99")
    m4.grid(row=11,column=3)
    b3 = Button(root,text = "   Quit      ",command =root.destroy)
    b3.grid(row=12,column=3)

        
    
def setting():
    global main_ab
    global ba_btn
    global ch1
    global ch2
    global enter

    m1.destroy()
    m2.destroy()
    m3.destroy()
    m4.destroy()
    m5.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    l.destroy()
    
    main_ab = Label(root,text ="\n\n\t\t\tSetting\n\n \t\t Choose Graphics : \t\t\t\t\n\n\n: ",bg="orange",fg="red",font="99")
    main_ab.grid(row=4,column=4)
    
    ch1 = Button(root,height = 55 ,width=55,command=unit_type_1)
    ch1.grid(row=5,column=4)
    ch1.config(image = ch1_w_king_w)

    ch2 = Button(root,height = 55 ,width=55,command=unit_type_2)
    ch2.grid(row=5,column=5)
    ch2.config(image = ch2_w_king_w)
    
    ba_btn = Button(root,text = "BACK",command = ask)
    ba_btn.grid(row=3,column=5)

    enter = "setting"

def unit_type_1():
    global type_of_unit
    type_of_unit = 1
    load_graphics()
def unit_type_2():
    global type_of_unit
    type_of_unit = 2   
    load_graphics()
def do(event):
            global state
            global whole_match
            global main_dic

            try:
                
                place = unit[0]
                place = int(place)
            except:
                
                pass
            else:
                main_dic[place]=unit[1]
                l = len(whole_match.keys())
                ew_dic_game= {l+1:main_dic}
                whole_match.update(ew_dic_game)
                if place == 11 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c1.config(image=b_sol_w)
                        row_1[1] = u
                    if u == "w_sol":
                        r1c1.config(image=w_sol_w)
                        row_1[1] = u
                    if u == "b_ele":
                        r1c1.config(image=b_ele_w)
                        row_1[1] = u
                    if u == "w_ele":
                        r1c1.config(image=w_ele_w)
                        row_1[1] = u
                    if u == "b_hor":
                        r1c1.config(image=b_hor_w)
                        row_1[1] = u
                    if u == "w_hor":
                        r1c1.config(image=w_hor_w)
                        row_1[1] = u
                    if u == "b_cam":
                        r1c1.config(image=b_cam_w)
                        row_1[1] = u
                    if u == "w_cam":
                        r1c1.config(image=w_cam_w)
                        row_1[1] = u
                    if u == "b_king":
                        r1c1.config(image=b_king_w)
                        row_1[1] = u
                    if u == "w_king":
                        r1c1.config(image=w_king_w)
                        row_1[1] = u
                    if u == "b_que":
                        r1c1.config(image=b_que_w)
                        row_1[1] = u
                    if u == "w_que":
                        r1c1.config(image=w_que_w)
                        row_1[1] = u
        ######################################################################
                        
                if place == 13 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c3.config(image=b_sol_w)
                        row_1[3] = u
                    if u == "w_sol":
                        r1c3.config(image=w_sol_w)
                        row_1[3] = u
                    if u == "b_ele":
                        r1c3.config(image=b_ele_w)
                        row_1[3] = u
                    if u == "w_ele":
                        r1c3.config(image=w_ele_w)
                        row_1[3] = u
                    if u == "b_hor":
                        r1c3.config(image=b_hor_w)
                        row_1[3] = u
                    if u == "w_hor":
                        r1c3.config(image=w_hor_w)
                        row_1[3] = u
                    if u == "b_cam":
                        r1c3.config(image=b_cam_w)
                        row_1[3] = u
                    if u == "w_cam":
                        r1c3.config(image=w_cam_w)
                        row_1[3] = u
                    if u == "b_king":
                        r1c3.config(image=b_king_w)
                        row_1[3] = u
                    if u == "w_king":
                        r1c3.config(image=w_king_w)
                        row_1[3] = u
                    if u == "b_que":
                        r1c3.config(image=b_que_w)
                        row_1[3] = u
                    if u == "w_que":
                        r1c3.config(image=w_que_w)
                        row_1[3] = u
        ##############################################################################################
                if place == 15 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c5.config(image=b_sol_w)
                        row_1[5] = u
                    if u == "w_sol":
                        r1c5.config(image=w_sol_w)
                        row_1[5] = u
                    if u == "b_ele":
                        r1c5.config(image=b_ele_w)
                        row_1[5] = u
                    if u == "w_ele":
                        r1c5.config(image=w_ele_w)
                        row_1[5] = u
                    if u == "b_hor":
                        r1c5.config(image=b_hor_w)
                        row_1[5] = u
                    if u == "w_hor":
                        r1c5.config(image=w_hor_w)
                        row_1[5] = u
                    if u == "b_cam":
                        r1c5.config(image=b_cam_w)
                        row_1[5] = u
                    if u == "w_cam":
                        r1c5.config(image=w_cam_w)
                        row_1[5] = u
                    if u == "b_king":
                        r1c5.config(image=b_king_w)
                        row_1[5] = u
                    if u == "w_king":
                        r1c5.config(image=w_king_w)
                        row_1[5] = u
                    if u == "b_que":
                        r1c5.config(image=b_que_w)
                        row_1[5] = u
                    if u == "w_que":
                        r1c5.config(image=w_que_w)
                        row_1[5] = u
        ######################################################################################
                if place == 17 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c7.config(image=b_sol_w)
                        row_1[7] = u
                    if u == "w_sol":
                        r1c7.config(image=w_sol_w)
                        row_1[7] = u
                    if u == "b_ele":
                        r1c7.config(image=b_ele_w)
                        row_1[7] = u
                    if u == "w_ele":
                        r1c7.config(image=w_ele_w)
                        row_1[7] = u
                    if u == "b_hor":
                        r1c7.config(image=b_hor_w)
                        row_1[7] = u
                    if u == "w_hor":
                        r1c7.config(image=w_hor_w)
                        row_1[7] = u
                    if u == "b_cam":
                        r1c7.config(image=b_cam_w)
                        row_1[7] = u
                    if u == "w_cam":
                        r1c7.config(image=w_cam_w)
                        row_1[7] = u
                    if u == "b_king":
                        r1c7.config(image=b_king_w)
                        row_1[7] = u
                    if u == "w_king":
                        r1c7.config(image=w_king_w)
                        row_1[7] = u
                    if u == "b_que":
                        r1c7.config(image=b_que_w)
                        row_1[7] = u
                    if u == "w_que":
                        r1c7.config(image=w_que_w)
                        row_1[7] = u
        ######################################################################################
                if place == 21 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c1.config(image=b_sol_b)
                        row_2[1] = u
                    if u == "w_sol":
                        r2c1.config(image=w_sol_b)
                        row_2[1] = u
                    if u == "b_ele":
                        r2c1.config(image=b_ele_b)
                        row_2[1] = u
                    if u == "w_ele":
                        r2c1.config(image=w_ele_b)
                        row_2[1] = u
                    if u == "b_hor":
                        r2c1.config(image=b_hor_b)
                        row_2[1] = u
                    if u == "w_hor":
                        r2c1.config(image=w_hor_b)
                        row_2[1] = u
                    if u == "b_cam":
                        r2c1.config(image=b_cam_b)
                        row_2[1] = u
                    if u == "w_cam":
                        r2c1.config(image=w_cam_b)
                        row_2[1] = u
                    if u == "b_king":
                        r2c1.config(image=b_king_b)
                        row_2[1] = u
                    if u == "w_king":
                        r2c1.config(image=w_king_b)
                        row_2[1] = u
                    if u == "b_que":
                        r2c1.config(image=b_que_b)
                        row_2[1] = u
                    if u == "w_que":
                        r2c1.config(image=w_que_b)
                        row_2[1] = u
        ######################################################################################
                if place == 23 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c3.config(image=b_sol_b)
                        row_2[3] = u
                    if u == "w_sol":
                        r2c3.config(image=w_sol_b)
                        row_2[3] = u
                    if u == "b_ele":
                        r2c3.config(image=b_ele_b)
                        row_2[3] = u
                    if u == "w_ele":
                        r2c3.config(image=w_ele_b)
                        row_2[3] = u
                    if u == "b_hor":
                        r2c3.config(image=b_hor_b)
                        row_2[3] = u
                    if u == "w_hor":
                        r2c3.config(image=w_hor_b)
                        row_2[3] = u
                    if u == "b_cam":
                        r2c3.config(image=b_cam_b)
                        row_2[3] = u
                    if u == "w_cam":
                        r2c3.config(image=w_cam_b)
                        row_2[3] = u
                    if u == "b_king":
                        r2c3.config(image=b_king_b)
                        row_2[3] = u
                    if u == "w_king":
                        r2c3.config(image=w_king_b)
                        row_2[3] = u
                    if u == "b_que":
                        r2c3.config(image=b_que_b)
                        row_2[3] = u
                    if u == "w_que":
                        r2c3.config(image=w_que_b)
                        row_2[3] = u
        ######################################################################################
                if place == 25 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c5.config(image=b_sol_b)
                        row_2[5] = u
                    if u == "w_sol":
                        r2c5.config(image=w_sol_b)
                        row_2[5] = u
                    if u == "b_ele":
                        r2c5.config(image=b_ele_b)
                        row_2[5] = u
                    if u == "w_ele":
                        r2c5.config(image=w_ele_b)
                        row_2[5] = u
                    if u == "b_hor":
                        r2c5.config(image=b_hor_b)
                        row_2[5] = u
                    if u == "w_hor":
                        r2c5.config(image=w_hor_b)
                        row_2[5] = u
                    if u == "b_cam":
                        r2c5.config(image=b_cam_b)
                        row_2[5] = u
                    if u == "w_cam":
                        r2c5.config(image=w_cam_b)
                        row_2[5] = u
                    if u == "b_king":
                        r2c5.config(image=b_king_b)
                        row_2[5] = u
                    if u == "w_king":
                        r2c5.config(image=w_king_b)
                        row_2[5] = u
                    if u == "b_que":
                        r2c5.config(image=b_que_b)
                        row_2[5] = u
                    if u == "w_que":
                        r2c5.config(image=w_que_b)
                        row_2[5] = u
        ######################################################################################
                if place == 27 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c7.config(image=b_sol_b)
                        row_2[7] = u
                    if u == "w_sol":
                        r2c7.config(image=w_sol_b)
                        row_2[7] = u
                    if u == "b_ele":
                        r2c7.config(image=b_ele_b)
                        row_2[7] = u
                    if u == "w_ele":
                        r2c7.config(image=w_ele_b)
                        row_2[7] = u
                    if u == "b_hor":
                        r2c7.config(image=b_hor_b)
                        row_2[7] = u
                    if u == "w_hor":
                        r2c7.config(image=w_hor_b)
                        row_2[7] = u
                    if u == "b_cam":
                        r2c7.config(image=b_cam_b)
                        row_2[7] = u
                    if u == "w_cam":
                        r2c7.config(image=w_cam_b)
                        row_2[7] = u
                    if u == "b_king":
                        r2c7.config(image=b_king_b)
                        row_2[7] = u
                    if u == "w_king":
                        r2c7.config(image=w_king_b)
                        row_2[7] = u
                    if u == "b_que":
                        r2c7.config(image=b_que_b)
                        row_2[7] = u
                    if u == "w_que":
                        r2c7.config(image=w_que_b)
                        row_2[7] = u
        ######################################################################################
                if place == 31 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c1.config(image=b_sol_w)
                        row_3[1] = u
                    if u == "w_sol":
                        r3c1.config(image=w_sol_w)
                        row_3[1] = u
                    if u == "b_ele":
                        r3c1.config(image=b_ele_w)
                        row_3[1] = u
                    if u == "w_ele":
                        r3c1.config(image=w_ele_w)
                        row_3[1] = u
                    if u == "b_hor":
                        r3c1.config(image=b_hor_w)
                        row_3[1] = u
                    if u == "w_hor":
                        r3c1.config(image=w_hor_w)
                        row_3[1] = u
                    if u == "b_cam":
                        r3c1.config(image=b_cam_w)
                        row_3[1] = u
                    if u == "w_cam":
                        r3c1.config(image=w_cam_w)
                        row_3[1] = u
                    if u == "b_king":
                        r3c1.config(image=b_king_w)
                        row_3[1] = u
                    if u == "w_king":
                        r3c1.config(image=w_king_w)
                        row_3[1] = u
                    if u == "b_que":
                        r3c1.config(image=b_que_w)
                        row_3[1] = u
                    if u == "w_que":
                        r3c1.config(image=w_que_w)
                        row_3[1] = u
        ######################################################################################
                if place == 33 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c3.config(image=b_sol_w)
                        row_3[3] = u
                    if u == "w_sol":
                        r3c3.config(image=w_sol_w)
                        row_3[3] = u
                    if u == "b_ele":
                        r3c3.config(image=b_ele_w)
                        row_3[3] = u
                    if u == "w_ele":
                        r3c3.config(image=w_ele_w)
                        row_3[3] = u
                    if u == "b_hor":
                        r3c3.config(image=b_hor_w)
                        row_3[3] = u
                    if u == "w_hor":
                        r3c3.config(image=w_hor_w)
                        row_3[3] = u
                    if u == "b_cam":
                        r3c3.config(image=b_cam_w)
                        row_3[3] = u
                    if u == "w_cam":
                        r3c3.config(image=w_cam_w)
                        row_3[3] = u
                    if u == "b_king":
                        r3c3.config(image=b_king_w)
                        row_3[3] = u
                    if u == "w_king":
                        r3c3.config(image=w_king_w)
                        row_3[3] = u
                    if u == "b_que":
                        r3c3.config(image=b_que_w)
                        row_3[3] = u
                    if u == "w_que":
                        r3c3.config(image=w_que_w)
                        row_3[3] = u
        ######################################################################################
                if place == 35 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c5.config(image=b_sol_w)
                        row_3[5] = u
                    if u == "w_sol":
                        r3c5.config(image=w_sol_w)
                        row_3[5] = u
                    if u == "b_ele":
                        r3c5.config(image=b_ele_w)
                        row_3[5] = u
                    if u == "w_ele":
                        r3c5.config(image=w_ele_w)
                        row_3[5] = u
                    if u == "b_hor":
                        r3c5.config(image=b_hor_w)
                        row_3[5] = u
                    if u == "w_hor":
                        r3c5.config(image=w_hor_w)
                        row_3[5] = u
                    if u == "b_cam":
                        r3c5.config(image=b_cam_w)
                        row_3[5] = u
                    if u == "w_cam":
                        r3c5.config(image=w_cam_w)
                        row_3[5] = u
                    if u == "b_king":
                        r3c5.config(image=b_king_w)
                        row_3[5] = u
                    if u == "w_king":
                        r3c5.config(image=w_king_w)
                        row_3[5] = u
                    if u == "b_que":
                        r3c5.config(image=b_que_w)
                        row_3[5] = u
                    if u == "w_que":
                        r3c5.config(image=w_que_w)
                        row_3[5] = u
        ######################################################################################
                if place == 37 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c7.config(image=b_sol_w)
                        row_3[7] = u
                    if u == "w_sol":
                        r3c7.config(image=w_sol_w)
                        row_3[7] = u
                    if u == "b_ele":
                        r3c7.config(image=b_ele_w)
                        row_3[7] = u
                    if u == "w_ele":
                        r3c7.config(image=w_ele_w)
                        row_3[7] = u
                    if u == "b_hor":
                        r3c7.config(image=b_hor_w)
                        row_3[7] = u
                    if u == "w_hor":
                        r3c7.config(image=w_hor_w)
                        row_3[7] = u
                    if u == "b_cam":
                        r3c7.config(image=b_cam_w)
                        row_3[7] = u
                    if u == "w_cam":
                        r3c7.config(image=w_cam_w)
                        row_3[7] = u
                    if u == "b_king":
                        r3c7.config(image=b_king_w)
                        row_3[7] = u
                    if u == "w_king":
                        r3c7.config(image=w_king_w)
                        row_3[7] = u
                    if u == "b_que":
                        r3c7.config(image=b_que_w)
                        row_3[7] = u
                    if u == "w_que":
                        r3c7.config(image=w_que_w)
                        row_3[7] = u
        ######################################################################################
                if place == 41 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c1.config(image=b_sol_b)
                        row_4[1] = u
                    if u == "w_sol":
                        r4c1.config(image=w_sol_b)
                        row_4[1] = u
                    if u == "b_ele":
                        r4c1.config(image=b_ele_b)
                        row_4[1] = u
                    if u == "w_ele":
                        r4c1.config(image=w_ele_b)
                        row_4[1] = u
                    if u == "b_hor":
                        r4c1.config(image=b_hor_b)
                        row_4[1] = u
                    if u == "w_hor":
                        r4c1.config(image=w_hor_b)
                        row_4[1] = u
                    if u == "b_cam":
                        r4c1.config(image=b_cam_b)
                        row_4[1] = u
                    if u == "w_cam":
                        r4c1.config(image=w_cam_b)
                        row_4[1] = u
                    if u == "b_king":
                        r4c1.config(image=b_king_b)
                        row_4[1] = u
                    if u == "w_king":
                        r4c1.config(image=w_king_b)
                        row_4[1] = u
                    if u == "b_que":
                        r4c1.config(image=b_que_b)
                        row_4[1] = u
                    if u == "w_que":
                        r4c1.config(image=w_que_b)
                        row_4[1] = u
        ######################################################################################
                if place == 43 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c3.config(image=b_sol_b)
                        row_4[3] = u
                    if u == "w_sol":
                        r4c3.config(image=w_sol_b)
                        row_4[3] = u
                    if u == "b_ele":
                        r4c3.config(image=b_ele_b)
                        row_4[3] = u
                    if u == "w_ele":
                        r4c3.config(image=w_ele_b)
                        row_4[3] = u
                    if u == "b_hor":
                        r4c3.config(image=b_hor_b)
                        row_4[3] = u
                    if u == "w_hor":
                        r4c3.config(image=w_hor_b)
                        row_4[3] = u
                    if u == "b_cam":
                        r4c3.config(image=b_cam_b)
                        row_4[3] = u
                    if u == "w_cam":
                        r4c3.config(image=w_cam_b)
                        row_4[3] = u
                    if u == "b_king":
                        r4c3.config(image=b_king_b)
                        row_4[3] = u
                    if u == "w_king":
                        r4c3.config(image=w_king_b)
                        row_4[3] = u
                    if u == "b_que":
                        r4c3.config(image=b_que_b)
                        row_4[3] = u
                    if u == "w_que":
                        r4c3.config(image=w_que_b)
                        row_4[3] = u
        ######################################################################################
                if place == 45 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c5.config(image=b_sol_b)
                        row_4[5] = u
                    if u == "w_sol":
                        r4c5.config(image=w_sol_b)
                        row_4[5] = u
                    if u == "b_ele":
                        r4c5.config(image=b_ele_b)
                        row_4[5] = u
                    if u == "w_ele":
                        r4c5.config(image=w_ele_b)
                        row_4[5] = u
                    if u == "b_hor":
                        r4c5.config(image=b_hor_b)
                        row_4[5] = u
                    if u == "w_hor":
                        r4c5.config(image=w_hor_b)
                        row_4[5] = u
                    if u == "b_cam":
                        r4c5.config(image=b_cam_b)
                        row_4[5] = u
                    if u == "w_cam":
                        r4c5.config(image=w_cam_b)
                        row_4[5] = u
                    if u == "b_king":
                        r4c5.config(image=b_king_b)
                        row_4[5] = u
                    if u == "w_king":
                        r4c5.config(image=w_king_b)
                        row_4[5] = u
                    if u == "b_que":
                        r4c5.config(image=b_que_b)
                        row_4[5] = u
                    if u == "w_que":
                        r4c5.config(image=w_que_b)
                        row_4[5] = u
        ######################################################################################
                if place == 47 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c7.config(image=b_sol_b)
                        row_4[7] = u
                    if u == "w_sol":
                        r4c7.config(image=w_sol_b)
                        row_4[7] = u
                    if u == "b_ele":
                        r4c7.config(image=b_ele_b)
                        row_4[7] = u
                    if u == "w_ele":
                        r4c7.config(image=w_ele_b)
                        row_4[7] = u
                    if u == "b_hor":
                        r4c7.config(image=b_hor_b)
                        row_4[7] = u
                    if u == "w_hor":
                        r4c7.config(image=w_hor_b)
                        row_4[7] = u
                    if u == "b_cam":
                        r4c7.config(image=b_cam_b)
                        row_4[7] = u
                    if u == "w_cam":
                        r4c7.config(image=w_cam_b)
                        row_4[7] = u
                    if u == "b_king":
                        r4c7.config(image=b_king_b)
                        row_4[7] = u
                    if u == "w_king":
                        r4c7.config(image=w_king_b)
                        row_4[7] = u
                    if u == "b_que":
                        r4c7.config(image=b_que_b)
                        row_4[7] = u
                    if u == "w_que":
                        r4c7.config(image=w_que_b)
                        row_4[7] = u
        ######################################################################################
                if place == 51 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c1.config(image=b_sol_w)
                        row_5[1] = u
                    if u == "w_sol":
                        r5c1.config(image=w_sol_w)
                        row_5[1] = u
                    if u == "b_ele":
                        r5c1.config(image=b_ele_w)
                        row_5[1] = u
                    if u == "w_ele":
                        r5c1.config(image=w_ele_w)
                        row_5[1] = u
                    if u == "b_hor":
                        r5c1.config(image=b_hor_w)
                        row_5[1] = u
                    if u == "w_hor":
                        r5c1.config(image=w_hor_w)
                        row_5[1] = u
                    if u == "b_cam":
                        r5c1.config(image=b_cam_w)
                        row_5[1] = u
                    if u == "w_cam":
                        r5c1.config(image=w_cam_w)
                        row_5[1] = u
                    if u == "b_king":
                        r5c1.config(image=b_king_w)
                        row_5[1] = u
                    if u == "w_king":
                        r5c1.config(image=w_king_w)
                        row_5[1] = u
                    if u == "b_que":
                        r5c1.config(image=b_que_w)
                        row_5[1] = u
                    if u == "w_que":
                        r5c1.config(image=w_que_w)
                        row_5[1] = u
        ######################################################################################
                if place == 53 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c3.config(image=b_sol_w)
                        row_5[3] = u
                    if u == "w_sol":
                        r5c3.config(image=w_sol_w)
                        row_5[3] = u
                    if u == "b_ele":
                        r5c3.config(image=b_ele_w)
                        row_5[3] = u
                    if u == "w_ele":
                        r5c3.config(image=w_ele_w)
                        row_5[3] = u
                    if u == "b_hor":
                        r5c3.config(image=b_hor_w)
                        row_5[3] = u
                    if u == "w_hor":
                        r5c3.config(image=w_hor_w)
                        row_5[3] = u
                    if u == "b_cam":
                        r5c3.config(image=b_cam_w)
                        row_5[3] = u
                    if u == "w_cam":
                        r5c3.config(image=w_cam_w)
                        row_5[3] = u
                    if u == "b_king":
                        r5c3.config(image=b_king_w)
                        row_5[3] = u
                    if u == "w_king":
                        r5c3.config(image=w_king_w)
                        row_5[3] = u
                    if u == "b_que":
                        r5c3.config(image=b_que_w)
                        row_5[3] = u
                    if u == "w_que":
                        r5c3.config(image=w_que_w)
                        row_5[3] = u
        ######################################################################################
                if place == 55 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c5.config(image=b_sol_w)
                        row_5[5] = u
                    if u == "w_sol":
                        r5c5.config(image=w_sol_w)
                        row_5[5] = u
                    if u == "b_ele":
                        r5c5.config(image=b_ele_w)
                        row_5[5] = u
                    if u == "w_ele":
                        r5c5.config(image=w_ele_w)
                        row_5[5] = u
                    if u == "b_hor":
                        r5c5.config(image=b_hor_w)
                        row_5[5] = u
                    if u == "w_hor":
                        r5c5.config(image=w_hor_w)
                        row_5[5] = u
                    if u == "b_cam":
                        r5c5.config(image=b_cam_w)
                        row_5[5] = u
                    if u == "w_cam":
                        r5c5.config(image=w_cam_w)
                        row_5[5] = u
                    if u == "b_king":
                        r5c5.config(image=b_king_w)
                        row_5[5] = u
                    if u == "w_king":
                        r5c5.config(image=w_king_w)
                        row_5[5] = u
                    if u == "b_que":
                        r5c5.config(image=b_que_w)
                        row_5[5] = u
                    if u == "w_que":
                        r5c5.config(image=w_que_w)
                        row_5[5] = u
        ######################################################################################
                if place == 57 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c7.config(image=b_sol_w)
                        row_5[7] = u
                    if u == "w_sol":
                        r5c7.config(image=w_sol_w)
                        row_5[7] = u
                    if u == "b_ele":
                        r5c7.config(image=b_ele_w)
                        row_5[7] = u
                    if u == "w_ele":
                        r5c7.config(image=w_ele_w)
                        row_5[7] = u
                    if u == "b_hor":
                        r5c7.config(image=b_hor_w)
                        row_5[7] = u
                    if u == "w_hor":
                        r5c7.config(image=w_hor_w)
                        row_5[7] = u
                    if u == "b_cam":
                        r5c7.config(image=b_cam_w)
                        row_5[7] = u
                    if u == "w_cam":
                        r5c7.config(image=w_cam_w)
                        row_5[7] = u
                    if u == "b_king":
                        r5c7.config(image=b_king_w)
                        row_5[7] = u
                    if u == "w_king":
                        r5c7.config(image=w_king_w)
                        row_5[7] = u
                    if u == "b_que":
                        r5c7.config(image=b_que_w)
                        row_5[7] = u
                    if u == "w_que":
                        r5c7.config(image=w_que_w)
                        row_5[7] = u
        ################################
                        #######################
                if place == 61 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c1.config(image=b_sol_b)
                        row_6[1] = u
                    if u == "w_sol":
                        r6c1.config(image=w_sol_b)
                        row_6[1] = u
                    if u == "b_ele":
                        r6c1.config(image=b_ele_b)
                        row_6[1] = u
                    if u == "w_ele":
                        r6c1.config(image=w_ele_b)
                        row_6[1] = u
                    if u == "b_hor":
                        r6c1.config(image=b_hor_b)
                        row_6[1] = u
                    if u == "w_hor":
                        r6c1.config(image=w_hor_b)
                        row_6[1] = u
                    if u == "b_cam":
                        r6c1.config(image=b_cam_b)
                        row_6[1] = u
                    if u == "w_cam":
                        r6c1.config(image=w_cam_b)
                        row_6[1] = u
                    if u == "b_king":
                        r6c1.config(image=b_king_b)
                        row_6[1] = u
                    if u == "w_king":
                        r6c1.config(image=w_king_b)
                        row_6[1] = u
                    if u == "b_que":
                        r6c1.config(image=b_que_b) 
                        row_6[1] = u
                    if u == "w_que":
                        r6c1.config(image=w_que_b)
                        row_6[1] = u
        ######################################################################################
                if place == 63 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c3.config(image=b_sol_b)
                        row_6[3] = u
                    if u == "w_sol":
                        r6c3.config(image=w_sol_b)
                        row_6[3] = u
                    if u == "b_ele":
                        r6c3.config(image=b_ele_b)
                        row_6[3] = u
                    if u == "w_ele":
                        r6c3.config(image=w_ele_b)
                        row_6[3] = u
                    if u == "b_hor":
                        r6c3.config(image=b_hor_b)
                        row_6[3] = u
                    if u == "w_hor":
                        r6c3.config(image=w_hor_b)
                        row_6[3] = u
                    if u == "b_cam":
                        r6c3.config(image=b_cam_b)
                        row_6[3] = u
                    if u == "w_cam":
                        r6c3.config(image=w_cam_b)
                        row_6[3] = u
                    if u == "b_king":
                        r6c3.config(image=b_king_b)
                        row_6[3] = u
                    if u == "w_king":
                        r6c3.config(image=w_king_b)
                        row_6[3] = u
                    if u == "b_que":
                        r6c3.config(image=b_que_b)
                        row_6[3] = u
                    if u == "w_que":
                        r6c3.config(image=w_que_b)
                        row_6[3] = u
        ######################################################################################
                if place == 65 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c5.config(image=b_sol_b)
                        row_6[5] = u
                    if u == "w_sol":
                        r6c5.config(image=w_sol_b)
                        row_6[5] = u
                    if u == "b_ele":
                        r6c5.config(image=b_ele_b)
                        row_6[5] = u
                    if u == "w_ele":
                        r6c5.config(image=w_ele_b)
                        row_6[5] = u
                    if u == "b_hor":
                        r6c5.config(image=b_hor_b)
                        row_6[5] = u
                    if u == "w_hor":
                        r6c5.config(image=w_hor_b)
                        row_6[5] = u
                    if u == "b_cam":
                        r6c5.config(image=b_cam_b)
                        row_6[5] = u
                    if u == "w_cam":
                        r6c5.config(image=w_cam_b)
                        row_6[5] = u
                    if u == "b_king":
                        r6c5.config(image=b_king_b)
                        row_6[5] = u
                    if u == "w_king":
                        r6c5.config(image=w_king_b)
                        row_6[5] = u
                    if u == "b_que":
                        r6c5.config(image=b_que_b)
                        row_6[5] = u
                    if u == "w_que":
                        r6c5.config(image=w_que_b)
                        row_6[5] = u
        ######################################################################################
                if place == 67 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c7.config(image=b_sol_b)
                        row_6[7] = u
                    if u == "w_sol":
                        r6c7.config(image=w_sol_b)
                        row_6[7] = u
                    if u == "b_ele":
                        r6c7.config(image=b_ele_b)
                        row_6[7] = u
                    if u == "w_ele":
                        r6c7.config(image=w_ele_b)
                        row_6[7] = u
                    if u == "b_hor":
                        r6c7.config(image=b_hor_b)
                        row_6[7] = u
                    if u == "w_hor":
                        r6c7.config(image=w_hor_b)
                        row_6[7] = u
                    if u == "b_cam":
                        r6c7.config(image=b_cam_b)
                        row_6[7] = u
                    if u == "w_cam":
                        r6c7.config(image=w_cam_b)
                        row_6[7] = u
                    if u == "b_king":
                        r6c7.config(image=b_king_b)
                        row_6[7] = u
                    if u == "w_king":
                        r6c7.config(image=w_king_b)
                        row_6[7] = u
                    if u == "b_que":
                        r6c7.config(image=b_que_b)
                        row_6[7] = u
                    if u == "w_que":
                        r6c7.config(image=w_que_b)
                        row_6[7] = u
        ######################################################################################
                if place == 71 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c1.config(image=b_sol_w)
                        row_7[1] = u
                    if u == "w_sol":
                        r7c1.config(image=w_sol_w)
                        row_7[1] = u
                    if u == "b_ele":
                        r7c1.config(image=b_ele_w)
                        row_7[1] = u
                    if u == "w_ele":
                        r7c1.config(image=w_ele_w)
                        row_7[1] = u
                    if u == "b_hor":
                        r7c1.config(image=b_hor_w)
                        row_7[1] = u
                    if u == "w_hor":
                        r7c1.config(image=w_hor_w)
                        row_7[1] = u
                    if u == "b_cam":
                        r7c1.config(image=b_cam_w)
                        row_7[1] = u
                    if u == "w_cam":
                        r7c1.config(image=w_cam_w)
                        row_7[1] = u
                    if u == "b_king":
                        r7c1.config(image=b_king_w)
                        row_7[1] = u
                    if u == "w_king":
                        r7c1.config(image=w_king_w)
                        row_7[1] = u
                    if u == "b_que":
                        r7c1.config(image=b_que_w)
                        row_7[1] = u
                    if u == "w_que":
                        r7c1.config(image=w_que_w)
                        row_7[1] = u
        ######################################################################################
                if place == 73 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c3.config(image=b_sol_w)
                        row_7[3] = u
                    if u == "w_sol":
                        r7c3.config(image=w_sol_w)
                        row_7[3] = u
                    if u == "b_ele":
                        r7c3.config(image=b_ele_w)
                        row_7[3] = u
                    if u == "w_ele":
                        r7c3.config(image=w_ele_w)
                        row_7[3] = u
                    if u == "b_hor":
                        r7c3.config(image=b_hor_w)
                        row_7[3] = u
                    if u == "w_hor":
                        r7c3.config(image=w_hor_w)
                        row_7[3] = u
                    if u == "b_cam":
                        r7c3.config(image=b_cam_w)
                        row_7[3] = u
                    if u == "w_cam":
                        r7c3.config(image=w_cam_w)
                        row_7[3] = u
                    if u == "b_king":
                        r7c3.config(image=b_king_w)
                        row_7[3] = u
                    if u == "w_king":
                        r7c3.config(image=w_king_w)
                        row_7[3] = u
                    if u == "b_que":
                        r7c3.config(image=b_que_w)
                        row_7[3] = u
                    if u == "w_que":
                        r7c3.config(image=w_que_w)
                        row_7[3] = u
        ######################################################################################
                if place == 75 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c5.config(image=b_sol_w)
                        row_7[5] = u
                    if u == "w_sol":
                        r7c5.config(image=w_sol_w)
                        row_7[5] = u
                    if u == "b_ele":
                        r7c5.config(image=b_ele_w)
                        row_7[5] = u
                    if u == "w_ele":
                        r7c5.config(image=w_ele_w)
                        row_7[5] = u
                    if u == "b_hor":
                        r7c5.config(image=b_hor_w)
                        row_7[5] = u
                    if u == "w_hor":
                        r7c5.config(image=w_hor_w)
                        row_7[5] = u
                    if u == "b_cam":
                        r7c5.config(image=b_cam_w)
                        row_7[5] = u
                    if u == "w_cam":
                        r7c5.config(image=w_cam_w)
                        row_7[5] = u
                    if u == "b_king":
                        r7c5.config(image=b_king_w)
                        row_7[5] = u
                    if u == "w_king":
                        r7c5.config(image=w_king_w)
                        row_7[5] = u
                    if u == "b_que":
                        r7c5.config(image=b_que_w)
                        row_7[5] = u
                    if u == "w_que":
                        r7c5.config(image=w_que_w)
                        row_7[5] = u
        ######################################################################################
                if place == 77 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c7.config(image=b_sol_w)
                        row_7[7] = u
                    if u == "w_sol":
                        r7c7.config(image=w_sol_w)
                        row_7[7] = u
                    if u == "b_ele":
                        r7c7.config(image=b_ele_w)
                        row_7[7] = u
                    if u == "w_ele":
                        r7c7.config(image=w_ele_w)
                        row_7[7] = u
                    if u == "b_hor":
                        r7c7.config(image=b_hor_w)
                        row_7[7] = u
                    if u == "w_hor":
                        r7c7.config(image=w_hor_w)
                        row_7[7] = u
                    if u == "b_cam":
                        r7c7.config(image=b_cam_w)
                        row_7[7] = u
                    if u == "w_cam":
                        r7c7.config(image=w_cam_w)
                        row_7[7] = u
                    if u == "b_king":
                        r7c7.config(image=b_king_w)
                        row_7[7] = u
                    if u == "w_king":
                        r7c7.config(image=w_king_w)
                        row_7[7] = u
                    if u == "b_que":
                        r7c7.config(image=b_que_w)
                        row_7[7] = u
                    if u == "w_que":
                        r7c7.config(image=w_que_w)
                        row_7[7] = u
        ######################################################################################
                if place == 81 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c1.config(image=b_sol_b)
                        row_8[1] = u
                    if u == "w_sol":
                        r8c1.config(image=w_sol_b)
                        row_8[1] = u
                    if u == "b_ele":
                        r8c1.config(image=b_ele_b)
                        row_8[1] = u
                    if u == "w_ele":
                        r8c1.config(image=w_ele_b)
                        row_8[1] = u
                    if u == "b_hor":
                        r8c1.config(image=b_hor_b)
                        row_8[1] = u
                    if u == "w_hor":
                        r8c1.config(image=w_hor_b)
                        row_8[1] = u
                    if u == "b_cam":
                        r8c1.config(image=b_cam_b)
                        row_8[1] = u
                    if u == "w_cam":
                        r8c1.config(image=w_cam_b)
                        row_8[1] = u
                    if u == "b_king":
                        r8c1.config(image=b_king_b)
                        row_8[1] = u
                    if u == "w_king":
                        r8c1.config(image=w_king_b)
                        row_8[1] = u
                    if u == "b_que":
                        r8c1.config(image=b_que_b)
                        row_8[1] = u
                    if u == "w_que":
                        r8c1.config(image=w_que_b)
                        row_8[1] = u
        ######################################################################################
                if place == 83 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c3.config(image=b_sol_b)
                        row_8[3] = u
                    if u == "w_sol":
                        r8c3.config(image=w_sol_b)
                        row_8[3] = u
                    if u == "b_ele":
                        r8c3.config(image=b_ele_b)
                        row_8[3] = u
                    if u == "w_ele":
                        r8c3.config(image=w_ele_b)
                        row_8[3] = u
                    if u == "b_hor":
                        r8c3.config(image=b_hor_b)
                        row_8[3] = u
                    if u == "w_hor":
                        r8c3.config(image=w_hor_b)
                        row_8[3] = u
                    if u == "b_cam":
                        r8c3.config(image=b_cam_b)
                        row_8[3] = u
                    if u == "w_cam":
                        r8c3.config(image=w_cam_b)
                        row_8[3] = u
                    if u == "b_king":
                        r8c3.config(image=b_king_b)
                        row_8[3] = u
                    if u == "w_king":
                        r8c3.config(image=w_king_b)
                        row_8[3] = u
                    if u == "b_que":
                        r8c3.config(image=b_que_b)
                        row_8[3] = u
                    if u == "w_que":
                        r8c3.config(image=w_que_b)
                        row_8[3] = u
        ######################################################################################
                if place == 85 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c5.config(image=b_sol_b)
                        row_8[5] = u
                    if u == "w_sol":
                        r8c5.config(image=w_sol_b)
                        row_8[5] = u
                    if u == "b_ele":
                        r8c5.config(image=b_ele_b)
                        row_8[5] = u
                    if u == "w_ele":
                        r8c5.config(image=w_ele_b)
                        row_8[5] = u
                    if u == "b_hor":
                        r8c5.config(image=b_hor_b)
                        row_8[5] = u
                    if u == "w_hor":
                        r8c5.config(image=w_hor_b)
                        row_8[5] = u
                    if u == "b_cam":
                        r8c5.config(image=b_cam_b)
                        row_8[5] = u
                    if u == "w_cam":
                        r8c5.config(image=w_cam_b)
                        row_8[5] = u
                    if u == "b_king":
                        r8c5.config(image=b_king_b)
                        row_8[5] = u
                    if u == "w_king":
                        r8c5.config(image=w_king_b)
                        row_8[5] = u
                    if u == "b_que":
                        r8c5.config(image=b_que_b)
                        row_8[5] = u
                    if u == "w_que":
                        r8c5.config(image=w_que_b)
                        row_8[5] = u
        ######################################################################################
                if place == 87 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c7.config(image=b_sol_b)
                        row_8[7] = u
                    if u == "w_sol":
                        r8c7.config(image=w_sol_b)
                        row_8[7] = u
                    if u == "b_ele":
                        r8c7.config(image=b_ele_b)
                        row_8[7] = u
                    if u == "w_ele":
                        r8c7.config(image=w_ele_b)
                        row_8[7] = u
                    if u == "b_hor":
                        r8c7.config(image=b_hor_b)
                        row_8[7] = u
                    if u == "w_hor":
                        r8c7.config(image=w_hor_b)
                        row_8[7] = u
                    if u == "b_cam":
                        r8c7.config(image=b_cam_b)
                        row_8[7] = u
                    if u == "w_cam":
                        r8c7.config(image=w_cam_b)
                        row_8[7] = u
                    if u == "b_king":
                        r8c7.config(image=b_king_b)
                        row_8[7] = u
                    if u == "w_king":
                        r8c7.config(image=w_king_b)
                        row_8[7] = u
                    if u == "b_que":
                        r8c7.config(image=b_que_b)
                        row_8[7] = u
                    if u == "w_que":
                        r8c7.config(image=w_que_b)
                        row_8[7] = u
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        
                if place == 12 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c2.config(image=b_sol_b)
                        row_1[2] = u
                    if u == "w_sol":
                        r1c2.config(image=w_sol_b)
                        row_1[2] = u
                    if u == "b_ele":
                        r1c2.config(image=b_ele_b)
                        row_1[2] = u
                    if u == "w_ele":
                        r1c2.config(image=w_ele_b)
                        row_1[2] = u
                    if u == "b_hor":
                        r1c2.config(image=b_hor_b)
                        row_1[2] = u
                    if u == "w_hor":
                        r1c2.config(image=w_hor_b)
                        row_1[2] = u
                    if u == "b_cam":
                        r1c2.config(image=b_cam_b)
                        row_1[2] = u
                    if u == "w_cam":
                        r1c2.config(image=w_cam_b)
                        row_1[2] = u
                    if u == "b_king":
                        r1c2.config(image=b_king_b)
                        row_1[2] = u
                    if u == "w_king":
                        r1c2.config(image=w_king_b)
                        row_1[2] = u
                    if u == "b_que":
                        r1c2.config(image=b_que_b)
                        row_1[2] = u
                    if u == "w_que":
                        r1c2.config(image=w_que_b)
                        row_1[2] = u


                if place == 14 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c4.config(image=b_sol_b)
                        row_1[4] = u
                    if u == "w_sol":
                        r1c4.config(image=w_sol_b)
                        row_1[4] = u
                    if u == "b_ele":
                        r1c4.config(image=b_ele_b)
                        row_1[4] = u
                    if u == "w_ele":
                        r1c4.config(image=w_ele_b)
                        row_1[4] = u
                    if u == "b_hor":
                        r1c4.config(image=b_hor_b)
                        row_1[4] = u
                    if u == "w_hor":
                        r1c4.config(image=w_hor_b)
                        row_1[4] = u
                    if u == "b_cam":
                        r1c4.config(image=b_cam_b)
                        row_1[4] = u
                    if u == "w_cam":
                        r1c4.config(image=w_cam_b)
                        row_1[4] = u
                    if u == "b_king":
                        r1c4.config(image=b_king_b)
                        row_1[4] = u
                    if u == "w_king":
                        r1c4.config(image=w_king_b)
                        row_1[4] = u
                    if u == "b_que":
                        r1c4.config(image=b_que_b)
                        row_1[4] = u
                    if u == "w_que":
                        r1c4.config(image=w_que_b)
                        row_1[4] = u

                if place == 16 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c6.config(image=b_sol_b)
                        row_1[6] = u
                    if u == "w_sol":
                        r1c6.config(image=w_sol_b)
                        row_1[6] = u
                    if u == "b_ele":
                        r1c6.config(image=b_ele_b)
                        row_1[6] = u
                    if u == "w_ele":
                        r1c6.config(image=w_ele_b)
                        row_1[6] = u
                    if u == "b_hor":
                        r1c6.config(image=b_hor_b)
                        row_1[6] = u
                    if u == "w_hor":
                        r1c6.config(image=w_hor_b)
                        row_1[6] = u
                    if u == "b_cam":
                        r1c6.config(image=b_cam_b)
                        row_1[6] = u
                    if u == "w_cam":
                        r1c6.config(image=w_cam_b)
                        row_1[6] = u
                    if u == "b_king":
                        r1c6.config(image=b_king_b)
                        row_1[6] = u
                    if u == "w_king":
                        r1c6.config(image=w_king_b)
                        row_1[6] = u
                    if u == "b_que":
                        r1c6.config(image=b_que_b)
                        row_1[6] = u
                    if u == "w_que":
                        r1c6.config(image=w_que_b)
                        row_1[6] = u


                if place == 18 :
                    u = unit[1]
                    if u == "b_sol":
                        r1c8.config(image=b_sol_b)
                        row_1[8] = u
                    if u == "w_sol":
                        r1c8.config(image=w_sol_b)
                        row_1[8] = u
                    if u == "b_ele":
                        r1c8.config(image=b_ele_b)
                        row_1[8] = u
                    if u == "w_ele":
                        r1c8.config(image=w_ele_b)
                        row_1[8] = u
                    if u == "b_hor":
                        r1c8.config(image=b_hor_b)
                        row_1[8] = u
                    if u == "w_hor":
                        r1c8.config(image=w_hor_b)
                        row_1[8] = u
                    if u == "b_cam":
                        r1c8.config(image=b_cam_b)
                        row_1[8] = u
                    if u == "w_cam":
                        r1c8.config(image=w_cam_b)
                        row_1[8] = u
                    if u == "b_king":
                        r1c8.config(image=b_king_b)
                        row_1[8] = u
                    if u == "w_king":
                        r1c8.config(image=w_king_b)
                        row_1[8] = u
                    if u == "b_que":
                        r1c8.config(image=b_que_b)
                        row_1[8] = u
                    if u == "w_que":
                        r1c8.config(image=w_que_b)
                        row_1[8] = u

                if place == 32 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c2.config(image=b_sol_b)
                        row_3[2] = u
                    if u == "w_sol":
                        r3c2.config(image=w_sol_b)
                        row_3[2] = u
                    if u == "b_ele":
                        r3c2.config(image=b_ele_b)
                        row_3[2] = u
                    if u == "w_ele":
                        r3c2.config(image=w_ele_b)
                        row_3[2] = u
                    if u == "b_hor":
                        r3c2.config(image=b_hor_b)
                        row_3[2] = u
                    if u == "w_hor":
                        r3c2.config(image=w_hor_b)
                        row_3[2] = u
                    if u == "b_cam":
                        r3c2.config(image=b_cam_b)
                        row_3[2] = u
                    if u == "w_cam":
                        r3c2.config(image=w_cam_b)
                        row_3[2] = u
                    if u == "b_king":
                        r3c2.config(image=b_king_b)
                        row_3[2] = u
                    if u == "w_king":
                        r3c2.config(image=w_king_b)
                        row_3[2] = u
                    if u == "b_que":
                        r3c2.config(image=b_que_b)
                        row_3[2] = u
                    if u == "w_que":
                        r3c2.config(image=w_que_b)
                        row_3[2] = u


                if place == 34 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c4.config(image=b_sol_b)
                        row_3[4] = u
                    if u == "w_sol":
                        r3c4.config(image=w_sol_b)
                        row_3[4] = u
                    if u == "b_ele":
                        r3c4.config(image=b_ele_b)
                        row_3[4] = u
                    if u == "w_ele":
                        r3c4.config(image=w_ele_b)
                        row_3[4] = u
                    if u == "b_hor":
                        r3c4.config(image=b_hor_b)
                        row_3[4] = u
                    if u == "w_hor":
                        r3c4.config(image=w_hor_b)
                        row_3[4] = u
                    if u == "b_cam":
                        r3c4.config(image=b_cam_b)
                        row_3[4] = u
                    if u == "w_cam":
                        r3c4.config(image=w_cam_b)
                        row_3[4] = u
                    if u == "b_king":
                        r3c4.config(image=b_king_b)
                        row_3[4] = u
                    if u == "w_king":
                        r3c4.config(image=w_king_b)
                        row_3[4] = u
                    if u == "b_que":
                        r3c4.config(image=b_que_b)
                        row_3[4] = u
                    if u == "w_que":
                        r3c4.config(image=w_que_b)
                        row_3[4] = u

                if place == 36 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c6.config(image=b_sol_b)
                        row_3[6] = u
                    if u == "w_sol":
                        r3c6.config(image=w_sol_b)
                        row_3[6] = u
                    if u == "b_ele":
                        r3c6.config(image=b_ele_b)
                        row_3[6] = u
                    if u == "w_ele":
                        r3c6.config(image=w_ele_b)
                        row_3[6] = u
                    if u == "b_hor":
                        r3c6.config(image=b_hor_b)
                        row_3[6] = u
                    if u == "w_hor":
                        r3c6.config(image=w_hor_b)
                        row_3[6] = u
                    if u == "b_cam":
                        r3c6.config(image=b_cam_b)
                        row_3[6] = u
                    if u == "w_cam":
                        r3c6.config(image=w_cam_b)
                        row_3[6] = u
                    if u == "b_king":
                        r3c6.config(image=b_king_b)
                        row_3[6] = u
                    if u == "w_king":
                        r3c6.config(image=w_king_b)
                        row_3[6] = u
                    if u == "b_que":
                        r3c6.config(image=b_que_b)
                        row_3[6] = u
                    if u == "w_que":
                        r3c6.config(image=w_que_b)
                        row_3[6] = u


                if place == 38 :
                    u = unit[1]
                    if u == "b_sol":
                        r3c8.config(image=b_sol_b)
                        row_3[8] = u
                    if u == "w_sol":
                        r3c8.config(image=w_sol_b)
                        row_3[8] = u
                    if u == "b_ele":
                        r3c8.config(image=b_ele_b)
                        row_3[8] = u
                    if u == "w_ele":
                        r3c8.config(image=w_ele_b)
                        row_3[8] = u
                    if u == "b_hor":
                        r3c8.config(image=b_hor_b)
                        row_3[8] = u
                    if u == "w_hor":
                        r3c8.config(image=w_hor_b)
                        row_3[8] = u
                    if u == "b_cam":
                        r3c8.config(image=b_cam_b)
                        row_3[8] = u
                    if u == "w_cam":
                        r3c8.config(image=w_cam_b)
                        row_3[8] = u
                    if u == "b_king":
                        r3c8.config(image=b_king_b)
                        row_3[8] = u
                    if u == "w_king":
                        r3c8.config(image=w_king_b)
                        row_3[8] = u
                    if u == "b_que":
                        r3c8.config(image=b_que_b)
                        row_3[8] = u
                    if u == "w_que":
                        r3c8.config(image=w_que_b)
                        row_3[8] = u        

                if place == 52 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c2.config(image=b_sol_b)
                        row_5[2] = u
                    if u == "w_sol":
                        r5c2.config(image=w_sol_b)
                        row_5[2] = u
                    if u == "b_ele":
                        r5c2.config(image=b_ele_b)
                        row_5[2] = u
                    if u == "w_ele":
                        r5c2.config(image=w_ele_b)
                        row_5[2] = u
                    if u == "b_hor":
                        r5c2.config(image=b_hor_b)
                        row_5[2] = u
                    if u == "w_hor":
                        r5c2.config(image=w_hor_b)
                        row_5[2] = u
                    if u == "b_cam":
                        r5c2.config(image=b_cam_b)
                        row_5[2] = u
                    if u == "w_cam":
                        r5c2.config(image=w_cam_b)
                        row_5[2] = u
                    if u == "b_king":
                        r5c2.config(image=b_king_b)
                        row_5[2] = u
                    if u == "w_king":
                        r5c2.config(image=w_king_b)
                        row_5[2] = u
                    if u == "b_que":
                        r5c2.config(image=b_que_b)
                        row_5[2] = u
                    if u == "w_que":
                        r5c2.config(image=w_que_b)
                        row_5[2] = u


                if place == 54 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c4.config(image=b_sol_b)
                        row_5[4] = u
                    if u == "w_sol":
                        r5c4.config(image=w_sol_b)
                        row_5[4] = u
                    if u == "b_ele":
                        r5c4.config(image=b_ele_b)
                        row_5[4] = u
                    if u == "w_ele":
                        r5c4.config(image=w_ele_b)
                        row_5[4] = u
                    if u == "b_hor":
                        r5c4.config(image=b_hor_b)
                        row_5[4] = u
                    if u == "w_hor":
                        r5c4.config(image=w_hor_b)
                        row_5[4] = u
                    if u == "b_cam":
                        r5c4.config(image=b_cam_b)
                        row_5[4] = u
                    if u == "w_cam":
                        r5c4.config(image=w_cam_b)
                        row_5[4] = u
                    if u == "b_king":
                        r5c4.config(image=b_king_b)
                        row_5[4] = u
                    if u == "w_king":
                        r5c4.config(image=w_king_b)
                        row_5[4] = u
                    if u == "b_que":
                        r5c4.config(image=b_que_b)
                        row_5[4] = u
                    if u == "w_que":
                        r5c4.config(image=w_que_b)
                        row_5[4] = u

                if place == 56 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c6.config(image=b_sol_b)
                        row_5[6] = u
                    if u == "w_sol":
                        r5c6.config(image=w_sol_b)
                        row_5[6] = u
                    if u == "b_ele":
                        r5c6.config(image=b_ele_b)
                        row_5[6] = u
                    if u == "w_ele":
                        r5c6.config(image=w_ele_b)
                        row_5[6] = u
                    if u == "b_hor":
                        r5c6.config(image=b_hor_b)
                        row_5[6] = u
                    if u == "w_hor":
                        r5c6.config(image=w_hor_b)
                        row_5[6] = u
                    if u == "b_cam":
                        r5c6.config(image=b_cam_b)
                        row_5[6] = u
                    if u == "w_cam":
                        r5c6.config(image=w_cam_b)
                        row_5[6] = u
                    if u == "b_king":
                        r5c6.config(image=b_king_b)
                        row_5[6] = u
                    if u == "w_king":
                        r5c6.config(image=w_king_b)
                        row_5[6] = u
                    if u == "b_que":
                        r5c6.config(image=b_que_b)
                        row_5[6] = u
                    if u == "w_que":
                        r5c6.config(image=w_que_b)
                        row_5[6] = u


                if place == 58 :
                    u = unit[1]
                    if u == "b_sol":
                        r5c8.config(image=b_sol_b)
                        row_5[8] = u
                    if u == "w_sol":
                        r5c8.config(image=w_sol_b)
                        row_5[8] = u
                    if u == "b_ele":
                        r5c8.config(image=b_ele_b)
                        row_5[8] = u
                    if u == "w_ele":
                        r5c8.config(image=w_ele_b)
                        row_5[8] = u
                    if u == "b_hor":
                        r5c8.config(image=b_hor_b)
                        row_5[8] = u
                    if u == "w_hor":
                        r5c8.config(image=w_hor_b)
                        row_5[8] = u
                    if u == "b_cam":
                        r5c8.config(image=b_cam_b)
                        row_5[8] = u
                    if u == "w_cam":
                        r5c8.config(image=w_cam_b)
                        row_5[8] = u
                    if u == "b_king":
                        r5c8.config(image=b_king_b)
                        row_5[8] = u
                    if u == "w_king":
                        r5c8.config(image=w_king_b)
                        row_5[8] = u
                    if u == "b_que":
                        r5c8.config(image=b_que_b)
                        row_5[8] = u
                    if u == "w_que":
                        r5c8.config(image=w_que_b)
                        row_5[8] = u

                if place == 72 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c2.config(image=b_sol_b)
                        row_7[2] = u
                    if u == "w_sol":
                        r7c2.config(image=w_sol_b)
                        row_7[2] = u
                    if u == "b_ele":
                        r7c2.config(image=b_ele_b)
                        row_7[2] = u
                    if u == "w_ele":
                        r7c2.config(image=w_ele_b)
                        row_7[2] = u
                    if u == "b_hor":
                        r7c2.config(image=b_hor_b)
                        row_7[2] = u
                    if u == "w_hor":
                        r7c2.config(image=w_hor_b)
                        row_7[2] = u
                    if u == "b_cam":
                        r7c2.config(image=b_cam_b)
                        row_7[2] = u
                    if u == "w_cam":
                        r7c2.config(image=w_cam_b)
                        row_7[2] = u
                    if u == "b_king":
                        r7c2.config(image=b_king_b)
                        row_7[2] = u
                    if u == "w_king":
                        r7c2.config(image=w_king_b)
                        row_7[2] = u
                    if u == "b_que":
                        r7c2.config(image=b_que_b)
                        row_7[2] = u
                    if u == "w_que":
                        r7c2.config(image=w_que_b)
                        row_7[2] = u


                if place == 74 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c4.config(image=b_sol_b)
                        row_7[4] = u
                    if u == "w_sol":
                        r7c4.config(image=w_sol_b)
                        row_7[4] = u
                    if u == "b_ele":
                        r7c4.config(image=b_ele_b)
                        row_7[4] = u
                    if u == "w_ele":
                        r7c4.config(image=w_ele_b)
                        row_7[4] = u
                    if u == "b_hor":
                        r7c4.config(image=b_hor_b)
                        row_7[4] = u
                    if u == "w_hor":
                        r7c4.config(image=w_hor_b)
                        row_7[4] = u
                    if u == "b_cam":
                        r7c4.config(image=b_cam_b)
                        row_7[4] = u
                    if u == "w_cam":
                        r7c4.config(image=w_cam_b)
                        row_7[4] = u
                    if u == "b_king":
                        r7c4.config(image=b_king_b)
                        row_7[4] = u
                    if u == "w_king":
                        r7c4.config(image=w_king_b)
                        row_7[4] = u
                    if u == "b_que":
                        r7c4.config(image=b_que_b)
                        row_7[4] = u
                    if u == "w_que":
                        r7c4.config(image=w_que_b)
                        row_7[4] = u

                if place == 76 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c6.config(image=b_sol_b)
                        row_7[6] = u
                    if u == "w_sol":
                        r7c6.config(image=w_sol_b)
                        row_7[6] = u
                    if u == "b_ele":
                        r7c6.config(image=b_ele_b)
                        row_7[6] = u
                    if u == "w_ele":
                        r7c6.config(image=w_ele_b)
                        row_7[6] = u
                    if u == "b_hor":
                        r7c6.config(image=b_hor_b)
                        row_7[6] = u
                    if u == "w_hor":
                        r7c6.config(image=w_hor_b)
                        row_7[6] = u
                    if u == "b_cam":
                        r7c6.config(image=b_cam_b)
                        row_7[6] = u
                    if u == "w_cam":
                        r7c6.config(image=w_cam_b)
                        row_7[6] = u
                    if u == "b_king":
                        r7c6.config(image=b_king_b)
                        row_7[6] = u
                    if u == "w_king":
                        r7c6.config(image=w_king_b)
                        row_7[6] = u
                    if u == "b_que":
                        r7c6.config(image=b_que_b)
                        row_7[6] = u
                    if u == "w_que":
                        r7c6.config(image=w_que_b)
                        row_7[6] = u


                if place == 78 :
                    u = unit[1]
                    if u == "b_sol":
                        r7c8.config(image=b_sol_b)
                        row_7[8] = u
                    if u == "w_sol":
                        r7c8.config(image=w_sol_b)
                        row_7[8] = u
                    if u == "b_ele":
                        r7c8.config(image=b_ele_b)
                        row_7[8] = u
                    if u == "w_ele":
                        r7c8.config(image=w_ele_b)
                        row_7[8] = u
                    if u == "b_hor":
                        r7c8.config(image=b_hor_b)
                        row_7[8] = u
                    if u == "w_hor":
                        r7c8.config(image=w_hor_b)
                        row_7[8] = u
                    if u == "b_cam":
                        r7c8.config(image=b_cam_b)
                        row_7[8] = u
                    if u == "w_cam":
                        r7c8.config(image=w_cam_b)
                        row_7[8] = u
                    if u == "b_king":
                        r7c8.config(image=b_king_b)
                        row_7[8] = u
                    if u == "w_king":
                        r7c8.config(image=w_king_b)
                        row_7[8] = u
                    if u == "b_que":
                        r7c8.config(image=b_que_b)
                        row_7[8] = u
                    if u == "w_que":
                        r7c8.config(image=w_que_b)
                        row_7[8] = u

                if place == 22 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c2.config(image=b_sol_w)
                        row_2[2] = u
                    if u == "w_sol":
                        r2c2.config(image=w_sol_w)
                        row_2[2] = u
                    if u == "b_ele":
                        r2c2.config(image=b_ele_w)
                        row_2[2] = u
                    if u == "w_ele":
                        r2c2.config(image=w_ele_w)
                        row_2[2] = u
                    if u == "b_hor":
                        r2c2.config(image=b_hor_w)
                        row_2[2] = u
                    if u == "w_hor":
                        r2c2.config(image=w_hor_w)
                        row_2[2] = u
                    if u == "b_cam":
                        r2c2.config(image=b_cam_w)
                        row_2[2] = u
                    if u == "w_cam":
                        r2c2.config(image=w_cam_w)
                        row_2[2] = u
                    if u == "b_king":
                        r2c2.config(image=b_king_w)
                        row_2[2] = u
                    if u == "w_king":
                        r2c2.config(image=w_king_w)
                        row_2[2] = u
                    if u == "b_que":
                        r2c2.config(image=b_que_w)
                        row_2[2] = u
                    if u == "w_que":
                        r2c2.config(image=w_que_w)
                        row_2[2] = u
        ######################################################################################
                if place == 24 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c4.config(image=b_sol_w)
                        row_2[4] = u
                    if u == "w_sol":
                        r2c4.config(image=w_sol_w)
                        row_2[4] = u
                    if u == "b_ele":
                        r2c4.config(image=b_ele_w)
                        row_2[4] = u
                    if u == "w_ele":
                        r2c4.config(image=w_ele_w)
                        row_2[4] = u
                    if u == "b_hor":
                        r2c4.config(image=b_hor_w)
                        row_2[4] = u
                    if u == "w_hor":
                        r2c4.config(image=w_hor_w)
                        row_2[4] = u
                    if u == "b_cam":
                        r2c4.config(image=b_cam_w)
                        row_2[4] = u
                    if u == "w_cam":
                        r2c4.config(image=w_cam_w)
                        row_2[4] = u
                    if u == "b_king":
                        r2c4.config(image=b_king_w)
                        row_2[4] = u
                    if u == "w_king":
                        r2c4.config(image=w_king_w)
                        row_2[4] = u
                    if u == "b_que":
                        r2c4.config(image=b_que_w)
                        row_2[4] = u
                    if u == "w_que":
                        r2c4.config(image=w_que_w)
                        row_2[4] = u
        ######################################################################################
                if place == 26 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c6.config(image=b_sol_w)
                        row_2[6] = u
                    if u == "w_sol":
                        r2c6.config(image=w_sol_w)
                        row_2[6] = u
                    if u == "b_ele":
                        r2c6.config(image=b_ele_w)
                        row_2[6] = u
                    if u == "w_ele":
                        r2c6.config(image=w_ele_w)
                        row_2[6] = u
                    if u == "b_hor":
                        r2c6.config(image=b_hor_w)
                        row_2[6] = u
                    if u == "w_hor":
                        r2c6.config(image=w_hor_w)
                        row_2[6] = u
                    if u == "b_cam":
                        r2c6.config(image=b_cam_w)
                        row_2[6] = u
                    if u == "w_cam":
                        r2c6.config(image=w_cam_w)
                        row_2[6] = u
                    if u == "b_king":
                        r2c6.config(image=b_king_w)
                        row_2[6] = u
                    if u == "w_king":
                        r2c6.config(image=w_king_w)
                        row_2[6] = u
                    if u == "b_que":
                        r2c6.config(image=b_que_w)
                        row_2[6] = u
                    if u == "w_que":
                        r2c6.config(image=w_que_w)
                        row_2[6] = u
        ######################################################################################
                if place == 28 :
                    u = unit[1]
                    if u == "b_sol":
                        r2c8.config(image=b_sol_w)
                        row_2[8] = u
                    if u == "w_sol":
                        r2c8.config(image=w_sol_w)
                        row_2[8] = u
                    if u == "b_ele":
                        r2c8.config(image=b_ele_w)
                        row_2[8] = u
                    if u == "w_ele":
                        r2c8.config(image=w_ele_w)
                        row_2[8] = u
                    if u == "b_hor":
                        r2c8.config(image=b_hor_w)
                        row_2[8] = u
                    if u == "w_hor":
                        r2c8.config(image=w_hor_w)
                        row_2[8] = u
                    if u == "b_cam":
                        r2c8.config(image=b_cam_w)
                        row_2[8] = u
                    if u == "w_cam":
                        r2c8.config(image=w_cam_w)
                        row_2[8] = u
                    if u == "b_king":
                        r2c8.config(image=b_king_w)
                        row_2[8] = u
                    if u == "w_king":
                        r2c8.config(image=w_king_w)
                        row_2[8] = u
                    if u == "b_que":
                        r2c8.config(image=b_que_w)
                        row_2[8] = u
                    if u == "w_que":
                        r2c8.config(image=w_que_w)
                        row_2[8] = u

                if place == 42 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c2.config(image=b_sol_w)
                        row_4[2] = u
                    if u == "w_sol":
                        r4c2.config(image=w_sol_w)
                        row_4[2] = u
                    if u == "b_ele":
                        r4c2.config(image=b_ele_w)
                        row_4[2] = u
                    if u == "w_ele":
                        r4c2.config(image=w_ele_w)
                        row_4[2] = u
                    if u == "b_hor":
                        r4c2.config(image=b_hor_w)
                        row_4[2] = u
                    if u == "w_hor":
                        r4c2.config(image=w_hor_w)
                        row_4[2] = u
                    if u == "b_cam":
                        r4c2.config(image=b_cam_w)
                        row_4[2] = u
                    if u == "w_cam":
                        r4c2.config(image=w_cam_w)
                        row_4[2] = u
                    if u == "b_king":
                        r4c2.config(image=b_king_w)
                        row_4[2] = u
                    if u == "w_king":
                        r4c2.config(image=w_king_w)
                        row_4[2] = u
                    if u == "b_que":
                        r4c2.config(image=b_que_w)
                        row_4[2] = u
                    if u == "w_que":
                        r4c2.config(image=w_que_w)
                        row_4[2] = u
        ######################################################################################
                if place == 44 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c4.config(image=b_sol_w)
                        row_4[4] = u
                    if u == "w_sol":
                        r4c4.config(image=w_sol_w)
                        row_4[4] = u
                    if u == "b_ele":
                        r4c4.config(image=b_ele_w)
                        row_4[4] = u
                    if u == "w_ele":
                        r4c4.config(image=w_ele_w)
                        row_4[4] = u
                    if u == "b_hor":
                        r4c4.config(image=b_hor_w)
                        row_4[4] = u
                    if u == "w_hor":
                        r4c4.config(image=w_hor_w)
                        row_4[4] = u
                    if u == "b_cam":
                        r4c4.config(image=b_cam_w)
                        row_4[4] = u
                    if u == "w_cam":
                        r4c4.config(image=w_cam_w)
                        row_4[4] = u
                    if u == "b_king":
                        r4c4.config(image=b_king_w)
                        row_4[4] = u
                    if u == "w_king":
                        r4c4.config(image=w_king_w)
                        row_4[4] = u
                    if u == "b_que":
                        r4c4.config(image=b_que_w)
                        row_4[4] = u
                    if u == "w_que":
                        r4c4.config(image=w_que_w)
                        row_4[4] = u
        ######################################################################################
                if place == 46 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c6.config(image=b_sol_w)
                        row_4[6] = u
                    if u == "w_sol":
                        r4c6.config(image=w_sol_w)
                        row_4[6] = u
                    if u == "b_ele":
                        r4c6.config(image=b_ele_w)
                        row_4[6] = u
                    if u == "w_ele":
                        r4c6.config(image=w_ele_w)
                        row_4[6] = u
                    if u == "b_hor":
                        r4c6.config(image=b_hor_w)
                        row_4[6] = u
                    if u == "w_hor":
                        r4c6.config(image=w_hor_w)
                        row_4[6] = u
                    if u == "b_cam":
                        r4c6.config(image=b_cam_w)
                        row_4[6] = u
                    if u == "w_cam":
                        r4c6.config(image=w_cam_w)
                        row_4[6] = u
                    if u == "b_king":
                        r4c6.config(image=b_king_w)
                        row_4[6] = u
                    if u == "w_king":
                        r4c6.config(image=w_king_w)
                        row_4[6] = u
                    if u == "b_que":
                        r4c6.config(image=b_que_w)
                        row_4[6] = u
                    if u == "w_que":
                        r4c6.config(image=w_que_w)
                        row_4[6] = u
        ######################################################################################
                if place == 48 :
                    u = unit[1]
                    if u == "b_sol":
                        r4c8.config(image=b_sol_w)
                        row_4[8] = u
                    if u == "w_sol":
                        r4c8.config(image=w_sol_w)
                        row_4[8] = u
                    if u == "b_ele":
                        r4c8.config(image=b_ele_w)
                        row_4[8] = u
                    if u == "w_ele":
                        r4c8.config(image=w_ele_w)
                        row_4[8] = u
                    if u == "b_hor":
                        r4c8.config(image=b_hor_w)
                        row_4[8] = u
                    if u == "w_hor":
                        r4c8.config(image=w_hor_w)
                        row_4[8] = u
                    if u == "b_cam":
                        r4c8.config(image=b_cam_w)
                        row_4[8] = u
                    if u == "w_cam":
                        r4c8.config(image=w_cam_w)
                        row_4[8] = u
                    if u == "b_king":
                        r4c8.config(image=b_king_w)
                        row_4[8] = u
                    if u == "w_king":
                        r4c8.config(image=w_king_w)
                        row_4[8] = u
                    if u == "b_que":
                        r4c8.config(image=b_que_w)
                        row_4[8] = u
                    if u == "w_que":
                        r4c8.config(image=w_que_w)
                        row_4[8] = u

                if place == 62 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c2.config(image=b_sol_w)
                        row_6[2] = u
                    if u == "w_sol":
                        r6c2.config(image=w_sol_w)
                        row_6[2] = u
                    if u == "b_ele":
                        r6c2.config(image=b_ele_w)
                        row_6[2] = u
                    if u == "w_ele":
                        r6c2.config(image=w_ele_w)
                        row_6[2] = u
                    if u == "b_hor":
                        r6c2.config(image=b_hor_w)
                        row_6[2] = u
                    if u == "w_hor":
                        r6c2.config(image=w_hor_w)
                        row_6[2] = u
                    if u == "b_cam":
                        r6c2.config(image=b_cam_w)
                        row_6[2] = u
                    if u == "w_cam":
                        r6c2.config(image=w_cam_w)
                        row_6[2] = u
                    if u == "b_king":
                        r6c2.config(image=b_king_w)
                        row_6[2] = u
                    if u == "w_king":
                        r6c2.config(image=w_king_w)
                        row_6[2] = u
                    if u == "b_que":
                        r6c2.config(image=b_que_w)
                        row_6[2] = u
                    if u == "w_que":
                        r6c2.config(image=w_que_w)
                        row_6[2] = u
        ######################################################################################
                if place == 64 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c4.config(image=b_sol_w)
                        row_6[4] = u
                    if u == "w_sol":
                        r6c4.config(image=w_sol_w)
                        row_6[4] = u
                    if u == "b_ele":
                        r6c4.config(image=b_ele_w)
                        row_6[4] = u
                    if u == "w_ele":
                        r6c4.config(image=w_ele_w)
                        row_6[4] = u
                    if u == "b_hor":
                        r6c4.config(image=b_hor_w)
                        row_6[4] = u
                    if u == "w_hor":
                        r6c4.config(image=w_hor_w)
                        row_6[4] = u
                    if u == "b_cam":
                        r6c4.config(image=b_cam_w)
                        row_6[4] = u
                    if u == "w_cam":
                        r6c4.config(image=w_cam_w)
                        row_6[4] = u
                    if u == "b_king":
                        r6c4.config(image=b_king_w)
                        row_6[4] = u
                    if u == "w_king":
                        r6c4.config(image=w_king_w)
                        row_6[4] = u
                    if u == "b_que":
                        r6c4.config(image=b_que_w)
                        row_6[4] = u
                    if u == "w_que":
                        r6c4.config(image=w_que_w)
                        row_6[4] = u
        ######################################################################################
                if place == 66 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c6.config(image=b_sol_w)
                        row_6[6] = u
                    if u == "w_sol":
                        r6c6.config(image=w_sol_w)
                        row_6[6] = u
                    if u == "b_ele":
                        r6c6.config(image=b_ele_w)
                        row_6[6] = u
                    if u == "w_ele":
                        r6c6.config(image=w_ele_w)
                        row_6[6] = u
                    if u == "b_hor":
                        r6c6.config(image=b_hor_w)
                        row_6[6] = u
                    if u == "w_hor":
                        r6c6.config(image=w_hor_w)
                        row_6[6] = u
                    if u == "b_cam":
                        r6c6.config(image=b_cam_w)
                        row_6[6] = u
                    if u == "w_cam":
                        r6c6.config(image=w_cam_w)
                        row_6[6] = u
                    if u == "b_king":
                        r6c6.config(image=b_king_w)
                        row_6[6] = u
                    if u == "w_king":
                        r6c6.config(image=w_king_w)
                        row_6[6] = u
                    if u == "b_que":
                        r6c6.config(image=b_que_w)
                        row_6[6] = u
                    if u == "w_que":
                        r6c6.config(image=w_que_w)
                        row_6[6] = u
        ######################################################################################
                if place == 68 :
                    u = unit[1]
                    if u == "b_sol":
                        r6c8.config(image=b_sol_w)
                        row_6[8] = u
                    if u == "w_sol":
                        r6c8.config(image=w_sol_w)
                        row_6[8] = u
                    if u == "b_ele":
                        r6c8.config(image=b_ele_w)
                        row_6[8] = u
                    if u == "w_ele":
                        r6c8.config(image=w_ele_w)
                        row_6[8] = u
                    if u == "b_hor":
                        r6c8.config(image=b_hor_w)
                        row_6[8] = u
                    if u == "w_hor":
                        r6c8.config(image=w_hor_w)
                        row_6[8] = u
                    if u == "b_cam":
                        r6c8.config(image=b_cam_w)
                        row_6[8] = u
                    if u == "w_cam":
                        r6c8.config(image=w_cam_w)
                        row_6[8] = u
                    if u == "b_king":
                        r6c8.config(image=b_king_w)
                        row_6[8] = u
                    if u == "w_king":
                        r6c8.config(image=w_king_w)
                        row_6[8] = u
                    if u == "b_que":
                        r6c8.config(image=b_que_w)
                        row_6[8] = u
                    if u == "w_que":
                        r6c8.config(image=w_que_w)
                        row_6[8] = u

                if place == 82 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c2.config(image=b_sol_w)
                        row_8[2] = u
                    if u == "w_sol":
                        r8c2.config(image=w_sol_w)
                        row_8[2] = u
                    if u == "b_ele":
                        r8c2.config(image=b_ele_w)
                        row_8[2] = u
                    if u == "w_ele":
                        r8c2.config(image=w_ele_w)
                        row_8[2] = u
                    if u == "b_hor":
                        r8c2.config(image=b_hor_w)
                        row_8[2] = u
                    if u == "w_hor":
                        r8c2.config(image=w_hor_w)
                        row_8[2] = u
                    if u == "b_cam":
                        r8c2.config(image=b_cam_w)
                        row_8[2] = u
                    if u == "w_cam":
                        r8c2.config(image=w_cam_w)
                        row_8[2] = u
                    if u == "b_king":
                        r8c2.config(image=b_king_w)
                        row_8[2] = u
                    if u == "w_king":
                        r8c2.config(image=w_king_w)
                        row_8[2] = u
                    if u == "b_que":
                        r8c2.config(image=b_que_w)
                        row_8[2] = u
                    if u == "w_que":
                        r8c2.config(image=w_que_w)
                        row_8[2] = u
        ######################################################################################
                if place == 84 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c4.config(image=b_sol_w)
                        row_8[4] = u
                    if u == "w_sol":
                        r8c4.config(image=w_sol_w)
                        row_8[4] = u
                    if u == "b_ele":
                        r8c4.config(image=b_ele_w)
                        row_8[4] = u
                    if u == "w_ele":
                        r8c4.config(image=w_ele_w)
                        row_8[4] = u
                    if u == "b_hor":
                        r8c4.config(image=b_hor_w)
                        row_8[4] = u
                    if u == "w_hor":
                        r8c4.config(image=w_hor_w)
                        row_8[4] = u
                    if u == "b_cam":
                        r8c4.config(image=b_cam_w)
                        row_8[4] = u
                    if u == "w_cam":
                        r8c4.config(image=w_cam_w)
                        row_8[4] = u
                    if u == "b_king":
                        r8c4.config(image=b_king_w)
                        row_8[4] = u
                    if u == "w_king":
                        r8c4.config(image=w_king_w)
                        row_8[4] = u
                    if u == "b_que":
                        r8c4.config(image=b_que_w)
                        row_8[4] = u
                    if u == "w_que":
                        r8c4.config(image=w_que_w)
                        row_8[4] = u
        ######################################################################################
                if place == 86 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c6.config(image=b_sol_w)
                        row_8[6] = u
                    if u == "w_sol":
                        r8c6.config(image=w_sol_w)
                        row_8[6] = u
                    if u == "b_ele":
                        r8c6.config(image=b_ele_w)
                        row_8[6] = u
                    if u == "w_ele":
                        r8c6.config(image=w_ele_w)
                        row_8[6] = u
                    if u == "b_hor":
                        r8c6.config(image=b_hor_w)
                        row_8[6] = u
                    if u == "w_hor":
                        r8c6.config(image=w_hor_w)
                        row_8[6] = u
                    if u == "b_cam":
                        r8c6.config(image=b_cam_w)
                        row_8[6] = u
                    if u == "w_cam":
                        r8c6.config(image=w_cam_w)
                        row_8[6] = u
                    if u == "b_king":
                        r8c6.config(image=b_king_w)
                        row_8[6] = u
                    if u == "w_king":
                        r8c6.config(image=w_king_w)
                        row_8[6] = u
                    if u == "b_que":
                        r8c6.config(image=b_que_w)
                        row_8[6] = u
                    if u == "w_que":
                        r8c6.config(image=w_que_w)
                        row_8[6] = u
        ######################################################################################
                if place == 88 :
                    u = unit[1]
                    if u == "b_sol":
                        r8c8.config(image=b_sol_w)
                        row_8[8] = u
                    if u == "w_sol":
                        r8c8.config(image=w_sol_w)
                        row_8[8] = u
                    if u == "b_ele":
                        r8c8.config(image=b_ele_w)
                        row_8[8] = u
                    if u == "w_ele":
                        r8c8.config(image=w_ele_w)
                        row_8[8] = u
                    if u == "b_hor":
                        r8c8.config(image=b_hor_w)
                        row_8[8] = u
                    if u == "w_hor":
                        r8c8.config(image=w_hor_w)
                        row_8[8] = u
                    if u == "b_cam":
                        r8c8.config(image=b_cam_w)
                        row_8[8] = u
                    if u == "w_cam":
                        r8c8.config(image=w_cam_w)
                        row_8[8] = u
                    if u == "b_king":
                        r8c8.config(image=b_king_w)
                        row_8[8] = u
                    if u == "w_king":
                        r8c8.config(image=w_king_w)
                        row_8[8] = u
                    if u == "b_que":
                        r8c8.config(image=b_que_w)
                        row_8[8] = u
                    if u == "w_que":
                        r8c8.config(image=w_que_w)
                        row_8[8] = u
                state[1]=1

def graphics():
    global l
    root.config(bg="black")
    l = Label(root,text="\n\n\n\n\n\n\n\n\n\t\t\t\t\t\n\n\t\t\t\t L O A D I N G . . . . \n\n\t\t\t\t\t",bg="black",fg="red",font="99")
    l.grid(row=1,column=1)
    root.after(5000,end_mai)

def end_mai():
    l.destroy()
    root.config(bg="orange")
    load_graphics()
    
def main():

    root.geometry("750x550")
    root.config(bg="orange")
    root.title("Chess- Build to win")
    graphics()
    root.mainloop()


def load_graphics():

    global b_ele_b
    global w_ele_b
    global b_hor_b
    global w_hor_b
    global b_cam_b
    global w_cam_b
    global b_king_b
    global w_king_b
    global b_que_b
    global w_que_b
    global b_sol_b
    global w_sol_b
    global b_plate
    global w_plate
    global b_ele_w
    global w_ele_w
    global b_hor_w
    global w_hor_w
    global b_cam_w
    global w_cam_w
    global b_king_w
    global w_king_w
    global b_que_w
    global w_que_w
    global b_sol_w
    global w_sol_w
    global clicked_w_ele
    global clicked_w_hor
    global clicked_w_cam
    global clicked_w_que
    global clicked_w_king
    global clicked_w_sol
    global clicked_b_ele
    global clicked_b_hor
    global clicked_b_cam
    global clicked_b_que
    global clicked_b_king
    global clicked_b_sol
    global blue_plate
    global ch1_w_king_w
    global ch2_w_king_w

    ch1_w_king_w = PhotoImage(file="l_1/ch_1.gif")
    ch2_w_king_w = PhotoImage(file="l_2/ch_2.gif")
    
    
    if type_of_unit == 1 :

        b_ele_b = PhotoImage(file="l_1/b_ele_b.gif")
        b_ele_w = PhotoImage(file="l_1/b_ele_w.gif")
        w_ele_b = PhotoImage(file="l_1/w_ele_b.gif")
        w_ele_w = PhotoImage(file="l_1/w_ele_w.gif")
        b_hor_b = PhotoImage(file="l_1/b_hor_b.gif")
        b_hor_w = PhotoImage(file="l_1/b_hor_w.gif")
        w_hor_w = PhotoImage(file="l_1/w_hor_w.gif")
        w_hor_b = PhotoImage(file="l_1/w_hor_b.gif")
        b_cam_b = PhotoImage(file="l_1/b_cam_b.gif")
        b_cam_w = PhotoImage(file="l_1/b_cam_w.gif")
        w_cam_w = PhotoImage(file="l_1/w_cam_w.gif")
        w_cam_b = PhotoImage(file="l_1/w_cam_b.gif")
        b_king_b = PhotoImage(file="l_1/b_king_b.gif")
        b_king_w = PhotoImage(file="l_1/b_king_w.gif")
        w_king_b = PhotoImage(file="l_1/w_king_b.gif")
        w_king_w = PhotoImage(file="l_1/w_king_w.gif")
        b_que_w = PhotoImage(file="l_1/b_que_w.gif")
        b_que_b = PhotoImage(file="l_1/b_que_b.gif")
        w_que_b = PhotoImage(file="l_1/w_que_b.gif")
        w_que_w = PhotoImage(file="l_1/w_que_w.gif")
        b_sol_b = PhotoImage(file="l_1/b_sol_b.gif")
        b_sol_w = PhotoImage(file="l_1/b_sol_w.gif")
        w_sol_w = PhotoImage(file="l_1/w_sol_w.gif")
        w_sol_b = PhotoImage(file="l_1/w_sol_b.gif")
        b_plate = PhotoImage(file="l_1/b_plate.gif")
        w_plate = PhotoImage(file="l_1/w_plate.gif")
        clicked_w_ele = PhotoImage(file="l_1/clicked_w_ele.gif")
        clicked_w_hor = PhotoImage(file="l_1/clicked_w_hor.gif")
        clicked_w_cam = PhotoImage(file="l_1/clicked_w_cam.gif")
        clicked_w_que = PhotoImage(file="l_1/clicked_w_que.gif")
        clicked_w_king = PhotoImage(file="l_1/clicked_w_king.gif")
        clicked_w_sol = PhotoImage(file="l_1/clicked_w_sol.gif")
        clicked_b_ele = PhotoImage(file="l_1/clicked_b_ele.gif")
        clicked_b_hor = PhotoImage(file="l_1/clicked_b_hor.gif")
        clicked_b_cam = PhotoImage(file="l_1/clicked_b_cam.gif")
        clicked_b_que = PhotoImage(file="l_1/clicked_b_que.gif")
        clicked_b_king = PhotoImage(file="l_1/clicked_b_king.gif")
        clicked_b_sol = PhotoImage(file="l_1/clicked_b_sol.gif")
        blue_plate = PhotoImage(file="l_1/blue_plate.gif")

    if type_of_unit == None or type_of_unit == 2 :
        
        b_ele_b = PhotoImage(file="l_2/b_ele_b.gif")
        b_ele_w = PhotoImage(file="l_2/b_ele_w.gif")
        w_ele_b = PhotoImage(file="l_2/w_ele_b.gif")
        w_ele_w = PhotoImage(file="l_2/w_ele_w.gif")
        b_hor_b = PhotoImage(file="l_2/b_hor_b.gif")
        b_hor_w = PhotoImage(file="l_2/b_hor_w.gif")
        w_hor_w = PhotoImage(file="l_2/w_hor_w.gif")
        w_hor_b = PhotoImage(file="l_2/w_hor_b.gif")
        b_cam_b = PhotoImage(file="l_2/b_cam_b.gif")
        b_cam_w = PhotoImage(file="l_2/b_cam_w.gif")
        w_cam_w = PhotoImage(file="l_2/w_cam_w.gif")
        w_cam_b = PhotoImage(file="l_2/w_cam_b.gif")
        b_king_b = PhotoImage(file="l_2/b_king_b.gif")
        b_king_w = PhotoImage(file="l_2/b_king_w.gif")
        w_king_b = PhotoImage(file="l_2/w_king_b.gif")
        w_king_w = PhotoImage(file="l_2/w_king_w.gif")
        b_que_w = PhotoImage(file="l_2/b_que_w.gif")
        b_que_b = PhotoImage(file="l_2/b_que_b.gif")
        w_que_b = PhotoImage(file="l_2/w_que_b.gif")
        w_que_w = PhotoImage(file="l_2/w_que_w.gif")
        b_sol_b = PhotoImage(file="l_2/b_sol_b.gif")
        b_sol_w = PhotoImage(file="l_2/b_sol_w.gif")
        w_sol_w = PhotoImage(file="l_2/w_sol_w.gif")
        w_sol_b = PhotoImage(file="l_2/w_sol_b.gif")
        b_plate = PhotoImage(file="l_2/b_plate.gif")
        w_plate = PhotoImage(file="l_2/w_plate.gif")
        clicked_w_ele = PhotoImage(file="l_2/clicked_w_ele.gif")
        clicked_w_hor = PhotoImage(file="l_2/clicked_w_hor.gif")
        clicked_w_cam = PhotoImage(file="l_2/clicked_w_cam.gif")
        clicked_w_que = PhotoImage(file="l_2/clicked_w_que.gif")
        clicked_w_king = PhotoImage(file="l_2/clicked_w_king.gif")
        clicked_w_sol = PhotoImage(file="l_2/clicked_w_sol.gif")
        clicked_b_ele = PhotoImage(file="l_2/clicked_b_ele.gif")
        clicked_b_hor = PhotoImage(file="l_2/clicked_b_hor.gif")
        clicked_b_cam = PhotoImage(file="l_2/clicked_b_cam.gif")
        clicked_b_que = PhotoImage(file="l_2/clicked_b_que.gif")
        clicked_b_king = PhotoImage(file="l_2/clicked_b_king.gif")
        clicked_b_sol = PhotoImage(file="l_2/clicked_b_sol.gif")
        blue_plate = PhotoImage(file="l_2/blue_plate.gif")

    ask()
main()
