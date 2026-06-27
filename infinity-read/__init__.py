import check50
import check50.c

@check50.check()
def exists():
    """ Tệp inifnity-read tồn tại """
    check50.exists("infinity-read.c")

@check50.check(exists)
def compile():
    """ biên dịch inifnity-read"""
    check50.c.compile("infinity-read.c", lcs50=True)

@check50.check(compile)
def check():
    """" Thử 1 dãy số """
    raise check50.Mismatch("4",check50.run("./infinity-read").stdin("2").stdin("4").stdin("0").stdout())
