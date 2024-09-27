#cricket tests
import unittest


def find_combinations(total_balls, target_score):
    score = [1, 4, 6]
    combinations = []

    for x in range(total_balls + 1):
        for y in range(total_balls + 1):
            for z in range(total_balls + 1):
                if (x + y + z) == total_balls:
                    if (x*1) + (y*4) + (z*6) == target_score:
                        combinations.append((x, y, z))
    return combinations

total_balls = 6
target_score = 24

combinations = find_combinations(total_balls, target_score)

print(f"Possible combinations to score {target_score} runs in {total_balls} are:")

for combo in combinations:
    print(f"Singles: {combo[0]}, boundaries: {combo[1]}, Sixes: {combo[2]}")


class TestFindCombinations(unittest.TestCase):

    def test_exact_scenario(self):
        # Test the exact scenario of 24 runs in 6 balls
        target_runs = 24
        total_balls = 6
        expected_combinations = [
            (0, 0, 4),
            (2, 3, 1),
            (4, 1, 3)
        ]
        result = find_combinations(target_runs, total_balls)
        self.assertEqual(sorted(result), sorted(expected_combinations))

    def test_no_combinations(self):
        # Test a scenario where no valid combinations exist
        target_runs = 10
        total_balls = 6
        expected_combinations = []  # There should be no way to score 10 runs in 6 balls using 1, 4, and 6 only
        result = find_combinations(target_runs, total_balls)
        self.assertEqual(result, expected_combinations)

    def test_all_singles(self):
        # Test a scenario where all runs are scored as singles
        target_runs = 6
        total_balls = 6
        expected_combinations = [(6, 0, 0)]  # Only one way: 6 singles
        result = find_combinations(target_runs, total_balls)
        self.assertEqual(result, expected_combinations)

    def test_all_fours(self):
        # Test a scenario where all runs are scored as fours
        target_runs = 24
        total_balls = 6
        expected_combinations = [(0, 6, 0)]  # Only one way: 6 fours
        result = find_combinations(target_runs, total_balls)
        self.assertEqual(result, expected_combinations)

    def test_edge_case(self):
        # Test the edge case where target_runs is 0
        target_runs = 0
        total_balls = 6
        expected_combinations = []  # Should be no way to score 0 runs with 6 balls using only 1, 4, or 6
        result = find_combinations(target_runs, total_balls)
        self.assertEqual(result, expected_combinations)


if __name__ == '__main__':
    unittest.main()