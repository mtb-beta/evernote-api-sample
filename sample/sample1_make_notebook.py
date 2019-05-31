"""
NOTE: ノートブックを作成するサンプル
"""
from decouple import config

from pyevernote import EvernoteApp

TOKEN = config("EVERNOTE_DEVELOPPER_TOKEN")
USE_SANDBOX = config("USE_SANDBOX", True, cast=bool)


def main():
    evernote_app = EvernoteApp(token=TOKEN, use_sandbox=USE_SANDBOX)
    evernote_app.create_notebook("My Sample Notebook3")

if __name__ == "__main__":
    main()
