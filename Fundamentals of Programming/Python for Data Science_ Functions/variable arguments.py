def greet(**kwargs):
    if kwargs:
        print("Hello {0},{1}".format(kwargs['name'],kwargs['msg']))
greet(name="satish",msg="good morning")
