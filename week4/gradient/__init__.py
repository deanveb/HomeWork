import check50
import check50.c

@check50.check()
def exists():
    """ Tệp gradient.c tồn tại """
    check50.exists("gradient.c")

@check50.check(exists)
def compile():
    """ biên dịch gradient"""
    check50.c.compile("gradient.c")

@check50.check(compile)
def test_1():
    """ chạy thử chương trình """
    out = check50.run("./gradient").stdout()
    correct = "f15f08b908897a2def07001398040c6ba4ea931948487db68914bc9f09293b71  image.ppm\n"
    test_red_background(correct, out)

@check50.check(compile)
def memory():
    """ kiểm tra leaks"""
    code = check50.c.valgrind("./gradient").exit(timeout=10)
    if code != 0:
       raise check50.Failure("valgrind returned a segfault")

def test_red_background(correct, out):
    if (correct != out):
        raise check50.Mismatch(correct, out)
