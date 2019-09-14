import pytest
from finder import comment_sign
from exceptions.exceptions import *


def test_ext_to_comment_sign_when_sign_is_in_dict_in_tuple():
    sign = comment_sign.ext_to_comment_sign('.c')
    assert sign == '//'


def test_ext_to_comment_sign_when_sign_is_in_dict_as_str():
    sign = comment_sign.ext_to_comment_sign('.m')
    assert sign == '%'


def test_ext_to_comment_sign_when_sign_not_in_dict():
    with pytest.raises(CommentSignNotFound):
        sign = comment_sign.ext_to_comment_sign('.qqq')
