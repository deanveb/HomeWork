import check50
import check50.c

@check50.check()
def exists():
    """ Tệp fibonacci tồn tại """
    check50.exists("fibonacci.c")

@check50.check(exists)
def compile():
    """ biên dịch fibonacci """
    check50.c.compile("fibonacci.c", lcs50=True)

@check50.check(compile)
def check_negative():
    """ kiểm tra nhập độ dài -1 """
    check50.run("./fibonacci").stdin("-1").reject()
@check50.check(compile)
def check_zero():
    """ kiểm tra nhập độ dài 0 """
    check50.run("./fibonacci").stdin("0").reject()

@check50.check(compile)
def check_4():
    """ kiểm tra nhập 4"""
    out = check50.run("./fibonacci").stdin("4").stdout()
    correct = "3"
    test_fibonacci(out, correct)

@check50.check(compile)
def check_7():
    """ kiểm tra nhập 7"""
    out = check50.run("./fibonacci").stdin("7").stdout()
    correct = "13"
    test_fibonacci(out, correct)

@check50.check(compile)
def check_9():
    """ kiểm tra nhập 9"""
    out = check50.run("./fibonacci").stdin("9").stdout()
    correct = "34"
    test_fibonacci(out, correct)

@check50.check(compile)
def check_13():
    """ kiểm tra nhập 13"""
    out = check50.run("./fibonacci").stdin("13").stdout()
    correct = "233"
    test_fibonacci(out, correct)

@check50.check(compile)
def check_20():
    """ kiểm tra nhập 20"""
    out = check50.run("./fibonacci").stdin("20").stdout()
    correct = "6765"
    test_fibonacci(out, correct)

def test_fibonacci(out, correct):
    if (out != correct):
        check50.Mismatch(correct, out)
