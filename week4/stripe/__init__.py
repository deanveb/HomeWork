import check50
import check50.c

@check50.check()
def exists():
    """ Tệp stripe.c tồn tại """
    check50.exists("stripe.c")

@check50.check(exists)
def compile():
    """ biên dịch stripe"""
    check50.c.compile("stripe.c")

@check50.check(compile)
def test_1():
    """ chạy thử chương trình """
    out = check50.run("./stripe").stdout()
    correct = "0d7fc45b29b9311caa9552c805e0f0a37ac81d293dd74c416bd289a518260772  image.ppm\n"
    test_red_background(correct, out)

@check50.check(compile)
def memory():
    """ kiểm tra leaks"""
    code = check50.c.valgrind("./stripe").exit(timeout=10)
    if code != 0:
       raise check50.Failure("valgrind returned a segfault")

def test_red_background(correct, out):
    if (correct != out):
        raise check50.Mismatch(correct, out)
