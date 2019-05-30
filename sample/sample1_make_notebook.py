"""
NOTE: ノートブックを作成するサンプル
"""
import os

from decouple import config

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types


TOKEN = config("EVERNOTE_DEVELOPPER_TOKEN")
USE_SANDBOX = config("USE_SANDBOX", True, cast=bool)


def main():
    notebook = Types.Notebook()
    notebook.name = "My Sample Notebook"

    client = EvernoteClient(token=TOKEN, sandbox=USE_SANDBOX)
    note_store = client.get_note_store()
    note_store.createNotebook(notebook)

if __name__ == "__main__":
    main()
