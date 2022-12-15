#https://www.codewars.com/kata/546dbd81018e956b51000077

add = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
mul = lambda a: lambda b: lambda f: a(b(f))
pow = lambda a: lambda b: b(a)