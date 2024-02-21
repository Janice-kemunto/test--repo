print("Hello , Class of 2020")
print("Welcome to the world of Python")
a=10
b=0
try:
  print("This is outer try block")
  try:
    print("a/b")
  except ZeroDivisionError:
    print("Division by zero ")
  finally:
    print("inside inner finally block")
except Exception:
    print("General exception")
finally:
    print("inside outer finally block")

