from team import Team

if __name__ == "__main__":
    bar = Team.Employee("Бараш")
    los = Team.Employee("Лосяш")
    kro = Team.Employee("Крощ")

    my_team = Team("Смешарики", "Лучшая команда", [bar, los, kro])

    nol = Team.Employee("Нолик")
    sim = Team.Employee("Симка")
    my_second_team = Team("Фиксики", "Плохая команда", [nol, sim])

    tm = my_team.get_task_mgr()
    tm2 = my_second_team.get_task_mgr()

    my_team.task_mgr.new_task("Прочитать книгу", stat="In Progress")
    my_team.task_mgr.new_task("Дописать проект", due = "30.04.24", stat="In Progress")
    my_team.task_mgr.new_task("Физика", stat="done")
    my_team.task_mgr.new_task("C++", stat="in progress")

    tm2.new_task("Починить всё", due="01.01.99", stat = "backlog")
    tm.show_all()