#write a program for exception handling
'''while True:
    try:
        x=int(input("Enter any number:"))
        y=100/x
        print(y)

    except ZeroDivisionError:
        print("Zero Division is not possible")
    except ValueError:
        print("Entered value is not valid")
    except SyntaxError:
        print("syntax error")
    except:
        print("somthing is wrong")
    else:
        print(y)
    finally:
        print("program ended")'''


#write a program to demonstrate how to raise an exception
'''x=int(input("Enter any numbers:"))
try:
    if x==2:
        raiseIoError
except IOError:
    print("An I/o Exception is raised")
else:
        print("Value is not 2")


#write a program to demonstrate use of finally clause in exception handling
while True:
    try:
        x=int(input("Enter any number:"))
        r=100/x
    except(ValueError,ZeroDivisionError):
        print("somthing is wrong")
    else:
        print(r)
    finally:
        print("files closed")
        break'''

#write a program for exception handling
'''while True:
    try:
        x=int(input("Enter any number:"))
        r=100/x
    except(ValueError,ZeroDivisionError):
        print("something is wrong")
    else:
        print(r)
        break'''


#write a program for exception handling
'''while True:
    try:
        x=int(input("Enter a number:"))
        r=100/x
    except ValueError:
        print("value is not int type")
    except ZeroDivisionError:
        print("Denominator is zero")
    else:
        print(r)
        break'''

'''while True:
    try:
        x=int(input('enter a number:'))
        y=100/x

    except ValueError:
        print('value is not int type')

    except ZeroDivisionError:

        print('denominator is zero')
    else:
        print(y)
        break'''

''''while True:
    try:
        x=int(input('enter number:'))
        y=100/x
    except (ValueError,ZeroDivisionError):
        print('somthing is wrong')
    else:
        print(y)
        break'''

'''while True:
    try:
        x=int(input('enter number:'))
        y=100/x
    except(ValueError,ZeroDivisionError):
        print('somthing is wrong')

    else:
        print(y)
    finally:
        print('file is closed')
        break'''

'''x=int(input('enter number:'))
try:
    if x==3:
        raise IOError
except IOError:
    print('an i/o error is raised')
else:
    print('value is not 3')'''

'''try:
    x=int(input('enter number:'))
    y=100/x
except Exception as e:
    print('Ececption:',type(e))'''


while True:
    try:
        x=int(input('enter number:'))
        y=100/x
    except ZeroDivisionError:
        print('zerodivision error')
    except ValueError:
        print('value is not integer type')
    except:
        print('somthing is wrong')
    else:
        print(y)
    finally:
        print('program ended')