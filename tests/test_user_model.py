"""
Authorization Test Cases
"""

from catalog.model import User, Role, Permission, AnonymousUser
import unittest
from catalog import create_app, db

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('application.testing.cfg')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u1 = User(password='cat')
        u2 = User(password='cat')
        self.assertFalse(u1.password_hash == u2.password_hash)

    def test_roles_and_permissions(self):
        u = User(email='a@a.com', password='cat')
        self.assertTrue(u.can(Permission.VIEW_CATALOG))
        self.assertFalse(u.can(Permission.MODERATE_CONTENT))
        self.assertFalse(u.can(Permission.ADMINISTER))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertTrue(u.can(Permission.VIEW_CATALOG))
        self.assertFalse(u.can(Permission.MODERATE_CONTENT))
        self.assertFalse(u.can(Permission.ADMINISTER))