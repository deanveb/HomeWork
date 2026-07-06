import check50
import check50.c

@check50.check()
def exists():
    """ Tệp vuong-xien.c tồn tại """
    check50.exists("vuong-xien.c")
    check50.include("3.txt", "5.txt", "40.txt")

@check50.check(exists)
def compile():
    """ biên dịch vuong-xien"""
    check50.c.compile("vuong-xien.c", lcs50=True)

@check50.check(compile)
def check_negative():
    """ kiểm tra nhập số âm """
    check50.run("./vuong-xien").stdin("-2341").reject()

@check50.check(compile)
def check_zero():
    """ kiểm tra nhập 0 """
    check50.run("./vuong-xien").stdin("0").reject()

@check50.check(compile)
def check_1():
    """ test 1"""
    out = check50.run("./vuong-xien").stdin("3").stdout()
    test_vuong_xien(open("3.txt").read(), out)

@check50.check(compile)
def check_2():
    """ test 2"""
    out = check50.run("./vuong-xien").stdin("5").stdout()
    test_vuong_xien(open("5.txt").read(), out)

@check50.check(compile)
def check_3():
    """ test 3"""
    out = check50.run("./vuong-xien").stdin("40").stdout()
    test_vuong_xien(open("40.txt").read(), out)

def test_vuong_xien(correct, out):
    if (correct != out):
        check50.Mismatch(correct, out)
