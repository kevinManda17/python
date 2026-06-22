"""
Programme principal
"""

import controllers.home as home_controller

def app():
    home_controller.index()


if __name__ == '__main__':
    app()