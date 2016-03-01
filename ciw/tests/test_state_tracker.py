import unittest
import ciw

class TestStateTracker(unittest.TestCase):

    def test_base_init_method(self):
        Q = ciw.Simulation(ciw.load_parameters(
          'ciw/tests/datafortesting/logs_test_for_simulation/parameters.yml'))
        B = ciw.StateTracker(Q)
        self.assertEqual(B.simulation, Q)
        self.assertEqual(B.state, None)

    def test_base_change_state_accept_method(self):
        Q = ciw.Simulation(ciw.load_parameters(
          'ciw/tests/datafortesting/logs_test_for_simulation/parameters.yml'))
        B = ciw.StateTracker(Q)
        self.assertEqual(B.state, None)
        B.change_state_accept(1, 1)
        self.assertEqual(B.state, None)

    def test_base_change_state_block_method(self):
        Q = ciw.Simulation(ciw.load_parameters(
          'ciw/tests/datafortesting/logs_test_for_simulation/parameters.yml'))
        B = ciw.StateTracker(Q)
        self.assertEqual(B.state, None)
        B.change_state_block(1, 1)
        self.assertEqual(B.state, None)

    def test_base_change_state_release_method(self):
        Q = ciw.Simulation(ciw.load_parameters(
          'ciw/tests/datafortesting/logs_test_for_simulation/parameters.yml'))
        B = ciw.StateTracker(Q)
        self.assertEqual(B.state, None)
        B.change_state_release(1, 1, True)
        self.assertEqual(B.state, None)


class TestNaiveTracker(unittest.TestCase):

    def test_naive_init_method(self):
        Q = ciw.Simulation(ciw.load_parameters(
          'ciw/tests/datafortesting/logs_test_for_simulation/parameters.yml'))
        B = ciw.NaiveTracker(Q)
        self.assertEqual(B.simulation, Q)
        self.assertEqual(B.state, [[0, 0], [0, 0], [0, 0], [0, 0]])

    def test_naive_change_state_accept_method(self):
        Q = ciw.Simulation(ciw.load_parameters(
          'ciw/tests/datafortesting/logs_test_for_simulation/parameters.yml'))
        B = ciw.NaiveTracker(Q)
        self.assertEqual(B.state, [[0, 0], [0, 0], [0, 0], [0, 0]])
        B.change_state_accept(1, 1)
        self.assertEqual(B.state, [[1, 0], [0, 0], [0, 0], [0, 0]])

    def test_naive_change_state_block_method(self):
        Q = ciw.Simulation(ciw.load_parameters(
          'ciw/tests/datafortesting/logs_test_for_simulation/parameters.yml'))
        B = ciw.NaiveTracker(Q)
        B.state = [[1, 0], [0, 0], [0, 0], [0, 0]]
        B.change_state_block(1, 1)
        self.assertEqual(B.state, [[0, 1], [0, 0], [0, 0], [0, 0]])

    def test_naive_change_state_release_method(self):
        Q = ciw.Simulation(ciw.load_parameters(
          'ciw/tests/datafortesting/logs_test_for_simulation/parameters.yml'))
        B = ciw.NaiveTracker(Q)
        B.state = [[2, 1], [3, 0], [1, 0], [4, 4]]
        B.change_state_release(1, 1, False)
        self.assertEqual(B.state, [[1, 1], [3, 0], [1, 0], [4, 4]])
        B.change_state_release(1, 1, True)
        self.assertEqual(B.state, [[1, 0], [3, 0], [1, 0], [4, 4]])