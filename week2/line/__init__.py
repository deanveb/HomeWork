import check50
import check50.c

@check50.check()
def exists():
    """ Tệp line tồn tại """
    check50.exists("line.c")

@check50.check(exists)
def compile():
    """ biên dịch line"""
    check50.c.compile("line.c", lcs50=True)

@check50.check(compile)
def check_negative():
    """ kiểm tra nhập độ dài -1 """
    check50.run("./line").stdin("-1").reject()
@check50.check(compile)
def check_zero():
    """ kiểm tra nhập độ dài 0 """
    check50.run("./line").stdin("0").reject()

@check50.check(compile)
def check_len_2():
    """ kiểm tra nhập độ dài 2 """
    out = check50.run("./line").stdin("2").stdout()
    if ("##\n" != out):
      raise check50.Mismatch("##\n", out)

@check50.check(compile)
def check_len_10():
    """ kiểm tra nhập độ dài 10 """
    out = check50.run("./line").stdin("10").stdout()
    if ("##########\n" != out):
      raise check50.Mismatch("##########\n", out)

