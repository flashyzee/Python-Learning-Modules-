 Define your "f_to_c" function here.
# Return ONLY the result of the calculation with no rounding or additional language.

def f_to_c(fahrenheit):
  celsius = (fahrenheit-32) / 1.8
  return celsius

# Define your main() function 
# Your main() will do three things:
#    1. Ask the user for the fahrenheit value
#    2. Pass an argument to the f_to_c(f) function
#    3. Print the returned value from the f_to_c(f) function

def main():
  f = int(input("What is the temperature you'd like to convert: "))
  answer = f_to_c(f)
  print(f"{f} equals {answer} in Celsius")

# Included here is the special language that runs your main() function by default.  
# Do NOT modify anything below this line
if __name__== "__main__":
  main()