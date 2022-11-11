#simple calculator project
num1=99#input("enter first number: ")
sign_='//'#input("enter sign: ")
num2=5.354#input("enter second number: ")


def control_(input_value):
    if isinstance(float(input_value), (int, float)):
        return(float(input_value))
    else:
        print("enter a number please")



def calculate_(num1,sign,num2):
    if sign=='+':
        result_=num1+num2
    elif sign=='-':
        result_=num1-num2
    elif sign=='*':
        result_=num1*num2
    elif sign=='/':
        result_=num1/num2
    elif sign=='**':
        sign="^"
        result_=num1**num2
    elif sign=='//':
        result_=num1//num2
    print("{:,g}".format(num1),sign,"{:,g}".format(num2),"=","{:,g}".format(result_))



num1=control_(num1)
num2=control_(num2)
if sign_=='+' or sign_=='-' or sign_=='*' or sign_=='/' or sign_=='**' or sign_=='//':
    calculate_(num1,sign_,num2)
else:
    print('enter a valid sign')
    exit()