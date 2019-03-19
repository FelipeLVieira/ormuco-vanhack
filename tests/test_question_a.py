import unittest

from question_a.overlap import are_overlapping


class TestOverlap(unittest.TestCase):
    def test_1(self):
        print("Lines (1,2) and (3, 4):")
        are_overlapping(1, 2, 3, 4)
        print()

    def test_2(self):
        print("Lines (1,4) and (2, 6):")
        are_overlapping(1, 4, 2, 6)
        print()

    def test_3(self):
        print("Lines (1,3) and (5, 6):")
        are_overlapping(1, 3, 5, 6)
        print()

    def test_4(self):
        print("Lines (2,2) and (2, 2):")
        are_overlapping(2, 2, 2, 2)
        print()

    def test_5(self):
        print("Lines ('a','b') and ('c', 'd'):")
        are_overlapping("a", "b", "c", "d")

    def test_6(self):
        print("Lines (1,10) and (-1, 5):")
        are_overlapping(1, 10, -1, 5)
        print()

    def test_7(self):
        print("Lines (1,2) and (2, 3):")
        are_overlapping(1, 2, 2, 3)
        print()


if __name__ == '__main__':
    unittest.main()
