##### Project 1 #######

# NAME: Adarsh Ram
# NetID: cho11
# Number: 30

import math
import Math_help as mh


# Question 1) Parameters are x,y

def Question_1(x,y):
        f = ((x**2) * (y**3)) / (4 * x * y)
        return f

# Question 2) Parameters are x,y

def Question_2(x,y):
    f = (math.cos(x) * math.sin(y)) / (x * y)
    return f

# Question 3) Parameters are n1,n2

def Question_3(n1,n2):  
    n = n2 - n1 + 1
    y = n * (n1 + n2) // 2
    return y

# Question 4) Parameters are x,y

def Question_4(x,y):
    f = mh.log(x) + mh.log3(x*y)
    return f

# Question 5) Parameters is x

def Question_5(x):
    y = math.factorial(5) + (3 * mh.log4(x) + math.exp(mh.log6(7*x)))
    return y

# Question 6) Parameters are x,y,z,m,n

def Question_6(x,y,z,m,n):
    f = (x + y + z + m + n) / 5
    return f

# Question 7) Parameters are x,y

def Question_7(x,y):
    f = math.sin(x)**2 + math.cos(y)**2 + math.sin(y)**2 + math.cos(x)**2
    return f

# Question 8) Parameters are x1,y1,x2,y2

def Question_8(x1,y1,x2,y2):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d

# Question 9)Parameters are x1,y1,x2,y2

def Question_9(x1,y1,x2,y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x,y

# Question 10) Parameters is x

def Question_10(x):
    f = (1 + x + (x**2)/math.factorial(2)+(x**3)/math.factorial(3)+(x**4)/math.factorial(4)+(x**5)/math.factorial(5)+(x**6)/math.factorial(6))
    true_value = math.exp(x)
    e = true_value - f
    return f,e # return values are f=e^x and error e=f-e^x (e^x can be calculated using math library)


if __name__ == '__main__':
    print("Testing Project 1")

    assert round(Question_1(1,2),3)==1.000
    assert round(Question_1(5,-2),3)==5.000
    assert round(Question_1(-10,4),3)==-40.000

    assert round(Question_2(1,2),3)==0.246
    assert round(Question_2(5,-2),3)==0.026
    assert round(Question_2(-10,4),3)==-0.016

    assert Question_3(10,22)==208
    assert Question_3(0,10)==55
    assert Question_3(-10,10)==0

    assert round(Question_4(10,2),3)==5.029
    assert round(Question_4(1,4),3)==1.262
    assert round(Question_4(10,20),3)==7.125
    
    assert round(Question_5(1),3)==122.962
    assert round(Question_5(10),3)==135.692
    assert round(Question_5(100),3)==168.681

    assert round(Question_6(10,20,30,40,50),3)==30.0
    assert round(Question_6(1,4,6,4,5),3)==4.0
    assert round(Question_6(1,3,7,9,13),3)==6.6
    
    assert round(Question_7(1,2),3)==2
    assert round(Question_7(5,-2),3)==2
    assert round(Question_7(-10,4),3)==2

    assert round(Question_8(1,2,4,8),3)==6.708
    assert round(Question_8(-2,5,7,-2),3)==11.402
    assert round(Question_8(-10,-10,4,4),3)==19.799

    assert Question_9(1,2,4,8)==(2.5, 5.0)
    assert Question_9(-2,5,7,-2)==(2.5, 1.5)
    assert Question_9(-10,-10,4,4)==(-3.0, -3.0)

    assert Question_10(1)==(2.7180555555555554, 0.0002262729034896438)
    assert Question_10(-2)==(0.1555555555555556, -0.02022027231894291)
    assert Question_10(2)==(7.355555555555555, 0.033500543375095226)  
    
    print("Testing completed")