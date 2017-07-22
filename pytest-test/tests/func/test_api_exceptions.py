import pytest
import tasks
from tasks import Task

def test_add_TypeError():
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')

def test_start_tasks_db_ValueError():
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path/', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"

def test_add_with_id_ValueError():
    new_task = Task('test task', owner='me', done=True, id=15)
    with pytest.raises(ValueError) as excinfo:
        tasks.add(new_task)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "task.id must None"

        
@pytest.mark.smoke
def test_list_TypeError():
    with pytest.raises(TypeError):
        tasks.list(owner=123)

@pytest.mark.get
@pytest.mark.smoke
def test_get_TypeError():
    with pytest.raises(TypeError):
        tasks.get(task_id='123')

class TestUpdate():

    def test_bad_id(self):
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead':1}, task=tasks.Task())

    def test_bad_task(self):
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')

