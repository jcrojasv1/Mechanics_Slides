from manim import *  # or: from manimlib import *
from manim_slides import Slide,ThreeDSlide
import numpy as np

class Slide1(Slide):
    def construct(self):
        title = Tex(r"\textbf{Conservación de la carga \\ y \\ la ecuación de continuidad} \\")
        eqn1 = MathTex(r"\pdv{\rho(\textbf{r},t)}{t} + \nabla \textbf{J} = 0")
        VGroup(title, eqn1).arrange(DOWN)
        self.play(
            Write(title,shift=DOWN),
            FadeIn(eqn1.move_to(DOWN+np.array((0.,-0.5,0.))), shift=UP),
        )   
        self.next_slide()
        
        transform_title = Tex("Ecuación de continuidad")
        transform_title.to_corner(UP + LEFT)
        
        transform_eqn = MathTex(r"\pdv{\rho(\textbf{r},t)}{t} + \nabla \textbf{J} = 0")
        transform_eqn.to_edge(  np.array((-1,3,0.0)))
        self.play(
            Transform(title, transform_title),
            Transform(eqn1,transform_eqn)
        )
        self.next_slide()
        
        def1 = Tex(r"$\textbf{J}$: Densidad de corriente")
        def2 = Tex(r"$\rho(\textbf{r},t)$: Densidad de carga volumétrica")
        VGroup(def1,def2).arrange(DOWN)
        self.play(
            Write(def1,shift=LEFT),
            Write(def2,shift=LEFT)
        )
        self.play(
            Transform(def1, (def1.copy()).to_edge(LEFT)),
            Transform(def2, (def2.copy()).to_edge(LEFT))
        )
        
        self.next_slide()
        
        self.play(
            FadeOut(def1),
            FadeOut(def2)
        )
        self.play(
            FadeOut(title),
            FadeOut(eqn1)
        )
        
class Slide2(ThreeDSlide):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        axes = ThreeDAxes()
        square = Square(side_length=1,color=RED,fill_color = RED).move_to(np.array((0.,0.,1.5)))
        square.set_fill(RED,opacity=1)
        cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)
        self.play(GrowFromCenter(cube))
        self.next_slide()
        self.play(FadeIn(square))
        dA = Arrow3D(np.array((0,0,1.5)),np.array((0,0,2.5)))
        dA.set_z_index(square.z_index +1)
        self.play(GrowFromPoint(dA,np.array((0.,0.,1.5))))
        dAtext = MathTex(r"\dd \textbf{A}").move_to(np.array((1.,2.,0.)))
        self.add_fixed_in_frame_mobjects(dAtext)
        self.play( Write(dAtext))
        self.next_slide(loop=True)
        
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, x_range=[-2,2,0.5],y_range=[-2,2,0.5],z_range=[-2,2,0.5],stroke_width=2, max_anchors_per_line=3,opacity=0.5)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=True, flow_speed=3)
        self.wait(1)
        self.play(stream_lines.end_animation())
        
        self.next_slide()
        
        Jvector = Arrow3D(np.array((0,0,1.5)), np.array((0,0,1.5)) + func(np.array((0,0,1.5))))
        Jvector.set_z_index(dA.z_index -1)
        self.play(GrowFromPoint(Jvector,np.array((0.,0.,1.5))))
        Jvector.set_z_index(dA.z_index)
        Jtext = MathTex(r"\textbf{J}").move_to(np.array((0,1.1,0)))
        self.add_fixed_in_frame_mobjects(Jtext)
        self.play(Write(Jtext))
        
        
        
        self.next_slide()
        text1 = MathTex(r"\dv{q}{t}=-\int_S \textbf{J}\cdot \text{d}\textbf{A}").move_to(np.array((-3,3,0)))
        self.add_fixed_in_frame_mobjects(text1)
        self.play(
            Write(text1,shift=LEFT)
        )
        

        