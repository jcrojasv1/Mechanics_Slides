from manim import *  # or: from manimlib import *
from manim_slides import Slide,ThreeDSlide
import numpy as np

def cylinder(self):
        # Cilindro
        center_ellipse = np.array((2.,-2.,0))
        radius = 2
        elipse1 = Ellipse(0.3,radius,color=WHITE).move_to(center_ellipse)
        elipse2 = elipse1.copy().move_to(center_ellipse + 3*RIGHT)
        line1 = Line(center_ellipse + UP,center_ellipse+3*RIGHT + UP) 
        line2 = Line(center_ellipse + DOWN,center_ellipse+3*RIGHT + DOWN) 
        grupo3 = VGroup(elipse1,elipse2,line1,line2)
        self.play(Create(grupo3))
        funct = lambda r: RIGHT*0.5
        flow = StreamLines(funct,color=BLUE_B,x_range=[1,3.2,0.3],y_range=[-3.2,-.9,0.3])
        self.add(flow)

        self.next_slide(loop=True)
        flow.start_animation()
        self.wait(3)
        self.play(flow.end_animation())
        self.next_slide()
        
        daa = MathTex(r"\dd A_{\perp}").next_to(center_ellipse,LEFT)
        vekJ = Arrow(center_ellipse + 2.8*RIGHT,center_ellipse + 5*RIGHT)
        textJa = MathTex(r"\mathbf{I}").next_to(center_ellipse + 4*RIGHT + 0.5*DOWN)
        self.play(Write(daa),GrowArrow(vekJ),Write(textJa))

        all = VGroup(grupo3,daa,vekJ,textJa)
        return all
    
class Slide1(Slide):
    
    def construct(self):
        title = Tex(r"\textbf{Ecuación de continuidad}")
        eqn1 = MathTex(r"\pdv{\rho(\textbf{r},t)}{t} + \nabla\cdot\textbf{J} = 0")
        group32 = VGroup(title, eqn1).arrange(DOWN)
        self.play(
            Write(title,shift=DOWN),
            FadeIn(eqn1, shift=UP)
        )   
        self.next_slide()
        
        transform_title = Tex(r"\textbf{Ecuación de continuidad}")
        transform_eqn = MathTex(r"\pdv{\rho(\textbf{r},t)}{t} + \nabla\cdot\textbf{J} = 0")
        group4 = VGroup(transform_title,transform_eqn).arrange(DOWN).to_edge(UP)
        self.play(
            Transform(title, transform_title),
            Transform(eqn1,transform_eqn)
        )
        self.next_slide()
        
        def1 = MathTex(r"\textbf{J} = \dv{\mathbf{I}}{A_{\perp}}")
        text1 = Tex(r"Densidad de corriente volumétrica")
        text1.font_size = 34
        group1 = VGroup(text1,def1).arrange(DOWN)
        
        self.play(
            Write(def1,shift=LEFT),
            Write(text1,shift=LEFT)
        )
        
        self.next_slide()
        
        self.play(
            Transform(group1,group1.copy().to_edge(LEFT))
        )
        
        self.next_slide()
        
        animation = cylinder(self)
        
        self.next_slide()
        
        self.play(FadeOut(animation))
        
        self.next_slide()
        
        def2 = MathTex(r"\rho(\mathbf{r},t) = \dv{Q}{V}")
        text2 = Tex(r"Densidad de carga volumétrica")
        text2.font_size = 34
        group2 = VGroup(text2,def2).arrange(DOWN).to_edge(RIGHT)
        self.play(
            Write(def2,shift=LEFT),
            Write(text2,shift=LEFT)
        )
        self.next_slide()  
        self.play(FadeOut(group2),FadeOut(group1),FadeOut(group32))  
        

        
class Slide2(Slide):
    def construct(self):
        imagen = SVGMobject("figura.svg",height=10)        
        self.play(FadeIn(imagen))
        vekA = MathTex(r" \mathbf{J}").move_to(2*LEFT + 2*UP)
        vekJ = MathTex(r"\dd \mathbf{A}").move_to(RIGHT + 1.7*UP)
        
        self.next_slide()
        
        self.play(Write(vekA))
        
        self.next_slide()
        
        self.play(Write(vekJ))
        
        grupo = VGroup(imagen,vekJ,vekA)
        self.next_slide()
        transform_img = grupo.copy().move_to(3*RIGHT)
        self.play(Transform(grupo,transform_img))
        
        self.next_slide()
        font_size = 40
        text1 = MathTex(r"\dv{Q}{t}", r"=",r"-\int_S \textbf{J}\cdot \text{d}\textbf{A}")
        text1.font_size = font_size
        
        text2 = MathTex(r"\dv{}{t}\left( \int_{V} \rho(\mathbf{r},t) \dd V \right)", r"=",r"-\int_S \textbf{J}\cdot \text{d}\textbf{A}")
        text2.font_size = font_size
        
        text3 = MathTex(r"\int_{V}\pdv{\rho}{t}\dd V",r"=",r"-\int_S \textbf{J}\cdot \text{d}\textbf{A}")
        text3.font_size = font_size
        
        text4 = MathTex(r"\int_{V}\pdv{\rho}{t}\dd V",r"=",r"-\int_V \nabla \cdot \mathbf{J}\dd V")
        text4.font_size = font_size
        
        text5 = MathTex(r"\pdv{\rho}{t}",r"=",r"- \nabla \cdot \mathbf{J}")
        text5.font_size = font_size
        
        text6 = MathTex(r"\pdv{\rho}{t}+ \nabla \cdot \mathbf{J}",r"=",r"0")
        text6.font_size = font_size
        
        
        grupoeq = VGroup(text1,text2,text3,text4,text5,text6).to_corner(LEFT)
        self.next_slide()
        
        self.play(Write(text1))
        
        self.next_slide()
        
        self.play(TransformMatchingTex(text1,text2))
        
        self.next_slide()
        
        self.play(TransformMatchingTex(text2,text3))
        
        self.next_slide()

        self.play(TransformMatchingTex(text3,text4))
        
        self.next_slide()
        
        self.play(TransformMatchingTex(text4,text5))
        
        self.next_slide()
        
        self.play(TransformMatchingTex(text5,text6))
        
        self.next_slide()
        
        titl1 = Tex(r"\textbf{Ecuación de continuidad}").move_to(4*LEFT+1.3*DOWN)
        self.play(Write(titl1),shift=UP)
        
        texto = Tex(r"¡Conservación \textbf{local} de la carga!").move_to(4*LEFT+2*DOWN)
        texto.font_size = 30
        self.play(FadeIn(texto),shift=UP)


class Test(Slide):
    def get_sub_indexes(tex):
        ni = VGroup()
        colors = [RED,TEAL,GREEN,BLUE,PURPLE]
        for i in range(len(tex)):
            n = Text(f"{i}",color=colors[i%5]).scale(0.1)
            n.next_to(tex[i],DOWN,buff=0.01)
            ni.add(n)
        return ni

    def construct(self):
        self.next_slide(loop=True)
        text1 = MathTex(r"\dv{Q}{t}", r"=",r"-\int_S \textbf{J}\cdot \text{d}\textbf{A}")
        text2 = MathTex(r"\dv{}{t}\left( \int_{V} \rho(\mathbf{r},t) \dd V \right)",r"=",r"-\int_S \textbf{J}\cdot \text{d}\textbf{A}")
        source_ind = Test.get_sub_indexes(text1)
        target_ind = Test.get_sub_indexes(text2)

        self.add(
            text1
        )
        self.play(TransformMatchingTex(text1,text2))

        
