def divide_by(a,b):
    return a/b;

try:
    ans = divide_by(102,0)
except Exception as e :
    print("something went wrong!",e)
print('ok here')