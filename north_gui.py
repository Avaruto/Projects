from star_pos import star_pos
import turtle
import random
import tkinter

class North:
    def __init__(self, window):
        self.window = window
        
        self.canvas = tkinter.Canvas(window, width = 1700, height = 1000, bg = '#2a408c')

        self.colors = ['#3d53a1','white','#4ad2ed',
                  '#4aa9ed','#e0d9b8','#f0dd86','#6499de','#f7e5e4','#e8e4f7',
                  '#415d82','#1e2b3d','#1d3d69','#36a4ff','#7293ad',
                  '#7b97d4','#4572d6','#5451a8','#eeedf2']
                
        self.num_turtles = 211
        self.stars = []
        self.iterations = 360
        self.extent = 90
        
        # Buttons
        self.play = tkinter.Button(window, text = "Play", command = self.animate, width = 12, height= 2).place(x=0, y=0) 
        self.c = tkinter.Button(window, text = "Clear", command = self.clear, width = 12, height = 2).place(x=0, y=50)
        self.q = tkinter.Button(window, text = "Quit", command = root.destroy, width = 12, height = 2).place(x=0, y=100)      
        self.e = tkinter.Entry(root, width = 12)
        self.e.insert(0, "Enter [1,0,10]")# Gives default value
        # Packs entry
        self.e.place(x=0, y = 250)

        self.canvas.pack()
        
    def radius(self, x1, x2, y1, y2):
        return (round((x2-x1)**2))
            
    def animate(self):
        turtle_screen = turtle.TurtleScreen(self.canvas)
        turtle_screen.bgcolor("#2a408c")

        self.canvas.pack()

        for i in range(0, self.num_turtles):
            DEC = star_pos[i][0]
            RA = star_pos[i][1]*2.5
            
            pen = turtle.RawTurtle(turtle_screen)
            self.canvas.pack()
            pen.hideturtle()
            
            pen.speed(int(self.e.get()))
            pen.pensize(2)
            pen.up()
            
            pen.forward(abs(RA-2.31)*16)
            pen.pendown()
            
            pen.left(90)
            pen.color(random.choice(self.colors))
            pen.circle(((self.radius(RA, 2.31, DEC, 89))*2), self.extent)
            self.stars.append(pen)
        
        for x in range(0, 4):    
            for i in range(0, self.num_turtles):
                DEC = star_pos[i][0]
                RA = star_pos[i][1]*2.5
                self.stars[i].circle(((self.radius(RA, 2.31, DEC, 89))*2), self.extent)
    
    def clear(self):
        self.canvas.delete('all')
        del self.stars
        
    
if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("North Star Timelapse")
    root.state('zoomed')
    app = North(root)
    root.mainloop()
