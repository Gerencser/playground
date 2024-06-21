from pgoutput import output_by_lang
import pytest

def test_list_supported_languages():
    list_of_languages = output_by_lang.list_lang()
    assert("hu" in list_of_languages)


