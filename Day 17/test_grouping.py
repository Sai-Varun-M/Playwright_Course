# TO run by groups :- pytest test_grouping.py -s -v -m "a"
# To run test common for two groupd :- pytest test_grouping.py -s -v -m "a and b"
# TO run test only in one group but not in other:- pytest test_grouping.py -s -v -m "a" -m "not b"

import pytest # pyright: ignore[reportMissingImports]

@pytest.mark.a
@pytest.mark.b
def test_loginbyemail():
    print("This is login by email test")
    assert 1==1

@pytest.mark.a
def test_loginbyfacebook():
    print("This is login by facebook")
    assert 1==1

@pytest.mark.b
def test_loginbyphone():
    print("This is login by phone")
    assert 1==1

@pytest.mark.a
@pytest.mark.b
def test_signupbyemail():
    print("This is signup by email test")
    assert True == True

@pytest.mark.b
def test_signupbyfacebook():
    print("This is signup by facebook test")
    assert True==True

@pytest.mark.a
def test_signupbyphone():
    print("This is signup by phone test")
    assert True == True

@pytest.mark.a
@pytest.mark.b
def test_paymentindollar():
    print("This is payment in dollar test")
    assert 1==1

@pytest.mark.b
def test_paymentinrupee():
    print("This is payment in rupee test")
    assert 1==1