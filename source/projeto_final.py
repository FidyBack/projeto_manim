from manim import *


# class CreateCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
#         self.play(Create(circle))  # show the circle on screen

# class SquareToCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set color and transparency

#         square = Square()  # create a square
#         square.rotate(PI / 4)  # rotate a certain amount

#         self.play(Create(square))  # animate the creation of the square
#         self.play(Transform(square, circle))  # interpolate the square into the circle
#         self.play(FadeOut(square))  # fade out animation

# class SquareAndCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

#         square = Square()  # create a square
#         square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

#         square.next_to(circle, RIGHT, buff=5)  # set the position
#         self.play(Create(circle), Create(square))  # show the shapes on screen


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

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

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

# Create a class that writes text on the screen
class WriteText(Scene):
    def construct(self):
        text = Text("Creating a Decision Tree")  # create the text
        self.play(Write(text))  # write the text on screen
        self.wait(2)  # wait for 3 seconds
        self.play(FadeOut(text))  # fade out the text

# Create a class that calls the WriteText class, and the creates a decision tree
class DecisionTree(Scene):
    def construct(self):
        text = Text("Creating a Decision Tree")
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))

        decision_tree = Rectangle(height=6, width=8)  # create a rectangle
        decision_tree.set_fill(BLUE, opacity=0.5)
        self.play(Create(decision_tree))

        self.wait(2)
        self.play(FadeOut(decision_tree))

# Create a class that calls the DecisionTree class, and the creates a decision tree with a root node
class CreateDecisionTree(Scene):
    def construct(self):
        self.create_text("Creating a Decision Tree", UP)

        # Create base for decision tree
        decision_tree = Rectangle(height=6, width=8)
        decision_tree.set_fill(BLUE, opacity=0.5)
        self.play(Create(decision_tree))

        # Create tree nodes
        root_node = Circle(radius=0.3)
        root_node.set_fill(GREEN, opacity=0.5)
        root_node.move_to(UP*2)

        node1 = Circle(radius=0.3)
        node1.set_fill(GREEN, opacity=0.5)
        node1.move_to(LEFT)

        node2 = Circle(radius=0.3)
        node2.set_fill(GREEN, opacity=0.5)
        node2.move_to(RIGHT)

        # Create all nodes at the same time
        self.play(Create(root_node), Create(node1), Create(node2))
        self.wait(1)

        # Create lines with direction from root node to child nodes
        arrow1 = Arrow(start=root_node.get_bottom(), end=node1.get_top(), buff=0, max_tip_length_to_length_ratio=0.1, stroke_width=4)
        arrow2 = Arrow(start=root_node.get_bottom(), end=node2.get_top(), buff=0, max_tip_length_to_length_ratio=0.1, stroke_width=4)

        self.play(Create(arrow1), Create(arrow2))
        self.wait(1)

    def create_text(self, text_input, position):
        text = Text(text_input)
        self.play(Write(text))
        self.wait(1)
        self.play(text.animate.scale(0.5))
        self.play(text.animate.to_edge(position))
        self.wait(1)


        