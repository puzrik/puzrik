from tkinter import *
import tkinter
import random
import tkinter as tk
import tkinter.filedialog as fd
import tkinter
import os
import time
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox
windowOpen = True
temp_1 = 0
after_id_1 = ''
clicks = 0
widt = 3
vibor = ""
ris = "ris"
word = "word"
gameOver = False
canvasWidth = 750
canvasHeight = 500
score = 0
squaresToClear = 0
def click_me():
    vibor = ris
    print(vibor)
    class Paint(object):
    
        DEFAULT_PEN_SIZE = 5.0
        DEFAULT_COLOR = 'black'
    
        def __init__(self):
            self.root = Tk()
            self.root.title("Полотно")
    
            self.pen_button = Button(self.root, text='Карандаш', command=self.use_pen)
            self.pen_button.grid(row=0, column=1)
    
    
            self.color_button = Button(self.root, text='Цвет', command=self.choose_color)
            self.color_button.grid(row=0, column=2)
    
            self.eraser_button = Button(self.root, text='Стёрка', command=self.use_eraser)
            self.eraser_button.grid(row=0, column=3)
    
            self.choose_size_button = Scale(self.root, from_=1, to=100, orient=HORIZONTAL)
            self.choose_size_button.grid(row=0, column=4)
    
            self.c = Canvas(self.root, bg='white', width=900, height=900)
            self.c.grid(row=1, columnspan=5)
    
            self.setup()
            self.root.mainloop()
    
        def setup(self):
            self.old_x = None
            self.old_y = None
            self.line_width = self.choose_size_button.get()
            self.color = self.DEFAULT_COLOR
            self.eraser_on = False
            self.active_button = self.pen_button
            self.c.bind('<B1-Motion>', self.paint)
            self.c.bind('<ButtonRelease-1>', self.reset)
    
        def use_pen(self):
            self.activate_button(self.pen_button)
    
        def use_brush(self):
            self.activate_button(self.brush_button)
    
        def choose_color(self):
            self.eraser_on = False
            self.color = askcolor(color=self.color)[1]
    
        def use_eraser(self):
            self.activate_button(self.eraser_button, eraser_mode=True)
    
        def activate_button(self, some_button, eraser_mode=False):
            self.active_button.config(relief=RAISED)
            some_button.config(relief=SUNKEN)
            self.active_button = some_button
            self.eraser_on = eraser_mode
    
        def paint(self, event):
            self.line_width = self.choose_size_button.get()
            paint_color = 'white' if self.eraser_on else self.color
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                   width=self.line_width, fill=paint_color,
                                   capstyle=ROUND, smooth=TRUE, splinesteps=36)
            self.old_x = event.x
            self.old_y = event.y
    
        def reset(self, event):
            self.old_x, self.old_y = None, None
    
    
    if __name__ == '__main__':
        Paint()
   
root = Tk()
bttn = Button(root, text='Рисовать', command=click_me)
bttn.pack()

