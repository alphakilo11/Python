#https://pypi.org/project/PuLP/
import pulp

x = pulp.LpVariable("x", 80, 200)
prob = pulp.LpProblem("myProblem")
prob += (0.27 * 2.19 * 1,225 / 2 * x ** 2) - (0.27 * 2.19 * 1,225 / 2 * x ** 2) * x / 0.25
