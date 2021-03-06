from tkinter import *
from math import cos, sin, radians

# Dots
width_of_board = 1200
height_of_board = 800
number_of_dots = 6
#symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
dot_color = '#7BC043'
player1_color = '#0492CF'
player1_color_light = '#67B0CF'
player2_color = '#EE4035'
player2_color_light = '#EE7E77'
Green_color = '#7BC043'
#dot_width = 0.25*size_of_board/number_of_dots
#edge_width = 0.1*size_of_board/number_of_dots
#distance_between_dots = size_of_board / (number_of_dots)

# Catan
number_of_board_spaces = 19
max_vertices_in_straight_line = 11
diameter_of_board = 5
distance_between_dots = min(width_of_board,height_of_board) / (max_vertices_in_straight_line)


class Dots_and_Boxes():


    def __init__(self):
        print("Start")
        self.window = Tk()
        self.window.title('Settlers of Catan')
        self.canvas = Canvas(self.window, width=width_of_board, height=height_of_board)
        self.canvas.pack()
        self.window.bind('<Button-1>', self.click)
        self.player1_starts = True
        self.length = 80
        self.x = (width_of_board/2) - (self.length/2)
        self.y = (height_of_board/2) - (self.length/2)
        self.color = "#eeeeee"
        self.draw_hexagon()

    def mainloop(self):
        self.window.mainloop()

    def refresh_board(self):
        for i in range(number_of_dots):
            x = i*distance_between_dots+distance_between_dots/2
            self.canvas.create_line(x, distance_between_dots/2, x,
                                    size_of_board-distance_between_dots/2,
                                    fill='gray', dash = (2, 2))
            self.canvas.create_line(distance_between_dots/2, x,
                                    size_of_board-distance_between_dots/2, x,
                                    fill='gray', dash=(2, 2))

        for i in range(number_of_dots):
            for j in range(number_of_dots):
                start_x = i*distance_between_dots+distance_between_dots/2
                end_x = j*distance_between_dots+distance_between_dots/2
                self.canvas.create_oval(start_x-dot_width/2, end_x-dot_width/2, start_x+dot_width/2,
                                        end_x+dot_width/2, fill=dot_color,
                                        outline=dot_color)

    def draw_hexagon(self):
        start_x = self.x
        start_y = self.y
        angle = 60
        coords = []
        for i in range(6):
            end_x = start_x + self.length * cos(radians(angle * i))
            end_y = start_y + self.length * sin(radians(angle * i))
            coords.append([start_x, start_y])
            start_x = end_x
            start_y = end_y

        self.canvas.create_polygon(coords,fill=self.color,outline="gray")

    def click(self, event):
        if not self.reset_board:
            grid_position = [event.x, event.y]
            logical_positon, valid_input = self.convert_grid_to_logical_position(grid_position)
            if valid_input and not self.is_grid_occupied(logical_positon, valid_input):
                self.update_board(valid_input, logical_positon)
                self.make_edge(valid_input, logical_positon)
                self.mark_box()
                self.refresh_board()
                self.player1_turn = not self.player1_turn

                if self.is_gameover():
                    # self.canvas.delete("all")
                    self.display_gameover()
                else:
                    self.display_turn_text()
        else:
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False




game_instance = Dots_and_Boxes()
game_instance.mainloop()
