"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    # global ball_is_released
    # ball_is_released = graphics.get_ball_is_released()
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        if graphics.out_of_border():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                graphics.game_end()
                break
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        graphics.ball.move(vx, vy)
        vx = graphics.set_vx(vx)
        vy = graphics.set_vy(vy)
        graphics.check_for_border()
        graphics.check_for_collision()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
