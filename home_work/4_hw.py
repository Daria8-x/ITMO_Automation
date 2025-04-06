class Rectangle:
    def __init__(self,height, width):
        self.height=height
        self.width=width

    def square(self):
        return self.width*self.height

    def perimeter(self):
        return (self.width+self.height)*2

rec1=Rectangle(10, 5)
rec2=Rectangle(25, 10)
rec3=Rectangle(4,8)
print(rec1.square(),rec1.perimeter())
print(rec2.square(), rec2.perimeter())
print(rec3.square(), rec3.perimeter())


class Math:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def addition (self):
        return self.a+self.b

    def multiplication (self):
        return self.a*self.b

    def division (self):
        return self.a/self.b

    def subtraction (self):
        return self.a-self.b
num=Math(15, 3)
print(num.addition())
print(num.multiplication())
print(num.division())
print(num.subtraction())


class ButtonsSidebar:
    def __init__(self, text, type='Кнопка', loc=None):
        self.text=text
        self.type=type
        self.loc=loc
    def press_button (self):
        print('Клик по кнопке {}'.format(self.text))
b1=ButtonsSidebar('Text Box')
b2=ButtonsSidebar('Check Box')
b3=ButtonsSidebar('Radio Button')
b4=ButtonsSidebar('Web Tables')
b5=ButtonsSidebar('Buttons')
b6=ButtonsSidebar('Links')
b7=ButtonsSidebar('Broken Links - Images')
b8=ButtonsSidebar('Upload and Download')
b9=ButtonsSidebar('Dynamic Properties')
b1.press_button()
b2.press_button()
b3.press_button()
b4.press_button()
b5.press_button()
b6.press_button()
b7.press_button()
b8.press_button()
b9.press_button()


