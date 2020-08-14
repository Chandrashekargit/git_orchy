from Settings.test_domains.create_domain import create_domain
from Settings.test_users.create_users import *
from Settings.test_domains.delete_domain import *
from Settings.test_users.delete_user import *
from Settings.test_teams.create_team import *
from Settings.test_users.create_users import *
from Settings.test_teams.delete_team import *
from pytest import mark


@mark.test_user
def test_create_user(driver):
    create_user(driver, fn="q"*31, ln="q"*31, email_id="qqqqqqqqqqqqqqqqqqq@xyz.com", un="q"*31, privilage="Admin")
