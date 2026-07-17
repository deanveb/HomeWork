import check50
import check50.c

@check50.check()
def exists():
    """ Tệp redBackground.c tồn tại """
    check50.exists("redBackground.c")

@check50.check(exists)
def compile():
    """ biên dịch redBackground"""
    check50.c.compile("redBackground.c")

@check50.check(compile)
def test_1():
    """ chạy thử chương trình """
    out = check50.run("./redBackground").stdout()
    correct = "cdd9348c55d753bbe2a3328620ce82df8d8803ce96e1413f0e7ceb6345bac5ee  image.ppm\n"
    test_red_background(correct, out)

@check50.check(compile)
def memory():
    """ kiểm tra leaks"""
    code = check50.c.valgrind("./redBackground").exit(timeout=10)
    if code != 0:
       raise check50.Failure("valgrind returned a segfault")

def test_red_background(correct, out):
    if (correct != out):
        raise check50.Mismatch(correct, out)
