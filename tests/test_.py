import unittest


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(3*4, 12)

    def test_strings_a_3(self):
        self.assertEqual('a'*3, 'aaa')

    def test_assert_true(self):
        self.assertTrue(True)

    def test_fail_unless(self):
        self.assertTrue(True)

    def test_fail_if(self):
        self.assertFalse(False)

    def test_assert_false(self):
        self.assertFalse(False)

    def test_equal(self):
        self.assertEqual(1, 3 - 2)

    def test_not_equal(self):
        self.assertNotEqual(2, 3 - 2)

    def test_equal_fail(self):
        self.assertNotEqual(1, 2)

    def test_not_equal_fail(self):
        self.assertEqual(2, 3 - 1)

    def test_not_almost_equal(self):
        self.assertNotAlmostEqual(1.1, 3.3 - 2.0, places=1)

    def test_almost_equal(self):
        self.assertAlmostEqual(1.1, 3.3 - 2.0, places=0)


if __name__ == "__main__":
    unittest.main()
