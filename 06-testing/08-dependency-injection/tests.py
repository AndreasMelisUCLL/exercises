from datetime import date, timedelta
from calendars import CalendarStub
from tasks import Task, TaskList


def test_task_becomes_overdue():
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    calendar = CalendarStub(today)
    task = Task('some description', tomorrow)
    task_list = TaskList(calendar)

    task_list.add_task(task)
    calendar.today += timedelta(days=2)

    assert [task] == task_list.overdue_tasks