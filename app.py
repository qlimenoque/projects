import re
import unittest


def bit_check(num):
    if re.match(r"^\d+", str(num)):
        result = format(int(num), "b")
        str(result)
        if "11" in result or "00" in result:
            return False
        elif "11" not in result and "00" not in result:
            return True
        else:
            return False


table = [0]
number = 1
counter = 0
indent = 20
print("Decimal".ljust(20, ' '), "Binary")

while len(table) <= 22:
    result = format(number, "b")
    if number % 2 == 0:
        number = number * 2 + 1
        table.append(int(number))
        if counter < 10:
            print("{}. {} {}".format(counter, (str(number).ljust(indent, ' ')), result))
        else:
            print("{}. {} {}".format(counter, (str(number).ljust(indent - 1, ' ')), result))
    else:
        number *= 2
        table.append(int(number))
        if counter < 10:
            print("{}. {} {}".format(counter, (str(number).ljust(indent, ' ')), result))
        else:
            print("{}. {} {}".format(counter, (str(number).ljust(indent - 1, ' ')), result))
    counter += 1


class TestStringMethods(unittest.TestCase):
    def test_bit_check_1(self):
        self.assertTrue(bit_check(1))

    def test_bit_check_2(self):
        self.assertTrue(bit_check(2))

    def test_bit_check_3(self):
        self.assertFalse(bit_check(3))

    def test_bit_check_negative_zero(self):
        self.assertTrue(bit_check(-0))

    def test_bit_check_positive_zero(self):
        self.assertTrue(bit_check(0))

    def test_bit_check_char(self):
        self.assertFalse(bit_check('test'))

    def test_bit_check_negative_5(self):
        self.assertFalse(bit_check(-5))

    def test_bit_check_special_char(self):
        self.assertFalse(bit_check("$"))

    def test_bit_check_char_and_number(self):
        self.assertFalse(bit_check("s2a1ff4"))

    def test_bit_check_number_as_string(self):
        self.assertFalse(bit_check("1024"))

    def test_bit_check_1365(self):
        self.assertTrue(bit_check(1365))

    def test_bit_check_none(self):
        self.assertFalse(bit_check(None))

    def test_bit_check_special_chars(self):
        self.assertFalse(bit_check("!@#$%^&*()[]"))

    def test_bit_check_special_char(self):
        self.assertFalse(bit_check("$"))

    def test_bit_check_loop(self):
        for i in range(2, max(table)):
            if i not in table:
                self.assertFalse(bit_check(i))
            else:
                self.assertTrue(bit_check(i))


if __name__ == '__main__':
    unittest.main()
