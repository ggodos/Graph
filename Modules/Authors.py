
"""Модуль с информацией о разработчиках программы."""



from textwrap import dedent


def getAuthors():
    """Возвращает строку с информацией об авторах.

    Returns:
        string: Строка с авторами.
    """
    return dedent(
        """
            Проект летней практики
            ВШ ЭКН ЮУрГУ 2021
            Авторы:
            Беляков Максим (ggodos) - Тимлид
            Гордеев Александр (MrSago) - Архитектор
            Рогов Дмитрий (kqant) - Back-end разработчик
            Баландин Захар (smaylninja) - Front-end разработчик
            Синельникова Илона (mouseLOL101) - Front-end разработчик
        """
    )