def click_me1():
    print('Hello, World!')
    vibor = word
    def colourswitch(window, colourbutton):
        global colour
        colour = colourbutton["bg"]
        window.destroy()

    def colourselect():
        window = Tk()
        window.title("Select Colour")
        window.grid()

        colourslist = ['snow', 'ghostwhite', 'whitesmoke', 'gainsboro', 'floralwhite', 'oldlace', 'linen', 'antiquewhite', 'papayawhip', 'blanchedalmond', 'bisque', 'peachpuff', 'navajowhite', 'lemonchiffon', 'mintcream', 'azure', 'aliceblue', 'lavender', 'lavenderblush', 'mistyrose', 'darkslategray', 'dimgray', 'slategray', 'lightslategray', 'gray', 'lightgrey', 'midnightblue', 'navy', 'cornflowerblue', 'darkslateblue', 'slateblue', 'mediumslateblue', 'lightslateblue', 'mediumblue', 'royalblue', 'blue', 'dodgerblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'steelblue', 'lightsteelblue', 'lightblue', 'powderblue', 'paleturquoise', 'darkturquoise', 'mediumturquoise', 'turquoise', 'cyan', 'lightcyan', 'cadetblue', 'mediumaquamarine', 'aquamarine', 'darkgreen', 'darkolivegreen', 'darkseagreen', 'seagreen', 'mediumseagreen', 'lightseagreen', 'palegreen', 'springgreen', 'lawngreen', 'mediumspringgreen', 'greenyellow', 'limegreen', 'yellowgreen', 'forestgreen', 'olivedrab', 'darkkhaki', 'khaki', 'palegoldenrod', 'lightgoldenrodyellow', 'lightyellow', 'yellow', 'gold', 'lightgoldenrod', 'goldenrod', 'darkgoldenrod', 'rosybrown', 'indianred', 'saddlebrown', 'sandybrown', 'darksalmon', 'salmon', 'lightsalmon', 'orange', 'darkorange', 'coral', 'lightcoral', 'tomato', 'orangered', 'red', 'hotpink', 'deeppink', 'pink', 'lightpink', 'palevioletred', 'maroon', 'mediumvioletred', 'violetred', 'mediumorchid', 'darkorchid', 'darkviolet', 'blueviolet', 'purple', 'mediumpurple', 'thistle', 'snow2', 'snow3', 'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3', 'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4', 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4', 'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1', 'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2', 'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1', 'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

        colourbutton = list()
        rowvar = 0

        for i in range(len(colourslist)):
            temp = i + 1
            colourbutton.append("")
            colourbutton[i] = Button(window, bg = colourslist[i], height = 1, width = 2, command = lambda i=i: colourswitch(window, colourbutton[i]))
            colourbutton[i].grid(row = rowvar, column = temp - 37 * rowvar)
            if temp % 37 == 0:
                rowvar = rowvar + 1

    def onclick(self):
        global colour
        if self["bg"] == colour:
            self["bg"] = "ghostwhite"
        else:
            self["bg"] = colour

    def Open(root2):
        openwindow = Tk()
        openwindow.title("Open")
        openwindow.grid()

        inputlabel = Label(openwindow, text = "Name of file:").grid(row = 1, column = 1)
        nameinput = Entry(openwindow)
        nameinput.grid(row = 1, column = 2)

        confirmbutton = Button(openwindow, text = "Open", command = lambda: openfile(nameinput, root2, openwindow))
        confirmbutton.grid(row = 2, column = 2)

    def openfile(nameinput, root2, openwindow):
        colourslist = ['snow', 'ghostwhite', 'whitesmoke', 'gainsboro', 'floralwhite', 'oldlace', 'linen', 'antiquewhite', 'papayawhip', 'blanchedalmond', 'bisque', 'peachpuff', 'navajowhite', 'lemonchiffon', 'mintcream', 'azure', 'aliceblue', 'lavender', 'lavenderblush', 'mistyrose', 'darkslategray', 'dimgray', 'slategray', 'lightslategray', 'gray', 'lightgrey', 'midnightblue', 'navy', 'cornflowerblue', 'darkslateblue', 'slateblue', 'mediumslateblue', 'lightslateblue', 'mediumblue', 'royalblue', 'blue', 'dodgerblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'steelblue', 'lightsteelblue', 'lightblue', 'powderblue', 'paleturquoise', 'darkturquoise', 'mediumturquoise', 'turquoise', 'cyan', 'lightcyan', 'cadetblue', 'mediumaquamarine', 'aquamarine', 'darkgreen', 'darkolivegreen', 'darkseagreen', 'seagreen', 'mediumseagreen', 'lightseagreen', 'palegreen', 'springgreen', 'lawngreen', 'mediumspringgreen', 'greenyellow', 'limegreen', 'yellowgreen', 'forestgreen', 'olivedrab', 'darkkhaki', 'khaki', 'palegoldenrod', 'lightgoldenrodyellow', 'lightyellow', 'yellow', 'gold', 'lightgoldenrod', 'goldenrod', 'darkgoldenrod', 'rosybrown', 'indianred', 'saddlebrown', 'sandybrown', 'darksalmon', 'salmon', 'lightsalmon', 'orange', 'darkorange', 'coral', 'lightcoral', 'tomato', 'orangered', 'red', 'hotpink', 'deeppink', 'pink', 'lightpink', 'palevioletred', 'maroon', 'mediumvioletred', 'violetred', 'mediumorchid', 'darkorchid', 'darkviolet', 'blueviolet', 'purple', 'mediumpurple', 'thistle', 'snow2', 'snow3', 'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3', 'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4', 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4', 'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1', 'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2', 'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1', 'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
        try:
            filetoread = open(nameinput.get() + ".txt", "r")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found! Please enter the name of a compatible text file")

        else:
            contents = filetoread.read()
            contents = contents.split()
            filetoread.close()
            verf = "Y"
            if len(contents) >= 2:

                if contents[0].isdigit() and contents[1].isdigit(): #This part of the program verifies that the file is compatible
                    for i in range(len(contents) - 2):

                        if i % 2 == 0:
                            if contents[i + 2].isdigit():
                                pass
                            else:
                                verf = "N"

                        else:
                            inlist = "N"
                            for x in range(len(colourslist)):
                                if contents[i + 2] == colourslist[x]:
                                    inlist = "Y"

                            if inlist == "N":
                                verf = "N"

                else:
                    verf = "N"


            else:
                verf = "N"

            if verf == "N":
                messagebox.showerror("Invalid Format", "File is formatted incorrectly and cannot be opened")

            else:
                newfile = "N"
                height = int(contents[0])
                width = int(contents[1])
                buildgrid(height, width, newfile, contents, openwindow, root2)

    def saveas(buttonslist, height, width):
        savewindow = Tk()
        savewindow.title("Save As")
        savewindow.grid()

        inputlabel = Label(savewindow, text = "Name of new file:").grid(row = 1, column = 1)
        nameinput = Entry(savewindow)
        nameinput.grid(row = 1, column = 2)

        confirmbutton = Button(savewindow, text = "Save as", command = lambda: createfile(buttonslist, nameinput, height, width, savewindow))
        confirmbutton.grid(row = 2, column = 2)

        savewindow.mainloop()

    def createfile(buttonslist, nameinput, height, width, savewindow):
        Clear = open(nameinput.get() + ".txt", "w")
        Clear.close()

        append = open(nameinput.get() + ".txt", "a+")
        append.write(height + " " + width)

        appendarray = list()
        for i in range(len(buttonslist)):
            for x in range(len(buttonslist[i])):
                appendarray.append(buttonslist[i][x]["bg"])

        completed = "N"
        repeated = 1
        finalappendarray = list()
        for i in range(len(appendarray) - 1):
            if appendarray[i] == appendarray[i + 1]:
                repeated = repeated + 1
            else:
                finalappendarray.append(repeated)
                finalappendarray.append(appendarray[i])
                repeated = 1

        finalappendarray.append(repeated)
        finalappendarray.append(appendarray[i + 1])

        for i in range(len(finalappendarray)):
            append.write(" " + str(finalappendarray[i]))

        append.close()
        savewindow.destroy()

    def buildgrid(height, width, newfile, contents, openwindow, root2):
        global colour
        colour = "gray1"

        decompressedcontents = list()

        if newfile == "N":
            for i in range(len(contents) - 2):
                if contents[i + 2].isdigit():
                    for x in range(int(contents[i + 2])):
                       decompressedcontents.append(contents[i + 3])

        root = Tk()
        root.title("Полотно")
        root.grid()

        menu = Menu(root)
        root.config(menu = menu)
        filemenu = Menu(menu) #This part creates the menu
        menu.add_cascade(label = "File", menu = filemenu)

        filemenu.add_command(label = "Open", command = lambda: Open(root))
        filemenu.add_command(label = "New", command = lambda: setup())
        filemenu.add_command(label = "Save As", command = lambda: saveas(buttonslist, height, width))

        buttonslist = list()

        cleanser = Frame(root)

        for i in range(int(height)):
            buttonslist.append([])

            for x in range(int(width)):
                buttonslist[i].append("")
                buttonslist[i][x] = Button(cleanser, bg = "ghostwhite",width = 2, height = 1, command = lambda i=i, x=x: onclick(buttonslist[i][x]))
                if newfile == "N":
                    temp = i * width
                    temp = temp + x

                    buttonslist[i][x]["bg"] = decompressedcontents[temp]
                buttonslist[i][x].grid(row = i, column = x)

        cleanser.grid(row = 1, column = 1)

        placeholderlabel = Label(root, text = "").grid(row = 2)

        ColourButton = Button(root, text = "Выбор цвета", command = lambda: colourselect()).grid(row = 3, column = 1, sticky = "W")

        if newfile == "N":
            openwindow.destroy()

        if root2 != 0:
            root2.destroy()

    def verification(heightentry, widthentry, setupwindow):
        width = widthentry.get()
        height = heightentry.get()
        newfile = "Y"
        openwindow = 0
        root2 = 0
        contents = list()

        if width.isdigit() and height.isdigit():
            if int(width) <= 80 and int(height) <= 35 and int(width) >= 2 and int(height) >= 2:
                setupwindow.destroy()
                buildgrid(height, width, newfile, contents, openwindow, root2)

            else:
                messagebox.showerror("Invalid", "Width must be between 2 and 80 and height must be between 2 and 35")

        else:
            messagebox.showerror("Invalid", "Width and Height must be integers!")


    def setup():
        setupwindow = Tk()
        setupwindow.title("Setup")
        setupwindow.grid()

        menu = Menu(setupwindow)
        setupwindow.config(menu = menu)
        filemenu = Menu(menu) #This part creates the menu
        menu.add_cascade(label = "File", menu = filemenu)

        filemenu.add_command(label = "Open", command = lambda: Open(setupwindow))

        heightlabel = Label(setupwindow, text = "       Высота:       ").grid(row = 1, column = 1)
        heightentry = Entry(setupwindow)
        heightentry.grid(row = 1, column = 2)

        widthlabel = Label(setupwindow, text = "       Ширина:       ").grid(row = 2, column = 1)
        widthentry = Entry(setupwindow)
        widthentry.grid(row = 2, column = 2)

        nextbutton = Button(setupwindow, text = "Continue", command = lambda: verification(heightentry, widthentry, setupwindow)).grid(row = 4, column = 2)

        setupwindow.mainloop()

    if __name__ == "__main__":
        setup()
        quit()


bttn = Button(root, text='ПиксельАрт', command=click_me1)
bttn.pack()

def click_me2():
    print('Hello, World!')
    class Notepad:
    
    	__root = Tk()
    
    	# default window width and height
    	__thisWidth = 300
    	__thisHeight = 300
    	__thisTextArea = Text(__root)
    	__thisMenuBar = Menu(__root)
    	__thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    	__thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    
    	# To add scrollbar
    	__thisScrollBar = Scrollbar(__thisTextArea)	 
    	__file = None
    
    	def __init__(self,**kwargs):
    
    		# Set icon
    		try:
    				self.__root.wm_iconbitmap("Notepad.ico") 
    		except:
    				pass
    
    		# Set window size (the default is 300x300)
    
    		try:
    			self.__thisWidth = kwargs['width']
    		except KeyError:
    			pass
    
    		try:
    			self.__thisHeight = kwargs['height']
    		except KeyError:
    			pass
    
    		# Set the window text
    		self.__root.title("Untitled - Notepad")
    
    		# Center the window
    		screenWidth = self.__root.winfo_screenwidth()
    		screenHeight = self.__root.winfo_screenheight()
    
    		# For left-align
    		left = (screenWidth / 2) - (self.__thisWidth / 2) 
    
    		# For right-align
    		top = (screenHeight / 2) - (self.__thisHeight /2) 
    
    		# For top and bottom
    		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
    											self.__thisHeight,
    											left, top)) 
    
    		# To make the textarea auto resizable
    		self.__root.grid_rowconfigure(0, weight=1)
    		self.__root.grid_columnconfigure(0, weight=1)
    
    		# Add controls (widget)
    		self.__thisTextArea.grid(sticky = N + E + S + W)
    
    		# To open new file
    		self.__thisFileMenu.add_command(label="New",
    										command=self.__newFile) 
    
    		# To open a already existing file
    		self.__thisFileMenu.add_command(label="Open",
    										command=self.__openFile)
    
    		# To save current file
    		self.__thisFileMenu.add_command(label="Save",
    										command=self.__saveFile) 
    
    		# To create a line in the dialog	 
    		self.__thisFileMenu.add_separator()										 
    		self.__thisFileMenu.add_command(label="Exit",
    										command=self.__quitApplication)
    		self.__thisMenuBar.add_cascade(label="File",
    									menu=self.__thisFileMenu)	 
    
    		# To give a feature of cut 
    		self.__thisEditMenu.add_command(label="Cut",
    										command=self.__cut)			 
    
    		# to give a feature of copy 
    		self.__thisEditMenu.add_command(label="Copy",
    										command=self.__copy)		 
    
    		# To give a feature of paste
    		self.__thisEditMenu.add_command(label="Paste",
    										command=self.__paste)		 
    
    		# To give a feature of editing
    		self.__thisMenuBar.add_cascade(label="Edit",
    									menu=self.__thisEditMenu)	 
    

    
    		self.__root.config(menu=self.__thisMenuBar)
    
    		self.__thisScrollBar.pack(side=RIGHT,fill=Y)				 
    
    		# Scrollbar will adjust automatically according to the content	 
    		self.__thisScrollBar.config(command=self.__thisTextArea.yview)	 
    		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
    
    	def __quitApplication(self):
    		self.__root.destroy()
    		# exit()
    
    	def __showAbout(self):
    		showinfo("Notepad","Mrinal Verma")
    
    	def __openFile(self):
    
    		self.__file = askopenfilename(defaultextension=".txt",
    									filetypes=[("All Files","*.*"),
    										("Text Documents","*.txt")])
    
    		if self.__file == "":
    
    			# no file to open
    			self.__file = None
    		else:
    
    			# Try to open the file
    			# set the window title
    			self.__root.title(os.path.basename(self.__file) + " - Notepad")
    			self.__thisTextArea.delete(1.0,END)
    
    			file = open(self.__file,"r")
    
    			self.__thisTextArea.insert(1.0,file.read())
    
    			file.close()
    
    
    	def __newFile(self):
    		self.__root.title("Untitled - Notepad")
    		self.__file = None
    		self.__thisTextArea.delete(1.0,END)
    
    	def __saveFile(self):
    
    		if self.__file == None:
    			# Save as new file
    			self.__file = asksaveasfilename(initialfile='Untitled.txt',
    											defaultextension=".txt",
    											filetypes=[("All Files","*.*"),
    												("Text Documents","*.txt")])
    
    			if self.__file == "":
    				self.__file = None
    			else:
    
    				# Try to save the file
    				file = open(self.__file,"w")
    				file.write(self.__thisTextArea.get(1.0,END))
    				file.close()
    
    				# Change the window title
    				self.__root.title(os.path.basename(self.__file) + " - Notepad")
    
    
    		else:
    			file = open(self.__file,"w")
    			file.write(self.__thisTextArea.get(1.0,END))
    			file.close()
    
    	def __cut(self):
    		self.__thisTextArea.event_generate("<<Cut>>")
    
    	def __copy(self):
    		self.__thisTextArea.event_generate("<<Copy>>")
    
    	def __paste(self):
    		self.__thisTextArea.event_generate("<<Paste>>")
    
    	def run(self):
    
    		# Run main application
    		self.__root.mainloop()
    
    
    
    
    # Run main application
    notepad = Notepad(width=600,height=400)
    notepad.run()

    

