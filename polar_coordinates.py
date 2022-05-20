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
        x_line=Line(point,xp).add_updater(lambda m: m.put_start_and_end_on(dot.get_center(),np.array([dot.get_center()[0],0,0])))
        y_line=Line(point,yp).add_updater(lambda m: m.put_start_and_end_on(dot.get_center(),np.array([0,dot.get_center()[1],0])))
        x_brace=always_redraw(lambda:Brace(y_line,UP,buff=SMALL_BUFF))
        y_brace=always_redraw(lambda:Brace(x_line,RIGHT,buff=SMALL_BUFF))
        dot=Dot(point,color=self.CONFIG['x_color'])
        x_coord=MathTex('x',color=self.CONFIG['x_color']).add_updater(lambda m: m.next_to(x_brace,UP,buff=SMALL_BUFF))
        y_coord=MathTex('y',color=self.CONFIG['y_color']).add_updater(lambda m: m.next_to(y_brace,RIGHT,buff=SMALL_BUFF))
        plane.add_coordinates()
        for mob in [plane,dot,x_line,y_line,x_brace,y_brace,x_coord,y_coord]:
            self.play(Create(mob))
        self.wait()
        for pos in [LEFT+0.5*UP,LEFT+0.5*DOWN,RIGHT+0.5*DOWN,RIGHT+0.5*UP]:
            self.play(dot.animate.shift(pos))
        self.play(dot.animate.move_to(point))
        axes_polar,circles,rays=self.get_polar_grid(plane)
        self.play(ReplacementTransform(plane,VGroup(axes_polar,circles,rays)))
        self.wait()
        polar_coord,radius_line,arco=self.get_polar_coord(dot,origin)
        self.play(ReplacementTransform(VGroup(x_coord,y_coord),polar_coord))
        self.wait()
        self.play(ReplacementTransform(VGroup(x_line,y_line,x_brace,y_brace),radius_line))
        self.play(TransformFromCopy(polar_coord[-2],arco))
        self.play(Rotating(radius_line,radians=np.pi*2,about_point=origin))
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
    def transition_to_polar_coord(self):
        pass
    def get_polar_grid(self,plane,radius=0.25):
        circles=VGroup(*[
            Circle(color=BLUE,stroke_width=1,radius=r)
            for r in np.arange(0.5,8.5,0.5)
        ])
        rays=VGroup(*[
            Line(plane.c2p(0,0),RIGHT*8.5,stroke_width=1,color=BLUE).set_angle(r)
            for r in np.arange(0,2*np.pi,np.pi/12)
        ])
        return VGroup(circles,rays)
    def get_polar_coord(self,dot,origin):
        theta_coord=MathTex("\\theta",color=self.CONFIG['theta_color'])
        r_coord=MathTex("r",color=self.CONFIG['r_color'])
        set_coord=VGroup(
            MathTex("("),
            r_coord,
            MathTex(","),
            theta_coord,
            MathTex(")"),
        ).arrange(RIGHT,buff=SMALL_BUFF)
        set_coord[2].align_to(set_coord[0],DOWN)
        set_coord.add_updater(lambda m: m.next_to(dot,UP,buff=SMALL_BUFF))
        radius=Line(origin,dot.get_center())
        arco=Angle(Line(origin,RIGHT),radius,radius=1,color=WHITE)
        return [set_coord,radius,arco]