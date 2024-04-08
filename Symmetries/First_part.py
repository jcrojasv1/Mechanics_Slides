from manim import *
from manim_slides import Slide,ThreeDSlide
import random
import numpy as np

#manim -pql "c:\Users\clauw\Documents\Programming\Trabajos-Manim\Manim-projects\First_part.py" PresentationSlide

#presentaciones
class PresentationSlide(Slide):
    def construct(self):
        text1 = Tex(r"$\textbf{Conservación de la carga}$")
        text2 = Tex(r"$\text{Integrantes:}$")
        text3 = Tex(r"$\text{Juan Carlos Rojas}$")
        text4 = Tex(r"$\text{Thomas Andrade}$")
        text5 = Tex(r"$\text{Claudia Cuellar}$")

        text2.next_to(text1,DOWN)
        text3.next_to(text2,DOWN)
        text4.next_to(text3,DOWN)
        text5.next_to(text4,DOWN)
        self.play(Write(text1),shift=UP)
        self.play(Write(eqn))
        self.play(Write(text2))
        self.play(Write(text3),Write(text4),Write(text5))

        self.wait(2)

class Slide1_1(Slide):
    def construct(self):
        title = Tex(r"\textbf{Convenciones}")
        VGroup(title).arrange(DOWN)
        self.play(
            Write(title,shift=DOWN))   
        self.next_slide()
        
        transform_title = Tex("Notación vectorial:")
        transform_title.to_corner(UP + LEFT)
        
        transform_eqn = MathTex(r"\Vec{v}=\textbf{v}")
        transform_eqn.to_edge(np.array((-1,2,0.0)))
        self.play(
            Transform(title, transform_title),
            Write(transform_eqn)
        )
        self.next_slide()
        
        texta = Tex("Convención de suma de Einstein para tensores:")
        defa = MathTex(r"\Bar{T}=\sum_{\mu,\nu=0}^3T^{\mu\nu}\textbf{e}_{\mu}\otimes \textbf{e}_{\nu}")
        defa2 = Tex(r"$\underbrace{\textbf{e}_{\mu}\otimes \textbf{e}_{\nu}}_{\text{base normal}} $")
        defa1 = Tex(r"$\Bar{T}=T^{\mu\nu}\textbf{e}_{\mu}\otimes \textbf{e}_{\nu}$")
        defa11 = Tex(r"$\Bar{T}=T^{\mu\nu}\textbf{e}_{\mu}\otimes \textbf{e}_{\nu}$")
        
        
        VGroup(texta,defa).arrange(DOWN)
        self.play(
            Write(texta,shift=LEFT),
            Write(defa,shift=LEFT)
        )
        self.play(
            Transform(defa, defa1),
            Transform(defa, defa2))
        self.wait(1)
        self.play(
            Transform(texta, (texta.copy()).to_edge(LEFT)),
            Transform(defa , (defa11).to_edge(LEFT))
        )
        
        self.next_slide()

        textb = Tex("Métrica de Minkowski:")
        defb = Matrix([[1, 0,0,0], [0, -1,0,0],[0, 0,-1,0],[0, 0,0,-1]],
            left_bracket="(",
            right_bracket=")").add_background_rectangle()
        defb1 = Tex(r"$\eta_{\mu\nu}  =\textit{diag}(1,-1,-1,-1)$")
        
        VGroup(textb,defb).arrange(DOWN)
        self.play(
            FadeOut(title,transform_eqn,texta,defa),
            Write(textb,shift=LEFT),
            Write(defb,shift=LEFT)
        )

        self.play(
            Write(transform_eqn),
            Write(title),
            Write(texta),
            Write(defa),
            Transform(textb, (textb.copy()).to_edge(LEFT).move_to(np.array((-4,-2,0.0)))),
            Transform(defb, (defb1).to_edge(LEFT).move_to(np.array((-4,-3,0.0))))
        )
        
        self.next_slide()

        self.play(
            FadeOut(title,transform_eqn,texta,defa,textb,defb)
        )
        
        textc = Tex("Elementos tensoriales:")
        defc = Tex(r"$\text{Covariante:} \quad T_{\mu}\textbf{e}_{\mu}\otimes \textbf{e}_{\nu}$")
        defc1 = Tex(r"$\text{Contravariante:} \quad T^{\mu}\textbf{e}^{\mu}\otimes \textbf{e}^{\nu}$")
        VGroup(textc,defc,defc1).arrange(DOWN)
        VGroup(textc,defc,defc1).to_corner(UP+LEFT)
        
        self.play(
            Write(textc,shift=LEFT),
            Write(defc,shift=LEFT),
            Write(defc1,shift=LEFT)
        )
        self.next_slide()
        self.play(
            Transform(textc, (textc.copy()).to_edge(LEFT)),
            Transform(defc, (defc.copy()).to_edge(LEFT)),
            Transform(defc1, (defc1.copy()).to_edge(LEFT))
        )
        
        self.next_slide()
        
        textd = Tex("Derivadas:")
        defd = Tex(r"$\frac{\partial}{\partial x^{\mu}}=\partial_{\mu}$")
        VGroup(textd,defd).arrange(DOWN)
        self.play(
            Write(textd,shift=LEFT),
            Write(defd,shift=LEFT)
        )

        self.play(
            Transform(textd, (textd.copy()).to_edge(LEFT)),
            Transform(defd, (defd.copy()).to_edge(LEFT))
        )
        
        self.next_slide()

        self.play(
            FadeOut(textc,defc,defc1,textd,defd)
            )
        
