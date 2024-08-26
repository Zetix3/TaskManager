from team import Team
from datetime import datetime
from task import Task

#pytest tests.py в терминале

def test_task():
    for _ in range(10):
        t = Task(
                name = "Дописать проект",
                desc='Описание',
                stat="in progress",
                due="30.04.24",
                exec=Team.Employee("Каркарыч"),
                 )
        #assert - утверждение
        assert t.name == "Дописать проект"
        assert t.desc == "Описание"
        assert t.stat == "in progress"
        assert t.due == datetime.strptime("30.04.24", "%d.%m.%y")
        assert t.exec.name == "Каркарыч"

def test_team():
    for _ in range(10):
        bar = Team.Employee("Бараш")
        los = Team.Employee("Лосяш")
        kro = Team.Employee("Крощ")

        my_team = Team("Смешарики", "Лучшая команда", [bar, los, kro])

        assert my_team.name == "Смешарики"
        assert my_team.desc == "Лучшая команда"
        assert len(my_team.lst) == 3
        assert len(my_team.task_mgr.task_list) == 0


        test_employee = Team.Employee("Test Test")
        my_team.add_employee(test_employee)
        assert len(my_team.lst) == 4
        my_team.remove_employee(test_employee)
        assert len(my_team.lst) == 3

        t1 = Task(
            name="Дописать проект",
            desc='Описание',
            stat="in progress",
            due="30.04.24",
            exec=Team.Employee("Каркарыч"),
        )
        t2 = Task(
            name="Дописать проект 2",
            desc='Описание 2',
            stat="in progress",
            due="30.04.24",
            exec=Team.Employee("Каркарыч"),
        )
        my_team.new_task(t1)
        my_team.new_task(t2)
        tm = my_team.get_task_mgr()
        assert len(tm.task_list) == 2
        my_team.del_task(t2)
        assert len(tm.task_list) == 1
        tm.show_all()
        tm.show_due_today()
        for status in ["backlog", "in progress", "in review", "done"]:
            tm.show_by_status("backlog")

