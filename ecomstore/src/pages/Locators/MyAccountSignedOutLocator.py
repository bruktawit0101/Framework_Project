from selenium.webdriver.common.by import By



class MyAccountSignedOutLocators:

      USERNAME_FIELD = (By.ID, 'username')
      PASSWORD_FIELD = (By.ID, 'password')
      LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login"]')
      REGISTER_EMAIL = (By.ID, 'reg_email')
      REGISTER_PASSWORD = (By.ID, 'reg_password')
      REGISTER_BTN = (By.CSS_SELECTOR, 'button.woocommerce-form-register__submit')