bttn = Button(root, text='Текстовый редактор', command=click_me2)
bttn.pack()



def click_me3():
    gameOver = False
    score = 0
    squaresToClear = 0
    def play_bombdodger():
        create_bombfield(bombfield)
        window = tkinter.Tk()
        layout_window(window)
        window.mainloop()
    bombfield = []
    def create_bombfield(bombfield):
        global squaresToClear
        for row in range(0,10):
            rowList = []
            for column in range(0,10):
                if random.randint(1,100) < 20:
                    rowList.append(1)
                else:
                    rowList.append(0)
                    squsresToClear = squaresToClear + 1
            bombfield.append(rowList)
        #printfield(bombfield)
    def printfield(bombfiled):
        for rowList in bombfiled:
            print(rowList)
    def layout_window(window):
        for rowNumber, rowList in enumerate(bombfield):
            for columnNumber, columnEntry in enumerate(rowList):
                if random.randint(1,100) < 25:
                    square = tkinter.Label(window, text = "    ", bg = "darkgreen")
                elif random.randint(1,100) > 75:
                    square = tkinter.Label(window, text = "    ", bg = "seagreen")
                else:
                    square = tkinter.Label(window, text = "    ", bg = "green")
                square.grid(row = rowNumber, column = columnNumber)
                square.bind("<Button-1>", on_click)
                square.bind("<Button-3>", on_click3)
    
    def on_click3(event):
        square = event.widget
        square.config(bg = "blue")
    
    
    def on_click(event):
        global score
        global gameOver
        global squaresToClear
        square = event.widget
        row = int(square.grid_info()["row"])
        column = int(square.grid_info()["column"])
        currentText = square.cget("text")
        if gameOver == False:
            if bombfield[row][column] == 1:
                gameOver = True
                square.config(bg = "red")
                print("Game Over! You hit a bomb!")
                print("you score was:", score)
            elif currentText == "    ":
                square.config(bg = "brown")
                totalBombs = 0
                if row < 9:
                    if bombfield[row+1][column] == 1:
                        totalBombs = totalBombs + 1
                if row > 0:
                    if bombfield[row-1][column] == 1:
                        totalBombs = totalBombs + 1
                if column > 0:
                    if bombfield[row][column-1] == 1:
                        totalBombs = totalBombs + 1
                if column < 9:
                    if bombfield[row][column+1] == 1:
                        totalBombs = totalBombs + 1
                if row > 0 and column > 0:
                    if bombfield[row-1][column-1] == 1:
                        totalBombs = totalBombs + 1
                if row < 9 and column > 0:
                    if bombfield[row+1][column-1] == 1:
                        totalBombs = totalBombs + 1
                if row > 0 and column < 9:
                    if bombfield[row-1][column+1] == 1:
                        totalBombs = totalBombs + 1
                if row < 9 and column < 9:
                    if bombfield[row+1][column+1] == 1:
                        totalBombs = totalBombs + 1
                square.config(text = " " + str(totalBombs) + " ")
                squaresToClear = squaresToClear - 1
                score = score + 1
                if squaresToClear == 0:
                    gameOver = True
                    print("You win!")
    play_bombdodger()  
    

