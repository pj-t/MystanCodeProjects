"""
File: my_drawing.py
Name: Baron
----------------------
The file uses campy to learn how a class makes an object and can be used as drawing
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant
SIZE = 13

# Global variable
window = GWindow(width=700, height=400)
oval = GOval(SIZE, SIZE)


def main():
    """
    Title: Good Times

    There are two tigers-one without a tail, and the other without a ear.
    Although life is a struggle, it is always a good time to accompany each other at the end of the day.
    """
    # Tell a coordinate.
    onmouseclicked(coordinate)
    oval.filled = True
    oval.fill_color = 'dimgray'
    oval.color = 'black'

    # Background
    sky = GRect(700, 200)
    sky.filled = True
    sky.fill_color = 'coral'
    sky.color = 'coral'
    window.add(sky)

    ground = GRect(700, 200, y=200)
    ground.filled = True
    ground.fill_color = 'darkred'
    window.add(ground)

    border = GOval(750, 200, x=-10, y=100)
    border.filled = True
    border.fill_color = 'coral'
    border.color = 'coral'
    window.add(border)

    sun_o = GOval(220, 220, x=200, y=80)
    sun_o.filled = True
    sun_o.fill_color = 'orangered'
    sun_o.color = 'coral'
    window.add(sun_o)

    sun = GOval(140, 140, x=240, y=100)
    sun.filled = True
    sun.fill_color = 'tomato'
    sun.color = 'orangered'
    window.add(sun)

    # t = tiger
    t_face = GOval(180, 140, x=90, y=60)
    t_face.filled = True
    t_face.fill_color = 'gold'
    t_face.color = 'gold'
    window.add(t_face)

    t_ear_l = GPolygon()
    t_ear_l.add_vertex((104, 50))
    t_ear_l.add_vertex((106, 117))
    t_ear_l.add_vertex((149, 73))
    t_ear_l.filled = True
    t_ear_l.fill_color = 'gold'
    t_ear_l.color = 'gold'
    window.add(t_ear_l)

    t_ear_r = GPolygon()
    t_ear_r.add_vertex((236, 50))
    t_ear_r.add_vertex((198, 73))
    t_ear_r.add_vertex((250, 117))
    t_ear_r.filled = True
    t_ear_r.fill_color = 'gold'
    t_ear_r.color = 'gold'
    window.add(t_ear_r)

    t_body = GOval(250, 180, x=80, y=160)
    t_body.filled = True
    t_body.fill_color = 'gold'
    t_body.color = 'gold'
    window.add(t_body)

    line_1 = GRect(130, 5, x=120, y=106)
    line_1.filled = True
    line_1.fill_color = 'saddlebrown'
    line_1.color = 'saddlebrown'
    line_2 = GRect(130, 5, x=120, y=126)
    line_2.filled = True
    line_2.fill_color = 'saddlebrown'
    line_2.color = 'saddlebrown'
    line_3 = GRect(130, 5, x=120, y=146)
    line_3.filled = True
    line_3.fill_color = 'saddlebrown'
    line_3.color = 'saddlebrown'
    line_4 = GRect(5, 40, x=180, y=110)
    line_4.filled = True
    line_4.fill_color = 'saddlebrown'
    line_4.color = 'saddlebrown'
    window.add(line_1)
    window.add(line_2)
    window.add(line_3)
    window.add(line_4)

    no_tail = GOval(50, 50, x=190, y=280)
    no_tail.filled = True
    no_tail.fill_color = 'lightyellow'
    no_tail.color = 'gold'
    window.add(no_tail)

    left_foot = GOval(100, 50, x=75, y=280)
    left_foot.filled = True
    left_foot.fill_color = 'gold'
    left_foot.color = 'gold'
    right_foot = GOval(80, 40, x=255, y=270)
    right_foot.filled= True
    right_foot.fill_color = 'gold'
    right_foot.color = 'gold'
    window.add(left_foot)
    window.add(right_foot)

    # t2 for tiger2
    t2_face = GOval(162, 126, x=300, y=100)
    t2_face.filled = True
    t2_face.fill_color = 'peru'
    t2_face.color = 'peru'
    window.add(t2_face)

    t_ear_r2 = GPolygon()
    t_ear_r2.add_vertex((408, 106))
    t_ear_r2.add_vertex((430, 92))
    t_ear_r2.add_vertex((429, 113))
    t_ear_r2.filled = True
    t_ear_r2.fill_color = 'peru'
    t_ear_r2.color = 'peru'
    window.add(t_ear_r2)

    t2_body = GOval(225, 162, x=310, y=190)
    t2_body.filled = True
    t2_body.fill_color = 'peru'
    t2_body.color = 'peru'
    window.add(t2_body)

    tail = GOval(100, 15, x=450, y=330)
    tail.filled = True
    tail.fill_color = 'peru'
    tail.color = 'peru'
    window.add(tail)

    left_foot2 = GOval(100, 50, x=290, y=300)
    left_foot2.filled = True
    left_foot2.fill_color = 'peru'
    left_foot2.color = 'peru'
    window.add(left_foot2)

    dot = GOval(35, 18, x=320, y=320)
    dot.filled = True
    dot.fill_color = 'saddlebrown'
    dot.color = 'saddlebrown'
    window.add(dot)

    dot = GOval(40, 40, x=440, y=225)
    dot.filled = True
    dot.fill_color = 'saddlebrown'
    dot.color = 'saddlebrown'
    window.add(dot)

    dot = GOval(50, 50, x=420, y=230)
    dot.filled = True
    dot.fill_color = 'saddlebrown'
    dot.color = 'saddlebrown'
    window.add(dot)

    dot = GOval(20, 20, x=320, y=180)
    dot.filled = True
    dot.fill_color = 'saddlebrown'
    dot.color = 'saddlebrown'
    window.add(dot)

    dot = GOval(20, 45, x=320, y=120)
    dot.filled = True
    dot.fill_color = 'saddlebrown'
    dot.color = 'saddlebrown'
    window.add(dot)

    hat = GRect(80, 15, x=330, y=100)
    hat.filled = True
    hat.fill_color = 'darkmagenta'
    hat.color = 'darkmagenta'
    hat2 = GRect(60, 30, x=340, y=70)
    hat2.filled = True
    hat2.fill_color = 'darkmagenta'
    hat2.color = 'darkmagenta'
    hat3 = GRect(60, 12, x=340, y=102)
    hat3.filled = True
    hat3.fill_color = 'magenta'
    hat3.color = 'magenta'
    window.add(hat)
    window.add(hat2)
    window.add(hat3)

    talk = GOval(180, 90, x=505, y=60)
    talk.filled = True
    talk.fill_color = 'white'
    talk.color = 'black'
    window.add(talk)

    talk = GOval(40, 20, x=478, y=133)
    talk.filled = True
    talk.fill_color = 'white'
    talk.color = 'black'
    window.add(talk)

    talk = GOval(20, 10, x=466, y=160)
    talk.filled = True
    talk.fill_color = 'white'
    talk.color = 'black'
    window.add(talk)

    label = GLabel('Bonsoir !')
    label.font = 'Gotham-40'
    label.color = 'midnightblue'
    window.add(label, x=525, y=130)


def coordinate(point):
    oval.x = point.x - oval.width/2
    oval.y = point.y - oval.height/2
    print(oval.x, oval.y)
    window.add(oval)


if __name__ == '__main__':
    main()
