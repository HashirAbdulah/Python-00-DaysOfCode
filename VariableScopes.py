# Global Scope:
x = "Jane"
def myfunc1():
    global x
    x = "hello"
myfunc1()
print(x)

# NonLocal Variabl for Nested Functions:
def abc():
  y = 10
  print(y)
  def efg():
    nonlocal y
    y = 20
    print(y)
  efg()
  print(y)

abc()
  