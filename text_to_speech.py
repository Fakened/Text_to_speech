from tkinter import *
import gtts.lang
from gtts import gTTS
from playsound import playsound

languages = gtts.lang.tts_langs()
###################### GUI ###############
root = Tk()
menuBar = Menu(root)
messegeFrame = Frame(root)
messegeFrame.pack(side = TOP, fill = X, pady=30)
insertFrame = Frame(root)
insertFrame.pack(side = TOP, fill = X, pady=10)
buttonFrame = Frame(root)
buttonFrame.pack(side = TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

root.title("TEXT TO SPEECH")

optionmenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Option", menu=optionmenu)
langmenu = Menu(optionmenu, tearoff=0)
langmenu.add_command(label='English')
langmenu.add_command(label='Polish')
optionmenu.add_cascade(label="Language", menu= langmenu)

Label(messegeFrame, text = "TEXT TO SPEECH", font = "arial 20 bold").pack(side = TOP)
Msg = StringVar()
Label(insertFrame,text ="Enter Text", font = 'arial 15 bold').pack(side = TOP)
entry_field = Entry(insertFrame, textvariable = Msg ,width ='50')
entry_field.pack(fill = X)


########## Functions ################
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('file.mp3')
    playsound('file.mp3')

def Exit():
    root.quit()

def Reset():
    Msg.set("")

################ Buttons ##########################
b1 = Button(buttonFrame, font = 'arial 15 bold' , text = "PLAY",  width = '4', command = Text_to_speech)
b2 = Button(buttonFrame, font = 'arial 15 bold', text = 'RESET', width = '6' , command = Reset)
b3 = Button(bottomFrame, font = 'arial 15 bold', text = 'EXIT' ,width='6', command = Exit, bg = 'OrangeRed1')
b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack( side = BOTTOM, fill = X)


####################################################
root.config(menu=menuBar)
root.mainloop()