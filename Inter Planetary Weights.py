# Inter Planetary Weights
# Nick Fernandes

# Here are my constants, they are floats. 

MERCURY_SGF = 0.38
VENUS_SGF = 0.91
MOON_SGF = 0.165
MARS_SGF = 0.38
JUPITER_SGF = 2.34
SATURN_SGF = 0.93
URANUS_SGF = 0.92
NEPTUNE_SGF = 1.12
PLUTO_SGF = 0.066

# Inputs and convert 

sName = input("What is your name? : ")
fWeight = float(input("Hello " + sName + ", please enter your weight: "))

# Calculations

fMercuryWeight = MERCURY_SGF * fWeight
fVenusWeight = VENUS_SGF * fWeight
fMoonWeight = MOON_SGF * fWeight
fMarsWeight = MARS_SGF * fWeight
fJupiterWeight = JUPITER_SGF * fWeight
fSaturnWeight = SATURN_SGF * fWeight
fUranusWeight = URANUS_SGF * fWeight
fNeptuneWeight = NEPTUNE_SGF * fWeight
fPlutoWeight = PLUTO_SGF * fWeight

# Output's

print(sName + " your weight on each of our Solar System's planets is:")
print('{:20}'.format("Weight on Mercury:"), format(fMercuryWeight, "10.2f"))
print('{:20}'.format("Weight on Venus:"), format(fVenusWeight, "10.2f"))
print('{:20}'.format("Weight on Moon:"), format(fMoonWeight, "10.2f"))
print('{:20}'.format("Weight on Mars:"), format(fMarsWeight, "10.2f"))
print('{:20}'.format("Weight on Jupiter:"), format(fJupiterWeight, "10.2f"))
print('{:20}'.format("Weight on Saturn:"), format(fSaturnWeight, "10.2f"))
print('{:20}'.format("Weight on Uranus:"), format(fUranusWeight, "10.2f"))
print('{:20}'.format("Weight on Neptune:"), format(fNeptuneWeight, "10.2f"))
print('{:20}'.format("Weight on Pluto:"), format(fPlutoWeight, "10.2f"))