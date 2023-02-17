import turtle
tao = turtle.Pen()
tao.shape('turtle')

def draw_hexagon():
   
    for i in range(150):
        tao.forward(150-i)#ลดขนาดลงทีละ1เพื่อให้มันเล็กลง
        tao.right(45)#มาจากมุม360/8

draw_hexagon()
