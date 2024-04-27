import pytest
from datetime import date, timedelta
from tasks import *


@pytest.mark.parametrize('description', ['some description'])
@pytest.mark.parametrize('due_date', [
    date.today() - timedelta(days=1),
    date.today(),
    date.today() + timedelta(days=1),
])
def test_task_creation(description, due_date):
    
    task = Task(description, due_date)
    
    assert task.description == description
    assert task.due_date == due_date


def test_task_list_creation():
    ...