from manim import *
from manim_slides import Slide, ThreeDSlide
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

class slide0(Slide):
    def construct(self):
        text1 = ["Leyes de Conservación: Teoremas de", "Noether y la Conservación de la carga"]
        text1 = Paragraph(*text1, alignment = "center")
        text1.scale(0.75)

        text2 = ["Integrantes:"]
        text2 = Paragraph(*text2, alignment = "left")
        text2.scale(0.5)
        text2.shift(LEFT*3 + DOWN*1.25)

        names = ["Juan C. Rojas V.", "Thomas A. Hernández", "Claudia A. Cuellar N."]
        names = Paragraph(*names, alignment = "center", line_spacing = 1)
        names.scale(0.5)
        names.shift(DOWN*2)

        noether = ImageMobject("Noether.jpg").scale(0.5)
        noether.shift(RIGHT*4.5)
        
        grupo_presentación = VGroup(text1, text2, names).shift(UP)
        
        grupo_presentación.to_edge(LEFT)

        self.play(Write(text1),FadeIn(noether))
        self.play(Write(text2))
        self.play(Write(names))

class slide1(Slide):
    def construct(self):

        title = Text("Noether: Primer y Segundo Teorema")
        title.scale(0.75)
        line = Line([-7, 3, 0], [7, 3, 0])
        
        self.play(
            Write(title)
            )
        
        self.next_slide()

        self.play(
            title.animate.shift(UP*3.5), Create(line)
            )
        
        text_0 = Text("Convenciones:")
        text_0.scale(0.75)
        text_0.shift(UP*2.5 + LEFT*4.5)
        
        self.play(
            Write(text_0)
            )   
        
        self.next_slide()
        
        text_1 = Text("Notación vectorial:")
        text_1.scale(0.5)
        text_1.shift(UP*0.5)
        
        formulae_0 = MathTex(r"\Vec{v} = \textbf{v}")

        self.play(
            Write(text_1),
            Write(formulae_0)
        )

        pack1 = VGroup(text_1, formulae_0)

        self.next_slide()

        self.play(
            pack1.animate.shift(UP*1.75)
            )
        
        self.next_slide()

        text_2 = Text("Convención de suma de Einstein para tensores:")
        text_2.scale(0.5)
        text_2.shift(UP*0.5)

        defa = MathTex(r"\Bar{T}", r"=", r"\sum_{\mu,\nu=0}^3T^{\mu\nu}\textbf{e}_{\mu}\otimes \textbf{e}_{\nu}")
        defa.shift(DOWN*0.5)
        defa2 = MathTex(r"\Bar{T}",  r"=", r"T^{\mu\nu} \underbrace{\textbf{e}_{\mu}\otimes \textbf{e}_{\nu}}_{\text{base normal}}")
        defa2.shift(DOWN*0.5)
        defa1 = MathTex(r"\Bar{T}", r"=", r"T^{\mu\nu}\textbf{e}_{\mu}\otimes \textbf{e}_{\nu}")
        defa1.shift(DOWN*0.5)
        
        pack2 = VGroup(text_2, defa)

        self.play(
            Write(pack2)
        )
        
        self.next_slide()

        self.play(
            TransformMatchingShapes(defa, defa2),
        )

        self.next_slide()

        self.play(
            TransformMatchingShapes(defa2, defa1)
            )
        
        self.next_slide()
        
        pack3 = VGroup(pack1, text_0, text_2, defa1)

        self.play(
            FadeOut(pack3)
        )

        text_3 = Text("Elementos tensoriales:")
        text_3.scale(0.75)
        text_3.shift(UP*2.5 + LEFT*4.5)
        
        self.play(
            Write(text_3)
            )  
        
        defc = MathTex(r"\text{Covariante:} \quad T_{\mu}\textbf{e}_{\mu}\otimes \textbf{e}_{\nu}")
        defc.shift(UP*1.5)
        defc1 = MathTex(r"\text{Contravariante:} \quad T^{\mu}\textbf{e}^{\mu}\otimes \textbf{e}^{\nu}")
        defc1.shift(UP*0.8)

        pack4 = VGroup(defc, defc1)
        
        self.play(
            Write(pack4)
        )
        
        self.next_slide()
        
        text_4 = Text("Derivadas:")
        text_4.scale(0.75)
        text_4.shift(DOWN*0.5 + LEFT*5.5)
        
        self.play(
            Write(text_4)
            )  
        
        defd = MathTex(r"\frac{\partial}{\partial x^{\mu}}=\partial_{\mu}")
        defd.shift(DOWN)
        pack5 = VGroup(text_4, defd)

        self.play(
            Write(pack5)
        )
        self.next_slide()

        self.play(
            FadeOut(text_3, pack4, pack5)
            )
        