bttn = Button(root, text='Сапёр', command=click_me3)
bttn.pack()


def click_me4():
    
    
    def btn_click(item):
        global expression
        try:
            input_field['state'] = "normal"
            expression += item
            input_field.insert(END, item)
    
            if item == '=':
                result = str(eval(expression[:-1]))
                input_field.insert(END, result)
                expression = ""
    
            input_field['state'] = "readonly"
        except ZeroDivisionError:
            input_field.delete(0, END)
            input_field.insert(0, 'Ошибка (деление на 0)')
        except SyntaxError:
            input_field.delete(0, END)
            input_field.insert(0, 'Ошибка')
    
    
    def bt_clear():
        global expression
        expression = ""
        input_field['state'] = "normal"
        input_field.delete(0, END)
        input_field['state'] = "readonly"
    
    
    root = Tk()
    root.geometry("268x288")
    root.title("Калькулятор")
    root.resizable(0, 0)
    
    frame_input = Frame(root)
    frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")
    
    input_field = Entry(frame_input, font='Arial 15 bold', width=24, state="readonly")
    input_field.pack(fill=BOTH)
    
    buttons = (('7', '8', '9', '/', '4'),
               ('4', '5', '6', '*', '4'),
               ('1', '2', '3', '-', '4'),
               ('0', '.', '=', '+', '4')
               )
    
    expression = ""
    
    button = Button(root, text='C', command=lambda: bt_clear())
    button.grid(row=1, column=3, sticky="nsew")
    
    for row in range(4):
        for col in range(4):
            Button(root, width=2, height=3, text=buttons[row][col],
                   command=lambda row=row, col=col: btn_click(buttons[row][col])).grid(row=row + 2, column=col, sticky="nsew", padx=1, pady=1)
    
    root.mainloop()
        
