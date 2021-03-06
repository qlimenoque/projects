import re
import unittest
import sys

arg = sys.argv[1]


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
while len(table) <= 10:
    result = format(number, "b")
    if number % 2 == 0:
        number = number * 2 + 1
        table.append(int(number))
        if counter < 10:
            print("{}. {} {}".format(counter, (str(number).ljust(indent, ' ')), result + '1'))
        else:
            print("{}. {} {}".format(counter, (str(number).ljust(indent - 1, ' ')), result + '0'))
    else:
        number *= 2
        table.append(int(number))
        if counter < 10:
            print("{}. {} {}".format(counter, (str(number).ljust(indent, ' ')), result + '0'))
        else:
            print("{}. {} {}".format(counter, (str(number).ljust(indent - 1, ' ')), result + '1'))
    counter += 1


# Making test for bit_check() function
class TestStringMethods(unittest.TestCase):
    def test_bit_check_negative_zero(self):
        self.assertTrue(bit_check(-0))

    def test_bit_check_positive_zero(self):
        self.assertTrue(bit_check(0))

    def test_bit_check_string(self):
        self.assertFalse(bit_check('test'))

    def test_bit_check_negative_5(self):
        self.assertFalse(bit_check(-5))

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

    # Test integers from min(table) to max(table)
    def test_bit_check_loop(self):
        for i in range(2, max(table)):
            if i not in table:
                self.assertFalse(bit_check(i))
            else:
                self.assertTrue(bit_check(i))


# Run tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

# Run main function bit_check()
run = bit_check(arg)
if run:
    print("\nThe result is: True\n")
else:
    print("\nThe result is: False\n")
