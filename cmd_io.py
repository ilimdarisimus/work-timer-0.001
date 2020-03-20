import sys
import timer
import session_manager


class Commands(object):
    name_current_session = ""
    id_current_session = None
    exit_code = False
    last_command_argument = None

    def stop(self, arg=None):
        try:
            elapsed = self.id_current_session.stop_time()
            print(f"Отлично поработал, ты занимался '{self.name_current_session}' аж целых {elapsed}!")
        except AttributeError:
            print("Нет ни одной активной ссесии, напиши start чтобы начать сессию")

    def start(self):
        # FIXME: Вот эта хуйня блядь придуманна укропами, после того как ставишь сессию на паузу, и прописываешь start
        # оно начинает новый отсчет, вместо того чтобы продолжть существующий. сейчас мне лень.

        if not self.id_current_session:
            if self.last_command_argument:
                self.name_current_session = self.last_command_argument
            else:
                self.name_current_session = input("Введите тег таймера:")
            self.id_current_session = timer.TimeEvent()
            self.id_current_session.start_timer(self.name_current_session)
            print(f"Сессия '{self.name_current_session}' запущена")
        else:
            self.id_current_session.start_timer(self.name_current_session)
            print(f"Cеcсия '{self.id_current_session.name_of_event}' cнята с паузы!")

    def pause(self, arg=None):
        self.id_current_session.pause_trigger()
        print(f"Сессия '{self.name_current_session}' поставлена на паузу.")

    @staticmethod
    def exit():
        sys.exit()

    def info(self):
        if self.id_current_session:
            self.id_current_session.info()
        else:
            print("Нет активной сессии ")

    commands = {
        "stop": stop,
        "start": start,
        "pause": pause,
        "exit": exit,
        "info": info
    }


# TODO: Добавить поддержку работы с несколькими сессиями таймеров
first_object = Commands()
while not first_object.exit_code:
    command = input("Введите комманду:")
    try:
        first_object.last_command_argument = command.split(" ")[1]
        command = command.split(" ")[0]
    except IndexError:
        pass
    except ValueError:
        print("Слишком большое количество аргументов")
    try:
        Commands.commands[command](first_object)
    except KeyError:
        print("Команда не найдена")


