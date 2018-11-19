import os
from dotenv import load_dotenv

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types


load_dotenv()
TOKEN = os.getenv("EVERNOTE_DEVELOPPER_TOKEN")

def main():
    notebook = Types.Notebook()
    notebook.name = "My Sample Notebook"

    client = EvernoteClient(token=TOKEN)
    note_store = client.get_note_store()
    note_store.createNotebook(notebook)

if __name__ == "__main__":
    main()
