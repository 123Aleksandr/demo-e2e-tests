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

    def __init__(self, case_type, section):

        # common attributes
        self.title = get_object_name()
        # self.section =

        # if case_type == 'exploratory_session':

