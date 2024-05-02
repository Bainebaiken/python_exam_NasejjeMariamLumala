base = int(input('\nEnter the base of the triangle: '))
height = int(input('Enter the height of the triangle: '))

def areaOfTriangleApproachTwo(b,h):

    area = (1/2) * b * h

    print(int(area))

areaOfTriangleApproachTwo(base,height)