from tkinter import *
from tkinter import messagebox
from tkvideo import tkvideo
from backend import *


# ---------------------------------------proces zamknięcia całego programu----------------------------------------------

def end():
    answer = messagebox.askyesno("Pytanie", "Czy na pewno chcesz wyjść?")

    if answer:
        quit()
    return


# ------------------------------------klasa odpowiedzialna za warstwę graficzną-----------------------------------------
class MainFrame:
    def __init__(self, parent):
        self.parent = parent
        self.is_logged = False
        self.is_users_training = False
        self.user = ''
        self.parent.geometry("1000x650")
        self.parent.minsize(width=1000, height=650)
        self.parent.maxsize(width=1000, height=650)
        self.parent.title("PyFitness")
        self.parent.configure(bg="Cyan3")

        self.frame = Frame(self.parent)
        self.frame.pack()

        self.createMainMenuFrame()

# ---------------------------------------------tworzenie ekranu startowego----------------------------------------------

    def createMainMenuFrame(self):
        self.parent.title("PyFitness")
        self.frame.forget()
        self.frame = Frame(self.parent, bg="Cyan3")
        self.frame.pack()

        title = Label(self.frame, text="PyFitness", font=("Helvetica", 80), bg="Cyan3", bd=40)

        login_button = Button(self.frame, text="Zaloguj", font=("Helvetica", 24), width=15, bd=10, bg="CadetBlue2",
                              relief="groove", activebackground="blue", command=self.createLoginFrame)

        register_button = Button(self.frame, text="Załóż konto", font=("Helvetica", 24), width=15, bd=10,
                                 bg="CadetBlue2", relief="groove", activebackground="blue",
                                 command=self.createRegisterFrame)

        browse_button = Button(self.frame, text="Przeglądaj treningi", font=("Helvetica", 24), width=15, bd=10,
                               bg="CadetBlue2", relief="groove", activebackground="blue",
                               command=self.createTrainingsBrowseFrame)

        exit_button = Button(self.frame, text="Zakończ", fg="DarkBlue", font=("Helvetica", 24), width=15, bd=10,
                             bg="CadetBlue2", relief="groove", activebackground="red", command=end)

        title.grid(column=0, row=0, pady=10)
        login_button.grid(column=0, row=1, pady=10)
        register_button.grid(column=0, row=2, pady=10)
        browse_button.grid(column=0, row=3, pady=10)
        exit_button.grid(column=0, row=4, pady=10)

# ------------------------------------------tworzenie ekranu logowania--------------------------------------------------

    def createLoginFrame(self):
        self.frame.forget()
        self.parent.title("Podaj login i hasło użytkownika")
        self.frame = Frame(self.parent, bg="Cyan3")
        self.frame.pack()

        username_label = Label(self.frame, text="Nazwa użytkownika:", font=("Helvetica", 38), bg="Cyan3", bd=20)
        username_entry = Entry(self.frame, width=20, font=("Helvetica", 20), bg="CadetBlue1", bd=5)
        password_label = Label(self.frame, text="Hasło:", font=("Helvetica", 38), bg="Cyan3")
        password_entry = Entry(self.frame, width=20, font=("Helvetica", 20), bg="CadetBlue1", bd=5)

        login_button = Button(self.frame, text="Zaloguj", font=("Helvetica", 20), width=14, bd=10, bg="CadetBlue2",
                              relief="groove", activebackground="blue",
                              command=lambda: self.tryLog(username_entry.get(), password_entry.get()))

        exit_button = Button(self.frame, text="Powrót", fg="DarkBlue", font=("Helvetica", 20), width=14, bd=10,
                             bg="CadetBlue2", relief="groove", activebackground="red", command=self.createMainMenuFrame)

        username_label.grid(column=0, row=0)
        username_entry.grid(column=0, row=1, pady=20)
        password_label.grid(column=0, row=2, pady=20)
        password_entry.grid(column=0, row=3)
        login_button.grid(column=0, row=4, pady=50)
        exit_button.grid(column=0, row=5)

