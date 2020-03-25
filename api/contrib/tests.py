from django.conf import settings
from django.test import TransactionTestCase
from django_test_migrations.migrator import Migrator


class TestSitesMigrations(TransactionTestCase):

    def test_default_site_updated(self):
        migrator = Migrator(database='default')
        migrator.before(('sites', '0002_alter_domain_unique'))
        
        new_state = migrator.after(('sites', '0003_set_site_domain_and_name'))
        Site = new_state.apps.get_model('sites', 'Site')
        site = Site.objects.get(id=settings.SITE_ID)

        self.assertEqual(site.domain, "staging.mmpl.systemiphus.com/")
        self.assertEqual(site.name, "mmpl_backend")

        migrator.reset()

    def test_default_site_rollback(self):
        migrator = Migrator(database='default')
        migrator.before(('sites', '0003_set_site_domain_and_name'))
        
        new_state = migrator.after(('sites', '0002_alter_domain_unique'))
        Site = new_state.apps.get_model('sites', 'Site')
        site = Site.objects.get(id=settings.SITE_ID)

        self.assertEqual(site.domain, "example.com")
        self.assertEqual(site.name, "example.com")

        migrator.reset()