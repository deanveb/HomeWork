import check50
import check50.c
from string import punctuation

@check50.check()
def exists():
    """ Tệp lap-chu.c tồn tại """
    check50.exists("lap-chu.c")

@check50.check(exists)
def compile():
    """ biên dịch lap-chu"""
    check50.c.compile("lap-chu.c", lcs50=True)

@check50.check(compile)
def check_zero():
    """ kiểm tra nhập độ dài 0 """
    check50.run("./lap-chu").stdin("").reject()

@check50.check(compile)
def check_alphabet():
    """ Kiểm tra nhập số"""
    check50.run("./lap-chu").stdin("12345").stdout("\n")

@check50.check(compile)
def check_special():
    """ Kiểm tra nhập ký tự đặt biệt """
    check50.run("./lap-chu").stdin(";\',/.").stdout("\n")

@check50.check(compile)
def check_special_and_words():
    """ Kiểm tra nhập ký tự đặt biệt cùng với chữ """
    out = check50.run("./lap-chu").stdin("Hello;").stdout()
    correct = "e:1 h:1 l:2 o:1\n"
    test_lap_chu(correct, out)


@check50.check(compile)
def test_1():
    """ Kiểm tra nhập Hello World """
    out = check50.run("./lap-chu").stdin("Hello World").stdout()
    correct = "d:1 e:1 h:1 l:3 o:2 r:1 w:1\n"
    test_lap_chu(correct, out)

@check50.check(compile)
def test_2():
    """ Kiểm tra test 1 """
    out = check50.run("./lap-chu").stdin("Congrats on passing this test").stdout()
    correct = "a:2 c:1 e:1 g:2 h:1 i:2 n:3 o:2 p:1 r:1 s:5 t:4\n"
    test_lap_chu(correct, out)

@check50.check(compile)
def test_3():
    """ Kiểm tra test 2 """
    out = check50.run("./lap-chu").stdin("Are sure you want to continue?").stdout()
    correct = "a:2 c:1 e:3 i:1 n:3 o:3 r:2 s:1 t:3 u:3 w:1 y:1"
    test_lap_chu(correct, out)

def test_lap_chu(correct, out):
    if (out != correct):
        help = ""
        if (out[-1] != "\n"):\
           help = "Có quên xuống hàng không"
        for char in out:
            if (char.isupper()):
                help = "Nhớ là không phân biệt chữ hoa, chữ thường"
        if (any(char in out for char in set(punctuation + "\n"))):
            help = "Nhớ là phải bỏ qua các ký tự đặt biệt"
        check50.Mismatch(correct, out, help=help)
