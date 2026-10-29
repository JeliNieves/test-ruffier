# escribe tu app aquí
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


from logic import *
from instructions import *

#Variable globales

name, age = "", 7
pulso_1, pulso_2, pulso_3 = 0, 0, 0


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        #WIDGETS
        instructions = Label (text = txt_instruction)
        txt_name = Label(text="Ingrese su nombre:")
        txt_age = Label(text="Ingrese su edad:")
        self.input_name = TextInput(multiline=False)
        self.input_age = TextInput(multiline=False, text = "7")
        self.btn = Button(text = "Iniciar Test", pos_hint={"center_x":0.5}, size_hint=(0.3, 0.2))
        
        # CORREGIDO: Se usa .bind para asociar el evento del botón en Kivy
        self.btn.bind(on_press=self.next_screen)

        #LAYOUT
        main_leyout = BoxLayout (orientation="vertical", padding=10, spacing=10)
        #LINEA1
        row_1 = BoxLayout(padding=10, spacing=10, size_hint_y=None, height= "50dp")
        row_1.add_widget(txt_name)
        row_1.add_widget(self.input_name)
        #LINEA2
        row_2 = BoxLayout(padding=10, spacing=10, size_hint_y=None, height= "50dp")
        row_2.add_widget(txt_age)
        row_2.add_widget(self.input_age)

        main_leyout.add_widget(instructions)
        main_leyout.add_widget(row_1)
        main_leyout.add_widget(row_2)
        main_leyout.add_widget(self.btn)

        self.add_widget(main_leyout)

    
    def next_screen(self, instance):
        global name, age

        name = self.input_name.text.strip()
        valor_edad = check_int(self.input_age.text.strip())

        if name == "" or valor_edad is False or valor_edad < 7:
            return 
        
        age = valor_edad
        self.manager.current = "pulso1"

class Pulso1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        #WIDGETS
        instructions = Label (text = txt_test1)
        txt_pulso1 = Label(text="Ingrese toma de pulso 1:")
        self.input_pulso1 = TextInput(multiline=False)
        self.btn = Button(text = "Siguiente", pos_hint={"center_x":0.5}, size_hint=(0.3, 0.2))
        
        self.btn.bind(on_press=self.next_screen)

        #LAYOUT
        main_leyout = BoxLayout (orientation="vertical", padding=10, spacing=10)
        #LINEA1
        row_1 = BoxLayout(padding=10, spacing=10, size_hint_y=None, height= "50dp")
        row_1.add_widget(txt_pulso1)
        row_1.add_widget(self.input_pulso1)

        main_leyout.add_widget(instructions)
        main_leyout.add_widget(row_1)
        main_leyout.add_widget(self.btn)

        self.add_widget(main_leyout)
    
    def next_screen(self, instance):
        global pulso_1

        texto_ingresado = self.input_pulso1.text.strip()
        valor = check_int(texto_ingresado)

        if texto_ingresado == "" or valor is False:
            return 

        pulso_1 = valor * 4
        self.manager.current = "pulso2"

class Pulso2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # WIDGETS
        instructions = Label(text=txt_test2)
        self.btn = Button(text="Siguiente", pos_hint={"center_x":0.5}, size_hint=(0.3, 0.2))
        
        self.btn.bind(on_press=self.next_screen)

        # LAYOUT
        main_leyout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        main_leyout.add_widget(instructions)
        main_leyout.add_widget(self.btn)
        
    
        self.add_widget(main_leyout)
        
        
    def next_screen(self, instance):
        global pulso_2

        self.manager.current = "pulso3"
        
class Pulso3Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        #WIDGETS
        instructions = Label (text = txt_test3)
        txt_toma1 = Label(text="Ingrese pulso de primeros 15 segundos:")
        txt_toma2 = Label(text="Ingrese pulso de ultimos 15 segundos")
        self.input_toma1 = TextInput(multiline=False)
        self.input_toma2 = TextInput(multiline=False)
        self.btn = Button(text = "Finalizar Test", pos_hint={"center_x":0.5}, size_hint=(0.3, 0.2))
        
        self.btn.bind(on_press=self.next_screen)

        #LAYOUT
        main_leyout = BoxLayout (orientation="vertical", padding=10, spacing=10)
        #LINEA1
        row_1 = BoxLayout(padding=10, spacing=10, size_hint_y=None, height= "50dp")
        row_1.add_widget(txt_toma1)
        row_1.add_widget(self.input_toma1)
        #LINEA2
        row_2 = BoxLayout(padding=10, spacing=10, size_hint_y=None, height= "50dp")
        row_2.add_widget(txt_toma2)
        row_2.add_widget(self.input_toma2)

        main_leyout.add_widget(instructions)
        main_leyout.add_widget(row_1)
        main_leyout.add_widget(row_2)
        main_leyout.add_widget(self.btn)

        self.add_widget(main_leyout)
        
        
    def next_screen(self, instance):
        global pulso_2, pulso_3
        
        txt_p2 = self.input_toma1.text.strip()
        txt_p3 = self.input_toma2.text.strip()
        
        p2 = check_int(txt_p2)
        p3 = check_int(txt_p3)
        
        if txt_p2 == "" or txt_p3 == "" or p2 is False or p3 is False:
            return 


        pulso_2 = p2 * 4
        pulso_3 = p3 * 4
        self.manager.current = "resultado"
        
class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.instructions = Label(text="Calculando resultado...")
        
        main_leyout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        main_leyout.add_widget(self.instructions)
        self.add_widget(main_leyout)

    def on_enter(self):
        global pulso_1, pulso_2, pulso_3, name, age
        
        
        indice = (pulso_1 + pulso_2 + pulso_3 - 200) / 10
        
        
        condicion = ruffier_index(indice, age)
        
        self.instructions.text = (
            f"Participante: {name}\n"
            f"Edad: {age} años\n\n"
            f"Índice de Ruffier: {indice:.1f}\n"
            f"Evaluación: {condicion}"
        )

class RuffierApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(MainScreen(name = "main"))
        manager.add_widget(Pulso1Screen(name = "pulso1"))
        manager.add_widget(Pulso2Screen(name = "pulso2"))
        manager.add_widget(Pulso3Screen(name = "pulso3"))
        manager.add_widget(ResultScreen(name="resultado"))
        
        return manager


if __name__ == "__main__":
    app = RuffierApp()
    app.run()