bttn = Button(root, text='Калькулятор', command=click_me4)
bttn.pack()

def click_me5():
    root = tkinter.Tk()
    


    root.geometry("750x500")
    canvas5 = Canvas(root, width = canvasWidth, 
        			height = canvasHeight, bg ="deepskyblue" ) 

    canvas5.pack() 

# Display image 

    bat = canvas5.create_rectangle(0, 0, 40, 10, fill="dark turquoise")
    ball = canvas5.create_oval(0, 0, 10, 10, fill="red")
    windowOpen = True
    
    def main_loop():
        while windowOpen == True:
            move_bat()
            move_ball()
            root.update()
            time.sleep(0.0005)
            if windowOpen == True:
                check_game_over()

    def on_key_press(event):
        global leftPress, rightPress
        if event.keysym == "Left":
            leftPress = 1
        elif event.keysym == "Right":
            rightPress = 1
    
    def on_key_release(event):
        global leftPress, rightPress
        if event.keysym == "Left":
            leftPress = 0
        elif event.keysym == "Right":
            rightPress = 0
    
    batSpeed = 6
    def move_bat():
        batMove = batSpeed*rightPress - batSpeed*leftPress
        (batLeft, batTop, batRight, batBottom) = canvas5.coords(bat)
        if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
            canvas5.move(bat, batMove, 0)
    
    ballMoveX = 4
    ballMoveY = -4
    setBatTop = canvasHeight-40
    setBatBottom = canvasHeight-30
    def move_ball():
        global ballMoveX, ballMoveY
        (ballLeft, ballTop, ballRight, ballBottom) = canvas5.coords(ball)
        if ballMoveX > 0 and ballRight > canvasWidth:
            ballMoveX = -ballMoveX
        if ballMoveX < 0 and ballLeft < 0:
            ballMoveX = -ballMoveX
        if ballMoveY < 0 and ballTop < 0:
            ballMoveY = - ballMoveY
        if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
            (batLeft, batTop, batRight, batBottom) = canvas5.coords(bat)
            if ballRight > batLeft and ballLeft < batRight:
                ballMoveY = -ballMoveY
        canvas5.move(ball, ballMoveX, ballMoveY)
    def check_game_over():
        (ballLeft, ballTop, ballRight, ballBottom) = canvas5.coords(ball)
        if ballTop > canvasHeight:
            playAgain = messagebox.askyesno('Играть', 'Играть снова?')
            if playAgain == True:
                reset()
            else:
                close()
    
    def close():
        global windowOpen
        windowOpen = False
        root.destroy()
    def reset():
        global leftPress, rightPress
        global ballMoveX, ballMoveY
        leftPress = 0
        rightPress = 0
        ballMoveX = 4
        ballMoveY = -4
        canvas5.coords(bat, 10, setBatTop, 50, setBatBottom)
        canvas5.coords(ball, 20, setBatTop-10, 30, setBatTop)
    
    root.protocol("WM_DELETE_WINDOW" , close)
    root.bind("<KeyPress>", on_key_press)
    root.bind("<KeyRelease>", on_key_release)
    
    reset()
    main_loop()
  
