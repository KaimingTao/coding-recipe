from sympy import symbols, Eq, solve

# define the variable
x = symbols('x')

# create an equation: x^2 - 4 = 0
equation = Eq(x**2 - 4, 0)

# solve the equation for x
solutions = solve(equation, x)

print("Solutions:", solutions)
