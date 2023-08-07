"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

# Global variable
ball_is_released = False
count = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, y=paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-self.paddle.y)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(width=self.ball_radius*2, height=self.ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Draw bricks
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick = GRect(width=self.brick_width, height=self.brick_height)
        self.draw_brick()  # Draw a brick array
        self.brick_total = self.brick_rows * self.brick_cols  # A number of total bricks

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Score board
        self.__score = 0
        self.score_label = GLabel(f'Score: {self.__score}')
        self.score_label.font = '-15'
        self.window.add(self.score_label, x=5, y=self.window.height-self.score_label.height)

        # Winner board
        self.win = GLabel('YOU WIN!')
        self.win.font = '-30'

        # End board
        self.end = GLabel('GAME OVER!')
        self.end.font = '-30'

        # Initialize our mouse listeners
        onmouseclicked(self.click)  # It serves a ball
        onmousemoved(self.reset_paddle)  # It tracks a paddle moving.

    def draw_brick(self):
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                self.brick = GRect(width=self.brick_width, height=self.brick_height)
                self.brick.filled = True
                if i < 2:
                    self.brick.fill_color = 'red'
                if 2 <= i < 4:
                    self.brick.fill_color = 'orange'
                if 4 <= i < 6:
                    self.brick.fill_color = 'yellow'
                if 6 <= i < 8:
                    self.brick.fill_color = 'green'
                if 8 <= i < 10:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=0 + (self.brick.width+self.brick_spacing) * j,
                                y=self.brick_offset + (self.brick.height+self.brick_spacing) * i)

    def reset_paddle(self, event):
        if 0 <= event.x < self.window.width-self.paddle.width:
            self.paddle.x = event.x
        elif 0 > event.x:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window.width-self.paddle.width

    def click(self, event):
        obj = self.window.get_object_at(event.x, event.y)
        if obj == self.ball:
            self.ball_velocity()

    def ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Getter is for user to take a private variable.
    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    # Setter is for user to pass a private variable back to "class", which needs to manipulate in "class".
    def set_vx(self, vx):
        self.__dx = vx

    def set_vy(self, vy):
        self.__dy = vy

    def check_for_border(self):
        if 0 >= self.ball.x or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if 0 >= self.ball.y:
            self.__dy = -self.__dy

    def out_of_border(self):
        is_out_of_border = self.ball.y + self.ball.height >= self.window.height
        return is_out_of_border

    def check_for_collision(self):
        ball_left_top = self.window.get_object_at(x=self.ball.x, y=self.ball.y)
        ball_right_top = self.window.get_object_at(x=self.ball.x+2*self.ball_radius, y=self.ball.y)
        ball_left_down = self.window.get_object_at(x=self.ball.x, y=self.ball.y + 2 * self.ball_radius)
        ball_right_down = self.window.get_object_at(x=self.ball.x+2*self.ball_radius, y=self.ball.y+2*self.ball_radius)

        if self.brick_total == 0:
            self.reset_ball()
            self.window.add(self.win, x=(self.window.width-self.win.width)/2,
                            y=(self.window.height-self.win.height)/2)

        if ball_left_top is not None:
            if ball_left_top == self.paddle:
                if self.__dy > 0:
                    self.__dy = -self.__dy
            for i in range(self.brick_rows):
                for j in range(self.brick_cols):
                    self.brick = GRect(width=self.brick_width, height=self.brick_height,
                                       x=0 + (self.brick.width + self.brick_spacing) * j,
                                       y=self.brick_offset + (self.brick.height + self.brick_spacing) * i)
                    maybe_brick = self.window.get_object_at(self.brick.x, self.brick.y)
                    if ball_left_top == maybe_brick:
                        self.__dy = -self.__dy
                        self.brick_total -= 1
                        self.__score += 1
                        self.score_label.text = f'Score: {self.__score}'
                        self.window.remove(maybe_brick)
        elif ball_right_top is not None:
            if ball_right_top == self.paddle:
                if self.__dy > 0:
                    self.__dy = -self.__dy
            for i in range(self.brick_rows):
                for j in range(self.brick_cols):
                    self.brick = GRect(width=self.brick_width, height=self.brick_height,
                                       x=0 + (self.brick.width + self.brick_spacing) * j,
                                       y=self.brick_offset + (self.brick.height + self.brick_spacing) * i)
                    maybe_brick = self.window.get_object_at(self.brick.x, self.brick.y)
                    if ball_right_top == maybe_brick:
                        self.__dy = -self.__dy
                        self.brick_total -= 1
                        self.__score += 1
                        self.score_label.text = f'Score: {self.__score}'
                        self.window.remove(maybe_brick)
        elif ball_left_down is not None:
            if ball_left_down == self.paddle:
                if self.__dy > 0:
                    self.__dy = -self.__dy
            for i in range(self.brick_rows):
                for j in range(self.brick_cols):
                    self.brick = GRect(width=self.brick_width, height=self.brick_height,
                                       x=0 + (self.brick.width + self.brick_spacing) * j,
                                       y=self.brick_offset + (self.brick.height + self.brick_spacing) * i)
                    maybe_brick = self.window.get_object_at(self.brick.x, self.brick.y)
                    if ball_left_down == maybe_brick:
                        self.__dy = -self.__dy
                        self.brick_total -= 1
                        self.__score += 1
                        self.score_label.text = f'Score: {self.__score}'
                        self.window.remove(maybe_brick)
        elif ball_right_down is not None:
            if ball_right_down == self.paddle:
                if self.__dy > 0:
                    self.__dy = -self.__dy
            for i in range(self.brick_rows):
                for j in range(self.brick_cols):
                    self.brick = GRect(width=self.brick_width, height=self.brick_height,
                                       x=0 + (self.brick.width + self.brick_spacing) * j,
                                       y=self.brick_offset + (self.brick.height + self.brick_spacing) * i)
                    maybe_brick = self.window.get_object_at(self.brick.x, self.brick.y)
                    if ball_right_down == maybe_brick:
                        self.__dy = -self.__dy
                        self.brick_total -= 1
                        self.__score += 1
                        self.score_label.text = f'Score: {self.__score}'
                        self.window.remove(maybe_brick)
        else:
            self.__dx = self.__dx
            self.__dy = self.__dy

    def reset_ball(self):
        self.set_ball_position()
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball)

    def game_end(self):
        self.reset_ball()
        self.window.add(self.end, x=(self.window.width-self.end.width)/2,
                        y=(self.window.height-self.end.height)/2)

    def set_ball_position(self):
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2

    # def get_ball_is_released(self):
    #     global ball_is_released
    #     return ball_is_released

    # def brick_y_position(self):
    #     for i in range(self.brick_rows):
    #         y = self.brick_offset + (self.brick.height + self.brick_spacing) * i
    #         return y
    #
    # def brick_x_position(self):
    #     for j in range(self.brick_cols):
    #         x = 0 + (self.brick.width + self.brick_spacing) * j
    #         return x
    #
    # def brick_position(self):
    #     for i in range(self.brick_rows):
    #         y = self.brick_offset + (self.brick.height + self.brick_spacing) * i
    #         for j in range(self.brick_cols):
    #             x = 0 + (self.brick.width + self.brick_spacing) * j
    #             brick_target = GRect(width=self.brick_width, height=self.brick_height, x=x, y=y)
    #             return brick_target











