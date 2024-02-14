
# Name: Hamza Sheikh
# Description: This program is a general purpose tool for quadratic functions.
# There is also class support for derivatives and functions past the degree of 2,
# however they are not used in the main program

"""
    Types of Classes:
    
    Equation(): Receives any amount of variables which will
    describe the coefficients of the functions
    
        The length of the list (coefficients) will describe the degree
    
        Each variable will correspond to the next coefficient of that function,
        starting with a, then b, c and so on:
        
        Example - Equation(2, 3) will correspond to 2x + 3
        Example - Equation(5, -3, 0) will correspond to 5x^2 - 3x
    
        Example - Equation(-1, 0, 3, 3) corresponds to -x^3 + 3x + 3
        
        The Equation class does not have support for rational or sinusodial functions,
        it is also assumed that equation must have atleast two arguments. Functions
        that are constants(only 1 argument) may break the class.
    
    Inherited classes:
    
    Derivative: meant for derivative functions
    Quadratic: Functions with a degree of 2
    
"""

# import libraries
from tkinter import *
import math



class Equation():
    
    # initialize
    def __init__(self, *coefficients):
        self._coefficients = list(coefficients)

    # getter
    def get_coeff(self, placement):
        return(self._coefficients[placement - 1])

    # setter
    def change_coeff(self, placement, coefficient):
        self._coefficients[placement - 1] = coefficient
    

    def display(self):
        """
           displays the equation in string format
        
        Args:
        self - the given equation
            
        Returns:
            equation(str) - the equation in string format
        """
                 
        # makes sure 1 or -1 isn't written when writing equation (ex: 1x^2)
        if self._coefficients[0] == -1:
            equation = "-" #only adds negative sign if -1
        elif self._coefficients[0] != 1:
            equation = str(self._coefficients[0])
        else:
            equation = ""
            
        #length of coefficients will tell us the degree
        total_vals = len(self._coefficients)
        
        # if the length > 2, there will be an exponent value
        if total_vals > 2:
            equation += "x^" + str(total_vals - 1)
        elif total_vals == 2:
            equation += "x"
        
        # add all other terms using for loop
        for i in range(1, total_vals):
            # make's sure coefficient is not 0
            if self._coefficients[i] != 0:
                #checks if coefficient is negative or positive and adds sign
                if self._coefficients[i] < 0:
                    equation += " - "
                else:
                    equation += " + "
                
                # makes sure coefficient will not be written if it's 1 or -1
                # unless it is the last value (the constant)
                if self._coefficients[i] not in [1, -1] or (i == total_vals - 1):
                    #adds the coefficient value to string
                    equation += str( abs(self._coefficients[i]))
                if i < total_vals - 2:
                    #adds x with exponent
                    equation += "x^" + str(total_vals - 1 - i)
                elif i == total_vals - 2:
                    #adds x without exponent
                    equation += "x"
        return equation

    def solve_for_y(self, x):
        """
           returns the y value given x
        
        Args:
        self - the given equation
        x - the x value
            
        Returns:
            total(int) - the equation in string format
        """
        total = 0
        total_vals = len(self._coefficients)
        
        for i in range(total_vals - 1):
            # adds x multiplied by the exponent and the coefficient to total
            total += self._coefficients[i] * (x ** (total_vals - 1 - i))
        # adds the constant term
        total += self._coefficients[-1]
        
        return total
    
    def __add__(self, other):
        
        """
           adds the two equations
        
        Args:
        self - the first equation
        other - the second equation
            
        Returns:
            Equation - the sum of both equations
        """
        
        #define variables for more organized code
        self_total = len(self._coefficients)
        other_total = len(other._coefficients)
        difference = abs(self_total - other_total)
        end_func = []
        
        #checks if one of the functions has a higher degree
        if self_total > other_total:
            
            #puts all terms that wont be added together in the function first
            end_func += (self._coefficients[:difference])
            for i in range(difference, self_total):
                #add each like term together
                end_func.append(self._coefficients[i] + other._coefficients[i - difference])
        #same case as above but if other function has a greater degree
        elif self_total < other_total:
            end_func += (other._coefficients[:difference])
            for i in range(difference, other_total):
                end_func.append(self._coefficients[i - difference] + other._coefficients[i])
        else:
            #special case if equations have equal degrees
            for i in range(self_total):
                end_func.append(self._coefficients[i] + other._coefficients[i])
        return Equation(*end_func)
    
    def __sub__(self, other):
        """
           subtracts the two equations
        
        Args:
        self - the first equation
        other - the second equation
            
        Returns:
            Equation - the difference of both equations
        """
        #create variables for more organized code
        self_total = len(self._coefficients)
        other_total = len(other._coefficients)
        difference = abs(self_total - other_total)
        end_func = []
        
        #checks if one function has a greater degree
        if self_total > other_total:
            #adds the extra degrees that wont be subtracted to the end function
            end_func += (self._coefficients[:difference])
            for i in range(difference, self_total):
                # adds the difference between each term to end function
                end_func.append(self._coefficients[i] - other._coefficients[i - difference])
        
        # similar case to above but if other is greater instead of self
        elif self_total < other_total:
            end_func += (other._coefficients[:difference])
            for i in range(difference, other_total):
                end_func.append(self._coefficients[i - difference] - other._coefficients[i])
        else:
            #special case if both equations are equal degrees
            for i in range(self_total):
                end_func.append(self._coefficients[i] - other._coefficients[i])
        return Equation(*end_func)
    
    
    
    def __gt__(self, other):
        """
           compares which function has a greater exponent degree
        
        Args:
        self - the first equation
        other - the 2nd equation
            
        Returns:
            boolean - whether self has a greater degree than other
        """
        
        if len(self._coefficients) > len(other._coefficients):
            return True
        else:
            return False
        
    def __eq__(self, other):
        """
           checks if the exponent degrees are equal
        
        Args:
        self - the first equation
        other - the 2nd equation
            
        Returns:
            boolean - whether self and other have equal degrees
        """
        if len(self._coefficients) == len(other._coefficients):
            return True
        else:
            return False
    
    def deriv(self):
        """
           returns the derivative of self equation
        
        Args:
        self - the given equation
            
        Returns:
            Equation - the derivative of the self equation
        """
        newf = []
        total_vals = len(self._coefficients)
        for i in range(total_vals):
            # make sure value is not a constant
            if (total_vals - i - 1) != 0:
                # append current coefficient multiplied by exponent (power rule)
                newf.append(self._coefficients[i] * (total_vals - i - 1))
        return Equation(*newf)