bttn = Button(root, text='Ракетка', command=click_me5)
bttn.pack()

def click_me6():
    window6 = tkinter.Tk()
    window6.title("Счётчик")
    
    label = tkinter.Label(window6, width = 8, height = 0, font= "size 80", text = clicks, bg = "aquamarine2")
    label.pack()
    def on_click():
        global clicks
        clicks = clicks + 1
        label.configure(text = clicks)
    def on_UNclick():
        global clicks
        clicks = clicks - 1
        label.configure(text = clicks)



    button = tkinter.Button(window6, font= "size 25", text = "  +  ", width=26, command = on_click, bg = "cyan3")
    button.pack()
    button1 = tkinter.Button(window6, font= "size 25", text = "  -  ", width=26, command = on_UNclick, bg = "cyan3")
    button1.pack()

    window6.mainloop()
    
bttn = Button(root, text='Счётчик', command=click_me6)
bttn.pack()

def click_me7():


    def tick_1():
        global temp_1, after_id_1
        after_id_1 = root.after(1000, tick_1)
        f_temp_1 = time.strftime("%H:%M:%S", time.gmtime(temp_1))
        label_1.configure(text=str(f_temp_1))
        temp_1 += 1
    def start_tick_1():
        btn_start_1.pack_forget() #Кнопка Start_1 исчезает
        tick_1() #Таймер_1 запускается
    def stop_tick_1():
        btn_stop_1.pack_forget() #Кнопка Stop_1 исчезает
        root.after_cancel(after_id_1) #Таймер_1 останавливается
    def continue_tick_1():
        root.mainloop()
        
    def ct():
        label_1.configure(text='00:00:00')
    root = Tk()
    root.title("Секмер")
    root.geometry('200x100')
    btn_start_1 = Button(root, text="Старт/продолжить", command=start_tick_1)
    btn_start_1.place(x=20, y=20)
    btn_stop_1 = Button(root, text="Стоп", command=stop_tick_1)
    btn_stop_1.place(x=20, y=50)  # Кнопка Stop_1 появляется

    
    label_1 = Label(root, text='00:00:00')
    label_1.place(x=140, y=30)
    root.mainloop()