# ----------------------------------------tworzenie ekranu błędu logowania----------------------------------------------

    def createLoginErrorFrame(self):
        self.frame.forget()
        self.parent.title("Podaj login i hasło użytkownika")
        self.frame = Frame(self.parent, bg="Cyan3")
        self.frame.pack()

        login_error_mg = Label(self.frame, text="Nieprawidłowy login lub hasło", font=("Helvetica", 24), bg="Cyan3",
                               bd=40)
        username_label = Label(self.frame, text="Nazwa użytkownika:", font=("Helvetica", 20), bg="Cyan3", bd=20)
        username_entry = Entry(self.frame, width=20, font=("Helvetica", 18), bg="CadetBlue1", bd=5)
        password_label = Label(self.frame, text="Hasło:", font=("Helvetica", 20), bg="Cyan3")
        password_entry = Entry(self.frame, width=20, font=("Helvetica", 18), bg="CadetBlue1", bd=5)
        register_label = Label(self.frame, text="Jesteś tu pierwszy raz?", font=("Helvetica", 24), bg="Cyan3", bd=40)

        login_button = Button(self.frame, text="Zaloguj", font=("Helvetica", 20), width=14, bd=10, bg="CadetBlue2",
                              relief="groove", activebackground="blue",
                              command=lambda: self.tryLog(username_entry.get(), password_entry.get()))

        register_button = Button(self.frame, text="Załóż konto", font=("Helvetica", 24), width=15, bd=10,
                                 bg="CadetBlue2", relief="groove", activebackground="blue",
                                 command=self.createRegisterFrame)

        exit_button = Button(self.frame, text="Powrót", fg="DarkBlue", font=("Helvetica", 20), width=14, bd=10,
                             bg="CadetBlue2", relief="groove", activebackground="red", command=self.createMainMenuFrame)

        login_error_mg.grid(column=0, row=0, pady=10)
        username_label.grid(column=0, row=1)
        username_entry.grid(column=0, row=2)
        password_label.grid(column=0, row=3)
        password_entry.grid(column=0, row=4)
        login_button.grid(column=0, row=5, pady=100)
        register_label.grid(column=1, row=0)
        register_button.grid(column=1, row=2, rowspan=3)
        exit_button.grid(column=1, row=5, pady=10)

# --------------------------------------------proces logowania użytkownika----------------------------------------------

    def tryLog(self, username, password):
        is_logged = logUser(username, password)

        if is_logged:
            self.is_logged = True
            self.user = username
            self.createUserMenuFrame(username)

        else:
            self.createLoginErrorFrame()

# ----------------------------------------------tworzenie ekranu rejestracji--------------------------------------------

    def createRegisterFrame(self):
        self.frame.forget()
        self.parent.title("Rejestracja użytkownika")
        self.frame = Frame(self.parent, bg="Cyan3")
        self.frame.pack()

        register_mg = Label(self.frame,
                            text="Wybierz nazwę użytkownika oraz hasło.\nHasło musi zawierać więcej niż 5 znaków.",
                            font=("Helvetica", 32), bg="Cyan3", bd=20)

        username_label = Label(self.frame, text="Nazwa użytkownika:", font=("Helvetica", 28), bg="Cyan3", bd=20)
        username_entry = Entry(self.frame, width=20, font=("Helvetica", 20), bg="CadetBlue1", bd=5)
        password_label = Label(self.frame, text="Hasło:", font=("Helvetica", 28), bg="Cyan3")
        password_entry = Entry(self.frame, width=20, font=("Helvetica", 20), bg="CadetBlue1", bd=5)

        register_button = Button(self.frame, text="Załóż konto", font=("Helvetica", 20), width=14, bd=10,
                                 bg="CadetBlue2", relief="groove", activebackground="blue",
                                 command=lambda: self.tryRegister(username_entry.get(), password_entry.get()))

        exit_button = Button(self.frame, text="Powrót", fg="DarkBlue", font=("Helvetica", 20), width=14, bd=10,
                             bg="CadetBlue2", relief="groove", activebackground="red", command=self.createMainMenuFrame)

        register_mg.grid(column=0, row=0)
        username_label.grid(column=0, row=1)
        username_entry.grid(column=0, row=2)
        password_label.grid(column=0, row=3, pady=10)
        password_entry.grid(column=0, row=4)
        register_button.grid(column=0, row=5, pady=20)
        exit_button.grid(column=0, row=6, pady=30)

