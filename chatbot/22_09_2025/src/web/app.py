import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web.streamlit_app import ChatBotApp


if __name__ == "__main__":
    app = ChatBotApp()
    app.run()
