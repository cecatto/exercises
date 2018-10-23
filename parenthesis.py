import unittest


def validate(a_string):
    print("Starting iteration")
    stack = []

    for c in a_string:
        print(str(stack))

        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            stack.pop()

    return True

class Test(unittest.TestCase):

    def testAll(self):
        self.assertEqual(validate("(())"), True)
        self.assertEqual(validate("()()"), True)
        self.assertEqual(validate(")())"), False)
        self.assertEqual(validate("(()))"), False)


if __name__ == "__main__":
    unittest.main()