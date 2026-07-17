import check50
import check50.c

@check50.check()
def exists():
    """ Tệp colorfulStripe.c tồn tại """
    check50.exists("colorfulStripe.c")

@check50.check(exists)
def compile():
    """ biên dịch colorfulStripe"""
    check50.c.compile("colorfulStripe.c")

@check50.check(compile)
def test_no_input():
    """ không nhập """
    check50.run("./colorfulStripe").exit(1)

@check50.check(compile)
def test_wrong_input():
    """ Nhập sai """
    check50.run("./colorfulStripe hello world").exit(1)

@check50.check(compile)
def test_wrong_len():
    """ sai độ dài màu """
    check50.run("./colorfulStripe 15 ff000000ff 011230ff00").exit(1)

@check50.check(compile)
def test_wrong_number():
    """ sai độ lớn """
    check50.run("./colorfulStripe 21 ff00ff 00ff00").exit(1)

@check50.check(compile)
def test_zero():
    """ Nhập 0 """
    check50.run("./colorfulStripe 0 ff00ff 00ff00").exit(1)

@check50.check(compile)
def test_invalid_color():
    """ sai mã màu """
    check50.run("./colorfulStripe 15 kmthqp lkpuyq").exit(1)

@check50.check(compile)
def test_1():
    """ kiểm tra test 1 """
    out = check50.run("./colorfulStripe 5 ff0000 00ff00").stdout()
    correct = "f016da71af8ba7e530a140f7194afa45cb91b16264ee10b3a6e022bc5b92b067  image.ppm\n"
    test_colorful_stripe(correct, out)

@check50.check(compile)
def test_2():
    """ kiểm tra test 2 """
    out = check50.run("./colorfulStripe 20 ff0000 00ff00").stdout()
    correct = "ca4a6c66d7dd1ec7de62cfaff9a297dd48cbe2717ac33decb4899f199bce3926  image.ppm\n"
    test_colorful_stripe(correct, out)

@check50.check(compile)
def test_3():
    """ kiểm tra test 3 """
    out = check50.run("./colorfulStripe 5 CF3476 ED760E").stdout()
    correct = "8e82f6cf816667f242ff1e7abcfa6f1856bca9e19030c061c1dbc6551cb5b824  image.ppm\n"
    test_colorful_stripe(correct, out)

@check50.check(compile)
def test_4():
    """ kiểm tra test 4 """
    out = check50.run("./colorfulStripe 20 1F3A3D 8673A1").stdout()
    correct = "c760faf7d0c5cf8aa117927581dec82ee4eae7b8f1e5ddf5711dacb0001f0195  image.ppm\n"
    test_colorful_stripe(correct, out)

def test_colorful_stripe(correct, out):
    if (correct != out):
        raise check50.Mismatch(correct, out, help=help)
