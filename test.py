# Install packages
!pip install tellurium -q

# Import packages
import tellurium as te # Python-based modeling environment for kinetic models

print("Hello World.")

r = te.loada("species a=3")
r.simulate()
r.plot()