class Slide1_2(Slide):
    def construct(self):
        title = Tex(r"\textbf{Teorema de Noether}")
        VGroup(title).arrange(DOWN)
        self.play(
            Write(title,shift=DOWN))   
        self.next_slide()
        
        transform_title = Tex(r"\textbf{Teorema 1:}")
        transform_title.to_corner(UP + LEFT)

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
        
        transform_text = Tex(r"Si la acción S es invariante bajo un grupo continuo de transformaciones que dependen suavemente de $\rho$ parámetros constantes independientes $\omega_k$ $(k=1,2,...,\rho)$ (grupo global de simetría), entonces", tex_template=myTemplate, tex_environment="justify")
        transform_eqn = MathTex(r"\sum_i E_i\delta_0\psi_i \circeq \sum_i \partial_{\mu}B_{\mu}^{i} \quad \text{implica} \quad \sum_i E_i\frac{\partial(\delta_0\psi_i)}{\partial(\delta\omega^k)} \circeq \partial_{\mu}j_{k}^{\mu}")
        transform_text.font_size = 38.0
        transform_eqn.font_size = 38.0
        transform_text.to_edge(np.array((-1,2,0.0)))
        self.play(
            Transform(title, transform_title),
            Write(transform_text),
            Write(transform_eqn)
        )
        self.wait(5)
        self.play(
            FadeOut(title,transform_eqn,transform_text)
            )
        self.next_slide()

        texta = Tex(r"\textbf{Teorema 2:}")
        texta.to_corner(UP + LEFT)

        textb = Tex(r"Si la acción S es invariante bajo un grupo continuo de transformaciones que dependen suavemente de $\rho$ funciones arbitrarias independientes $p_k(x)$ $(k=1,2,...,\rho)$ y sus primeras derivadas (grupo local de simetría), entonces", tex_template=myTemplate, tex_environment="justify")
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
        self.wait(5)
        self.play(
            FadeOut(texta,textb,defb,textb1)
            )
        self.next_slide()

        textc = Tex("Notación:")
        VGroup(textc).arrange(DOWN)
        VGroup(textc).to_corner(UP+LEFT)

        eqn1 = MathTex(r"\sum_i", r"E_i",r"\delta_0\psi_i",r"\circeq", r"\sum_i \partial_{\mu}",r"B_{\mu}^{i}")
        eqn2 = MathTex(r"\sum_i", r"E_i",r"a_{ki}", r"\circeq", r"\partial_{\mu}(E_i",r"b_{ki}^{\mu}",r")")
        eqn3 = MathTex(r"\sum_i", r"E_i",r"\partial(\delta_0\psi_i)",r"\over",r"\partial(\delta\omega^k)" ,r"\circeq",r"\partial_{\mu}",r"j_{k}^{\mu}")

        eqn1.to_edge(np.array((0.0,0.0,0.0)))
        eqn2.to_edge(np.array((0.0,2.0,0.0)))
        eqn3.to_edge(np.array((0.0,-2.0,0.0)))

        eqn1[1].set_color(YELLOW)
        eqn2[1].set_color(YELLOW)
        eqn3[1].set_color(YELLOW)

        self.play(
            Write(textc,shift=UP),
            Write(eqn1),
            Write(eqn2),
            Write(eqn3)
        )
        self.wait(2)

        defei = MathTex(r"\text{Expresión de Lagrange:} \quad E_i :=\frac{\partial L}{\partial\psi_i}-\partial_{\mu}\left( \frac{\partial L}{\partial(\partial_{\mu}\psi_i)}\right)")

        self.play(
            FadeOut(eqn1,eqn2,eqn3)
        )

        self.play(
            Write(defei)
        )

        self.wait(1)

        self.play(
            FadeOut(defei)
        )

        eqn1[1].set_color(WHITE)
        eqn2[1].set_color(WHITE)
        eqn3[1].set_color(WHITE)

        eqn1[2].set_color(YELLOW)
        eqn3[2].set_color(YELLOW)

        self.play(
            Write(textc,shift=UP),
            Write(eqn1),
            Write(eqn2),
            Write(eqn3)
        )
        self.wait(2)

        defd0 = MathTex(r"\text{Cambio en la coordenada fija:} \quad  \delta_0\psi_i=\psi'_i(x)-\psi_i(x)")

        self.play(
            FadeOut(eqn1,eqn2,eqn3)
        )

        self.play(
            Write(defd0)
        )

        self.wait(1)

        self.play(
            FadeOut(defd0)
        )

        eqn1[2].set_color(WHITE)
        eqn3[2].set_color(WHITE)
        eqn1[5].set_color(YELLOW)

        self.play(
            Write(textc,shift=UP),
            Write(eqn1),
            Write(eqn2),
            Write(eqn3)
        )
        self.wait(2)

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

        self.wait(1)

        self.play(
            FadeOut(defdB,textdB)
        )

        eqn1[5].set_color(WHITE)
        eqn3[7].set_color(YELLOW)

        self.play(
            Write(textc,shift=UP),
            Write(eqn1),
            Write(eqn2),
            Write(eqn3)
        )
        self.wait(2)

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

        self.wait(1)

        self.play(
            FadeOut(defdj,d12)
        )

        eqn3[7].set_color(WHITE)
        eqn1[3].set_color(YELLOW)
        eqn2[3].set_color(YELLOW)
        eqn3[5].set_color(YELLOW)

        self.play(
            Write(textc,shift=UP),
            Write(eqn1),
            Write(eqn2),
            Write(eqn3)
        )
        self.wait(2)

        defdc = Tex(r"$\circeq$ indica aquellas ecuaciones que se mantienen independientemente del cumplimiento de las ecuaciones de movimiento de Euler-Lagrange.", tex_template=myTemplate, tex_environment="justify")
        defdc.font_size=38.0
        self.play(
            FadeOut(eqn1,eqn2,eqn3)
        )

        self.play(
            Write(defdc)
        )

        self.wait(1)

        self.play(
            FadeOut(defdc,textc)
        )

        self.next_slide()

        a = Tex("¿Grupos de simetría?")
        self.play(
            Write(a)
        )

        self.wait(1)

        self.play(
            FadeOut(a)
        )

class Slide1_3(Slide):
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
        self.wait(3)

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
        self.wait(3)
        self.play(
            FadeOut(textb,textc,textc1)
        )
        
        self.play(
            Write(textd),
            Write(texte),
            Write(texte1)
        )
        self.wait(2)
        self.play(
            FadeOut(textd,texte,title2,texte1)
        )

        title3 = Tex(r"\textbf{Caso específico}")
        VGroup(title3).arrange(DOWN)
        self.play(
            Write(title3,shift=DOWN))   
        self.next_slide()

        transform_title3 = Tex(r"\textbf{Conservación local de la carga.}")
        
        self.play(
            Transform(title3,transform_title3)
        )
        self.wait(3)

        self.play(FadeOut(title3))







