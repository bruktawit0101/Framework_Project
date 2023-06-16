import pytest
from ecomstore.src.utilities.genericUtility import generate_random_email_and_password
from ecomstore.src.utilities.wooAPIUtility import WooAPIUtility
from ecomstore.src.dao.customers_dao import CustomerDao
from ecomstore.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper
import logging as logger

pytestmarks = [pytest.mark.regression, pytest.mark.besmoke, pytest.mark.customers]

@pytest.mark.customers
@pytest.mark.tcid29
@pytest.mark.qactcid4
def test_create_customer_only_email_password():

    # create payload with email and password only

    email_password = generate_random_email_and_password(email_prefix='betest')
    email = email_password['email']
    password = email_password['password']
    print(email_password)

    # make the call

    woo_helper = WooAPIUtility()

    print(woo_helper)
    payload = {
        "email": email,
        "password": password
    }

    rs_body = woo_helper.post("customers", params=payload, expected_status_code=201)


    # verify response is good

    assert rs_body, f"The response should not be empty."
    assert rs_body['id'], f"ID should be present on the response."
    assert isinstance(rs_body['id'], int), f" The id in response of create customer should be numeric"
    assert email == rs_body['email'], f"Create customer endpoint email does not match in request." \
                                      f"Expected: {email}, Actual:{rs_body['email']}"

   # verify customer is created by checking database

    customer_helper = CustomerDao()
    db_info = customer_helper.get_customer_by_email(email)
    assert len(db_info) == 1, f"Expected 1 record for customer in 'user' table. but found: {len(db_info)}"
    assert db_info[0]['user_pass'], f"After created user with api, the password field in DB is empty."

    expected_display_name = email.split('@')[0]


    assert db_info[0]['display_name'] == expected_display_name, f"Displayed name database does not match expected." \
                                                                f"Email: {email}, Expected display: {expected_display_name}" \
                                                                f"DB display name: {db_info[0]['display_name']}"
    assert db_info[0]['user_login'] == expected_display_name, f"user_login name database does not match expected." \
                                                              f"Email: {email}, Expected display: {expected_display_name}" \
                                                              f"DB user_login name: {db_info[0]['user_login']}"
@pytest.mark.customers
@pytest.mark.tcid47
@pytest.mark.qactcid5

def test_create_customer_fail_for_existing_email():


    #get randon existing user email address form DB or api
    cust_dao = CustomerDao()
    random_cust = cust_dao.get_random_customer_from_db(qty=1)
    random_email = random_cust[0]['user_email']
    logger.debug(f"Random email for the test: {random_email}")



    # make a call

    email_password = generate_random_email_and_password(email_prefix='betest')
    random_password = email_password['password']

    woo_helper = WooAPIUtility()
    payload = {
        "email": random_email,
        "password": random_password
    }
    rs_body = woo_helper.post("customers", params=payload, expected_status_code=400)


    assert rs_body['code'] == 'registration-error-email-exists', f"Create customer with existing user response does not"\
                              f" have expected text. Expected:'registration-error-email-exists', Actual: {rs_body['code']}"

    assert rs_body['data']['status'] == 400, f"Unexpected status code in body of response"\
                                             f"Expected 400 actual: {rs_body['data']['status']}"
@pytest.mark.customers
@pytest.mark.tcid32
@pytest.mark.qactcid6
def test_create_customer_fail_when_no_password_provided():
    #get random email
    random_info = generate_random_email_and_password(email_prefix='bleutc')
    email = random_info['email']
    # make customer api call without password in the payload

    payload = {"email": email}

    woo_api_utility = WooAPIUtility()

    rs_body = woo_api_utility.post(wc_endpoint='customers', params=payload, expected_status_code=400)

    expected_response = {'code': 'rest_missing_callback_param','data': {'params':['password'], 'status': 400},'message':'Missing parameter(s): password'}
    assert rs_body == expected_response, f"Got unexpected error creating user without password." \
                                         f"Expected response: {expected_response}." \
                                         f"Actual response: {rs_body}"

@pytest.mark.customers
@pytest.mark.tcid45
@pytest.mark.qactcid7

def test_create_customer_names_should_be_empty_string_if_not_proveded():
    """
    Alternate tc name:
        Verify create customer with only email and password has names as empty string
    :return:
    """

    logger.info("TEST: Verify create customer with only email and password has names as empty string")

    random_info = generate_random_email_and_password()
    email = random_info['email']
    password = random_info['password']

    # make the call

    cust_obj = CustomersAPIHelper()
    cust_api_info = cust_obj.call_create_customer(email=email, password=password)

    assert cust_api_info['first_name'] == '', f"Creating user without providing name expected to create first_name='' but it was first_name={cust_api_info['first_name']}"
    assert cust_api_info['last_name'] == '', f"Creating user without providing name expected to create last_name='' but it was first_name={cust_api_info['last_name']}"

@pytest.mark.customers
@pytest.mark.tcid46
@pytest.mark.qactcid8
def test_create_customer_with_email_and_password_and_verify_username_autogenerated_based_on_email():
    """
    Alternate tc name:
        Verify 'username' is autogenerated_based on email
    :return:
    """
    logger.info("abcdefg")

    random_info = generate_random_email_and_password()
    email = random_info['email']
    password = random_info['password']

    payload = {
        "email": email,
        "password": password
    }

    woo_api_helper = WooAPIUtility()
    rs_body = woo_api_helper.post('customers', params=payload, expected_status_code=201)
    api_username = rs_body['username']
    expected_username = email.split('@')[0]

    assert api_username == expected_username, f"Creating user with email and password should've created user name base on email." \
                                              f"Expected username:{expected_username}, Actual username:{api_username}"













