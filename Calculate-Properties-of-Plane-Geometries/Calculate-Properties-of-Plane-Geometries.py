import math
π = 3.14


def circle_all():
    def areaofCircle():
        user_function = input("Find-Area with [r, d] ").lower()
        if user_function == "r":
            r = float(input("Enter radius in cm. "))
            print("The Area of Circle with radius is ", ((r**2) * (π)), "cm**2" )
        elif user_function == "d" :
            d = float(input("Enter diameter in cm. "))
            print("The Area of Circle with diameter is", (((d // 2)**2) * π), "cm**2")
        else:
            print("Data Not Applicable")

    def circumferance():
        user_function = input("Find-Circumferance with [r, d] ").lower()
        if user_function == "r":
            r = float(input("Enter radius in cm. "))
            print("The circumferance of Circle with radius is ", ((2) * (r) * (π)), "cm**2" )
        elif user_function == "d" :
            d = float(input("Enter diameter in cm. "))
            print("The circumferance of Circle with diameter is", (2 * (d / 2) * π), "cm**2")
        else:
            print("Data Not Applicable")

    def radius():
        user_function = input("Find-Radius with [A or Area, d or diameter] ").lower()
        if user_function == "a" or user_function == "area":
            area = float(input("Enter area of circle. "))
            print("Radius of circle is. ", (math.sqrt((area)/(π))) )
        elif user_function == "d" or user_function == "diameter":
            d = float(input("Enter diameter of circle. "))
            print("Radius of circle is ", (d / 2))
        else:
            print("Data Not Applicable")

    def diameter():
        user_function = input("Find-Daimeter with [A or Area, r or radius] ").lower()
        if user_function == "area" or user_function == "a":
            area = float(input("Enter area of circle. "))
            print("Diameter of circle is. ", ((4 * area) / (π)) )
        elif user_function == "radius" or user_function == "r":
            r = float(input("Enter Radius."))
            print("diameter is", (r + r) )
        else:
            print("Data Not Applicable")

    while True:
        user_want_to_find = input("what do you want to find?  [A or Area, C or Circunferance, r or radius, d or diameter]").lower()
        if user_want_to_find == "area" or user_want_to_find ==  "a":
            areaofCircle()
        elif user_want_to_find == "circumferance" or user_want_to_find == "c":
            circumferance()
        elif user_want_to_find == "radius" or user_want_to_find == "r":
            radius()
        elif user_want_to_find == "diameter" or user_want_to_find == "d":
            diameter()
        else:
            print("Data Not Applicable")

        calculate = input("Want to find again? (y/n) : ")
        if calculate.lower() != "y":
            break




def elipse_all():
    def area_ofElipse():
        a = float(input("Enter length of Vertical axis from centre of ellipse. "))
        b = float(input("Enter length of Horizontal  axis from centre of ellipse. "))
        print("Area of Elipse", (π*a*b))

    def vertiAxis_a():
        Area = float(input("Enter Area of ellipse. "))
        b = float(input("Enter length of Horizontal  axis from centre of ellipse. "))
        a = Area/(π*b)
        print("Length of vertical axis from centre of ellipse. ", a)

    def horiAxis_b():
        Area = float(input("Enter Area of ellipse. "))
        a = float(input("Enter length of Vertical axis from centre of ellipse. "))
        b = Area/(π*a)
        print("Length of horizontal axis from centre of ellipse. ",b)


        '''Area of Elipse
        a = distance of vertical axis from centre of ellipse
        b = distance of Horizontal axis from centre of ellipse
        Area of Ellipse = 𝜋ab.
        Area of Ellipse = 𝜋ab. to find a, a = Area/(π*b)
        Area of Ellipse = 𝜋ab. To find b, b = Area/(π*a)
    '''
    while True:
        user_want_to_find = input("Select what to find? [A or Area, a, b] :").lower()
        print("""a = distance of vertical axis from centre of ellipse
        b = distance of Horizontal axis from centre of ellipse""")
        if user_want_to_find == "a" or user_want_to_find == "area":
            area_ofElipse()
        elif user_want_to_find == "a":
            vertiAxis_a()
        elif user_want_to_find == "b":
            horiAxis_b()
        else:
            print("Enter Correct input.")

        find_again = input("Want to find again? (y/n): ")
        if find_again.lower() != "y":
            break




def parallelogram_all():
    def area_ofParallelogram():
        b = float(input("Enter base lenght of parallelgrram: "))
        h = float(input("Enter height of Parallelogram: "))
        Aera = b * h
        print("Area of Parallelogram is ", Aera)

    def base_ofParallelogram():
        A = float(input("Area of Parallelogram: "))
        h = float(input("Entar height of Parallelogram: "))
        b = (A / h)
        print("Base of Parallelogram is ", b)


    def height_ofParallelogram():
        A = float(input("Area of Parallelogram: "))
        b = float(input("Entar base of Parallelogram: "))
        h = (A / b)
        print("Height of Parallelogram is ", h)

    def perineter_ofParallelogram():
        a = float(input("Enter side length of Parallelogram: "))
        b = float(input("Enter base length of Paralleloigram: "))
        P = (2 * (a + b))
        print("Perimeter of Parallelogram: ", P)

    def sidelength_ofParallelogram():
        P = float(input("Enter perimeter of Parallelogram: "))
        b = float(input("Enter base of Parallelogram: "))
        a = ((P / 2) - b)
        print("Side of Parallelogram, a: ", a)

    '''Area of Parallelogram
    A= Area, b = base, h= height(perpendicular to base)
    Perimeter = P, a = side length'''
    while True:
        User_want_to_find = input("Select what to find? [Area or A, base or b, height of h, Perimeter or P, side length or a ]").lower()
        if User_want_to_find == "area" or User_want_to_find == "a":
            area_ofParallelogram()
        elif User_want_to_find == "base" or User_want_to_find == "b":
            base_ofParallelogram()
        elif User_want_to_find == "height" or User_want_to_find == "h":
            height_ofParallelogram()
        elif User_want_to_find == "perineter" or User_want_to_find == "p":
            perineter_ofParallelogram()
        elif User_want_to_find == "side length" or User_want_to_find == "a":
            sidelength_ofParallelogram()
        else:
            print("Enter Correct input.")


        find_again = input("Want to find again? (y/n): ")
        if find_again.lower() != "y":
            break




def rectangle_all():
    def area_ofRectangle():
        w = float(input("Enter width of Rectangle in cm. "))
        l = float(input("Enter Length of Rectangle in cm. "))
        A = (w * l)
        print("Area of Rectangle is ", A, "cm**2")

    def width_ofRectangle():
        A = float(input("Enter Area of Rectangle in cm. "))
        l = float(input("Enter Length of Rectangle in cm. "))
        w = (A / l)
        print("width of Rectangle is ", w, "cm**2")

    def length_ofRectangle():
        A = float(input("Enter Area of Rectangle in cm. "))
        w = float(input("Enter width of Rectangle in cm. "))
        l = (A / w)
        print("Length of Rectangle is ", l, "cm**2")

    '''    
        Area of Ractangle = width * length i.e. A = w * l
        w = width of Rectangle in cm.
        l = Length of Rectangle in cm.
        A = w * l, w = A / l.
        A = w * l, l = A / w.
    '''
    while True:
        user_want_to_find = input("Slect what to Find? [A or Area, w or width, l or lenght] :").lower()
        if user_want_to_find == "area" or user_want_to_find == "a":
            area_ofRectangle()
        elif user_want_to_find == "w" or user_want_to_find == "width":
            width_ofRectangle()
        elif user_want_to_find == "l" or user_want_to_find == "length":
            length_ofRectangle()
        else:
            print("Enter Correct input.")

            find_again = input("Want to find again? (y/n): ")
            if find_again.lower() != "y":
                break




def rightAngledTriangle_all():
    def area_ofRAngleTriangle():
        a = float(input("vertical Side of triangle a: "))
        b = float(input("Base side of triangle b: "))
        print("Area of Right angled triangle is A: ", ((a * b) /  2))

    def baselength_ofRAngleTriangle():
        A = float(input("Enter Area of Triangle is A: " ))
        a = float(input("Enter verticle side of right angled Triangle a: "))
        print ("base line length of right angled triangle is b: ", (2 * ( A / a)))

    def vertilinelen_ofRAngleTriangle():
        A = float(input("Enter Area of Triangle is A: " ))
        b = float(input("Enter base lin length of right angled Triangle a: "))
        print ("Verticle line length of right angled triangle is b: ", (2 * ( A / b)))

    def hypotenuse_ofRAngleTriangle():
        a = float(input("Verticle Side of triangle a: "))
        b = float(input("Base side of triangle b: "))
        print("Length of Hypotenuse is ", math.sqrt((a**2) + (b**2)))

    def perimeter_ofRAngleTriangle():
        a = float(input("vertical Side of triangle a: "))
        b = float(input("Base side of triangle b: "))
        print("Perimeter if Right Angled Triangle, P is ", (a + b) + (math.sqrt((a**2) + (b**2))) )

    '''
    A = Area, a = verticle line, b = base line of triangle.
    c = Hypotenuse, Perimeter = c
    '''
    while True:
        user_want_to_find = input("""Select what to find? [Perimeter or c, Hypotenuse or c, A or Area, base lenght or b, Verticle line length or a]: """)

        if user_want_to_find == "a" or user_want_to_find == "area":
            area_ofRAngleTriangle()
        elif user_want_to_find == "base lenght" or user_want_to_find == "b":
            baselength_ofRAngleTriangle()
        elif user_want_to_find == "Verticle line length" or user_want_to_find == "a":
            vertilinelen_ofRAngleTriangle()
        elif user_want_to_find == "Hypotenuse" or user_want_to_find == "c":
            hypotenuse_ofRAngleTriangle()
        elif user_want_to_find == "Perimeter" or user_want_to_find == "c":
            perimeter_ofRAngleTriangle()
        else:
            print("Enter Correct input.")

        find_again = input("Want to find again? (y/n): ")
        if find_again.lower() != "y":
            break





def square_all():
    def area_ofSquare():
        a = float(input("Enter length of one side of square in cm : "))
        Area = a**2
        print("Area of Square is : ", Area, "cm**2" )

    def diagonal_ofSquare():
        a = float(input("Enter length of one side of square in cm : "))
        Diagonal = ((math.sqrt(2)) * (a))
        print("Diagonal of square is : ", Diagonal)

    def perimeter_ofSquare():
        a = float(input("Enter length of one side of square in cm : "))
        Perimeter = (4) * (a)
        print("Area of Square is : ", Perimeter, "cm**2" )

    def side_a_ofSquare():
        user_choice = input("Find length of side of Square by [Area or A, Diagonal or D, Perimeter or P]").loer()
        if user_choice == "area" or user_choice == "a":
            Area = float(input("Enter Area of square in cm**2 : "))
            a = (math.sqrt(Area))
            print("length of one side of Square is : ", a, "cm")
        elif user_choice == "diagonal" or user_choice == "d":
            Diagonal = float(input("Enter length of diagonal in cm : "))
            a = (Diagonal) / (math.sqrt(2))
            print("length of one side of Square is : ", a, "cm")
        elif user_choice == "perimeter" or user_choice == "p":
            Perimeter = float(input("Enter Perimeter : "))
            a = (Perimeter / 4)
            print("length of one side of Square is : ", a, "cm")

    '''
    Area of Square = a**2
    a = length of one side of square
    Perimeter of square = P = 4a
    A = a**2, a = (math.sqrt(Area))
    '''
    while True:
        user_want_to_find = input("Slect what to Find? [A or Area, Diagonal or D, Perimeter or P, side a or a ] :")
        if user_want_to_find == "area" or  user_want_to_find == "a":
            area_ofSquare()
        elif user_want_to_find == "diagonal" or user_want_to_find == "d":
            diagonal_ofSquare()
        elif user_want_to_find == "perimeter" or user_want_to_find == "p":
            perimeter_ofSquare()
        elif user_want_to_find == "side a" or user_want_to_find == "a":
            side_a_ofSquare()
        else:
            print("Enter Correct input. and Try Again..!")

        find_again = input("Want to find again? (y/n): ")
        if find_again.lower() != "y":
            break




def trapezoid_all():
    def area_ofTrapezoid():
            A = float(input("Area of Trapezoid is: "))
            b = float(input("Length of Lower base: "))
            h = float(input("Length of Hieght: "))
            a = ((2 * (A / h)) -b )
            print("Length of upper base: ", a)

    def lowerbase_ofTrapezoid():
            A = float(input("Area of Trapezoid is: "))
            a = float(input("Length of upper base: "))
            h = float(input("Length of Hieght: "))
            b = ((2 * (A / h)) - a)
            print("Length of Lower base: ", b)

    def height_ofTrapezoid():
            A = float(input("Area of Trapezoid is: "))
            a = float(input("Length of upper base: "))
            b = float(input("Length of Lower base: "))
            h = (2 * (A / ( a + b)))
            print("Length of Hieght: ", h)


    def perimeter_ofTrapezoid():
            a = float(input("Length of upper base: "))
            b = float(input("Length of Lower base: "))
            c = float(input("Length of side c(right): "))
            d = float(input("Length of side d(left): "))
            P = (a + b + c + d)
            print("Perimeter of trapezoid: ", P)


    def sidec_ofTrapezoid():
            P = float(input("Perimeter of trapezoid: "))
            a = float(input("Length of upper base: "))
            b = float(input("Length of Lower base: "))
            d = float(input("Length of side d(left): "))
            c = (a + b + P + d)
            print("Length of side c(right): ", c)


    def sided_ofTrapezoid():
            P = float(input("Perimeter of trapezoid: "))
            a = float(input("Length of upper base: "))
            b = float(input("Length of Lower base: "))
            c = float(input("Length of side c(right): "))
            d = (P - a - b - c)
            print("Length of side d(left): ", d)

    '''
    Area of Trapezoid
    a= upper base, b = lower base, h = Height (perpendicular line to base)
    Perimeter = P, c = side c(right), d = side d(left)

    '''

    while True:
        User_want_to_find = input("Select what to find: [upper base or a, b or lower base, h or Height, Perimeter or P, c or side c(right), d or side d(left)]")
        if User_want_to_find =="upper base" or User_want_to_find == "a":
            area_ofTrapezoid()
        elif User_want_to_find == "lower base" or User_want_to_find == "b":
            lowerbase_ofTrapezoid()
        elif User_want_to_find == "Height" or User_want_to_find == "h":
            height_ofTrapezoid()
        elif User_want_to_find == "Perimeter" or User_want_to_find == "P":
            perimeter_ofTrapezoid()
        elif User_want_to_find ==  "side c" or User_want_to_find == "c":
            sidec_ofTrapezoid()
        elif User_want_to_find == "side d" or User_want_to_find == "d":
            sided_ofTrapezoid()
        else:
            print("Enter Correct input.")

        find_again = input("Want to find again? (y/n): ")
        if find_again.lower() != "y":
            break




def triangle_all():
    def area_ofTriangle():
            hb = float(input("Enter lenght of Hight perpendicular to base. hb: "))
            b =  float(input("Enter lenght of  base. b: "))
            A = ((hb * b) / 2)
            print("Area of Triangle is, A: ", A)


    def perimeter_ofTriangle():
            a = float(input("Enter length of side a: "))
            b = float(input("Enter lenght of  base. b: "))
            c = float(input("Enter length of side c: "))
            P = (a + b + c)
            print("Perimeter of Triangle is: ", P)


    def baselength_ofTriangle():
            A = float(input("Enter Area of Triangle A: "))
            hb = float(input("Enter lenght of Hight perpendicular to base. hb: "))
            b = (2 * (A / hb))
            print(" Length of base is, b = ", b)


    def height_ofTriangle():
            A = float(input("Enter Area of Triangle A: "))
            b =  float(input("Enter lenght of  base. b: "))
            hb =  (2 * (A / b))
            print("Height of triangle is, hb = ", hb)


    def lensidea_ofTriangle():
            P = float(input("Enter Perimeter P: "))
            b = float(input("Enter lenght of  base. b: "))
            c = float(input("Enter length of side c: "))
            a = (P - b - c)
            print("Lenght of side a is: ", a)


    def lensidec_ofTriangle():
            P = float(input("Enter Perimeter P: "))
            a = float(input("Enter length of side a: "))
            b = float(input("Enter lenght of  base. b: "))
            c = (P - a - b)
            print("length of side c is: ", c)



    while True:
        user_want_to_find = input("Select what to find? [Area or A, Perimeter or P, base length or b, height or hb, length of side a or a, length of side c or c ]")

        if user_want_to_find == "area" or user_want_to_find == "A":
            area_ofTriangle()
        elif user_want_to_find == "Perimeter" or user_want_to_find == "P":
            perimeter_ofTriangle()
        elif user_want_to_find == "base length" or  user_want_to_find == "b":
            baselength_ofTriangle()
        elif user_want_to_find == "Height" or user_want_to_find == "hb":
            height_ofTriangle()
        elif user_want_to_find == "length of side a " or user_want_to_find == "a":
            lensidea_ofTriangle()
        elif user_want_to_find == "length of side c" or user_want_to_find == "c":
            lensidec_ofTriangle()
        else:
            print("Enter correct input.")
        
        find_again = input("Want to find again? (y/n) :")
        if find_again.lower() != "y":
            break
        


while True:
    user_input = input("""
            Circle, Elipse, Parallelogram, rectangle, 
        Right Angled Triangle, Square, Trapezoide, Triangle
        
        Enter the Geometry name to Find Solution: """).lower()
    
    if user_input == "circle":
        circle_all()
    elif user_input == "elipse":
        elipse_all()
    elif user_input == "parllelogram":
        parallelogram_all()
    elif user_input == "rectangle":
        rectangle_all()
    elif user_input == "right angled traingle":
        rightAngledTriangle_all()
    elif user_input == "square":
        square_all()
    elif user_input == "trapezoide":
        trapezoid_all()
    elif user_input == "triange":
        triangle_all()
    else:
        print("Enter Correct input. and Try Again..!")
    find_againOptions = input("Want to go main geometry options again? (y/n): ")
    if find_againOptions.lower() != "y":
        break