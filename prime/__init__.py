import check50
import check50.c

@check50.check()
def exists():
    """ Tệp prime tồn tại """
    check50.exists("prime.c")

@check50.check(exists)
def compile():
    """ biên dịch tien-di.c """
    check50.c.compile("prime.c", lcs50=True)

@check50.check(compile)
def check_negative():
    """ kiểm tra nhập độ dài -1 """
    check50.run("./prime").stdin("-1").reject()

@check50.check(compile)
def check_2():
    """ kiểm tra số 2 """
    out = check50.run("./prime").stdin("2").stdout()
    correct = "YES\n"
    test_prime(out, correct)

@check50.check(compile)
def check_4():
    """ kiểm tra số 4 """
    out = check50.run("./prime").stdin("4").stdout()
    correct = "NO\n"
    test_prime(out, correct)

@check50.check(compile)
def check_21():
    """ kiểm tra số 21 """
    out = check50.run("./prime").stdin("21").stdout()
    correct = "NO\n"
    test_prime(out, correct)

@check50.check(compile)
def check_13():
    """ kiểm tra số 13 """
    out = check50.run("./prime").stdin("13").stdout()
    correct = "YES\n"
    test_prime(out, correct)

@check50.check(compile)
def check_113():
    """ kiểm tra số 113 """
    out = check50.run("./prime").stdin("113").stdout()
    correct = "YES\n"
    test_prime(out, correct)

def test_prime(out, correct):
    if (out != correct):
        check50.Mismatch(correct, out)
