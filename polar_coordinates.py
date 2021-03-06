from manim import *
from numpy import number
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
        plane=NumberPlane()
        x=3*np.cos(np.pi/6)
        y=3*np.sin(np.pi/6)
        xp=plane.c2p(x,0)
        yp=plane.c2p(0,y)
        origin=plane.c2p(0,0)
        point=plane.c2p(x,y)
        dot=Dot(point,color=self.CONFIG['x_color'])
        x_line=Line(point,xp).add_updater(lambda m:m.put_start_and_end_on(dot.get_center(),-dot.get_center()[1]*DOWN))
        y_line=Line(point,yp).add_updater(lambda m:m.put_start_and_end_on(dot.get_center(),-dot.get_center()[0]*LEFT))
        #get_coord_label
        coord_label=self.get_coord_label(x,y,self.CONFIG['x_color'],self.CONFIG['y_color'])
        coord_label.next_to(dot,UR,buff=SMALL_BUFF)
        x_brace=Brace(x_line,RIGHT).add_updater(lambda m:m.next_to(y_line,RIGHT,buff=SMALL_BUFF))
        y_brace=Brace(y_line,UP).add_updater(lambda m:m.next_to(x_line,UP,buff=SMALL_BUFF))
        plane.add_coordinates()
        for mob in [
            plane,
            dot,
            x_line,
            y_line,
            x_brace,
            y_brace
        ]:
            self.play(Create(mob))
        self.add(x_brace,y_brace)
        self.wait()
        for mob in [
            LEFT+.1*UP,
            RIGHT+.1*UP,
            LEFT+.4*DOWN,
            RIGHT+.4*DOWN,
        ]:
            self.play(
                dot.animate.shift(mob)
            )
        self.play(dot.animate.move_to(point))
        self.wait()
    def get_coord_label(self,x=0,y=0,x_color=WHITE,y_color=WHITE,include_background_rectangle=True,**decimal_kwargs):
        coords=VGroup()
        for n in x,y:
            if isinstance(n,number): #en el cuaderno aparece numbers.Number
                coord=DecimalNumber(n,**decimal_kwargs)
            elif isinstance(n,str):
                coord=MathTex(n)
            else:
                raise Exception("Invalid type of number")
            coords.add(coord)
        x_coord,y_coord=coords
        x_coord.set_color(x_color)
        y_coord.set_color(y_color)
        coord_label=VGroup(
            MathTex("("),
            x_coord,
            MathTex(","),
            y_coord,
            MathTex(")"),
        )
        coord_label.arrange(RIGHT,buff=SMALL_BUFF)
        coord_label[2].align_to(coord_label[0],DOWN)
        coord_label.x_coord=x_coord
        coord_label.y_coord=y_coord
        if include_background_rectangle:
            coord_label.add_background_rectangle()
        return coord_label