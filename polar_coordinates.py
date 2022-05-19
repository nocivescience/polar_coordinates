from manim import *
class PolarCoordinatesScene(MovingCameraScene):
    CONFIG={
        'x_color':YELLOW,
        'y_color':RED,
        'r_color':GREEN,
        'theta_color':BLUE,
    }
    def construct(self):
        self.show_xy_axis()
    def show_xy_axis(self):
        plane=NumberLine()
        plane.add_coordinates()
        self.play(Create(plane))
        self.wait()