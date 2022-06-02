def shape_calculator():
    return None


class Category:

    def __init__(self, width=5, height=10):
        self.width = width
        self.heigth = height

    def get_area(self, width, height):
        area = width * height
        return area
    

    def get_perimeter(self, width, heigth):
        perimeter = 2 * width + 2 * heigth
        return perimeter

    def get_diagonal(self, width, heigth):
        diagonal = width**2 + heigth**2
        return diagonal
    
    def get_picture(self, width, height):
        if width > 50 or height > 50:
            return 'Too big for picture.'