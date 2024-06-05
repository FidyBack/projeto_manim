from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.elevenlabs import ElevenLabsService


class test(Scene):
    def construct(self):
        number_line = NumberLine(
            x_range=[0, 1, 1], length=2.5, include_numbers=True
        ).shift(DOWN * 2)
        pure_label = Text("Purest State", font_size=20).next_to(
            number_line.get_left(), DOWN * 1.75
        )
        impure_label = Text("Most Impure State", font_size=20).next_to(
            number_line.get_right(), DOWN * 1.75
        )
        self.play(Write(number_line), Write(pure_label), Write(impure_label))
        self.wait(0.5)


class CreateDecisionTree(VoiceoverScene, MovingCameraScene):
    def construct(self):
        # Voice Configuration
        self.set_speech_service(
            ElevenLabsService(
                voice_name="Adam",
                voice_settings={"stability": 0.01, "similarity_boost": 0.6},
                model="eleven_multilingual_v2",
            )
        )

        # Parte 1 - Introdução
        introduction_voiceover_01 = "Neste vídeo, vamos mostrar como é o funcionamento de uma árvore de decisão."
        introduction_voiceover_02 = "Iremos explicar como ela é criada, como funciona e como são calculadas as medidas de impureza."
        introduction_voiceover_03 = "Vamos primeiro criar uma pequena base de dados para exemplificar o funcionamento da árvore."
        introduction_voiceover_04 = (
            "A base de dados é composta por 3 classes: Basquete, Sumô e Jockey."
        )
        introduction_voiceover_05 = "Cada classe é representada por um ponto no gráfico, onde o eixo horizontal representa o peso e o eixo vertical a altura."
        introduction_voiceover_06 = "A partir deste gráfico, vamos criar uma árvore de decisão que irá classificar os pontos em suas respectivas classes."
        introduction_voiceover_15 = "Vimos como é feito a classificação dos pontos em uma árvore de decisão. Mas como os parâmetros são escolhidos?"

        with self.voiceover(text=introduction_voiceover_01) as tracker:
            text_intro = Text("Criando uma Árvore de Decisão")
            self.play(Write(text_intro), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text=introduction_voiceover_02) as tracker:
            pass
        self.wait(0.5)

        self.play(text_intro.animate.scale(0.5))
        self.play(text_intro.animate.to_edge(UP * 0.5))

        with self.voiceover(text=introduction_voiceover_03) as tracker:
            plane = self.create_graph(tracker)
        self.wait(0.5)

        points = [
            (140, 2.15, RED),
            (130, 1.70, BLUE),
            (79, 1.70, GREEN),
            (65, 1.72, GREEN),
            (120, 1.70, BLUE),
            (125, 1.75, BLUE),
            (120, 2.05, RED),
            (75, 1.79, GREEN),
            (115, 1.95, RED),
        ]
        with self.voiceover(
            text=introduction_voiceover_04 + introduction_voiceover_05
        ) as tracker:
            self.add_points_to_graph(plane, points)
        self.wait(0.5)

        with self.voiceover(text=introduction_voiceover_06) as tracker:
            pass
        self.wait(0.5)

        tree = self.create_fisrt_tree(points)

        with self.voiceover(text=introduction_voiceover_15) as tracker:
            pass
        self.wait(0.5)

        self.clear_screen()
        tree.move_to(ORIGIN)

        # Parte 2 - Como funciona
        hiw_voiceover_01 = "Isso é feito com base em medidas de impureza."
        hiw_voiceover_02 = "As medidas de impureza são utilizadas para calcular a pureza dos nós da árvore: quanto mais puro o nó, mais homogênea é a classe dos pontos que estão nele."
        hiw_voiceover_03 = "Vamos pegar a árvore que criamos anteriormente e calcular as medidas de impureza de cada nó."
        hiw_voiceover_09 = "Assim, é possível reparar que, quanto mais descemos na árvore, mais puros são os nós."

        with self.voiceover(text=hiw_voiceover_01) as tracker:
            impurity_text = Text("Medidas de Impureza")
            self.play(Write(impurity_text))
        self.wait(0.5)

        with self.voiceover(text=hiw_voiceover_02) as tracker:
            pass
        self.wait(0.5)

        self.play(impurity_text.animate.scale(0.5))
        self.play(impurity_text.animate.to_edge(UP * 0.5))

        with self.voiceover(text=hiw_voiceover_03) as tracker:
            self.play(Create(tree))
        self.wait(0.5)

        self.add_proportions(tree)
        with self.voiceover(text=hiw_voiceover_09) as tracker:
            pass
        self.wait(0.5)

        self.clear_screen()

        # Parte 3 - Equações
        equation_voiceover_01 = (
            "Agora, vamos explicar como são calculadas as medidas de impureza."
        )

        with self.voiceover(text=equation_voiceover_01) as tracker:
            impurity_math_text = Text("Calculo de Impureza")
            impurity_math_text.shift(UP * 2)
            self.play(Write(impurity_math_text))
        self.wait(0.5)

        self.create_equations(impurity_math_text)
        self.wait(3)

    def create_graph(self, tracker):
        plane = (
            NumberPlane(
                x_range=[0, 140, 20],
                x_length=6,
                y_range=[0, 3, 0.5],
                y_length=6.5,
            )
            .to_edge(LEFT, buff=0)
            .to_edge(DOWN, buff=0.5)
            .add_coordinates()
        )
        labels = VGroup(
            Text("Peso").scale(0.5).next_to(plane.x_axis.get_right(), UP),
            Text("Altura")
            .scale(0.5)
            .next_to(plane.y_axis.get_top(), RIGHT)
            .shift(0.2 * UP),
        )
        dot1 = Dot(color=RED).scale(0.5)
        text1 = Text("Basquete", font="Roboto").scale(0.5).next_to(dot1, RIGHT)

        dot2 = Dot(color=BLUE).scale(0.5).next_to(dot1, DOWN)
        text2 = Text("Sumô", font="Roboto").scale(0.5).next_to(dot2, RIGHT)

        dot3 = Dot(color=GREEN).scale(0.5).next_to(dot2, DOWN)
        text3 = Text("Jockey", font="Roboto").scale(0.5).next_to(dot3, RIGHT)

        legend = (
            VGroup(dot1, text1, dot2, text2, dot3, text3)
            .next_to(plane, UP + RIGHT)
            .shift(2 * DOWN)
        )

        self.play(
            Create(plane), Create(labels), Create(legend), run_time=tracker.duration
        )

        return plane

    def add_points_to_graph(self, graph, points: list):
        vg_points = VGroup()

        for point in points:
            x, y, color = point
            dot = Dot(graph.coords_to_point(x, y), color=color)
            self.play(Create(dot), run_time=0.2)
            vg_points.add(dot)

        return vg_points

    def create_fisrt_tree(self, points: list):
        introduction_voiceover_07 = "Vamos começar criando a raiz da árvore. A raiz irá classificar os pontos de acordo com a altura."
        introduction_voiceover_08 = "Se a altura do ponto for maior que 1 e 90, o ponto irá para o nó da esquerda."
        introduction_voiceover_09 = "Casos contrário, o ponto irá para o da direita."
        introduction_voiceover_10 = (
            "No nó da direita, os pontos serão classificados de acordo com o peso."
        )
        introduction_voiceover_11 = (
            "Se o peso for maior que 100, o ponto irá para o nó da esquerda."
        )
        introduction_voiceover_12 = "Caso contrário, o ponto irá para a direita."
        introduction_voiceover_13 = "Após este processo, é possível classificar os pontos em suas respectivas classes."
        introduction_voiceover_14 = "Os pontos vermelhos são classificados como Basquete, os azuis como Sumô e os verdes como Jockey."

        ######## Root Node ########
        with self.voiceover(text=introduction_voiceover_07) as tracker:
            tree_root = RoundedRectangle(height=1, width=2.3, corner_radius=0.2)
            tree_root.set_fill(BLUE, opacity=0.5)
            tree_root.to_edge(UP, buff=1.5).to_edge(RIGHT, buff=3)
            self.play(Create(tree_root))

            b, g, r = 0, 0, 0
            dots_01 = []
            for point in points:
                _, _, color = point
                if color == BLUE:
                    b += 1
                    dot = Dot(color=color).next_to(tree_root, RIGHT * b, buff=0.2)
                    dot.shift(UP * 0.25)
                elif color == RED:
                    r += 1
                    dot = Dot(color=color).next_to(tree_root, RIGHT * r, buff=0.2)
                else:
                    g += 1
                    dot = Dot(color=color).next_to(tree_root, RIGHT * g, buff=0.2)
                    dot.shift(DOWN * 0.25)
                dots_01.append(dot)
            self.play(AnimationGroup(*[Create(dot) for dot in dots_01]), run_time=0.5)

            text_height = Text("Altura > 1.90", font="Roboto", font_size=20)
            text_height.move_to(tree_root)
            self.play(Write(text_height))
        self.wait(0.5)

        ######## Leaf Node 1 ########
        with self.voiceover(text=introduction_voiceover_08) as tracker:
            node1 = RoundedRectangle(height=1, width=2, corner_radius=0.2)
            node1.set_fill(GREEN, opacity=0.5).next_to(tree_root, DOWN, buff=1.5).shift(
                LEFT * 1.1
            )
            arrow_r1 = Arrow(
                start=tree_root.get_bottom(),
                end=node1.get_top(),
                buff=0,
                max_tip_length_to_length_ratio=0.1,
                stroke_width=4,
            )
            arrow_text_r1 = Text("Sim", font="Roboto", font_size=20).next_to(
                arrow_r1, LEFT * 0.3
            )
            self.play(Create(node1), Create(arrow_r1), Write(arrow_text_r1))

            r = 0
            dots_02 = []
            for point in points:
                _, _, color = point
                if color == RED:
                    r += 1
                    dot = Dot(color=color).next_to(node1, LEFT * r, buff=0.2)
                    dots_02.append(dot)

            self.play(AnimationGroup(*[Create(dot) for dot in dots_02]), run_time=0.5)
        self.wait(0.5)

        ######## Leaf Node 2 ########
        with self.voiceover(text=introduction_voiceover_09) as tracker:
            node2 = RoundedRectangle(height=1, width=2, corner_radius=0.2)
            node2.set_fill(BLUE, opacity=0.5).next_to(tree_root, DOWN, buff=1.5).shift(
                RIGHT * 1.1
            )
            arrow_r2 = Arrow(
                start=tree_root.get_bottom(),
                end=node2.get_top(),
                buff=0,
                max_tip_length_to_length_ratio=0.1,
                stroke_width=4,
            )
            arrow_text_r2 = Text("Não", font="Roboto", font_size=20).next_to(
                arrow_r2, RIGHT * 0.4
            )
            self.play(Create(node2), Create(arrow_r2), Write(arrow_text_r2))

            b, g = 0, 0
            dots_03 = []
            for point in points:
                _, _, color = point
                if color == BLUE:
                    b += 1
                    dot = (
                        Dot(color=color)
                        .next_to(node2, RIGHT * b, buff=0.2)
                        .shift(UP * 0.125)
                    )
                    dots_03.append(dot)
                elif color == GREEN:
                    g += 1
                    dot = (
                        Dot(color=color)
                        .next_to(node2, RIGHT * g, buff=0.2)
                        .shift(DOWN * 0.125)
                    )
                    dots_03.append(dot)

            self.play(AnimationGroup(*[Create(dot) for dot in dots_03]), run_time=0.5)
        self.wait(0.5)

        with self.voiceover(text=introduction_voiceover_10) as tracker:
            text_weight = Text("Peso > 100", font="Roboto", font_size=20).move_to(node2)
            self.play(Write(text_weight))
        self.wait(0.5)

        ######## Leaf Node 3 ########
        with self.voiceover(text=introduction_voiceover_11) as tracker:
            node3 = RoundedRectangle(height=1, width=2, corner_radius=0.2)
            node3.set_fill(GREEN, opacity=0.5).next_to(node2, DOWN, buff=1.5).shift(
                LEFT * 1.1
            )
            arrow_r3 = Arrow(
                start=node2.get_bottom(),
                end=node3.get_top(),
                buff=0,
                max_tip_length_to_length_ratio=0.1,
                stroke_width=4,
            )
            arrow_text_r3 = Text("Sim", font="Roboto", font_size=20).next_to(
                arrow_r3, LEFT * 0.3
            )
            self.play(Create(node3), Create(arrow_r3), Write(arrow_text_r3))

            b = 0
            dots_04 = []
            for point in points:
                _, _, color = point
                if color == BLUE:
                    b += 1
                    dot = Dot(color=color).next_to(node3, LEFT * b, buff=0.2)
                    dots_04.append(dot)

            self.play(AnimationGroup(*[Create(dot) for dot in dots_04]), run_time=0.5)
        self.wait(0.5)

        ######## Leaf Node 4 ########
        with self.voiceover(text=introduction_voiceover_12) as tracker:
            node4 = RoundedRectangle(height=1, width=2, corner_radius=0.2)
            node4.set_fill(GREEN, opacity=0.5).next_to(node2, DOWN, buff=1.5).shift(
                RIGHT * 1.1
            )
            arrow_r4 = Arrow(
                start=node2.get_bottom(),
                end=node4.get_top(),
                buff=0,
                max_tip_length_to_length_ratio=0.1,
                stroke_width=4,
            )
            arrow_text_r4 = Text("Não", font="Roboto", font_size=20).next_to(
                arrow_r4, RIGHT * 0.4
            )
            self.play(Create(node4), Create(arrow_r4), Write(arrow_text_r4))

            g = 0
            dots_05 = []
            for point in points:
                _, _, color = point
                if color == GREEN:
                    g += 1
                    dot = Dot(color=color).next_to(node4, RIGHT * g, buff=0.2)
                    dots_05.append(dot)

            self.play(AnimationGroup(*[Create(dot) for dot in dots_05]), run_time=0.5)
        self.wait(0.5)

        ######## Classification ########
        with self.voiceover(text=introduction_voiceover_13) as tracker:
            pass
        self.wait(0.5)

        with self.voiceover(text=introduction_voiceover_14) as tracker:
            text_basket = Text("Basquete", font="Roboto", font_size=20).move_to(node1)
            self.play(Write(text_basket))

            text_sumo = Text("Sumô", font="Roboto", font_size=20).move_to(node3)
            self.play(Write(text_sumo))

            text_jockey = Text("Jockey", font="Roboto", font_size=20).move_to(node4)
            self.play(Write(text_jockey))
        self.wait(0.5)

        # Create the VGroup
        tree = VGroup(
            tree_root,
            node1,
            node2,
            node3,
            node4,
            arrow_r1,
            arrow_r2,
            arrow_r3,
            arrow_r4,
            arrow_text_r1,
            arrow_text_r2,
            arrow_text_r3,
            arrow_text_r4,
            text_height,
            text_weight,
            text_basket,
            text_sumo,
            text_jockey,
            *dots_01,  # 19
            *dots_02,  # 19+9 = 28
            *dots_03,  # 28+3 = 31
            *dots_04,  # 31+6 = 37
            *dots_05  # 37+3 = 40
        )

        return tree

    def add_proportions(self, tree):
        hiw_voiceover_04 = "No primeiro nó, temos uma proporção igual de pontos de cada classe: um terço para cada."
        hiw_voiceover_05 = "Porém, conforme descemos na árvore, a proporção dos pontos de cada classe muda."
        hiw_voiceover_06 = "No segundo nó, todos os pontos são da classe Basquete, sendo esse o estado mais puro possível para um nó."
        hiw_voiceover_07 = "No terceiro nó, temos uma proporção igual de pontos das classes Sumô e Jockey"
        hiw_voiceover_08 = "Nos últimos nós, todos os pontos são da mesma classe, sendo o estado mais puro possível."

        ######## Root Node ########
        with self.voiceover(text=hiw_voiceover_04) as tracker:
            dots_o1 = tree[24]
            proportion_text = MathTex(
                r"p = \left[ \frac{1}{3}, \frac{1}{3}, \frac{1}{3} \right]"
            ).next_to(dots_o1, RIGHT * 1.5)
            proportion_text.scale(0.7)
            proportion_text[0][3:6].set_color(BLUE)
            proportion_text[0][7:10].set_color(RED)
            proportion_text[0][11:14].set_color(GREEN)
            self.play(Write(proportion_text))
        self.wait(0.5)

        with self.voiceover(text=hiw_voiceover_05) as tracker:
            pass
        self.wait(0.5)

        ######## Leaf Node 1 ########
        with self.voiceover(text=hiw_voiceover_06) as tracker:
            dots_o2 = tree[28]
            proportion_text_2 = MathTex(r"p = \left[ 0, 1, 0 \right]").next_to(
                dots_o2, LEFT * 1.5
            )
            proportion_text_2.scale(0.7)
            proportion_text_2[0][3].set_color(BLUE)
            proportion_text_2[0][5].set_color(RED)
            proportion_text_2[0][7].set_color(GREEN)
            self.play(Write(proportion_text_2))
        self.wait(0.5)

        ######## Leaf Node 2 ########
        with self.voiceover(text=hiw_voiceover_07) as tracker:
            dots_o3 = tree[31]
            proportion_text_3 = MathTex(
                r"p = \left[ \frac{1}{2}, 0, \frac{1}{2} \right]"
            ).next_to(dots_o3, RIGHT * 1.5)
            proportion_text_3.scale(0.7)
            proportion_text_3[0][3:6].set_color(BLUE)
            proportion_text_3[0][7].set_color(RED)
            proportion_text_3[0][9:12].set_color(GREEN)
            self.play(Write(proportion_text_3))
        self.wait(0.5)

        ######## Leaf Node 3 and 4 ########
        with self.voiceover(text=hiw_voiceover_08) as tracker:
            dots_o4 = tree[37]
            proportion_text_4 = MathTex(r"p = \left[ 1, 0, 0 \right]").next_to(
                dots_o4, LEFT * 1.5
            )
            proportion_text_4.scale(0.7)
            proportion_text_4[0][3].set_color(BLUE)
            proportion_text_4[0][5].set_color(RED)
            proportion_text_4[0][7].set_color(GREEN)
            self.play(Write(proportion_text_4))
            self.wait()

            dots_o5 = tree[40]
            proportion_text_5 = MathTex(r"p = \left[ 0, 0, 1 \right]").next_to(
                dots_o5, RIGHT * 1.5
            )
            proportion_text_5.scale(0.7)
            proportion_text_5[0][3].set_color(BLUE)
            proportion_text_5[0][5].set_color(RED)
            proportion_text_5[0][7].set_color(GREEN)
            self.play(Write(proportion_text_5))
        self.wait(0.5)

    def create_equations(self, impurity_text):
        equation_voiceover_02 = (
            "As medidas de impureza mais comuns são a Entropia e o Gini."
        )
        equation_voiceover_03 = "A Entropia é uma medida de impureza que mede a aleatoriedade e desordem dos dados. Quanto maior a entropia, mais imprevísiveis e impuros são os dados."
        equation_voiceover_04 = "A Entropia é calculada pela seguinte fórmula:"
        equation_voiceover_05 = "Onde Ê é a Entropia, c é o número de classes, e p i é a proporção de pontos da classe i."
        equation_voiceover_06 = "O Gíni é uma medida de impureza que mede a probabilidade de classificar erroneamente um ponto. Quanto maior o Gíni, mais impuros são os dados e mais difícil é classificá-los."
        equation_voiceover_07 = "O Gíni é calculado pela seguinte fórmula:"
        equation_voiceover_08 = "Onde G é o Gíni, c é o número de classes, e p i é a proporção de pontos da classe i."
        equation_voiceover_09 = "Ambas medidas variam de 0 a 1, sendo 0 o estado mais puro e 1 o estado mais impuro."

        entropy_text = (
            Text("Entropia", font_size=35)
            .next_to(impurity_text, DOWN * 2.5, buff=0.5)
            .shift(LEFT * 2)
        )

        gini_text = (
            Text("Gini", font_size=35)
            .next_to(impurity_text, DOWN * 2.5, buff=0.5)
            .shift(RIGHT * 2)
        )

        arrow_entropy = Arrow(
            start=impurity_text.get_bottom(),
            end=entropy_text.get_top(),
            buff=0.2,
            max_tip_length_to_length_ratio=0.1,
            stroke_width=4,
        )

        arrow_gini = Arrow(
            start=impurity_text.get_bottom(),
            end=gini_text.get_top(),
            buff=0.2,
            max_tip_length_to_length_ratio=0.1,
            stroke_width=4,
        )

        entropy_equation = (
            MathTex("E = -\\sum_{i=1}^{c} p_i \\log_2(p_i)")
            .scale(0.7)
            .next_to(entropy_text, DOWN * 1.5)
        )

        gini_equation = (
            MathTex("G = 1 - \\sum_{i=1}^{c} p_i^2")
            .scale(0.7)
            .next_to(gini_text, DOWN * 1.5)
        )

        entropy_group = VGroup(entropy_text, entropy_equation)
        gini_group = VGroup(gini_text, gini_equation)

        with self.voiceover(text=equation_voiceover_02) as tracker:
            self.play(
                Create(arrow_entropy),
                Create(arrow_gini),
                Write(entropy_text),
                Write(gini_text),
            )
        self.wait(0.5)

        self.camera.frame.save_state()
        with self.voiceover(text=equation_voiceover_03) as tracker:
            self.play(
                self.camera.frame.animate.set(
                    width=entropy_group.get_width() + 1
                ).move_to(entropy_group)
            )
        self.wait(0.5)

        with self.voiceover(text=equation_voiceover_04) as tracker:
            self.play(Write(entropy_equation))
        self.wait(0.5)

        with self.voiceover(text=equation_voiceover_05) as tracker:
            pass
        self.wait(0.5)

        with self.voiceover(equation_voiceover_06) as tracker:
            self.play(
                self.camera.frame.animate.set(width=gini_group.get_width() + 1).move_to(
                    gini_group
                )
            )
        self.wait(0.5)

        with self.voiceover(equation_voiceover_07) as tracker:
            self.play(Write(gini_equation))
        self.wait(0.5)

        with self.voiceover(equation_voiceover_08) as tracker:
            pass
        self.wait(0.5)

        self.play(Restore(self.camera.frame))

        number_line = NumberLine(
            x_range=[0, 1, 1], length=2.5, include_numbers=True
        ).shift(DOWN * 2)
        pure_label = Text("Purest State", font_size=20).next_to(
            number_line.get_left(), DOWN * 1.75
        )
        impure_label = Text("Most Impure State", font_size=20).next_to(
            number_line.get_right(), DOWN * 1.75
        )
        with self.voiceover(equation_voiceover_09) as tracker:
            self.play(Write(number_line), Write(pure_label), Write(impure_label))
        self.wait(0.5)

    def clear_screen(self, obj=None):
        if not obj:
            self.play(*[FadeOut(mob) for mob in self.mobjects])
        else:
            self.play(*[FadeOut(mob) for mob in obj])
