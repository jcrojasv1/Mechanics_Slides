from manim import *  # or: from manimlib import *
from manim_slides import Slide
import numpy as np

class principal(Slide):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{physics}")
        title = Tex(r"\textbf{Conservación de la carga \\ y \\ la ecuación de continuidad} \\")
        eqn1 = MathTex(r"\frac{\partial\rho(\textbf{r},t)}{\partial t} + \nabla \textbf{J} = 0")
        VGroup(title, eqn1).arrange(DOWN)
        self.play(
            Write(title,shift=UP),
            FadeIn(eqn1, shift=DOWN),
        )   
        self.next_slide()
        
        transform_title = Tex("Ecuación de continuidad")
        transform_title.to_corner(UP + LEFT)
        
        transform_eqn = MathTex(r"\frac{\partial\rho(\textbf{r},t)}{\partial t} + \nabla \textbf{J} = 0")
        transform_eqn.to_edge(UP + LEFT + np.array((0.0,1.,0.0)))
        
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
        self.wait(0.1)
        self.play(
            Transform(def1, (def1.copy()).to_edge(LEFT)),
            Transform(def2, (def2.copy()).to_edge(LEFT))
        )
        
        self.next_slide()