# ------------------------------------------proces rejestracji użytkownika----------------------------------------------

    def tryRegister(self, username, password):
        is_registered = registerUser(username, password)

        if is_registered == 1:
            messagebox.showerror("Błąd podczas tworzenia użytkownika",
                                 "Uzytkownik o podanym loginie istnieje w systemie.\nWybierz inną nazwę użytkownika.")

        if is_registered == 2:
            messagebox.showerror("Błąd podczas tworzenia użytkownika",
                                 "Hasło nie spełnia warunku:\nHasło musi składać się z więcej niż 5 znaków.")

        if is_registered == 0:
            self.createMainMenuFrame()
            messagebox.showinfo("Pomyslnie utworzono konto użytkownika", "Możesz zalogować się na swoje konto i cieszyć"
                                " się korzystaniem ze wszytskich funkcji aplikacji.\nCzas zacząć treningi.")

# ----------------------------------------------tworzenie ekranu użytkownika--------------------------------------------

    def createUserMenuFrame(self, username):
        self.is_users_training = False
        self.frame.forget()
        self.parent.title(f"Menu użytkownika {username}")
        self.frame = Frame(self.parent, bg="Cyan3")
        self.frame.pack()

        user_label = Label(self.frame, text=f"Witaj {username}", font=("Helvetica", 50), bg="Cyan3", bd=40)

        browse_trainings_button = Button(self.frame, text="Dostępne treningi", font=("Helvetica", 24), width=15, bd=10,
                                         bg="CadetBlue2", relief="groove", activebackground="blue",
                                         command=self.createTrainingsBrowseFrame)

        browse_user_trainings_button = Button(self.frame, text="Zapisane treningi", font=("Helvetica", 24), width=15,
                                              bd=10, bg="CadetBlue2", relief="groove", activebackground="blue",
                                              command=lambda: self.createUserTrainingsBrowseFrame(username))

        logout_button = Button(self.frame, text="Wyloguj", fg="DarkBlue", font=("Helvetica", 24), width=15, bd=10,
                               bg="CadetBlue2", relief="groove", activebackground="red", command=self.logoutUser)

        user_label.grid(column=0, row=0, pady=10)
        browse_trainings_button.grid(column=0, row=1, pady=30)
        browse_user_trainings_button.grid(column=0, row=2, pady=30)
        logout_button.grid(column=0, row=3, pady=30)

