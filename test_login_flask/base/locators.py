from selenium.webdriver.common.by import By


class Locators:
	"""Class containing all locators"""
	username_field: tuple = (By.XPATH, "/html/body/section/input[1]")
	password_field: tuple = (By.XPATH, "/html/body/section/input[2]")
	login_button: tuple = (By.XPATH, "/html/body/section/a")
	form_login: tuple = (By.XPATH, "/html/body/section")
