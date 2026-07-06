import check50
import check50.c

@check50.check()
def exists():
    """ Tệp tien-viet.c tồn tại """
    check50.exists("tien-viet.c")

@check50.check(exists)
def compile():
    """ biên dịch tien-viet"""
    check50.c.compile("tien-viet.c", lcs50=True)

@check50.check(compile)
def check_zero():
    """ kiểm tra nhập 0 """
    check50.run("./tien-viet").stdin("0").stdout("0")

@check50.check(compile)
def check_one():
    """ kiểm tra nhập 1 """
    check50.run("./tien-viet").stdin("1").stdout("0")

@check50.check(compile)
def check_1():
    """ test 1 """
    out = check50.run("./tien-viet").stdin("12000").stdout()
    correct = "2\n"
    test_tien_viet(correct, out)

@check50.check(compile)
def check_2():
    """ test 2 """
    out = check50.run("./tien-viet").stdin("99000").stdout()
    correct = "6\n"
    test_tien_viet(correct, out)

@check50.check(compile)
def check_3():
    """ test 3 """
    out = check50.run("./tien-viet").stdin("196500").stdout()
    correct = "7\n"
    test_tien_viet(correct, out)

@check50.check(compile)
def check_4():
    """ test 4 """
    out = check50.run("./tien-viet").stdin("196514").stdout()
    correct = "7\n"
    test_tien_viet(correct, out)

@check50.check(compile)
def check_5():
    """ test 5 """
    out = check50.run("./tien-viet").stdin("1234567").stdout()
    correct = "8\n"
    test_tien_viet(correct, out)

def test_tien_viet(correct, out):
    if (correct != out):
        check50.Mismatch(correct, out)
