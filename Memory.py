# implementation of card game - Memory

import simplegui
import random

CARDS_WIDTH=50
CARDS_HEIGTH=100
turns=0

# helper function to initialize globals
def new_game():
    global lst,exposed,state,turns
   
    lst=[]
    exposed=[False]*16
    state=0
    turns=0
    lst1 = range(8)
    lst2 = range(8)
    lst = lst1+lst2
    random.shuffle(lst)
     
# define event handlers
def mouseclick(pos):
    
    global lst,exposed,CARDS_WIDTH,state,var1,var2,turns
    card=pos[0] // CARDS_WIDTH
    if state == 0:
        exposed[card]=True 
        var1=card
        state = 1
    elif state == 1:
        if exposed[card]==False:
            exposed[card]=True
            var2=card
            state = 2
            turns+=1
    else:
        if (lst[var1] != lst[var2]):            
            exposed[var1]=False
            exposed[var2]=False
        else:
            exposed[var1]=True
            exposed[var2]=True
        if exposed[card] == False:
            state = 1
            var1=card
            exposed[card]=True
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    global lst,exposed,CARDS_WIDTH,CARDS_HEIGTH
    j=25
    k=50
    label.set_text("Turns = "+str(turns))
    for cards in range(len(lst)): 
        for i in exposed:
            if exposed[cards] == True:
                canvas.draw_text(str(lst[cards]), (j-10, 70), 40, 'White')
            else:
                canvas.draw_line((j, 0), (j, CARDS_HEIGTH), CARDS_WIDTH, 'Green')
        j+=50
        canvas.draw_line((k, 0), (k, CARDS_HEIGTH), 1, 'Red')
        k+=50


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
