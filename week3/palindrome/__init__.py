import check50
import check50.c

@check50.check()
def exists():
    """ Tệp palindrome.c tồn tại """
    check50.exists("palindrome.c")

@check50.check(exists)
def compile():
    """ biên dịch palindrome"""
    check50.c.compile("palindrome.c", lcs50=True)

@check50.check(compile)
def check_zero():
    """ kiểm tra nhập độ dài 0 """
    check50.run("./palindrome").stdin("").reject()

@check50.check(compile)
def check_whitespace():
    """ kiểm tra white_space """
    check50.run("./palindrome").stdin("hello world").reject()

@check50.check(compile)
def check_number():
    """ kiểm tra số """
    check50.run("./palindrome").stdin("12345").reject()

@check50.check(compile)
def check_special():
    """ kiểm tra ký tự đặc biệt """
    check50.run("./palindrome").stdin("hello;:!@#$%^&").reject()

@check50.check(compile)
def check_1():
    """ test 1"""
    out = check50.run("./palindrome").stdin("ABba").stdout()
    correct = "YES"
    test_palindrome(correct, out)

@check50.check(compile)
def check_2():
    """ test 2"""
    out = check50.run("./palindrome").stdin("noodle").stdout()
    correct = "NO"
    test_palindrome(correct, out)

@check50.check(compile)
def check_3():
    """ test 3"""
    out = check50.run("./palindrome").stdin("racecar").stdout()
    correct = "YES"
    test_palindrome(correct, out)

@check50.check(compile)
def check_4():
    """ test 4"""
    out = check50.run("./palindrome").stdin("funny").stdout()
    correct = "NO"
    test_palindrome(correct, out)

@check50.check(compile)
def check_5():
    """ test 5"""
    out = check50.run("./palindrome").stdin("madam").stdout()
    correct = "YES"
    test_palindrome(correct, out)

@check50.check(compile)
def check_6():
    """ test 6"""
    out = check50.run("./palindrome").stdin("corny").stdout()
    correct = "NO"
    test_palindrome(correct, out)

@check50.check(compile)
def check_7():
    """ test 7"""
    out = check50.run("./palindrome").stdin("level").stdout()
    correct = "YES"
    test_palindrome(correct, out)

@check50.check(compile)
def check_8():
    """ test 8"""
    out = check50.run("./palindrome").stdin("radar").stdout()
    correct = "YES"
    test_palindrome(correct, out)

def test_palindrome(correct, out):
    if (correct != out):
        raise check50.Mismatch(correct, out)
