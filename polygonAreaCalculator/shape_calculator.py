def shape_calculator():
    return Rectangle


class Rectangle:

    def __init__(self, width=5, height=10):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


    def set_width(self, newW):
        self.width = newW

    def set_height(self, newH):
        self.height = newH


    def get_area(self):
        area = self.width * self.height
        return area
    

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = self.width**2 + self.height**2
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            tot = self.height
            res = ''
            while tot > 0:
                res += f'*'*self.width + '\n'
                tot-=1
            return res
    
    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())



class Square(Rectangle):
    def __init__(self, side=9):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_side(self, newS):
        self.width = newS
        self.height = newS
