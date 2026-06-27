import check50
import check50.c

@check50.check()
def exists():
    """ Tệp box tồn tại """
    check50.exists("box.c")
    check50.include("2.txt", "5.txt", "10.txt", "20.txt");

@check50.check(exists)
def compile():
    """ biên dịch tien-di.c """
    check50.c.compile("box.c", lcs50=True)

@check50.check(compile)
def check_negative():
    """ kiểm tra nhập độ dài -1 """
    check50.run("./box").stdin("-1").reject()
@check50.check(compile)
def check_zero():
    """ kiểm tra nhập độ dài 0 """
    check50.run("./box").stdin("0").reject()

@check50.check(compile)
def check_len_2():
    """ kiểm tra nhập độ dài 2"""
    out = check50.run("./box").stdin("2").stdout()
    correct = open("2.txt").read()
    check_box(out, correct)

@check50.check(compile)
def check_len_5():
    """ kiểm tra nhập độ dài 5 """
    out = check50.run("./box").stdin("5").stdout()
    correct = open("5.txt").read()
    check_box(out, correct)

@check50.check(compile)
def check_len_10():
    """ kiểm tra nhập độ dài 10 """
    out = check50.run("./box").stdin("10").stdout()
    correct = open("10.txt").read()
    check_box(out, correct)

@check50.check(compile)
def check_len_20():
    """ kiểm tra nhập độ dài 20 """
    out = check50.run("./box").stdin("20").stdout()
    correct = open("20.txt").read()
    check_box(out, correct)

def check_box(out, correct):
    help = ""
    if correct != out:
        if (out.count('\n') != correct.count('\n')):
            help = "Kiểm tra lại có xuống hàng dư không"
        raise check50.Mismatch(correct, out, help=help)

