class Rectangle:
    def __init__(self, width, height) :
        self.width = width
        self.height = height


    def set_width (self, width) :
        self.width = width


    def set_height (self,height) :
        self.height = height


    def get_area (self) :
        area = self.width * self.height

        return area


    def get_perimeter (self) :
        perimeter = (2 * self.width + 2 * self.height)

        return perimeter


    def get_diagonal (self) :
        diagonal = (self.width **2 + self.height **2) **0.5

        return diagonal


    def get_picture (self) :
        num_lines = self.height
        num_symbol = self.width
        line_rep = '*' * (self.width) + "\n"

        if num_lines > 50 or num_symbol > 50 :
            
            return "Too big for picture."

        else :
           picture = line_rep * num_lines

        return picture


    def get_amount_inside (self, obj) :
        num_fit_in = int (self.get_area () / obj.get_area ())

        return num_fit_in


    def __repr__(self) -> str:
        representation = 'Rectangle(width={}, height={})'. format (self.width, self.height)
        
        return representation

class Square (Rectangle):
    def __init__(self, side) :
        super().__init__(side, side)

    def set_side (self, side):
        self.width = side
        self.height = side 


    def __repr__(self) -> str:
        representation = 'Square(side={})'. format (self.width)


        return representation





