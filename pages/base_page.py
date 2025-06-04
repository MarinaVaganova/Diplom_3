import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    TIMEOUT = 20

    def __init__(self,driver):
        self.driver = driver

    @allure.step('Ожидание загрузки элемента страницы')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located(locator))

    @allure.step('Поиск элемента на странице')
    def find_element_on_page(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Проверка отображения элемента на странице')
    def check_element_display(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Проверка кликабельности элемента на странице')
    def check_element_clickability(self, locator):
        return WebDriverWait(self.driver, BasePage.TIMEOUT).until(EC.element_to_be_clickable(locator))

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        target = self.check_element_clickability(locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    @allure.step('Ввод значения в поле ввода')
    def entering_value_input_field(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Получение текста элемента')
    def get_text_on_element(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator).text

    @allure.step('Ожидание смены текста на элементе')
    def wait_for_element_to_change_text(self, locator, value):
        return WebDriverWait(self.driver, BasePage.TIMEOUT).until_not(EC.text_to_be_present_in_element(locator, value))

    @allure.step('Ожидание закрытия элемента')
    def wait_for_closing_of_element(self, locator):
        WebDriverWait(self.driver, BasePage.TIMEOUT).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Перенос элемента')
    def drag_and_drop_element(self, source_element, target_element):
        from_element = self.find_element_on_page(source_element)
        to_element = self.find_element_on_page(target_element)
        self.driver.execute_script("""
        const [from_element, to_element] = arguments;
        const dataTransfer = new DataTransfer();
        // Эмуляция событий drag-and-drop
        ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {
        const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
        (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);
        });
        """, from_element, to_element)