import datetime
import os


class Logger:
    file_name = f"C:\\Users\\Ilona\\Documents\\main_project\\logs\\log_" + \
                str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + \
                ".log"

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_start_step(cls, method: str):  # что происходит ДО начала функции
        test_name = os.environ.get('PYTEST_CURRENT_TEST')  # тут будет название того теста, который будет запускаться

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"  # название метода (теста)
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"  # начало запуска метода (теста)
        data_to_add += f"Start name method: {method}\n"  # название функции, которая запускается
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)  # пишем в наш файл все вот эти данные сверху

    @classmethod
    def add_end_step(cls, url: str, method: str):  # что происходит ПОСЛЕ окончания работы функции
        data_to_add = f"End time: {str(datetime.datetime.now())}\n"  # когда закончился метод (тест)
        data_to_add += f"End name method: {method}\n"  # название отработавшей функции
        data_to_add += f"URL: {url}\n"  # где мы оказали в конце теста (url)
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)

