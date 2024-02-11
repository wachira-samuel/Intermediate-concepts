#Exception and errors
try:
    a=5/0
except Exception as e:
    print(e)
except TypeError as e:
    print(e)

class ValueTooHighError(Exception):
    pass
class ValueTooSmallError(Exception):
    def __int__(self,message,test_value):
        self.message=message
        self.value=value

    def test_value(x):
        if x>100:
            raise ValueTooHighError("value is too high")
        if x<5:
            raise ValueTooSmallError('value is small',x)
try:
    False
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message,e.value)