from ivr_phone_tree_python import app
from flask.ext.script import Manager

manager = Manager(app)


@manager.command
def test():
    """Run the unit tests."""
    import sys, unittest
    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if not result.wasSuccessful():
            sys.exit(1)


if __name__ == "__main__":
    manager.run()
