from uuid import UUID
from faker import Faker


fake = Faker('en_US')

def get_object_name():
    return '{0}_{1}'.format(fake.word(ext_word_list=None), UUID.hex[:6])

def get_text(max_chars):
    return fake.text(max_nb_chars=max_chars, ext_word_list=None)

