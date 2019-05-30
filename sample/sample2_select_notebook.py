"""
NOTE: ノートブック一覧を取得するサンプル
"""
import os

from decouple import config

from evernote.api.client import EvernoteClient


TOKEN = config("EVERNOTE_DEVELOPPER_TOKEN")
USE_SANDBOX = config("USE_SANDBOX", True, cast=bool)

def main():
    client = EvernoteClient(token=TOKEN, sandbox=USE_SANDBOX)
    note_store = client.get_note_store()
    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        print("id:{}, name:{}".format(notebook.guid, notebook.name))

if __name__ == "__main__":
    main()
