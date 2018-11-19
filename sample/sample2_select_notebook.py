import os
from dotenv import load_dotenv

from evernote.api.client import EvernoteClient


load_dotenv()
TOKEN = os.getenv("EVERNOTE_DEVELOPPER_TOKEN")

def main():
    client = EvernoteClient(token=TOKEN)
    note_store = client.get_note_store()
    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        print("id:{}, name:{}".format(notebook.guid, notebook.name))

if __name__ == "__main__":
    main()
