import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, StringProperty
from kivy.core.window import Window

from appliance import Appliance
from saver import ResultSaver 

kivy.require('2.0.0')

class ApplianceApp(App):
    power = NumericProperty(0)
    hours = NumericProperty(0)
    days = NumericProperty(0)
    rate = NumericProperty(0)
    result_text = StringProperty("Результат: ")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.appliance = None  # Store the Appliance object

    def build(self):
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # входные данные
        self.power_input = TextInput(hint_text='Мощность прибора (Вт)', input_type='number', multiline=False)
        self.hours_input = TextInput(hint_text='Часы использования в день', input_type='number', multiline=False)
        self.days_input = TextInput(hint_text='Количество дней', input_type='number', multiline=False)
        self.rate_input = TextInput(hint_text='Стоимость электроэнергии (руб/кВт*ч)', input_type='number', multiline=False)

        # кнопка
        self.calculate_button = Button(text='Рассчитать', on_press=self.calculate)

        # кнопки сохранения вычислений
        self.save_doc_button = Button(text='Сохранить в DOC', on_press=self.save_doc)
        self.save_xls_button = Button(text='Сохранить в XLS', on_press=self.save_xls)

        # вывод результата
        self.result_label = Label(text=self.result_text)

        # вид
        self.main_layout.add_widget(Label(text='Мощность прибора (Вт):'))
        self.main_layout.add_widget(self.power_input)
        self.main_layout.add_widget(Label(text='Часы использования в день:'))
        self.main_layout.add_widget(self.hours_input)
        self.main_layout.add_widget(Label(text='Количество дней:'))
        self.main_layout.add_widget(self.days_input)
        self.main_layout.add_widget(Label(text='Стоимость электроэнергии (руб/кВт*ч):'))
        self.main_layout.add_widget(self.rate_input)
        self.main_layout.add_widget(self.calculate_button)
        self.main_layout.add_widget(self.result_label)
        self.main_layout.add_widget(self.save_doc_button)
        self.main_layout.add_widget(self.save_xls_button)

        return self.main_layout
#функция вычисления
    def calculate(self, instance):
        try:
            power = float(self.power_input.text)
            hours = float(self.hours_input.text)
            days = float(self.days_input.text)
            rate = float(self.rate_input.text)

            self.appliance = Appliance(power, hours, days, rate)  
            self.result_text = str(self.appliance)  
            self.result_label.text = self.result_text


        except ValueError:
            self.show_popup("Ошибка", "Пожалуйста, введите корректные числовые значения.")
        except Exception as e:
            self.show_popup("Ошибка", f"Произошла ошибка: {e}")

    def save_doc(self, instance):
        if self.appliance:
            try:
                saver = ResultSaver(str(self.appliance))
                saver.save_to_doc()
                self.show_popup("Сохранено", "Результат сохранен в lab12.docx")
            except Exception as e:
                self.show_popup("Ошибка", f"Ошибка при сохранении в DOC: {e}")
        else:
            self.show_popup("Предупреждение", "Сначала выполните расчет.")

    def save_xls(self, instance):
        if self.appliance:
            try:
                saver = ResultSaver(str(self.appliance))
                saver.save_to_xls()
                self.show_popup("Сохранено", "Результат сохранен в lab12.xlsx")
            except Exception as e:
                self.show_popup("Ошибка", f"Ошибка при сохранении в XLS: {e}")
        else:
            self.show_popup("Предупреждение", "Сначала выполните расчет.")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    ApplianceApp().run()