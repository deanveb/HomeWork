import check50
import check50.c

@check50.check()
def exists():
    """ Tệp colorfulBackground.c tồn tại """
    check50.exists("colorfulBackground.c")

@check50.check(exists)
def compile():
    """ biên dịch colorfulBackground"""
    check50.c.compile("colorfulBackground.c")

@check50.check(compile)
def test_no_input():
    """ không nhập """
    check50.run("./colorfulBackground").exit(1)

@check50.check(compile)
def test_wrong_input():
    """ Nhập sai """
    check50.run("./colorfulBackground hello world").exit(1)

@check50.check(compile)
def test_wrong_len():
    """ sai độ dài """
    check50.run("./colorfulBackground fffffffffffffffffffffffffff").exit(1)

@check50.check(compile)
def test_invalid_color():
    """ sai màu """
    check50.run("./colorfulBackground kmthqp").exit(1)

@check50.check(compile)
def test_1():
    """ chạy test 1 """
    out = check50.run("./colorfulBackground ff0000").stdout()
    correct = "cdd9348c55d753bbe2a3328620ce82df8d8803ce96e1413f0e7ceb6345bac5ee  image.ppm\n"
    test_colorful_background(correct, out)

@check50.check(compile)
def test_2():
    """ chạy test 2 """
    out = check50.run("./colorfulBackground ff00ff").stdout()
    correct = "013020c3b72a82c7a066102b00cdd0dcdcac24c3f54ea0015e6ec1d8133f9852  image.ppm\n"
    test_colorful_background(correct, out)

@check50.check(compile)
def test_3():
    """ chạy test 3"""
    out = check50.run("./colorfulBackground d4aa42").stdout()
    correct = "75af8acf16549e880c2bbf1e47fb5e33b028f1914fdff7c0b42a0256b5d88a85  image.ppm\n"
    test_colorful_background(correct, out)

@check50.check(compile)
def test_4():
    """ chạy test 4"""
    out = check50.run("./colorfulBackground CF3476").stdout()
    correct = "078bd586f80ec2f6c0e753b94bf0aa325d4539455405e317e4540b2e121861b8  image.ppm\n"
    test_colorful_background(correct, out)

def test_colorful_background(correct, out):
    if (correct != out):
        help = ""
        if ("image.ppm" not in out):
            help = "Tên phải là image.ppm\n"
        raise check50.Mismatch(correct, out, help=help)
