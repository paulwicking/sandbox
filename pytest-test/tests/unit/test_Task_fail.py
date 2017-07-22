from tasks import Task
import pytest

@pytest.mark.skip(reason="Designed to fail, for example only.")
def test_task_equality():
    t1 = Task('sit there', 'brian')
    t2 = Task('do something', 'okken')
    assert t1 == t2

@pytest.mark.skip(reason="Designed to fail, for example only.")
def test_dict_equality():
    t1_dict = Task('make sandwich', 'okken')._asdict()
    t2_dict = Task('make sandwich', 'okkem')._asdict()
    assert t1_dict == t2_dict
