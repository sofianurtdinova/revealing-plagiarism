"""Database module for plagiarism detector."""

# Я перенесла модуль под src, т.к. здесь он и должен быть.
# В целом, название модуля не очень удачное, т.к. вы используете библиотеку с таким же названием - неоднозначность

from .connection import get_connection
from .db_utils import (
    create_database,
    add_synonym_pair,
    add_plagiarism_check,
    get_synonyms_for_word,
    load_synonyms_dict_from_db,
)

__all__ = [
    "get_connection",
    "create_database",
    "add_synonym_pair",
    "add_plagiarism_check",
    "get_synonyms_for_word",
    "load_synonyms_dict_from_db",
]
