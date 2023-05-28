from typing import Type, Union

from django.db import connection


def get_text_notes(slug: str) -> Union[Type[Exception], str]:
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"""
        SELECT
            text
        FROM api_notes
        WHERE slug = '{slug}';
        """
        )
        text = cursor.fetchall()
    except BaseException:
        return Exception
    finally:
        if cursor is not None:
            cursor.close()
    return text


def get_folders() -> Union[Type[Exception], str]:
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"""
        SELECT
            name
        FROM api_folder;
        """
        )
        text = cursor.fetchall()
    except BaseException:
        return Exception
    finally:
        if cursor is not None:
            cursor.close()
    return text


def get_notes_in_folder(name: str) -> Union[Type[Exception], str]:
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"""
        SELECT
            name,
            slug
        FROM api_folder
        LEFT JOIN api_notes_folders anf on api_folder.id = anf.folder_id
        LEFT JOIN api_notes an on an.id = anf.notes_id
        WHERE name = '{name}'
        ORDER BY name;
        """
        )
        text = cursor.fetchall()
    except BaseException:
        return Exception
    finally:
        if cursor is not None:
            cursor.close()
    return text


def get_notes_user(id_user: int) -> Union[Type[Exception], str]:
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"""
        SELECT
            id,
            slug
        FROM api_notes
        WHERE author_id = '{id_user}'
        """
        )
        text = cursor.fetchall()
    except BaseException:
        return Exception
    finally:
        if cursor is not None:
            cursor.close()
    return text
