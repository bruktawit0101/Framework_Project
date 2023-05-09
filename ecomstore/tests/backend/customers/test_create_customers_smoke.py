import pytest
from ecomstore.src.utilities.genericUtility import generate_random_email_and_password
from ecomstore.src.utilities.wooAPIUtility import WooAPIUtility
from ecomstore.src.dao.customers_dao import CustomerDao

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
    breakpoint()

    assert db_info[0]['display_name'] == expected_display_name, f"Displayed name database does not match expected." \
                                                                f"Email: {email}, Expected display: {expected_display_name}" \
                                                                f"DB display name: {db_info[0]['display_name']}"
    assert db_info[0]['user_login'] == expected_display_name, f"user_login name database does not match expected." \
                                                                f"Email: {email}, Expected display: {expected_display_name}" \
                                                    f"DB user_login name: {db_info[0]['user_login']}"