class slide2(Slide):
    def construct(self):       

        title = Text("Teoremas de Noether:")
        VGroup(title).arrange(DOWN)
        self.play(
            Write(title,shift=DOWN))   
        self.next_slide()
        
        transform_title = Tex(r"\text{Teorema I:}")

        transform_title.to_corner(UP + LEFT)

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        
        transform_text = Tex(r"Si la acción $S$ es invariante bajo un grupo continuo de transformaciones que dependen suavemente de $\rho$ parámetros constantes independientes $\omega_k$ $(k=1,2,...,\rho)$ (grupo global de simetría), entonces", tex_template=myTemplate, tex_environment="justify")
        transform_eqn = MathTex(r"\sum_i E_i\delta_0\psi_i \circeq \sum_i \partial_{\mu}B_{\mu}^{i} \quad \text{implica} \quad \sum_i E_i\frac{\partial(\delta_0\psi_i)}{\partial(\delta\omega^k)} \circeq \partial_{\mu}j_{k}^{\mu}")
        transform_text.font_size = 38.0
        transform_eqn.font_size = 38.0
        transform_text.to_edge(np.array((-1,2,0.0)))
        self.play(
            Transform(title, transform_title),
            Write(transform_text),
            Write(transform_eqn)
        )
        self.next_slide()
        self.play(
            FadeOut(title,transform_eqn,transform_text)
            )

        texta = Tex(r"\textbf{Teorema 2:}")
        texta.to_corner(UP + LEFT)

        textb = Tex(r"Si la acción $S$ es invariante bajo un grupo continuo de transformaciones que dependen suavemente de $\rho$ funciones arbitrarias independientes $p_k(x)$ $(k=1,2,...,\rho)$ y sus primeras derivadas (grupo local de simetría), entonces", tex_template=myTemplate, tex_environment="justify")
        defb = MathTex(r"\sum_i E_i\delta_0\psi_i \circeq \sum_i \partial_{\mu}B_{\mu}^{i} \quad \text{implica} \quad \sum_i E_ia_{ki} \circeq \partial_{\mu}(E_ib_{ki}^{\mu})")
        textb1 = Tex(r"Donde $a_{ki},b_{ki}^{\mu}$ son funciones de $\psi_i,\partial_{\mu}\psi_i,x^{\mu}$", tex_template=myTemplate, tex_environment="justify")
        textb.font_size = 38.0
        textb1.font_size = 38.0
        defb.font_size = 38.0
        textb.to_edge(np.array((-1,2,0.0)))
        textb1.next_to(defb,DOWN)
        self.play(
            Write(texta,shift=LEFT),
            Write(textb,shift=LEFT),
            Write(defb,shift=LEFT),
            Write(textb1,shift=LEFT)
        )
        self.next_slide()
        self.play(
            FadeOut(texta,textb,defb,textb1)
            )
        self.next_slide()

        textc = Tex("Notación:").to_corner(UP+LEFT)

        eqn1 = MathTex(r"\sum_i", r"E_i",r"\delta_0\psi_i",r"\circeq", r"\sum_i \partial_{\mu}",r"B_{\mu}^{i}")
        eqn2 = MathTex(r"\sum_i", r"E_i",r"a_{ki}", r"\circeq", r"\partial_{\mu}(E_i",r"b_{ki}^{\mu}",r")")
        eqn3 = MathTex(r"\sum_{i} \frac{E_i \partial(\delta_{0}\psi_{i})}{\partial(\delta\omega^k)} \circeq \partial_{\mu}j^{\mu}_{k}")
        eqn1.to_edge(np.array((0.0,0.0,0.0)))
        eqn2.to_edge(np.array((0.0,2.0,0.0)))
        eqn3.to_edge(np.array((0.0,-2.0,0.0)))

        eqn1[1].set_color(YELLOW)
        eqn2[1].set_color(YELLOW)
        eqn3[0][2].set_color(YELLOW)
        eqn3[0][3].set_color(YELLOW)

        self.play(
            Write(textc,shift=UP),
            Write(eqn1),
            Write(eqn2),
            Write(eqn3)
        )
        self.next_slide()

        defei = MathTex(r"\text{Expresión de Lagrange:} \quad E_i :=\frac{\partial L}{\partial\psi_i}-\partial_{\mu}\left( \frac{\partial L}{\partial(\partial_{\mu}\psi_i)}\right)")

        self.play(
            FadeOut(eqn1,eqn2,eqn3)
        )

        self.play(
            Write(defei)
        )

        self.next_slide()

        self.play(
            FadeOut(defei)
        )

        eqn1[1].set_color(WHITE)
        eqn2[1].set_color(WHITE)
        eqn3[0][2].set_color(WHITE)
        eqn3[0][3].set_color(WHITE)

        eqn1[2].set_color(YELLOW)
        eqn3[0][6].set_color(YELLOW)
        eqn3[0][7].set_color(YELLOW)
        eqn3[0][8].set_color(YELLOW)
        eqn3[0][9].set_color(YELLOW)

        self.play(
            Write(textc,shift=UP),
            Write(eqn1),
            Write(eqn2),
            Write(eqn3)
        )
        self.next_slide()

        defd0 = MathTex(r"\text{Cambio en la coordenada fija:} \quad  \delta_0\psi_i=\psi'_i(x)-\psi_i(x)")

        self.play(
            FadeOut(eqn1,eqn2,eqn3)
        )

        self.play(
            Write(defd0)
        )

        self.next_slide()

        self.play(
            FadeOut(defd0)
        )

        eqn1[2].set_color(WHITE)
        eqn3[0][6].set_color(WHITE)
        eqn3[0][7].set_color(WHITE)
        eqn3[0][8].set_color(WHITE)
        eqn3[0][9].set_color(WHITE)
        eqn1[5].set_color(YELLOW)

        self.play(
            Write(textc,shift=UP),
            Write(eqn1),
            Write(eqn2),
            Write(eqn3)
        )
        self.next_slide()

        defdB = MathTex(r"B_i^{\mu}= \left( L- \frac{\partial L}{\partial(\partial_{\nu}\psi_i)} \partial_{\nu}\psi_i\right)\delta x^{\mu}+\frac{\partial L}{\partial(\partial_{\mu}\psi_i)}\delta \psi_i")
        textdB = Tex(r"Donde $L=L(\psi_i,\partial_{\mu}\psi_i,x^{\mu})$, $\psi_i$ son componentes del campo $\psi$, $x^{\mu}$ es la variable dependiente del campo y $\partial_{mu}\psi_i=\frac{\partial}{\partial x^{\mu}}\psi i$ derivada de cada componente del campo con respecto a $x^{\mu}$", tex_template=myTemplate, tex_environment="justify")
        textdB.font_size=38
        defdB.to_edge(np.array((-5,4,0.0)))
        textdB.next_to(defdB,DOWN)
        self.play(
            FadeOut(eqn1,eqn2,eqn3)
        )

        self.play(
            Write(defdB),
            Write(textdB)
        )

        self.next_slide()

        self.play(
            FadeOut(defdB,textdB)
        )

        eqn1[5].set_color(WHITE)
        eqn3[0][21].set_color(YELLOW)
        eqn3[0][22].set_color(YELLOW)
        eqn3[0][23].set_color(YELLOW)

        self.play(
            Write(textc,shift=UP),
            Write(eqn1),
            Write(eqn2),
            Write(eqn3)
        )
        self.next_slide()

        defdj = MathTex(r"\text{Corrientes asociadas a $\omega_k$:} ")
        d12 = MathTex(r"j_{k}^{\mu}=\sum_i \left( L- \frac{\partial L}{\partial(\partial_{\nu}\psi_i)} \partial_{\nu}\psi_i\right)\frac{\partial(\delta x^{\mu})}{\partial (\delta \omega_k)}+\frac{\partial L}{\partial(\partial_{\mu}\psi_i)}\frac{\partial(\delta \psi_i)}{\partial(\delta \omega_k)}")
        defdj.to_edge(np.array((0,4,0.0)))
        # d12.font_size=38
        d12.next_to(defdj,DOWN)
        self.play(
            FadeOut(eqn1,eqn2,eqn3)
        )

        self.play(
            Write(defdj),
            Write(d12)
        )

        self.next_slide()

        self.play(
            FadeOut(defdj,d12)
        )

        eqn3[0][21].set_color(WHITE)
        eqn3[0][22].set_color(WHITE)
        eqn3[0][23].set_color(WHITE)
        eqn1[3].set_color(YELLOW)
        eqn2[3].set_color(YELLOW)
        eqn3[0][18].set_color(YELLOW)

        self.play(
            Write(textc,shift=UP),
            Write(eqn1),
            Write(eqn2),
            Write(eqn3)
        )
        self.next_slide()

        defdc = Tex(r"$\circeq$ indica aquellas ecuaciones que se mantienen independientemente del cumplimiento de las ecuaciones de movimiento de Euler-Lagrange.", tex_template=myTemplate, tex_environment="justify")
        defdc.font_size=38.0
        self.play(
            FadeOut(eqn1,eqn2,eqn3)
        )

        self.play(
            Write(defdc)
        )

        self.next_slide()

        self.play(
            FadeOut(defdc,textc)
        )


        a = Tex("¿Grupos de simetría?")
        self.play(
            Write(a)
        )

        self.next_slide()

        self.play(
            FadeOut(a)
        )

