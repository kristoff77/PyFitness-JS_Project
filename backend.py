import os


# --------------------------------------------proces rejestracji użytkownika--------------------------------------------

def registerUser(username, password):
    if len(password) < 6:
        return 2

    try:
        users = open("user_list.txt", "r+", encoding="utf-8")

        for line in users:
            line = line.strip("\n")
            line = line.split('\t')
            if line[0] == username:
                return 1
    except IOError:
        raise IOError

    users.write(f"{username}\t{password}\n")

    return 0


# ---------------------------------------------proces logowania użytkownika---------------------------------------------

def logUser(username, password):
    try:
        users = open("user_list.txt", "r", encoding="utf-8")

        for line in users:
            line = line.strip("\n")
            line = line.split("\t")

            if line[0] == username and line[1] == password:
                return True
    except IOError:
        raise IOError

    return False


# ----------------------------------tworzenie listy z nazwami wszystkich treningów--------------------------------------

def createTrainingsList():
    trainings_list = os.listdir("Lista_treningów")

    for i in range(len(trainings_list)):
        trainings_list[i] = trainings_list[i].replace("_", " ")

    return trainings_list


# --------------------tworzenie listy z nazwami wszystkich zapisanych treningów uzytkownika-----------------------------

def createUsersTrainingsList(username):
    try:
        users_data = open("user_list.txt", "r", encoding="utf-8")
        users_trainings = []

        for line in users_data:
            if username in line:
                line = line.strip("\n")
                line = line.replace("Lista_treningów\\", '')
                line = line.replace('_', ' ')
                line = line.split("\t")
                users_trainings = line[2::]
    except IOError:
        raise IOError

    return users_trainings


# ------------------------------tworzenie listy z nazwami ćwiczeń w danym treningu--------------------------------------

def createExercisesList(training_path):
    exercises_list = os.listdir(training_path)

    for i in range(len(exercises_list)):
        exercises_list[i] = exercises_list[i].replace("_", " ")

    return exercises_list


# -----------------------------------------pobieranie opisu danego ćwiczenia--------------------------------------------

def loadExerciseInfo(exercise_info_path):
    exercise_info_file = open(exercise_info_path, "r", encoding='utf-8')
    exercise_info = ''
    line = exercise_info_file.readline()

    while line != '':
        exercise_info += line
        line = exercise_info_file.readline()

    return exercise_info


# ---------------------------------dodawanie treningu do listy treningów użytkownika------------------------------------

def addTrainingToUsersTrainingList(username, training_path):
    try:
        users = open("user_list.txt", "r", encoding="utf-8")
        new_users_file_content = ""

        for line in users:
            if username in line:
                if training_path in line:
                    return False
                else:
                    new_line = line.replace('\n', '\t' + training_path + '\n')
                    new_users_file_content += new_line
            else:
                new_users_file_content += line

    except IOError:
        raise IOError

    try:
        file_to_write = open("user_list.txt", "w", encoding="utf-8")
        file_to_write.write(new_users_file_content)
        file_to_write.close()

    except IOError:
        raise IOError

    return True


# ---------------------------------usuwanie treningu z listy treningów użytkownika--------------------------------------

def removeTrainingFromUsersTrainingList(username, training_path):
    try:
        users = open("user_list.txt", "r", encoding="utf-8")
        new_users_file_content = ""

        for line in users:
            if username in line:
                if training_path in line:
                    new_line = line.replace(f"\t{training_path}", '')
                    new_users_file_content += new_line
                else:
                    return False
            else:
                new_users_file_content += line

    except IOError:
        raise IOError

    try:
        file_to_write = open("user_list.txt", "w", encoding="utf-8")
        file_to_write.write(new_users_file_content)
        file_to_write.close()

    except IOError:
        raise IOError

    return True


# ------------------------------------------------Strefa testowa--------------------------------------------------------


if __name__ == "__main__":
    pass
