import check50
import check50.c

@check50.check()
def exists():
    """ Tệp binary.c tồn tại """
    check50.exists("binary.c")
    check50.include("hello.txt", "welcome.txt", "emoji.txt", "special.txt")

@check50.check(exists)
def compile():
    """ biên dịch binary"""
    check50.c.compile("binary.c")

@check50.check(compile)
def test_no_input():
    """ chạy thử không nhập """
    check50.run("./binary").exit(1)

@check50.check(compile)
def test_not_found():
    """ chạy thử file không tồn tại """
    check50.run("./binary wel.txt").exit(2)

@check50.check(compile)
def test_1():
    """ chạy thử test 1 """
    out = check50.run("./binary hello.txt").stdout()
    check50.log(out)
    correct = "48 65 6c 6c 6f 20 57 6f 72 6c 64 0a\n"
    correct1 = "48 65 6c 6c 6f 20 57 6f 72 6c 64 0a \n"
    test_binary([correct, correct1], out)

@check50.check(compile)
def test_2():
    """ chạy thử test 2 """
    out = check50.run("./binary welcome.txt").stdout()
    correct = "54 68 69 73 20 69 73 20 61 20 6d 65 73 73 61 67 65 20 66 72 6f 6d 20 74 68 65 20 66 75 74 75 72 65 21 0a\n"
    correct1 = "54 68 69 73 20 69 73 20 61 20 6d 65 73 73 61 67 65 20 66 72 6f 6d 20 74 68 65 20 66 75 74 75 72 65 21 0a \n"
    test_binary([correct, correct1], out)

@check50.check(compile)
def test_3():
    """ chạy thử test 3 """
    out = check50.run("./binary special.txt").stdout()
    correct = "53 70 65 63 69 61 6c 20 63 68 61 72 61 63 74 65 72 20 64 6f 65 73 6e 27 74 20 62 72 65 61 6b 20 69 74 20 72 69 67 68 74 3f 0a 0a 20 20 20 20 20 20 77 6f 69 65 0a 20 20 20 20 20 20 20 6d 6a 6c 61 73 64 66 3b 6c 6b 6a 6c 6b 3b 6a 7a 6c 78 63 76 0a 20 20 20 20 20 20 20 2a 28 26 5e 26 29 21 5e 21 40 26 2a 24 5e 26 2a 5e 25 54 24 28 2a 21 5e 40 25 26 5e 29 0a\n"
    correct1 = "53 70 65 63 69 61 6c 20 63 68 61 72 61 63 74 65 72 20 64 6f 65 73 6e 27 74 20 62 72 65 61 6b 20 69 74 20 72 69 67 68 74 3f 0a 0a 20 20 20 20 20 20 77 6f 69 65 0a 20 20 20 20 20 20 20 6d 6a 6c 61 73 64 66 3b 6c 6b 6a 6c 6b 3b 6a 7a 6c 78 63 76 0a 20 20 20 20 20 20 20 2a 28 26 5e 26 29 21 5e 21 40 26 2a 24 5e 26 2a 5e 25 54 24 28 2a 21 5e 40 25 26 5e 29 0a \n"
    test_binary([correct, correct1], out)

@check50.check(compile)
def test_4():
    """ chạy thử test 4 """
    out = check50.run("./binary emoji.txt").stdout()
    correct = "6f 68 20 62 6f 79 20 49 20 68 6f 70 65 20 74 68 69 73 20 66 69 6c 65 20 64 6f 65 73 6e 27 74 20 62 72 65 61 6b 20 79 6f 75 72 20 70 72 6f 67 72 61 6d 20 f0 9f 98 8a 0a\n"
    correct1 = "6f 68 20 62 6f 79 20 49 20 68 6f 70 65 20 74 68 69 73 20 66 69 6c 65 20 64 6f 65 73 6e 27 74 20 62 72 65 61 6b 20 79 6f 75 72 20 70 72 6f 67 72 61 6d 20 f0 9f 98 8a 0a \n"
    test_binary([correct, correct1], out);

@check50.check(compile)
def memory():
    """ kiểm tra leaks"""
    code = check50.c.valgrind("./binary hello.txt").exit(timeout=10)
    if code != 0:
       raise check50.Failure("valgrind returned a segfault")

def test_binary(corrects, out):
    if (out not in corrects):
        help = "Nhớ dùng kỹ thuật logging hoặc dùng debugger để tìm lỗi"
        raise check50.Mismatch(corrects[1], out, help=help)
