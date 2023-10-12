from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('contains_duplicates') as testcase:
        testcase([])
        testcase([1])
        testcase([1, 1])
        testcase([1, 2, 1])
        testcase([3, 1, 2, 1])
        testcase([3, 6, 2, 1])
        testcase([3, 6, 2, 1, 6])
