from datetime import datetime


class TimeEvent(object):
    """Дефолтный класс содержащий информацию об событии учет времени которого ведется"""
    name_of_event = None
    start_time = None
    end_time = None
    elapsed_time = None
    is_pause_active = False

    def start_timer(self, name):
        if self.is_pause_active:
            self.is_pause_active = False
        else:
            self.name_of_event = name
        self.start_time = datetime.now()

    def stop_time(self):
        if self.is_pause_active:
            return self.elapsed_time
        else:
            self.end_time = datetime.now()
            if not self.elapsed_time:
                self.elapsed_time = self.end_time - self.start_time
            else:
                self.elapsed_time = self.end_time - self.start_time
            return self.elapsed_time

    def pause_trigger(self):
        if not self.is_pause_active:
            self.is_pause_active = True
            self.end_time = datetime.now()
            if not self.elapsed_time:
                self.elapsed_time = self.end_time - self.start_time
            else:

                self.elapsed_time += self.end_time - self.start_time

    def info(self):
        if self.name_of_event:
            now = datetime.now()
            print(f"Вы занимаетесь задачей '{self.name_of_event}' уже {datetime.now() - self.start_time}")
        else:
            print("Нет активной задачи")

    @staticmethod
    def strfdelta(tdelta, fmt):
        d = {"days": tdelta.days}
        d["hours"], rem = divmod(tdelta.seconds, 3600)
        d["minutes"], d["seconds"] = divmod(rem, 60)
        return fmt.format(**d)