class Quadratic(Equation):
    #a, b and c are all weakly private variables
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self._a = self._coefficients[0]
        self._b = self._coefficients[1]
        self._c = self._coefficients[2]
        
    # getter
    def get_coeff(self, coeff_type):
        coeff_types = {"a": self._a,
                       "b": self._b,
                       "c": self._c}
        return coeff_types[coeff_type]
    
    # setter
    def change_coeff(self, coeff_type, coefficient):
        
        if coeff_type == "a":
            self._coefficients[0], self._a = coefficient
        elif coeff_type == "b":
            self._coefficients[1], self._b = coefficient
        else:
            self._coefficients[2], self._c = coefficient
        
    def get_intercepts(self):
        """
           returns the x intercepts using quadratic formula
        
        Args:
        self - the given equation
            
        Returns:
            intercept1 - the first intercept
            intercept2 - the second intercept
        """
        
        try:
            intercept1_top = -1 * self._b + (math.sqrt(self._b ** 2 - 4 * self._a * self._c))
            intercept_bottom = 2 * self._a
            intercept2_top = -1 * self._b - (math.sqrt(self._b ** 2 - 4 * self._a * self._c))
        
            intercept1 = intercept1_top / intercept_bottom
            intercept2 = intercept2_top / intercept_bottom
            
            return intercept1, intercept2
        
        except:
            #returns none if there are no real solutions
            return None, None
    @property
    def RealSolutions(self):
        """
           checks if the function has real solutions
        
        Args:
        self - the given equation
            
        Returns:
            boolean - whether the function has any real solutions
        """
        
        discriminant = (self._b ** 2) - (4 * self._a * self._c)
        if discriminant < 0:
            return False
        else:
            return True
    

    @classmethod
    def perfect_square(cls, x_coeff, intercept):
        """
        creates a perfect square trinomial
        
        Args:
        cls - the class that will be returned
        x_coefficient - the a value on x (ax - b)^2
        intercept - the x intercept (the opposite in this case)
            
        Returns:
            cls(Quadratic): the equation of the perfect square trinomial
        """
        a_val = x_coeff ** 2
        b_val = 2 * x_coeff * intercept
        c_val = intercept ** 2
        return cls(a_val, b_val, c_val)
    
    @staticmethod
    def isupwards(a_value):
        """
           checks if the parabola is upwards or downwards
        
        Args:
        a_value - the a value of the quadratic
            
        Returns:
            boolean - wheter the function is upwards or not
        """
        
        if a_value > 0:
            return True
        else:
            return False