class slide3(Slide):
    def construct(self):
        title = Tex(r"\textbf{Teoría de Gauge}")
        VGroup(title).arrange(DOWN)
        self.play(
            Write(title,shift=DOWN))   
        self.next_slide()

        transform_title = Tex(r"\textbf{Grupos Gauge}")
        transform_title.to_corner(UP + LEFT)
        transform_text = Tex(r"\textbf{Invarianzas de Gauge}")
        transform_text.to_edge(np.array((0,0,0.0)))

        textf = Tex("El grupo de simetría del teorema de Noether es un grupo Gauge.")
        textf.to_edge(np.array((0,0,0.0)))
        textf1 = Tex("Transformaciones de coordenadas continuas")
        textf1.next_to(textf,DOWN)

        texta = Tex(r"Invarianza Gauge $\rightarrow$ simetría")
        texta.to_edge(np.array((0,0,0.0)))
        texta1 = Tex("Electromagnetismo clásico")
        texta1.next_to(texta,DOWN)

        self.play(
            Transform(title, transform_title),
            Write(transform_text),
                    )
        self.play(
            FadeOut(transform_text)
        )
        self.play(
            Write(textf),
            Write(textf1),
        )
        self.play(
            Transform(textf,texta),
            Transform(textf1,texta1),
        )
        self.next_slide()

        self.play(
            FadeOut(title,textf,textf1)
        )

        title2 = Tex(r"\textbf{¿Invariante con respecto a qué?}")
        VGroup(title2).arrange(DOWN)
        
        self.play(
            Write(title2,shift=DOWN))
           
        self.next_slide()

        transform_title2 = Tex(r"\textbf{Tipos de invarianza de Gauge}")
        transform_title2.to_corner(UP + LEFT)

        textb = Tex("Invarianza Gauge local")
        textb.to_edge(np.array((0,0,0.0)))
        textc = Tex("Leyes de la naturaleza invariantes a transformaciones locales.")
        textc.next_to(textb,DOWN)
        textc1 = Tex("Transformaciones en puntos individuales del espacio-tiempo.")
        textc1.next_to(textc,DOWN)


        textd = Tex("Invarianza Gauge global")
        textd.to_edge(np.array((0,0,0.0)))
        texte = Tex("Leyes de la naturaleza invariantes a transformaciones globales.")
        texte.next_to(textd,DOWN)
        texte1 = Tex("Transformaciones simultáneas en el espacio-tiempo.")
        texte1.next_to(texte,DOWN)

        self.play(
            Transform(title2,transform_title2),
            Write(textb),
            Write(textc),
            Write(textc1)
        )
        
        self.next_slide()

        self.play(
            FadeOut(textb,textc,textc1)
        )

        self.next_slide()
        
        self.play(
            Write(textd),
            Write(texte),
            Write(texte1)
        )

        self.next_slide()

        self.play(
            FadeOut(textd,texte,title2,texte1)
        )

        title3 = Tex(r"\textbf{Caso específico}")
        VGroup(title3).arrange(DOWN)

        self.next_slide()

        self.play(
            Write(title3,shift=DOWN))   
        
        self.next_slide()

        transform_title3 = Tex(r"\textbf{Conservación local de la carga.}")
        
        self.play(
            Transform(title3,transform_title3)
        )
        self.next_slide()

        self.play(FadeOut(title3))

class slide4(Slide):
    
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
        
class slide5(Slide):
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

class slide6(Slide):
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
