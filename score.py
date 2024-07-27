def add_score(difficulty, score_file_name):
    point_of_winning = (difficulty * 3) + 5
    try:
        file = open(score_file_name, 'r+')
        old_points = int(file.read())
        new_points = old_points + point_of_winning
        file.seek(0)
        file.write(str(new_points))
        file.close()

    except FileNotFoundError:
        file = open(score_file_name, 'w')
        file.write(str(point_of_winning))
        file.close()
