def read_whole_number(prompt):
    try:
        text=input(prompt).strip()
    except EOFError:
        return None
    if not text.isdecimal() or len(text)>1000:
        print("Please enter a whole number like 153. digits should not exceed 1000")
        return None
    return int(text)

def is_armstrong(n):
    d=len(str(n))
    total=0
    steps=0
    temp=n
    while temp>0:
        digit=temp%10
        total=total + digit ** d
        temp=temp//10
        steps=steps+1
    return total==n, steps
for n in[0,1,9,10,153,154,154,370,371,407,9474]:
    ok,steps=is_armstrong(n)
    if ok:
        print(f"{n:>5}) is an armstrong number. digit steps: {steps}")
    else:
        print(f"{n:>5}) is not armstrong number. digit steps: {steps}")

print()
n=read_whole_number("type a number to check, (press enter to finish)")
if n is None:
    print("No number checked")
else:
    ok,steps=is_armstrong(n)
    print(f"{n} is an armstrong number, {ok}, digit={steps}")