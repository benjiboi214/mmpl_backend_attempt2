from django.conf import settings
from django.test import TransactionTestCase
from django_test_migrations.migrator import Migrator


class TestSitesMigrations(TransactionTestCase):

    def test_default_superuser_created(self):
        migrator = Migrator(database='default')
        migrator.before(('users', None))

        auth_user_model = settings.AUTH_USER_MODEL.split('.')

        new_state = migrator.after(('users', '0001_initial'))
        User = new_state.apps.get_model(auth_user_model[0], auth_user_model[1])
        user = User.objects.all()

        self.assertEqual(user[0].username, settings.DJANGO_SU_NAME)
        self.assertEqual(user[0].email, settings.DJANGO_SU_EMAIL)

        migrator.reset()

    def test_default_superuser_rollback(self):
        migrator = Migrator(database='default')
        migrator.after(('users', '0001_initial'))

        auth_user_model = settings.AUTH_USER_MODEL.split('.')

        new_state = migrator.before(('users', None))
        User = new_state.apps.get_model(auth_user_model[0], auth_user_model[1])
        user = User.objects.all()

        self.assertEqual(len(user), 0)

        migrator.reset()
