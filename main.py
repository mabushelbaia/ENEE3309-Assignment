import prettytable as pt
import sympy
from sympy.plotting import plotm
import numpy as np

an = {}
bn = {}
for n in range(4):
    t = sympy.Symbol('t')
    w = 2*np.pi*n/0.1
    a = (2/0.1) * (sympy.integrate(sympy.cos(w*t), (t, 0, 0.1/2)) + sympy.integrate((-20*t + 2)*sympy.cos(w*t), (t, 0.1/2, 0.1)))
    b = (2/0.1) * (sympy.integrate(sympy.sin(w*t), (t, 0, 0.1/2)) + sympy.integrate((-20*t + 2)*sympy.sin(w*t), (t, 0.1/2, 0.1)))
    an[n] = round(a, 5)
    bn[n] = round(b, 5)
an[0] = an[0]/2
table = pt.PrettyTable()
table.field_names = ["n", "An", "Bn"]
table.set_style(pt.DOUBLE_BORDER)
table.max_width = 20
table.min_width = 20
table.align = "c"
for n in range(4):
    table.add_row([n, "%.5f" % an[n], "%.5f" % bn[n]])
print(table)


def approximate(t, r=4):
    return an[0]+ sum([an[n]*sympy.cos(2*np.pi*n*t/0.1) + bn[n]*sympy.sin(2*np.pi*n*t/0.1) for n in range(1, r)])


t = sympy.Symbol('t')
function = sympy.Piecewise((1, t <= 0.05), (-20*t + 2, True))
p = plot(function, approximate(t), (t, 0, 0.1), show=False)
p[0].line_color = 'r'
p[0].label = 'g(t)'
p[1].line_color = 'b'
p[1].label = 'g(t) approximated'
p.title = 'g(t) and g(t) approximated'
p.legend = True
p.xlabel = 't'
p.ylabel = 'g(t)'
p.show()

def mse(function, approximate):
    return 10 * sympy.integrate((function - approximate)**2, (t, 0, 0.1))

table = pt.PrettyTable()
table.field_names = ["K", "MSE"]
table.set_style(pt.DOUBLE_BORDER)
table.max_width = 31
table.min_width = 31
table.align = "c"
for k in range(1, 4):
    table.add_row([k, mse(function, approximate(t, k))])
print(table)
