#To run :- pytest test_demos.py
#To run with outputs:- pytest test_demos.py -s
#To get more clear outputs:- pytest test_demos.py -s -v
#To run only one test:- pytest test_demos.py::test_one 


# def test_one():
#     print("This is my test one")

# def test_two():
#     print("This is my test two")

# def test_three():
#     print("This is my test three")


class TestClass:
    def test_one(self):
        print("This is my test one")

    def test_two(self):
        print("This is my test two")

    def test_three(self):
        print("This is my test three")