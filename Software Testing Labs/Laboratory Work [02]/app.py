import re
import unittest


# Define main function
def bit_check(num):
    # If input matches regex "from 0 to infinity" then
    if re.match(r"^\d+", str(num)):
        # Convert integer to binary
        result = format(int(num), "b")
        # Convert binary to string
        str(result)
        # Check if string "result" has 11 or 00 in it
        if "11" in result or "00" in result:
            # If string has 11 or 00 return False
            return False
        elif "11" not in result and "00" not in result:
            # If string hasn't 11 and 00 in it, return True
            return True
        else:
            # In other cases return False (if string has special or other characters etc)
            return False


# Define the variable @table with 0 in 0 index
table = [0]
number = 1
counter = 0
indent = 20

# Print headers of the table
print("Decimal".ljust(20, ' '), "Binary")

# Appending table with numbers that return True in bit_check() function
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


# Making test for bit_check() function
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


# Run tests
if __name__ == '__main__':
    unittest.main()
