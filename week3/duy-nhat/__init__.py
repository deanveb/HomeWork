import check50
import check50.c

@check50.check()
def exists():
    """ Tệp duy-nhat.c tồn tại """
    check50.exists("duy-nhat.c")

@check50.check(exists)
def compile():
    """ biên dịch duy-nhat"""
    check50.c.compile("duy-nhat.c", lcs50=True)

@check50.check(compile)
def check_zero():
    """ kiểm tra nhập độ dài 0 """
    check50.run("./duy-nhat").stdin("").reject()

@check50.check(compile)
def check_1():
    """ test 1 """
    out = check50.run("./duy-nhat").stdin("Hello World").stdout()
    correct = "Helo Wrd\n"
    test_duy_nhat(correct, out)

@check50.check(compile)
def check_2():
    """ test 2 """
    out = check50.run("./duy-nhat").stdin("12345 123TisaTest wow").stdout()
    correct = "12345 Tisaet wow\n"
    test_duy_nhat(correct, out)

@check50.check(compile)
def check_3():
    """ test 3 """
    out = check50.run("./duy-nhat").stdin("Fake: Program: heloo();").stdout()
    correct = "Fake: Progm hl();\n"
    test_duy_nhat(correct, out)

def test_duy_nhat(correct, out):
    if (correct != out):
        raise check50.Mismatch(correct, out)
