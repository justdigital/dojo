import unittest
from fizzbuzzer import player

class FizzBuzzer(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(player(1), "1")

    def test_say_2_when_2(self):
        self.assertEqual(player(2), "2")

    def test_say_4_when_4(self):
        self.assertEqual(player(4), "4")

    def test_say_fizz_when_3(self):
        self.assertEqual(player(3), "fizz")

    def test_say_fizz_when_6(self):
        self.assertEqual(player(6), "fizz")

    def test_say_fizz_when_9(self):
        self.assertEqual(player(9),"fizz")

    def test_say_buzz_when_5(self):
        self.assertEqual(player(5), "buzz")

    def test_say_buzz_when_10(self):
        self.assertEqual(player(10), "buzz")

    def test_say_buzz_when_20(self):
        self.assertEqual(player(20), "buzz")

    def test_say_fizzbuzz_when_15(self):
        self.assertEqual(player(15), "fizzbuzz")

    def test_say_fizzbuzz_when_30(self):
        self.assertEqual(player(30), "fizzbuzz")

    def test_say_fizzbuzz_when_45(self):
        self.assertEqual(player(45), 'fizzbuzz')

if __name__ == "__main__":
    unittest.main()