class Derivative(Equation):
    def antiderivative(self):
        """
           returns the antiderivative of the equation(+C not included)
        
        Args:
        self - the given equation
            
        Returns:
            Equation - the equation of the antiderivative
        """
        
        newf = []
        total_vals = len(self._coefficients)
        
        for i in range(total_vals):
            if self._coefficients[i] != 0:
                #does the opposite of power rule for each term
                newf.append(self._coefficients[i] // (total_vals - i))
            else:
                newf.append(0)
        #antiderivative will never have a constant so 0 is added
        newf.append(0)
        return Equation(*newf)
    def limit(self, x):
        return super().solve_for_y(x)


#####################################################################
# Tkinter Code

def display_rules():
    """
           returns the rules of each tool into the outputer
        
        Args:
        None
            
        Returns:
            None
    """
    chosen_game = player_choice.get()
    output = ""
    # derivative 
    if chosen_game == "d":
        output = "Add your a, b and c values on the bottom" \
        + " and the program will output the derivative of that function"
    # solve for y   
    elif chosen_game == "y":
        output = "Add your a, b and c values and your chosen x value" \
        + " and the program will output the y value at that point."
    # solve for x intercepts
    elif chosen_game == "x":
        output = "Add your a, b, and c values and the program will" \
        + " give you the x intercepts if there are any."
    # general info
    elif chosen_game == "i":
        output = "Add your a, b, and c values and the program will" \
        + " give you some general characteristics of the function"
    # perfect square trinomial
    elif chosen_game == "p":
        output = "Change the x and a value on the bottom to receieve a perfect" \
        + " square trinomial of that x value, described as (ax + X value)^2."
    else:
        output = "You must select an option first!"
    outputer.delete(0.0, END) 
    outputer.insert(0.0, output)
        



def choice_selected():
    """
        checks which tool was selected
        
        Args:
        None
            
        Returns:
        None
    """
    
    a = a_val.get()
    if a == 0:
        output = "your a value cannot be 0!"
        outputer.delete(0.0, END) 
        outputer.insert(0.0, output)
    else:
        chosen_game = player_choice.get()
        if chosen_game == "d":
            find_derivative()
        elif chosen_game == "y":
            get_y_value()
        elif chosen_game == "x":
            x_intercepts()
        elif chosen_game == "p":
            find_perfect_trinomial()
        elif chosen_game == "i":
            get_info()
        else:
            output = "you must select a valid option!"
            outputer.delete(0.0, END) 
            outputer.insert(0.0, output)

#decorates all tool functions so it is outputted to program
def output_info(function):
    def wrap():
        output = function()
        outputer.delete(0.0, END) 
        outputer.insert(0.0, output)
    return wrap

@output_info
def find_derivative():
    #receive values
    a = a_val.get()
    b = b_val.get()
    c = c_val.get()
    func = Quadratic(a, b, c)
    #get derivative
    func_deriv = func.deriv()
    output = func.display() + " has derivative of:\n" + func_deriv.display()
    return output
    
@output_info
def get_y_value():
    # get values
    a = a_val.get()
    b = b_val.get()
    c = c_val.get()
    x = x_val.get()
    # get quadratic and output answer
    func = Quadratic(a, b, c)
    output = "{} at the point x = {} is {}".format(func.display(), \
            x, func.solve_for_y(x))
    return output

@output_info
def get_info():
    a = a_val.get()
    b = b_val.get()
    c = c_val.get()
    func = Quadratic(a, b, c)
    #checks for real solutions
    if func.RealSolutions:
        x1, x2 = func.get_intercepts()
        if x1 == x2:
            output = "This function has 1 real solution.\n"
        else:
            output = "This function has 2 real solutions.\n"
    else:
        output = "This function has no real solutions.\n"
    # checks if parabola is upwards
    if func.isupwards(a):
        output += "This function is an upwards parabola.\n"
    else:
        output += "This function is a downwards parabola. \n"
    # finds y intercept
    output += "The y intercept of this function is {}".format(func.solve_for_y(0))
    return output


@output_info
def x_intercepts():
    #get values
     a = a_val.get()
     b = b_val.get()
     c = c_val.get()
     func = Quadratic(a, b, c)
     x1, x2 = func.get_intercepts()
     
     #checks if there are real solutions
     if x1 == None:
         output = "This function has no real solutions."
     elif x1 == x2:
        # checks if there is only one intercept
        output = "{} has 1 intercept at x = {}".format( \
             func.display(), x1)
     else:
         output = "{} has x intercepts at {} and {}".format( \
             func.display(), x1, x2)
     return output

@output_info
def find_perfect_trinomial():
    #get values
    x = x_val.get()
    a = a_val.get()
    func = Quadratic.perfect_square(a, x)
    #get factored version of function
    factored_func = Equation(a, x)
    # print equation
    output = "your perfect square trinomial, ({})^2, is expanded as {}".format(\
        factored_func.display(), func.display())
    return output


def main():
    #initialize variables
    global player_choice
    global outputer
    player_choice = None
    window = Tk()
    window.geometry("600x350")
    window.resizable(False, False)
    Title = Label(window, text="Quadratic Functions Tool")
    
    #create radio buttons on top
    player_choice = StringVar()
    Derivative = Radiobutton(window, text='Derivative', value="d", variable=player_choice)
    Y_Value = Radiobutton(window, text='Find y value', value="y", variable=player_choice)
    X_Intercept = Radiobutton(window, text='x Intercepts', value="x", variable=player_choice)
    Info = Radiobutton(window, text='Info', value="i", variable=player_choice)
    Trinomial = Radiobutton(window, text='Perfect Square Trinomial', value="p", variable=player_choice)
    Rules_button = Button(window, text="Tool Rules", width=10, height=1, command=display_rules)
    Game_button = Button(window, text="Use Tool", width=70, height=1, command=choice_selected)

    # initialize variables program requires for calcuations
    global a
    global b
    global c
    global x
    
    global a_val
    global b_val
    global c_val
    global x_val
    
    # initialize variables for the spinboxes
    a_val = IntVar()
    b_val = IntVar()
    c_val = IntVar()
    x_val = IntVar()
    
    a_val.set(0)
    b_val.set(0)
    c_val.set(0)
    x_val.set(0)
    
    #create spinboxes and text
    a = Spinbox(window, from_ = -9999, to = 9999, width = 20, textvariable = a_val)
    b = Spinbox(window, from_ = -9999, to = 9999, width = 20, textvariable = b_val)
    c = Spinbox(window, from_ = -9999, to = 9999, width = 20, textvariable = c_val)
    a_text = Label(window, text="A value")
    b_text = Label(window, text="B value")
    c_text = Label(window, text="C value")
    
    x = Spinbox(window, from_ = -9999, to = 9999, width = 20, textvariable = x_val)
    x_text = Label(window, text="X Value")
    
    #create outputer that will output all info
    outputer = Text(window, width=74, height=8, wrap=WORD)
    
    #place all items onto the grid
    Title.grid(row=1, column=0, columnspan=5)
    Derivative.grid(row=2, column=0)
    Y_Value.grid(row=2, column=1)
    X_Intercept.grid(row=2, column=2)
    Info.grid(row=3, column=0)
    Trinomial.grid(row=3, column=1)
    Game_button.grid(row=4, column=0, columnspan=5)
    outputer.grid(row=5, column=0, columnspan=5)
    
    a_text.grid(row=6, column=0)
    b_text.grid(row=6, column=1)
    c_text.grid(row=6,column=2)
    
    a.grid(row=7, column=0)
    b.grid(row=7, column=1)
    c.grid(row=7, column=2)
    
    x.grid(row=9, column=0)
    x_text.grid(row=8, column = 0)
    
    Rules_button.grid(row=10,column=0)
    
    # starts the window
    window.mainloop()

if __name__ == '__main__':
    main()


