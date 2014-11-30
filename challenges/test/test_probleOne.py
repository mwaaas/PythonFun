from __future__ import absolute_import
from unittest import TestCase
from challenges.problemOne import tree_n_plus_one_problem

class TestProblemOne(TestCase):

    def test_correct_results_is_returned(self):
        # input of 22 should result to the given list
        input_param = 22
        results = [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

        self.assertEqual(results, tree_n_plus_one_problem(input_param))

    def test_wrong_parameters_raises_errors(self):
        # wrong input parameters
        wrong_prams = [0, 1000000]
        for i in wrong_prams:
            self.assertRaises(TypeError, tree_n_plus_one_problem, i)