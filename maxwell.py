from manim import *
from manim_slides import Slide, ThreeDSlide
import numpy as np

class Formulae(Slide):
    def construct(self):
        # Texto inicial:
        
        text_0 = Text("Conservacion de la Carga")
        text_0.scale(0.75)
        line = Line([-7, 3, 0], [7, 3, 0])
        
        self.play(
            Write(text_0)
            )
        
        self.next_slide()

        self.play(
            text_0.animate.shift(UP*3.5), Create(line)
            )

        self.next_slide()

        # Forma integral de las ecuaciones de Maxwell:
        
        formulae_1 = MathTex(r"\oint \mathbf{E} \cdot d\mathbf{A} = \frac{Q_{enc}}{\epsilon_{0}}")
        formulae_1.scale(0.75)
        
        formulae_2 = MathTex(r"\oint \mathbf{B} \cdot d\mathbf{A} = 0")
        formulae_2.scale(0.75)
        formulae_2.move_to(DOWN*1)

        formulae_3 = MathTex(r"\oint \mathbf{E} \cdot d\mathbf{s} = - \dv{\Phi_{\mathbf{B}}}{t}")
        formulae_3.scale(0.75)
        formulae_3.move_to(DOWN*2)

        formulae_4 = MathTex(r"\oint \mathbf{B} \cdot d\mathbf{s} = \mu_{0}\varepsilon_{0}\dv{\Phi_{\mathbf{E}}}{t} + \mu_{0}i_{enc}")
        formulae_4.scale(0.75)
        formulae_4.move_to(DOWN*3)
        
        # Forma diferencial de las ecuaciones de Maxwell:

        formulae_5 = MathTex(r"\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_{0}}")
        formulae_5.scale(0.75)
        
        formulae_6 = MathTex(r"\nabla \times \mathbf{E} = - \pdv{\mathbf{B}}{t}")
        formulae_6.scale(0.75)
        formulae_6.move_to(DOWN*1)
        
        formulae_7 = MathTex(r"\nabla \cdot \mathbf{B} = 0")
        formulae_7.scale(0.75)
        formulae_7.move_to(DOWN*2)

        formulae_8 = MathTex(r"\nabla \times \mathbf{B}",  r"=", r"\mu_{0}\mathbf{J}", r"+", r"\mu_{0}\varepsilon_{0} \pdv{\mathbf{E}}{t}")
        formulae_8.scale(0.75)
        formulae_8.move_to(DOWN*3)

        # Grupos de ecuaciones:

        integral_equations = VGroup(formulae_1, formulae_2, formulae_3, formulae_4)
        
        differential_equations = VGroup(formulae_5, formulae_6, formulae_7, formulae_8)
        differential_equations.shift(RIGHT*0.5)
        
        # Nombrecitos :3

        text_a = Text("Ley de Gauss")
        text_a.scale(0.5)

        text_b = ["Ley de Gauss", "para el Magnetismo"]
        text_b = Paragraph(*text_b, alignment = "center")
        text_b.scale(0.5)
        text_b.move_to(DOWN*1)

        text_c = Text("Ley de Maxwell-Faraday")
        text_c.scale(0.5)
        text_c.move_to(DOWN*2)

        text_d = Text("Ley de Ampère-Maxwell")
        text_d.scale(0.5)
        text_d.move_to(DOWN*3)

        text_e = ["Ecuaciones de Maxwell", "en Forma Integral"]
        text_e = Paragraph(*text_e, alignment = "center")
        text_e.scale(0.5)
        text_e.move_to(UP)
        
        text_f = ["Ecuaciones de Maxwell en", "Forma Diferencial"]
        text_f = Paragraph(*text_f, alignment = "center")
        text_f.scale(0.5)
        text_f.move_to(RIGHT*0.5 + UP)
        
        # Grupo de nombres:

        equations_names = VGroup(text_a, text_b, text_c, text_d)
        equations_names.shift(RIGHT*4.75)

        # Cajitas:

        box_1 = Rectangle(width = 5.2, height = 4, color = WHITE)
        box_1.shift(DOWN*1.5)
        box_2 = Rectangle(width = 4.15, height = 4, color = WHITE)
        box_2.shift(RIGHT*0.5 + DOWN*1.5)
        box_3 = Rectangle(width = 2.4, height = 1, color = WHITE)
        box_3.shift(DOWN)
        box_4 = Rectangle(width = 6, height = 1.6, color = WHITE)
        box_4.shift(UP*0.325)
        box_5 = Rectangle(width = 6, height = 4, color = WHITE)
        box_5.shift(DOWN*0.5)
        box_6 = Rectangle(width = 5, height = 1.8, color = WHITE)
        box_6.shift(UP*0.5)
        box_7 = Rectangle(width = 5, height = 2, color = WHITE)
        box_7.shift(UP*0.5)
        box_8 = Rectangle(width = 3, height = 1.25, color = WHITE)


        # Zona de animaciones de la primera slide:

        temp_Group1 = VGroup(integral_equations, text_e)

        self.play(
            Write(temp_Group1), Create(box_1)
             )
        
        self.next_slide()

        temp_Group1.add(box_1)

        self.play(
            temp_Group1.animate.shift(LEFT*4.25)
            )

        self.play(
            Write(differential_equations), Create(box_2), Write(text_f)
             )

        self.next_slide()

        self.play(
            Write(equations_names)
            )
        
        self.next_slide()

        # Momento en el que desaparecen los elementos para pasar a la segunda slide:
        
        slide1_vanished = VGroup(box_1, box_2, integral_equations, differential_equations[:3], equations_names, text_0, text_e, text_f)
        self.play(
            FadeOut(slide1_vanished),
            )

        # Inicio de la segunda slide:
        
        text_1 = Text("Primer acercamiento: Ecuaciones de Maxwell")
        text_1.move_to(UP*3.5)
        text_1.scale(0.75)
        a_maxwell_0 = differential_equations.remove(*differential_equations[:3]) # Nos quedamos sólo con la ecuación de Ampère-Maxwell para nuestra prueba.

        # Proceso de deducción de la conservación de la carga a partir de las ecuaciones de Maxwell.

        self.play(
            Write(text_1), a_maxwell_0.animate.shift(LEFT*0.5 + UP*5)
            )

        self.next_slide()

        a_maxwell_1 = MathTex(r"\nabla \times", r"\left(\nabla \cdot \mathbf{B}\right)", r"=", r"\nabla \times \left(\mu_{0}\mathbf{J}", r"+", r"\mu_{0}\varepsilon_{0} \pdv{\mathbf{E}}{t}",r"\right)")
        a_maxwell_1_0 = a_maxwell_0.copy()
        a_maxwell_1.scale(0.75)
        a_maxwell_1.shift(UP)

        self.play(
            a_maxwell_1_0.animate.shift(DOWN), TransformMatchingShapes(a_maxwell_1_0, a_maxwell_1)
            )
        
        self.next_slide()

        # En este apartado se describen la propiedad para campos vectoriales:

        text_g = Text("Propiedad para Campos Vectoriales:")
        text_g.scale(0.5)
        text_g.move_to(UP*0.65)
        formulae_9 = MathTex(r"\nabla \times \left(\nabla \cdot \mathbf{A}\right) = 0")

        v_propertie = VGroup(text_g, formulae_9, box_4)
        v_propertie.shift(LEFT*3 + DOWN*3)
        
        self.play(
            Write(v_propertie)
        )

        self.next_slide()

        # Se continua el proceso de deducción:

        a_maxwell_2 = MathTex(r"0", r"=", r"\mu_{0} \nabla \cdot \mathbf{J}", r"+", r"\mu_{0}\varepsilon_{0} \nabla \cdot \left(\pdv{\mathbf{E}}{t}\right)")
        a_maxwell_2.scale(0.75)
        a_maxwell_2_0 = a_maxwell_1.copy()
        self.play(
            a_maxwell_2_0.animate.shift(DOWN), TransformMatchingShapes(a_maxwell_2_0, a_maxwell_2)    
            )

        self.next_slide()

        a_maxwell_3 = MathTex(r"0", r"=", r"\mu_{0} \nabla \cdot \mathbf{J}", r"+", r"\mu_{0}\varepsilon_{0} \nabla \cdot \frac{\partial}{\partial{t}}\left(\nabla \cdot \mathbf{E}\right)")
        a_maxwell_3.scale(0.75)
        self.play(
            TransformMatchingShapes(a_maxwell_2, a_maxwell_3)
            )
        
        self.next_slide()

        a_maxwell_4 = MathTex(r"0", r"=", r"\mu_{0} \nabla \cdot \mathbf{J}", r"+", r"\mu_{0}\varepsilon_{0}  \frac{\partial}{\partial{t}}\left(\frac{\rho}{\varepsilon_{0}}\right)")
        a_maxwell_4.scale(0.75)
        self.play(
            TransformMatchingShapes(a_maxwell_3, a_maxwell_4)
            )
        
        self.next_slide()

        a_maxwell_5 = MathTex(r"0", r"=", r"\nabla \cdot \mathbf{J}", r"+", r"\pdv{\rho}{t}")
        a_maxwell_5_0 = a_maxwell_4.copy()
        a_maxwell_5.shift(DOWN)
        self.play(
            a_maxwell_5_0.animate.shift(DOWN), TransformMatchingShapes(a_maxwell_5_0, a_maxwell_5)    
            )
        
        self.next_slide()
        
        a_maxwell_6 = MathTex(r"\nabla \cdot \mathbf{J}", r"=", r"-", r"\pdv{\rho}{t}")
        a_maxwell_6.shift(DOWN)
        a_maxwell_6.scale(0.75)
        self.play(
            TransformMatchingShapes(a_maxwell_5, a_maxwell_6), Create(box_3)
        )

        # Se cierra el proceso de deducción:

        text_h = ["Obtuvimos una ecuación de", "continuidad, luego, la cantidad", "representativa se conserva."]   
        text_h = Paragraph(*text_h, alignment = "center")
        text_h.scale(0.5)
        text_h.move_to(RIGHT*3.5 + DOWN*2.5)
    
        self.play(
            Write(text_h)
            )
        
        self.next_slide()

        # Momento en el que desaparecen los elementos para pasar a la segunda slide:

        slide2_vanished = VGroup(a_maxwell_0, a_maxwell_1, a_maxwell_4, a_maxwell_6, v_propertie, text_1, text_h, box_3)
        self.play(
            FadeOut(slide2_vanished)
            )

        # Inicia la tercera slide:

        text_2 = Text("Segundo acercamiento: II Teorema de Noether")
        text_2.move_to(UP*3.5)
        text_2.scale(0.75)
        self.play(
            Write(text_2)
            )
        
        self.next_slide()

        # Determinación del Lagrangiano:

        maxwell_lagrangian = MathTex(r"\mathcal{L}", r"=", r"\frac{1}{4}", r"F^{\mu\nu}", r"F_{\mu\nu}", r"-", r"J^{\mu}", r"A_{\mu}")
        maxwell_lagrangian.scale(1.2)
        text_3 = Text("Lagrangiano de las Ecuaciones de Maxwell")
        text_3.move_to(DOWN)
        text_3.scale(0.65)

        self.play(
            Write(maxwell_lagrangian), Write(text_3)
            )
        
        self.next_slide()

        self.play(
            FadeOut(text_3), maxwell_lagrangian.animate.shift(UP*2)
            )

        # Explicación de los términos del Lagrangiano:
        text_4 = Text("Tensor de Campo Electromagnético")
        text_4.scale(0.65)
        text_4.shift(DOWN*3)
        tensorF = MathTex(r"F^{\mu\nu}", r"=", r"\begin{pmatrix} 0 & - \dfrac{E_{x}}{c} & - \dfrac{E_{y}}{c} & - \dfrac{E_{z}}{c} \\ \
                          &&& \\ \dfrac{E_{x}}{c} & 0 & - B_{z} & B_{y} \\ \
                          &&& \\ \dfrac{E_{y}}{c} &  B_{z} & 0 & - B_{x} \\ &&& \\ \dfrac{E_{z}}{c} &  -B_{y} & B_{x} & 0 \end{pmatrix}")
        tensorF.scale(0.75)
        tensorF_Group = VGroup(tensorF, text_4)

        text_5 = Text("Covariente del Tensor de Campo Electromagnético")
        text_5.scale(0.65)
        text_5.shift(DOWN*3)
        cov_tensorF = MathTex(r"F_{\mu\nu}", r"=", r"\begin{pmatrix} 0 & \dfrac{E_{x}}{c} & \dfrac{E_{y}}{c} & \dfrac{E_{z}}{c} \\ \
                          &&& \\ -\dfrac{E_{x}}{c} & 0 & - B_{z} & B_{y} \\ \
                          &&& \\ -\dfrac{E_{y}}{c} &  B_{z} & 0 & - B_{x} \\ &&& \\ -\dfrac{E_{z}}{c} &  -B_{y} & B_{x} & 0 \end{pmatrix}")
        cov_tensorF.scale(0.75)
        cov_tensorF_Group = VGroup(cov_tensorF, text_5)
        
        self.next_slide()

        self.play(
            FadeOut(maxwell_lagrangian[0:3] + maxwell_lagrangian[5::]), TransformMatchingShapes(maxwell_lagrangian[3:5], tensorF_Group)
            ) 
        
        self.next_slide()

        self.play(
            TransformMatchingShapes(tensorF_Group, cov_tensorF_Group)
            )
        
        self.next_slide()

        self.play(
            FadeOut(cov_tensorF_Group), FadeIn(maxwell_lagrangian)
            )
        
        self.next_slide()

        text_6 = Text("Cuadricorriente")
        text_6.scale(0.65)
        text_6.shift(DOWN)
        four_current = MathTex(r"J^{\mu}", r"=", r"\left(c\rho, \mathbf{J}\right)")
        current_Group = VGroup(four_current, text_6)
        self.play(
            TransformMatchingShapes(maxwell_lagrangian[6].copy(), current_Group)
            )
        
        self.next_slide()

        self.play(
            FadeOut(current_Group)
            )
        
        self.next_slide()

        text_7 = Text("Cuadripotencial")
        text_7.scale(0.65)
        text_7.shift(DOWN)
        four_current = MathTex(r"A_{\mu}", r"=", r"\left(\frac{\phi}{c}, \mathbf{A}\right)")
        potential_Group = VGroup(text_7, four_current)
        self.play(
            TransformMatchingShapes(maxwell_lagrangian[7].copy(), potential_Group)
            )
        
        self.next_slide()

        self.play(
            FadeOut(potential_Group)
            )
        
        self.next_slide()

        self.play(
            FadeOut(maxwell_lagrangian)
            )
        
        text_8 = Text("Apliquemos el segundo Teorema de Noether:")
        text_8.scale(0.5)
        text_8.shift(UP*2.5 + LEFT*3.5)
        
        self.play(
            Write(text_8)
            )
        
        self.next_slide()
        
        noether_second0 = Text("II Teorema de Noether:")
        noether_second0.scale(0.5)
        noether_second0.shift(UP)
        noether_second1 = MathTex(r"\sum_{i} E_{i}a_{ki} \circeq \sum_{i} \partial_{\mu} \left(E_{i}b_{ki}^{\nu}\right)")   
        noether_second1.shift(DOWN*1.6)
        noether_statement = ["Existe una simetría sí y solo sí existen", "relaciones diferenciales entre", "las ecuaciones de Euler-Lagrange"]
        noether_statement = Paragraph(*noether_statement, alignment = "center")
        noether_statement.scale(0.5)
        noether_second = VGroup(box_5,  noether_second0, noether_statement, noether_second1)

        self.play(
            FadeIn(noether_second), noether_second.animate.shift(LEFT*3)
            )
        
        self.next_slide()

        text_10 = Text("Expresión de Lagrange:")
        text_10.scale(0.5)
        text_10.shift(UP)
        lagrange_exp = MathTex(r"E_{A_{\mu}} = \partial_{\nu}F^{\mu\nu} - J^{\mu}")

        lagrange_exp_Group = VGroup(text_10, lagrange_exp, box_6)
        lagrange_exp_Group.shift(RIGHT*4 + UP*1)
        
        self.play(
            FadeIn(lagrange_exp_Group)
            )

        self.next_slide()

        text_11 = ["Para un lagrangiano", "gauge-invariante:"]
        text_11 = Paragraph(*text_11, alignment = "center")
        text_11.scale(0.5)
        text_11.shift(UP)
        aki = MathTex(r"a_{ki} = 0")
        aki.shift(LEFT)
        bki = MathTex(r"b_{ki}^{\nu} = \delta^{\gamma}_{\mu}")
        bki.shift(RIGHT)

        constants_group = VGroup(text_11, aki, bki, box_7)
        constants_group.shift(RIGHT*4 + DOWN*3)

        self.play(
            FadeIn(constants_group)
            )
        
        self.next_slide()
        
        slide3_vanished = VGroup(text_10, text_11, noether_statement, noether_second0, box_5, box_6, box_7)
        
        self.play(
            FadeOut(slide3_vanished)
            )
        
        box_5.shift(RIGHT*6.2 + UP*0.2)

        self.play(
            noether_second1.animate.shift(RIGHT*6.2 + UP), constants_group[1:3].animate.shift(UP*1.2 + LEFT*0.8), lagrange_exp.animate.shift(LEFT*0.8   ), Create(box_5)
            )
     
        self.next_slide()
        
        second_theorem_1 = MathTex(r"0 = \partial_{\mu}\left[\left(\partial_{\nu}F^{\mu\nu} - J^{\mu}\right)\cdot\delta_{\mu}^{\nu}\right]")
        second_theorem_1.shift(LEFT*3.5 + UP*1.5)
        self.play(
            TransformMatchingShapes(noether_second1.copy(), second_theorem_1)
            )
        
        self.next_slide()

        second_theorem_2 = MathTex(r"\partial_{\mu}\partial_{\nu}F^{\mu\nu} - \partial_{\mu}J^{\mu} = 0")
        second_theorem_2.shift(LEFT*3.5 + UP*0.25)
        self.play(
            TransformMatchingShapes(second_theorem_1.copy(), second_theorem_2)
            )
        
        self.next_slide()

        second_theorem_3 = MathTex(r"\partial_{\mu}J^{\mu} = \nabla \cdot \mathbf{J} + \pdv{\rho}{t} = 0")
        second_theorem_3.shift(LEFT*3.5 + DOWN)
        self.play(
            TransformMatchingShapes(second_theorem_2.copy(), second_theorem_3)
            )
        
        self.next_slide()

        second_theorem_4 = MathTex(r"\nabla \cdot \mathbf{J}", r"=", r"-", r"\pdv{\rho}{t}")
        second_theorem_4.shift(LEFT*3.5 + DOWN*2.5)
        self.play(
            TransformMatchingShapes(second_theorem_3.copy(), second_theorem_4), Create(box_8.shift(DOWN*2.5 + LEFT*3.5))
            )
        
        self.next_slide()

        # Desaparece el contenido de la tercera slide:

        slide4_vanished = VGroup(second_theorem_1, second_theorem_2, second_theorem_3, second_theorem_4, box_8, noether_second1, constants_group[1:3], lagrange_exp, text_2, box_5, text_8)
        self.play(
            FadeOut(slide4_vanished)
            )
        
        # Pasamos a la cuarta slide:
        text_9 = Text("¿Es realmente Gauge-Invariante?")
        text_9.move_to(UP*3.5)
        text_9.scale(0.75)
        self.play(
            Write(text_9)
            )
        
        # Explicar la no gauge-invarianza.
        
        self.next_slide()

        maps = MathTex(r"A_{\mu} \mapsto A'_{\mu} = A_{\mu} + \partial_{\mu}\Theta") 
        maps.shift(UP*2.25)
        text_12 = Text("Transformación de Gauge U(1)")
        text_12.scale(0.75)
        text_12.shift(UP*1.5)
        non_invariant_0 = MathTex(r"\mathcal{L} \mapsto \mathcal{L}' = \frac{1}{4}F^{\mu\nu}F_{\mu\nu} - J^{\mu}\left(A_{\mu} + \partial_{\mu}\Theta\right)")
        non_invariant_1 = MathTex(r"\mathcal{L}' = \mathcal{L} - J^{\mu}\partial_{\mu}\Theta")
        non_invariant_1.shift(DOWN*1.25)
        text_13 = MathTex(r"\text{El término } J^{\mu}\partial_{\mu}\Theta \text{ genera invarianza", r"de gauge solamente cuando se cumple } \partial_{\mu} J^{\mu} = 0.")
        text_13.scale(0.75)
        text_13.shift(DOWN*3)
        
        self.next_slide()

        self.play(
            Write(maps), Write(text_12)
            )
        
        self.next_slide()

        self.play(
            Write(non_invariant_0)
            )
        
        self.next_slide()

        self.play(
            Write(non_invariant_1)
            )
        
        self.next_slide()

        self.play(
            Write(text_13)
            )

        self.next_slide()

        slide5_vanished = VGroup(text_9, text_12, non_invariant_1, non_invariant_0, text_13, line, maps)
        self.play(
            FadeOut(slide5_vanished)
           )

        self.next_slide()

        # Slide Final:

        paper01 = ImageMobject("images\\Paper_01.png")
        paperbox1 = Rectangle(width = 5.5, height = 3.3, color = WHITE)
        paper01.scale(0.75)
        paptex1 = ["Which Symmetry? Noether, Weyl", "and conservation of electric charge"]
        paptex1 = Paragraph(*paptex1, alignment = "center")
        paptex1.scale(0.5)
        paptex1.shift(DOWN*2.25)
        pap1_Group = VGroup(paperbox1, paptex1)
        pap1_Group.shift(LEFT*4 + UP*2)
        paper01.shift(LEFT*4 + UP*2)
        self.play(FadeIn(pap1_Group), FadeIn(paper01))

        paper02 = ImageMobject("images\\Paper_02.png")
        paper02.scale(0.75)
        paperbox2 = Rectangle(width = 5.9, height = 3, color = WHITE)
        paptex2 = ["Noether's Theorems", "and Gauge Symmetries"]
        paptex2 = Paragraph(*paptex2, alignment = "center")
        paptex2.scale(0.5)
        paptex2.shift(DOWN*2)
        pap2_Group = VGroup(paperbox2, paptex2)
        pap2_Group.shift(RIGHT*3.25 + DOWN)
        paper02.shift(RIGHT*3.25 + DOWN)
        self.play(FadeIn(pap2_Group), FadeIn(paper02))
        
        self.next_slide()

        self.wait(2)
