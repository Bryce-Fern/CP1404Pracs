from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKM(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        try:
            result = float(value) * 1.609
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

    def increase_decrease(self, value):
        try:
            result = self.miles_float() + value
            self.root.ids.input_number.text = str(result)
        except ValueError:
            pass

    def miles_float(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKM().run()
