from tasks import tasks 

def test_defaults():
    t1 = tasks.Task()
    t2 = tasks.Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    t = tasks.Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)
