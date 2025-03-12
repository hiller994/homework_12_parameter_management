import os

import allure
from selene import browser, be, have
#from tests.models.file_path import path

class RegistrationPage:
    @allure.step("Открываем браузер")
    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    @allure.step("Ввод имени")
    def fill_first_name(self, value):
        browser.element('[id="firstName"]').should(be.blank).type(value)
        return self

    @allure.step("Ввод фамилии")
    def fill_last_name(self, value):
        browser.element('[id="lastName"]').should(be.blank).type(value)
        return self

    @allure.step("Ввод емаил")
    def fill_email(self, value):
        browser.element('[id="userEmail"]').should(be.blank).type(value)

    @allure.step("Выбор гендера")
    def fill_gender(self,value):
        browser.element(value).click()

    @allure.step("Ввод номера")
    def fill_mobile(self, value):
        browser.element('[id="userNumber"]').should(be.blank).type(value)

    @allure.step("Ввод даты рождения")
    def fill_date_of_birth(self, year, month, day):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('[class="react-datepicker__month-select"]').click().element(f'[value="{month}"]').click()
        browser.element('[class="react-datepicker__year-select"]').click().element(f'[value="{year}"]').click()
        browser.element(f'[class="react-datepicker__day react-datepicker__day--0{day}"]').click()

    @allure.step("Выбор предмета")
    def fill_subjects(self, value):
        browser.element('[id="subjectsInput"]').set_value('his').element(f'//*[contains(text(),"{value}")]').click()

    @allure.step("Выбор хобби")
    def fill_hobbies(self,value):
        browser.element(value).click()

    #@allure.step("Загрузка фото")
    #def fill_picture(self, value):
    #    browser.element('[id="uploadPicture"]').send_keys(path(value))

    @allure.step("Ввод адреса")
    def fill_current_address(self, value):
        browser.element('[id="currentAddress"]').should(be.blank).type(value)

    @allure.step("Выбор страны")
    def fill_state(self, state):
        browser.element('[id="react-select-3-input"]').set_value('Hary').element(
            f'//*[contains(text(),"{state}")]').click()
        return self

    @allure.step("Выбор города")
    def fill_city(self, city):
        browser.element('[id="react-select-4-input"]').set_value('Kar').element(
            f'//*[contains(text(),"{city}")]').click()

    @allure.step("Проверка итоговой формы")
    def should_registered_user_with(self, full_name, email, gender, mobile, date_of_birth, subjects, hobbies, address, state_and_city):
        browser.element('[id="submit"]').click()
        browser.element('[class="modal-content"]').should(be.visible)
        browser.element('[class="modal-content"]').should(have.text(full_name))  # Student Name
        browser.element('[class="modal-content"]').should(have.text(email))  # Student Email
        browser.element('[class="modal-content"]').should(have.text(gender))  # Gender
        browser.element('[class="modal-content"]').should(have.text(mobile))  # Mobile
        browser.element('[class="modal-content"]').should(have.text(date_of_birth))  # Date of Birth
        browser.element('[class="modal-content"]').should(have.text(subjects))  # Subjects
        browser.element('[class="modal-content"]').should(have.text(hobbies))  # Hobbies
        browser.element('[class="modal-content"]').should(have.text(address))
        browser.element('[class="modal-content"]').should(have.text(state_and_city))