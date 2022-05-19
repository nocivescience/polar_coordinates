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
        x_line=Line(point,xp)
        y_line=Line(point,yp)
        x_brace=Brace()
        dot=Dot(point,color=self.CONFIG['x_color'])
        plane.add_coordinates()
        for mob in [plane,dot,x_line,y_line]:
            self.play(Create(mob))
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
    def show_polar_coordinates(self,dot,plane):
        origin=plane.c2p(0,0)
        r_line=Line(origin,dot.get_center())
        r_line.set_color(self.CONFIG['r_color'])
        r_value=r_line.get_length()
        theta_value=r_line.get_angle()
        coord_label=self.get_coord_label(r_value,theta_value,self.CONFIG['r_color'],self.CONFIG['theta_color'])
        r_coord=coord_label.x_coord
        theta_coord=coord_label.y_coord
        coord_label.add_updater(lambda m: m.next_to(dot,RIGHT,buff=0))
        r_coord.add_updater(lambda m: m.set_value(r_line.get_length()))
        theta_value.add_updater(lambda m: m.set_value(r_line.get_angle()))
        self.play(Create(coord_label))
    def transition_to_polar_coord(self):
        pass
    def get_polar_grid(self,plane,radius=0.25):
        axes=VGroup(
            
        )