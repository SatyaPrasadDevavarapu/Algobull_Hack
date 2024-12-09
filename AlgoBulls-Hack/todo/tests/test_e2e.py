from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException


class TodoE2ETestCase(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://127.0.0.1:8000/admin/login/")

        # Log in to the admin site
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        username_field.send_keys("shimer")  # Replace with your username
        password_field.send_keys("qwerty56565")  # Replace with your password
        password_field.send_keys(Keys.RETURN)

        # Wait for the login to complete
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "site-name"))
        )

    def tearDown(self):
        self.driver.quit()

    # def test_view_todos(self):
    #     # Navigate to the todos page
    #     self.driver.get("http://127.0.0.1:8000/admin/todo/todo/")

    #     # Increase the timeout and use visibility_of_element_located
    #     WebDriverWait(self.driver, 20).until(
    #         EC.visibility_of_element_located(
    #             (By.XPATH, "//*[contains(text(), 'Test Todo')]")
    #         )
    #     )

    #     # Verify if 'Test Todo' is in the page source
    #     self.assertIn("Test Todo", self.driver.page_source)

    def test_create_todo(self):
        # Navigate to the "Add Todo" page
        self.driver.get("http://127.0.0.1:8000/admin/todo/todo/add/")

        # Create a new todo
        self.driver.find_element(By.NAME, "title").send_keys("New Todo")
        self.driver.find_element(By.NAME, "description").send_keys(
            "This is a new test todo."
        )
        self.driver.find_element(By.XPATH, "//input[@value='Save']").click()

        # Wait for the new todo to appear on the page
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'New Todo')]")
            )
        )

        # Check if the new todo is displayed
        self.assertIn("New Todo", self.driver.page_source)

    def test_edit_todo(self):
        # Navigate to an existing todo's edit page
        self.driver.get("http://127.0.0.1:8000/admin/todo/todo/1/change/")

        # Edit the title of the todo
        title_field = self.driver.find_element(By.NAME, "title")
        title_field.clear()
        title_field.send_keys("Edited Todo")

        # Save the changes
        self.driver.find_element(By.XPATH, "//input[@value='Save']").click()

        # Wait for the edited todo to appear on the page
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Edited Todo')]")
            )
        )

        # Check if the edited todo is displayed
        self.assertIn("Edited Todo", self.driver.page_source)

    # def test_delete_todo(self):
    #     # Navigate to the todo list
    #     self.driver.get("http://127.0.0.1:8000/admin/todo/todo/")

    #     # Wait for the 'Test Todo' element to be visible
    #     WebDriverWait(self.driver, 20).until(
    #         EC.visibility_of_element_located(
    #             (By.XPATH, "//tr[contains(., 'Test Todo')]")
    #         )
    #     )

    #     # Locate and delete the 'Test Todo'
    #     delete_button = self.driver.find_element(
    #         By.XPATH, "//tr[contains(., 'Test Todo')]//a[contains(@href, 'delete')]"
    #     )
    #     delete_button.click()

    #     # Confirm deletion
    #     WebDriverWait(self.driver, 20).until(
    #         EC.element_to_be_clickable((By.XPATH, "//input[@value='Yes, I’m sure']"))
    #     ).click()

    #     # Wait for the todo to be deleted and ensure it's no longer visible
    #     WebDriverWait(self.driver, 20).until(
    #         EC.invisibility_of_element_located(
    #             (By.XPATH, "//*[contains(text(), 'Test Todo')]")
    #         )
    #     )

    #     # Verify that the todo is deleted
    #     self.assertNotIn("Test Todo", self.driver.page_source)
