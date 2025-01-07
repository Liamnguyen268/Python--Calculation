def squareArea(s):
    area=s**2
    return area
def squarePerim(s):
    return s*4
def triPerim(s1,s2,s3):
    perim= s1+s2+s3
    return perim
def triArea(s1,s2,s3):
    p=triPerim(s1,s2,s3)/2
    Area=(p*(p*s1)*(p*s2)*(p*s3))**(1/2)
    return Area
def main():
    print("This program computes the area and perimeter of a square and a triangle")

    side=float(input("Enter square side length: "))
    ans=squareArea(side)
    print("The area of the square is: "+str(ans))
    p = squarePerim(side)
    print("The Perimeter of the square is: "+str(p))

    tside1=float(input("Enter traingle side 1: "))
    tside2=float(input("Enter triangle side 2: "))
    tside3=float(input("Enter triangle side 3: "))
    ans2= triPerim(tside1,tside2,tside3)
    print("The Perimeter of the triangle is: "+str(ans2))
    p2= triArea(tside1,tside2,tside3)
    print("The Area of the Triangle is: "+str(p2))
main()