class Karatsuba:
    @staticmethod
    def product(x, y):
        # convert input data to strings
        x_string = str(x)
        y_string = str(y)

        # define the longest string and set it up as 'n'
        n = max(len(x_string), len(y_string))

        # return simple product if there are one-digit numbers
        if n == 1:
            return x * y

        middle = (n + 1) // 2

        # define a, b, c, d
        if n > len(x_string):
            a = 0
            b = x
        else:
            a = int(x_string[:middle])
            b = int(x_string[middle:])

        if n > len(y_string):
            c = 0
            d = y
        else:
            c = int(y_string[:middle])
            d = int(y_string[middle:])

        # recursive calculations
        ac = Karatsuba.product(a, c)
        bd = Karatsuba.product(b, d)
        gauss_trick = Karatsuba.product(a + b, c + d) - ac - bd

        # the power must be always even, so make it this way
        pow = n // 2
        pow = pow * 2

        # the main calculation by Karatsuba method
        return ac * (10 ** pow) + gauss_trick * (10 ** (pow // 2)) + bd


# Input data
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

# Print out the result
print("X =", x)
print("Y =", y)
print("----------------------------------------------------------------------------------------------------------------------------------------")
print("X * Y =", Karatsuba.product(x, y))
print("----------------------------------------------------------------------------------------------------------------------------------------")


#output
#X = 3141592653589793238462643383279502884197169399375105820974944592
#Y = 2718281828459045235360287471352662497757247093699959574966967627
#----------------------------------------------------------------------------------------------------------------------------------------
#X * Y = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
#----------------------------------------------------------------------------------------------------------------------------------------
