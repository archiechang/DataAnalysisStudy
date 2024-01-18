# %% クロージャー
def closure(pi):
    def cal(radius):
        return pi * radius * radius

    return cal


c = closure(3.14)
ca2 = closure(3.1415926)

print(f"ca1:{c(10)}")
print(f"ca2:{ca2(10)}")

# %%　decorator
def decorator(func):
    def wrapper(*args,**kwargs):
        print("before decorator")
        result = func(*args,**kwargs)
        print("after decorator")
        return result
    return wrapper
@decorator
def add_num(a,b):
    return a+b

r=add_num(10,20)
print(r)
# %%
