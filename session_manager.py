# TODO: Добавить поддержку работы с несколькими сессиями таймеров


class SessionManager:
    _active_session_list = {
    }

    def __init__(self, tag, commands_object):
        self._active_session_list = {tag: commands_object}

    def get_session(self, name):
        return self._active_session_list[name]


