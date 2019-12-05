from utils import *


class Project(object):

    def __init__(self, show_announcement=True, view='suite_mode_single'):

        self.name = get_object_name()
        self.announcement = get_text(max_chars=160)
        self.show_announcement = show_announcement
        self.view = view


class TestCases(object):
    pass


class Subsection(object):
    pass


class Case(object):

    def __init__(self, case_type='text_test_case'):

        self.title = get_object_name()
        if case_type == 'text_test_case':
            self.preconditions = get_text(max_chars=100)
            self.steps = get_text(max_chars=150)
            self.result = get_text(max_chars=100)
        elif case_type == 'step_test_case':
            pass
        elif case_type == 'session_test_case':
            pass
        else:
            raise ValueError('Указаанного типа кейсов не существует!')

