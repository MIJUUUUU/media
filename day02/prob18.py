class Rectangle:
    def set(self, width, height): 
        self.width = width
        self.height = height

    def area(self): 
        return self.width * self.height

    def perimeter(self):  
        return (self.width + self.height) * 2


width, height = map(int, input().split())


rect = Rectangle()
rect.set(width, height)


print("width:", rect.area(), "perimeter:", rect.perimeter())
