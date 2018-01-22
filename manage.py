from flask_script import Server, Manager

from app import app

manager = Manager(app)
manager.add_command('runserver', Server(port=9854))

if __name__ == '__main__':
    manager.run()