# ------------------------------------tworzenie ekranu z listą dostępnych treningów-------------------------------------

    def createTrainingsBrowseFrame(self):
        self.parent.title("Lista dostępnych treningów")
        self.frame.forget()
        self.frame = Frame(self.parent, bg="Cyan3")
        self.frame.pack()

        label_frame = LabelFrame(self.frame)
        training_list_label = Label(self.frame, text="Dostępne treningi", font=("Helvetica", 40), bg="Cyan3", bd=20)

        exit_button = Button(self.frame, text="Powrót", fg="DarkBlue", font=("Helvetica", 16), width=10, bd=10,
                            bg="CadetBlue2", relief="groove", activebackground="red", command=self.redirectToProperMenu)

        my_canvas = Canvas(label_frame, height=350, width=550, bg="Cyan3")
        scrollbar = Scrollbar(label_frame, orient=VERTICAL, command=my_canvas.yview)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        button_frame = Frame(my_canvas, bg="Cyan3")
        my_canvas.create_window((285, 50), window=button_frame, anchor="center")

        training_list_label.grid(column=0, row=0, rowspan=2, pady=10)
        label_frame.grid(column=0, row=2)
        exit_button.grid(column=0, row=3, pady=30)

        trainings_list = createTrainingsList()

        button_dict = {}

        for training in trainings_list:
            def func(x=training):
                return self.createExercisesListFrame(x)

            button_dict[training] = Button(button_frame, text=f"{training}", font=("Helvetica", 16), width=20, bd=10,
                                           bg="CadetBlue2", relief="groove", activebackground="blue", command=func)
            button_dict[training].grid(pady=10)

        my_canvas.update_idletasks()
        my_canvas.yview_moveto(0)

