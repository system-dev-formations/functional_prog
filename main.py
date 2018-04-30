# ---
from pymonad.Reader import curry
from pygraph.classes.graph import graph


gr = graph()

@curry
def systolic_bp(bmi, age, gender_male, treatment):
    return 68.15+0.58*bmi+0.65*age+0.94*gender_male+6.44*treatment


print(systolic_bp(25, 50, 1, 0))
print(systolic_bp(25,50,0,1))

treated= systolic_bp(25, 50, 0)
print(treated(0))
print(treated(1))