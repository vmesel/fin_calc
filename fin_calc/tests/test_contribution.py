import unittest
import pandas as pd

from fin_calc.calculations import *

from .fixtures.data_fixtures import *


class ContributionTest(unittest.TestCase):
    def setUp(self):
        self.df = generate_dataset_with_patrimony()

    def test_calculate_right_movements_sum(self):
        expected = 900
        returned = calculate_movements_sum(self.df, "movements")
        self.assertEqual(expected, returned)

    def test_calculate_periodic_contribution(self):
        expected = generate_dataset_with_patrimony_and_periodic_contributions()
        returned = calculate_periodic_contribution(self.df, "patrimony", "movements")

        self.assertAlmostEqual(
            returned["contribution"].iloc[-1], expected["contribution"].iloc[-1]
        )

    def test_contribution_return_calculation(self):
        expected = 1.039695599
        df = generate_dataset_with_patrimony_and_periodic_contributions()
        returned = calculate_return_based_on_index(df, "contribution", 0, -1)
        self.assertAlmostEqual(expected, returned)


if __name__ == "__main__":
    unittest.main()
