def func(x):
    return x + 1


# def test_answer():
#     assert func(4) == 5
#
#
# def test_answer_2():
#     assert func(5) == 6


# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "y" in x, "some error test message"

    # def test_two(self):
    #     x = "hello"
    #     assert hasattr(x, "check")

def test_sum_2_obj_str():
    assert "a" + "b" == "ab"


def test_sum_2_obj_int():
    assert 2 + 4 == 6


def test_sum_2_obj_int_str():
    assert 1 + "b" == "ab"


def test_sum_2_obj_str():
    assert raise "a" + "b" == "ab"