# ------------------------------tworzenie ekranu z listą zapisanych treningów użytkownika-------------------------------

    def createUserTrainingsBrowseFrame(self, username):
        self.is_users_training = True
        self.parent.title(f"Lista zapisanych treningów {username}")
        self.frame.forget()
        self.frame = Frame(self.parent, bg="Cyan3")
        self.frame.pack()

        users_trainings_list = createUsersTrainingsList(username)

        if len(users_trainings_list) == 0:
            info_label = Label(self.frame, text="Brak zapisanych treningów", font=("Helvetica", 40), bg="Cyan3", bd=20)

            exit_button = Button(self.frame, text="Powrót", fg="DarkBlue", font=("Helvetica", 16), width=10, bd=10,
                             bg="CadetBlue2", relief="groove", activebackground="red",
                                 command=self.redirectToProperMenu)

            info_label.grid(column=0, row=0, pady=150)
            exit_button.grid(column=0, row=1)

        else:
            label_frame = LabelFrame(self.frame)
            training_list_label = Label(self.frame, text=f"{username} - zapisane treningi", font=("Helvetica", 40),
                                        bg="Cyan3", bd=20)

            exit_button = Button(self.frame, text="Powrót", fg="DarkBlue", font=("Helvetica", 16), width=10, bd=10,
                             bg="CadetBlue2", relief="groove", activebackground="red",
                                 command=self.redirectToProperMenu)

            my_canvas = Canvas(label_frame, height=350, width=550, bg="Cyan3")
            scrollbar = Scrollbar(label_frame, orient=VERTICAL, command=my_canvas.yview)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            scrollbar.pack(side=RIGHT, fill=Y)
            my_canvas.configure(yscrollcommand=scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

            button_frame = Frame(my_canvas, bg="Cyan3")
            my_canvas.create_window((285, 50), window=button_frame, anchor="center")

            training_list_label.grid(column=0, row=0, rowspan=2, pady=20)
            label_frame.grid(column=0, row=2)
            exit_button.grid(column=0, row=3, pady=30)

            button_dict = {}

            for training in users_trainings_list:
                def func(x=training):
                    return self.createExercisesListFrame(x)

                button_dict[training] = Button(button_frame, text=f"{training}",font=("Helvetica", 16), width=20, bd=10,
                                           bg="CadetBlue2", relief="groove", activebackground="blue", command=func)
                button_dict[training].grid(pady=10)

            my_canvas.update_idletasks()
            my_canvas.yview_moveto(0)

# --------------------------------tworzenie ekranu z listą ćwiczeń danego treningu--------------------------------------

    def createExercisesListFrame(self, training):
        self.parent.title(f"Zestaw ćwiczeń w {training}")
        self.frame.forget()
        self.frame = Frame(self.parent, bg="Cyan3")
        self.frame.pack()

        label_frame = LabelFrame(self.frame)

        training_list_label = Label(self.frame, text=f"Zestaw ćwiczeń w {training}", font=("Helvetica", 32), bg="Cyan3",
                                    bd=20)

        exit_button = Button(self.frame, text="Powrót", fg="DarkBlue", font=("Helvetica", 16), width=15, bd=10,
                             bg="CadetBlue2", relief="groove", activebackground="red",
                             command=self.redirectToProperTrainingBrowser)

        if self.is_logged and not self.is_users_training:
            save_button = Button(self.frame, text="Zapisz trening", font=("Helvetica", 16), width=15, bd=10,
                                 bg="CadetBlue2", relief="groove", activebackground="blue",
                                 command=lambda: self.saveTraining(training_path))
            save_button.grid(column=0, row=3, pady=10)

        if self.is_users_training:
            delete_button = Button(self.frame, text="Usuń trening", font=("Helvetica", 16), width=15, bd=10,
                                 bg="CadetBlue2", relief="groove", activebackground="blue",
                                   command=lambda: self.deleteTraining(training_path))
            delete_button.grid(column=0, row=3, pady=10)

        my_canvas = Canvas(label_frame, height=300, width=500, bg="Cyan3")
        scrollbar = Scrollbar(label_frame, orient=VERTICAL, command=my_canvas.yview)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        button_frame = Frame(my_canvas, bg="Cyan3")
        my_canvas.create_window((260, 50), window=button_frame, anchor="center")

        training_list_label.grid(column=0, row=0, rowspan=2, pady=10)
        label_frame.grid(column=0, row=2)
        exit_button.grid(column=0, row=4, pady=30)

        training_path = "Lista_treningów\\" + training.replace(" ", "_")
        exercise_list = createExercisesList(training_path)

        button_dict = {}

        for exercise in exercise_list:
            def func(x=exercise):
                return self.createExerciseInfoFrame(x, training)

            button_dict[exercise] = Button(button_frame, text=f"{exercise}", font=("Helvetica", 14), width=40, bd=10,
                                           bg="CadetBlue2", relief="groove", activebackground="blue", command=func)
            button_dict[exercise].grid(pady=10)

        my_canvas.update_idletasks()
        my_canvas.yview_moveto(0)

# ----------------------tworzenie ekranu zawierającego informację o danym ćwiczeniu-------------------------------------

    def createExerciseInfoFrame(self, exercise, training):
        self.parent.title(f"{exercise} - szczegóły")
        self.frame.forget()
        self.frame = Frame(self.parent, bg="Cyan3")
        self.frame.pack()

        exercise_name = exercise.replace(" ", "_")
        exercise_video_path = f"Lista_ćwiczeń\\{exercise_name}\\{exercise_name}.mp4"
        exercise_info_path = f"Lista_ćwiczeń\\{exercise_name}\\{exercise_name}.txt"

        label_frame = LabelFrame(self.frame)
        exercise_name_label = Label(self.frame, text=f"{exercise}", font=("Helvetica", 30), bg="Cyan3", bd=20)

        exit_button = Button(self.frame, text="Powrót", fg="DarkBlue", font=("Helvetica", 18), width=20, bd=10,
                             bg="CadetBlue2", relief="groove", activebackground="red",
                             command=lambda: self.createExercisesListFrame(training))

        video_button = Button(self.frame, text="Wideo instruktarzowe", font=("Helvetica", 18), width=20, bd=10,
                              bg="CadetBlue2", relief="groove", activebackground="blue",
                              command=lambda: self.playExerciseVideo(exercise_video_path, exercise, training))

        my_canvas = Canvas(label_frame, width=700, height=300, bg="Cyan3")
        scrollbar = Scrollbar(label_frame, orient=VERTICAL, command=my_canvas.yview)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        exercise_name_label.grid(column=0, row=0, rowspan=2)
        label_frame.grid(column=0, row=2, pady=40)
        video_button.grid(column=0, row=3)
        exit_button.grid(column=0, row=4, pady=30)

        exercise_info = loadExerciseInfo(exercise_info_path)
        my_canvas.create_text(300, 100, text=exercise_info)

        my_canvas.update_idletasks()
        my_canvas.yview_moveto(0)

    # ---------------------tworzenie ekranu z filmem przedstawiającym sposób wykonywania ćwiczenia----------------------

    def playExerciseVideo(self, exercise_video_path, exercise_name, training_name):
        self.frame.forget()
        self.parent.title(f"{exercise_name} - wideo instruktarzowe")
        self.frame = Frame(self.parent, bg="Cyan3")
        self.frame.pack()

        play_button = Button(self.frame, text="Odtwórz ponownie", font=("Helvetica", 10), width=20, bg="CadetBlue2",
                             relief="groove", activebackground="blue",
                             command=lambda: self.playExerciseVideo(exercise_video_path, exercise_name, training_name))

        exit_button = Button(self.frame, text="Zamknij wideo", fg="DarkBlue", font=("Helvetica", 10), width=20,
                             bg="CadetBlue2", relief="groove", activebackground="red",
                             command=lambda: self.createExerciseInfoFrame(exercise_name, training_name))

        video_label = Label(self.frame)

        video_label.grid(columnspan=2, row=0)
        play_button.grid(column=0, row=1, pady=10)
        exit_button.grid(column=1, row=1, pady=10)

        player = tkvideo(exercise_video_path, video_label, loop=0, size=(1000, 600))
        player.play()

# -------------------------------zapisywanie treningu do listy treningów użytkownika------------------------------------

    def saveTraining(self, training_path):
        is_saved = addTrainingToUsersTrainingList(self.user, training_path)

        if is_saved:
            messagebox.showinfo("Informacja", "Pomyślnie zapisano trening na liście użytkownika")
            self.createTrainingsBrowseFrame()
        else:
            messagebox.showerror("Błąd", "Nie udało się dodać treningu do listy użytkownika.\n"
                                         "Trening znajduje się już na liście.")

    # -------------------------------usuwanie treningu z listy treningów użytkownika------------------------------------

    def deleteTraining(self, training_path):
        is_deleted = removeTrainingFromUsersTrainingList(self.user, training_path)

        if is_deleted:
            messagebox.showinfo("Informacja", "Pomyślnie usunięto trening z listy użytkownika")
            self.redirectToProperTrainingBrowser()
        else:
            messagebox.showerror("Błąd", "Usuwanie nie powiodło się.\n"
                                         "Trening nie znajduje się na liście treningów użytkownika.")

# ------przenoszenie użytkownika do odpowiedniego menu z poziomu przeglądania listy dostępnych treningów----------------
# -------------------------(menu ogólne - niezalogowany, menu użytkownika - zalogowany)---------------------------------

    def redirectToProperMenu(self):
        if self.is_logged:
            self.createUserMenuFrame(self.user)

        else:
            self.createMainMenuFrame()

# -----przenoszenie użytkownika do odpowiedniej listy treningów z poziomu przeglądania listy ćwiczeń danego treningu----
# -------------------(zapisane treningi - uzytkownik przeglądał wcześniej zapisane treningi)----------------------------
# -------------------(dostepne treningi - użytkownik przeglądał wcześniej dostępne treningi)----------------------------

    def redirectToProperTrainingBrowser(self):
        if self.is_users_training:
            self.createUserTrainingsBrowseFrame(self.user)

        else:
            self.createTrainingsBrowseFrame()

# ---------------------------------------proces wylogowania użytkownika-------------------------------------------------

    def logoutUser(self):
        answer = messagebox.askyesno("Pytanie", "Czy na pewno chcesz się wylogować?")

        if answer:
            self.is_logged = False
            self.user = ''
            self.is_users_training = False
            self.createMainMenuFrame()
            messagebox.showinfo("Wylogowano", "Poprawnie wylogowano użytkownika.")
