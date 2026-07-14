import check50
import check50.c

@check50.check()
def exists():
    """ Tệp tam-giac-pascal.c tồn tại """
    check50.exists("tam-giac-pascal.c")
    check50.include("4.txt", "8.txt", "20.txt", "10.txt")

@check50.check(exists)
def compile():
    """ biên dịch tam-giac-pascal"""
    check50.c.compile("tam-giac-pascal.c", lcs50=True)

@check50.check(compile)
def check_negative():
    """ kiểm tra nhập -21 """
    check50.run("./tam-giac-pascal").stdin("-21").reject()

@check50.check(compile)
def check_zero():
    """ kiểm tra nhập 0 """
    check50.run("./tam-giac-pascal").stdin("0").reject()

@check50.check(compile)
def check_1():
    """ test 1 """
    out = check50.run("./tam-giac-pascal").stdin("4").stdout()
    test_tam_giac_pascal(open("4.txt").read(), out)

@check50.check(compile)
def check_2():
    """ test 2 """
    out = check50.run("./tam-giac-pascal").stdin("8").stdout()
    test_tam_giac_pascal(open("8.txt").read(), out)

@check50.check(compile)
def check_3():
    """ test 3 """
    out = check50.run("./tam-giac-pascal").stdin("10").stdout()
    test_tam_giac_pascal(open("10.txt").read(), out)

@check50.check(compile)
def check_4():
    """ test 4 """
    out = check50.run("./tam-giac-pascal").stdin("20").stdout()
    test_tam_giac_pascal(open("20.txt").read(), out)

def test_tam_giac_pascal(correct, out):
    if (correct != out):
        raise check50.Mismatch(correct, out)