bttn = Button(root, text='Секундомер', command=click_me7)
bttn.pack()    


def click_me7():
    root = Tk()
    
    # setting geometry of tk window
    root.geometry("300x250")
    
    # Using title() to display a message in
    # the dialogue box of the message in the
    # title bar.
    root.title("Таймер")
    
    # Declaration of variables
    hour=StringVar()
    minute=StringVar()
    second=StringVar()
    
    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")
    
    # Use of Entry class to take input from the user
    hourEntry= Entry(root, width=3, font=("Arial",18,""),
    				textvariable=hour)
    hourEntry.place(x=80,y=20)
    
    minuteEntry= Entry(root, width=3, font=("Arial",18,""),
    				textvariable=minute)
    minuteEntry.place(x=130,y=20)
    
    secondEntry= Entry(root, width=3, font=("Arial",18,""),
    				textvariable=second)
    secondEntry.place(x=180,y=20)
    
    
    def submit():
    	try:
    		# the input provided by the user is
    		# stored in here :temp
    		temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    	except:
    		print("Please input the right value")
    	while temp >-1:
    
    		# divmod(firstvalue = temp//60, secondvalue = temp%60)
    		mins,secs = divmod(temp,60) 
    
    		# Converting the input entered in mins or secs to hours,
    		# mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
    		# 50min: 0sec)
    		hours=0
    		if mins >60:
    
    			# divmod(firstvalue = temp//60, secondvalue 
    			# = temp%60)
    			hours, mins = divmod(mins, 60)
    
    		# using format () method to store the value up to 
    		# two decimal places
    		hour.set("{0:2d}".format(hours))
    		minute.set("{0:2d}".format(mins))
    		second.set("{0:2d}".format(secs))
    
    		# updating the GUI window after decrementing the
    		# temp value every time
    		root.update()
    		time.sleep(1)
    
    		# when temp value = 0; then a messagebox pop's up
    		# with a message:"Time's up"
    		if (temp == 0):
    			messagebox.showinfo("Время", "Есть пробитие!")
    
    		# after every one sec the value of temp will be decremented
    		# by one
    		temp -= 1
    
    # button widget
    btn = Button(root, text='Задать время', bd='5',
    			command= submit)
    btn.place(x = 70,y = 120)
    
    # infinite loop which is required to
    # run tkinter program infinitely
    # until an interrupt occurs
    root.mainloop()
bttn = Button(root, text='Таймер(В разработке)', command=click_me7)
bttn.pack()

root.mainloop()
    

