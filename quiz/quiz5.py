for week in range(1, 51):
    with open("{}주차.txt".format(week), "w", encoding="utf8") as report_file:
        report_file.write("- {} 주차 주간보고 -\n부서 : \n이름 : \n업무 요약 : ".format(week))
