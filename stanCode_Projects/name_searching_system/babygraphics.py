"""
File: babygraphics.py
Name: Baron
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    width = CANVAS_WIDTH
    year = YEARS[year_index-1]
    length = 20 + 80 * year_index
    return length


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for x in range(len(YEARS)):
        x_width = get_x_coordinate(CANVAS_WIDTH, x)
        canvas.create_line(x_width, 0, x_width, CANVAS_HEIGHT)
        canvas.create_text(x_width+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[x], anchor=tkinter.NW, fill='dimgrey', font="arial 18")


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # color_index = -1
    label = []
    label_lst = []
    dic_lookup_name = {}
    for i in range(len(lookup_names)):
        color_index = i
        dic_lookup_name[lookup_names[i]] = i
    for name in name_data:
        if name in lookup_names:  # Fix four line colors and the others are all blue.
            color_index = dic_lookup_name[name]
            if color_index % 4 == 0:
                color_index = 0
            elif color_index % 4 == 1:
                color_index = 1
            elif color_index % 4 == 2:
                color_index = 2
            elif color_index % 4 == 3:
                color_index = 3
            # color_index += 1  # To change line colors in a cycle, but the order are decided by ranking of name.
            # if color_index == 4:
            #     color_index = 0
            color = COLORS[color_index]
            for x in range(len(YEARS) - 1):  # Line x-coordinate of one and the next year.
                x_width = get_x_coordinate(CANVAS_WIDTH, x)
                x_width_next = get_x_coordinate(CANVAS_WIDTH, x + 1)
                x_year = YEARS[x]
                x_year_next = YEARS[x + 1]
                label.append(name)
                if str(x_year) in name_data[name]:  # Line y-coordinate of one and the next year based on name's rank.
                    rk1 = name_data[str(name)][str(x_year)]
                    y1 = int(rk1) * 560/1000
                    label.append(rk1)
                else:
                    y1 = 1000 * 560/1000
                    label[0] = name+"*"
                if str(x_year_next) in name_data[name]:
                    rk2 = name_data[str(name)][str(x_year_next)]
                    y2 = int(rk2) * 560/1000
                    if x == len(YEARS) - 2:
                        label_lst.append(name)
                        label_lst.append(rk2)
                else:
                    y2 = 1000 * 560/1000
                    if x == len(YEARS) - 2:
                        label_lst.append(name+"*")

                # Draw a figure by creating lines and texts
                canvas.create_line(x_width, GRAPH_MARGIN_SIZE+y1, x_width_next, GRAPH_MARGIN_SIZE+y2, width=LINE_WIDTH, fill=color)
                if x == len(YEARS) - 2:
                    canvas.create_text(x_width_next+TEXT_DX, GRAPH_MARGIN_SIZE+y2, text=label_lst, anchor=tkinter.SW, fill=color, font="georgia 12")
                    label_lst.clear()
                canvas.create_text(x_width + TEXT_DX, GRAPH_MARGIN_SIZE + y1, text=label, anchor=tkinter.SW,fill=color, font="georgia 12")
                label.clear()


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
