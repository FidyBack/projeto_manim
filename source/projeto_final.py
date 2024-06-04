from manim import *

# class SquareToCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set color and transparency

#         square = Square()  # create a square
#         square.rotate(PI / 4)  # rotate a certain amount

#         self.play(Create(square))  # animate the creation of the square
#         self.play(Transform(square, circle))  # interpolate the square into the circle
#         self.play(FadeOut(square))  # fade out animation


# class AnimatedSquareToCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         square = Square()  # create a square

#         self.play(Create(square))  # show the square on screen
#         self.play(square.animate.flip(UP))
#         self.play(Transform(square, circle))  # rotate and transform the square into a circle simultaneously
#         self.play(
#             square.animate.set_fill(PINK, opacity=0.5)
#         )  # color the circle on screen

# class DifferentRotations(Scene):
#     def construct(self):
#         left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
#         right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
#         self.play(
#             left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
#         )
#         self.wait()

# class TwoTransforms(Scene):
#     def transform(self):
#         a = Circle()
#         b = Square()
#         c = Triangle()
#         self.play(Transform(a, b))
#         self.play(Transform(a, c))
#         self.play(FadeOut(a))

#     def replacement_transform(self):
#         a = Circle()
#         b = Square()
#         c = Triangle()
#         self.play(ReplacementTransform(a, b))
#         self.play(ReplacementTransform(b, c))
#         self.play(FadeOut(c))

#     def construct(self):
#         self.transform()
#         self.wait(0.5)  # wait for 0.5 seconds
#         self.replacement_transform()


# Create a class that calls the DecisionTree class, and the creates a decision tree with a root node
class CreateDecisionTree(Scene):
    def construct(self):
        # Parte 1 - Introdução
        text_intro = Text("Criando uma Árvore de Decisão")
        self.play(Write(text_intro))
        self.wait()
        self.play(text_intro.animate.scale(0.5))
        self.play(text_intro.animate.to_edge(UP * 0.5))

        plane = self.create_graph()
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
        self.add_points_to_graph(plane, points)

        tree = self.create_fisrt_tree(points)

        # Parte 2 - Como funciona
        self.clear_screen()
        self.wait(0.5)

        impurity_text = Text("Medidas de Impureza")
        self.play(Write(impurity_text))
        self.wait()
        self.play(impurity_text.animate.scale(0.5))
        self.play(impurity_text.animate.to_edge(UP * 0.5))

        self.play(Create(tree))
        self.wait()

        self.add_proportions(tree)

        # Parte 3 - Equações
        self.clear_screen()
        self.wait(0.5)
        
        impurity_math_text = Text("Calculo de Impureza")
        impurity_math_text.shift(UP * 2)
        self.play(Write(impurity_math_text))
        self.wait()
        self.create_equations(impurity_math_text)
        self.wait(3)


    def create_graph(self):
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

        self.play(Create(plane), run_time=2)
        self.wait(0.5)
        self.play(Create(labels))
        self.play(Create(legend))
        self.wait()

        return plane


    def add_points_to_graph(self, graph, points: list):
        vg_points = VGroup()

        for point in points:
            x, y, color = point
            dot = Dot(graph.coords_to_point(x, y), color=color)
            self.play(Create(dot), run_time=0.2)
            vg_points.add(dot)

        self.wait()

        return vg_points


    def create_fisrt_tree(self, points: list):
        ######## Root Node ########
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
        self.wait()

        ######## Leaf Node 1 ########
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
        self.wait()

        ######## Leaf Node 2 ########
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
        self.wait()
        text_weight = Text("Peso > 100", font="Roboto", font_size=20).move_to(node2)
        self.play(Write(text_weight))
        self.wait()

        ######## Leaf Node 3 ########
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
        self.wait()

        ######## Leaf Node 4 ########
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

        ######## Classification ########
        text_basket = Text("Basquete", font="Roboto", font_size=20).move_to(node1)
        self.play(Write(text_basket))
        self.wait()
        text_sumo = Text("Sumô", font="Roboto", font_size=20).move_to(node3)
        self.play(Write(text_sumo))
        self.wait()
        text_jockey = Text("Jockey", font="Roboto", font_size=20).move_to(node4)
        self.play(Write(text_jockey))
        self.wait(3)

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
            *dots_01, # 19
            *dots_02, # 19+9 = 28
            *dots_03, # 28+3 = 31
            *dots_04, # 31+6 = 37
            *dots_05 # 37+3 = 40
        )

        # Move the VGroup to the center
        tree.move_to(ORIGIN)

        return tree


    def create_equations(self, impurity_text):
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
        self.play(
            Create(arrow_entropy),
            Create(arrow_gini),
            Write(entropy_text),
            Write(gini_text),
        )
        self.wait()

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

        self.play(Write(entropy_equation), Write(gini_equation))
        self.wait(3)


    def add_proportions(self, tree):
        dots_o1 = tree[24]
        proportion_text = MathTex(
            r"p = \left[ \frac{1}{3}, \frac{1}{3}, \frac{1}{3} \right]"
        ).next_to(dots_o1, RIGHT * 1.5)
        proportion_text.scale(0.7)
        proportion_text[0][3:6].set_color(BLUE)
        proportion_text[0][7:10].set_color(RED)
        proportion_text[0][11:14].set_color(GREEN)
        self.play(Write(proportion_text))
        self.wait()

        dots_o2 = tree[28]
        proportion_text_2 = MathTex(
            r"p = \left[ 0, 1, 0 \right]"
        ).next_to(dots_o2, LEFT * 1.5)
        proportion_text_2.scale(0.7)
        proportion_text_2[0][3].set_color(BLUE)
        proportion_text_2[0][5].set_color(RED)
        proportion_text_2[0][7].set_color(GREEN)
        self.play(Write(proportion_text_2))
        self.wait()

        dots_o3 = tree[31]
        proportion_text_3 = MathTex(
            r"p = \left[ \frac{1}{2}, 0, \frac{1}{2} \right]"
        ).next_to(dots_o3, RIGHT * 1.5)
        proportion_text_3.scale(0.7)
        proportion_text_3[0][3:6].set_color(BLUE)
        proportion_text_3[0][7].set_color(RED)
        proportion_text_3[0][9:12].set_color(GREEN)
        self.play(Write(proportion_text_3))
        self.wait()

        dots_o4 = tree[37]
        proportion_text_4 = MathTex(
            r"p = \left[ 1, 0, 0 \right]"
        ).next_to(dots_o4, LEFT * 1.5)
        proportion_text_4.scale(0.7)
        proportion_text_4[0][3].set_color(BLUE)
        proportion_text_4[0][5].set_color(RED)
        proportion_text_4[0][7].set_color(GREEN)
        self.play(Write(proportion_text_4))
        self.wait()

        dots_o5 = tree[40]
        proportion_text_5 = MathTex(
            r"p = \left[ 0, 0, 1 \right]"
        ).next_to(dots_o5, RIGHT * 1.5)
        proportion_text_5.scale(0.7)
        proportion_text_5[0][3].set_color(BLUE)
        proportion_text_5[0][5].set_color(RED)
        proportion_text_5[0][7].set_color(GREEN)
        self.play(Write(proportion_text_5))
        self.wait(3)


    def clear_screen(self, obj=None):
        if not obj:
            self.play(*[FadeOut(mob) for mob in self.mobjects])
        else:
            self.play(*[FadeOut(mob) for mob in obj])
