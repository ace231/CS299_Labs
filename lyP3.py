# Alfredo Ceballos
# CS 299
# Project 3

# Problem 1 #
# Farenheit to Celsius formula : Tc = (Tf - 32) / 1.8
def faren_to_cels(f):
    return (f - 32) / 1.8

f_temp = -459.67 # Just start off at absolute zero
while f_temp <= 200:
    if f_temp == -459.67:
        print("%7.2fF   %7.2fC   absolute zero" % (f_temp, faren_to_cels(f_temp)))
        f_temp = -60.0
    elif f_temp == 30:
        # We're incrementing by 10 but set to 32
        # or else it'll skip and keep going up
        print("%7.2fF   %7.2fC" % (f_temp, faren_to_cels(f_temp)))
        f_temp = 32
        print("%7.2fF   %7.2fC   freezing//melting point of water" \
              % (f_temp, faren_to_cels(f_temp)))
        f_temp -= 2   # Set back to 30
    elif f_temp == 70:
        print("%7.2fF   %7.2fC   room temperature" % (f_temp, faren_to_cels(f_temp)))
    elif f_temp == 90:
        print("%7.2fF   %7.2fC" % (f_temp, faren_to_cels(f_temp)))
        f_temp = 98.6
        print("%7.2fF   %7.2fC   body temperature" % (f_temp, faren_to_cels(f_temp)))
        f_temp -= 8.6
    elif f_temp == 200:
        print("%7.2fF   %7.2fC" % (f_temp, faren_to_cels(f_temp)))
        f_temp = 212
        print("%7.2fF   %7.2fC   boiling temperature of water" \
              % (f_temp, faren_to_cels(f_temp)))
    else:
        print("%7.2fF   %7.2fC" % (f_temp, faren_to_cels(f_temp)))
    f_temp += 10
        
