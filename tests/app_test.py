import pytest

from codechallenge.app import is_date_valid
from codechallenge.app import is_email_valid


# Test is_date_valid(date)
@pytest.mark.parametrize('date', [
    '26-08-1977',
    '30-09-2010',
    '30-11-1983',
    '01-01-1934',
    '01-12-1900'
])
def test_correct_date(date):
    assert is_date_valid(date) == True


@pytest.mark.parametrize('date', [
    '26-08-1899',
    '30-13-2010',
    '31-11-1983',
    '30-02-1934',
    '02/06/1979',
    '01 02 2011',
    '11122000',
    'abcdefghil',
    '',
])
def test_incorrect_date(date):
    assert is_date_valid(date) == False


# Test is_email_valid(email)
@pytest.mark.parametrize('email', [
    'larazilio@gmail.com',
    'la@kalsdkjkalsdj.de',
    'asdsdad@ssadsd.sdad.com',
    'lara.zilio@gmail.com',
])
def test_correct_email(email):
    assert is_email_valid(email) == True


@pytest.mark.parametrize('email', [
    'larazilio#gmail.com',
    'larazilio@gmail,com',
    'laraziliogmailcom',
    'lara$ilio@gmail.com',
    '12234@23232.232',
    '@sdsd.com',
    '',
])
def test_incorrect_email(email):
    assert is_email_valid(email) == False
