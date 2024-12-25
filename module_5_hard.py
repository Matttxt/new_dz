import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self, nickname, password):
        hashed_password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)
        return
    def log_out(self):
        self.current_user = None
    def add(self, *videos):
        for video in videos:
            already_exists = False
            for v in self.videos:
                if video.title == v.title:
                    already_exists = True
                    break
            if not already_exists:
                self.videos.append(video)
    def get_videos(self, search_word):
        res = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                res.append(video.title)
        return res
    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        else:
            for video in self.videos:
                if video.title == title:
                    if video.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=" ")
                        time.sleep(1)
                    print("Конец видео")
                    video.time_now = 0
                    return
            print("Видео не найдено")
ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user.nickname)

ur.watch_video('Лучший язык программирования 2024 года!')


