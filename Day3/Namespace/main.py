a=5
def outer():
    z=12
    def inner():
      b=10
      global a
      print('inside inner function is:',b,a)
    inner()
    print(a)
    print(z)
outer()
