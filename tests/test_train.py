from lib.train import *

def test_train_intantiates_with_8_wheels():
    train = Train('red')
    
    # actual = train.wheels

    expected = 8

    assert train.wheels == 8
    assert train.colour == 'red'

def test_train_instantiates_with_color():
    train = Train('red')

    actual = train.colour

    expected = 'red'

    assert actual == expected

def test_train_instantiates_with_passengers():
    train = Train('red')

    actual = train.passengers

    expected = []

    assert actual == expected

def test_train_can_add_passenger():
    train = Train('red')
    train.add_passenger('Xiao')

    actual = train.passengers

    expected = ['Xiao']

    assert actual == expected

def test_train_can_add_passengers():
    train = Train('red')
    train.add_passenger('Xiao')
    train.add_passenger('Jose')

    actual = train.passengers

    expected = ['Xiao', 'Jose']

    assert actual == expected