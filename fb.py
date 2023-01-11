import unittest


def fizzbuzz(n, debug):
    
    FIZZ = 3
    BUZZ = 5
    numbers = []

    for i in range(n):
        i += 1
        if i % FIZZ == 0 and i % BUZZ == 0:
            numbers.append("FIZZBUZZ")
        elif i % FIZZ == 0:
            numbers.append("FIZZ")
        elif i % BUZZ == 0:
            numbers.append("BUZZ")
        else:
            numbers.append(i)

    # if not in debug mode, return the full list 
    if not debug:
        return numbers
    else:
        return numbers[n-1]


class TestFizzbuzz(unittest.TestCase):
    def test_fizz(self):
        result = fizzbuzz(3, True)
        self.assertEqual(result, "FIZZ")

    def test_buzz(self):
        result = fizzbuzz(5, True)
        self.assertEqual(result, "BUZZ")

    def test_integers(self):
        result = fizzbuzz(2, True)
        self.assertEqual(result, 2)

    def test_list(self):
        result = fizzbuzz(3, False)
        self.assertEqual(result, [1,2,"FIZZ"])


if __name__ == "__main__":
    unittest.main()