class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def set_width(self, width2):
        self.width = width2

    def set_height(self, height2):
        self.height = height2

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        a=""
        if self.width > 50 or self.height >50:
            return "Too big for picture."
        else:
            for n in range(self.height):
                a+=f"{self.width * '*'}\n"
            return a

    def get_amount_inside(self, shape):
        b=self.get_area()//shape.get_area()
        return b

    def __str__(self):
        a = f"Rectangle(width={self.width}, height={self.height})"
        return a


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side2):
        super().__init__(side2, side2)

    def __str__(self):
        a = f"Square(side={self.width})"
        return a