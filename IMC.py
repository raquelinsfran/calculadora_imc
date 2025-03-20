import tkinter as tk 
import customtkinter as ctk 

class IMCApp(ctk.CTk):  # Clase principal de la aplicación
    def __init__(self):
        super().__init__()
        
        self.title("Calculadora de IMC") 
        self.geometry("400x500")  
        
        # Sección para ingresar el peso
        ctk.CTkLabel(self, text="Indique su Peso en (kg):").pack(pady=5)
        self.peso_slider = tk.Scale(self, from_=30, to=200, orient="horizontal", length=300, command=self.actualizar_imc)
        self.peso_slider.pack()
        self.peso_entry = ctk.CTkEntry(self, state="readonly", width=80)
        self.peso_entry.pack(pady=5)
        
        # Sección para ingresar la altura
        ctk.CTkLabel(self, text="Indique su Altura en (cm):").pack(pady=5)
        self.altura_slider = tk.Scale(self, from_=100, to=250, orient="horizontal", length=300, command=self.actualizar_imc)
        self.altura_slider.pack()
        self.altura_entry = ctk.CTkEntry(self, state="readonly", width=80)
        self.altura_entry.pack(pady=5)
        
        # Selección del sexo
        ctk.CTkLabel(self, text="Seleccione su sexo:").pack(pady=5)
        self.sexo = tk.StringVar(value="Masculino")  
        frame_sexo = ctk.CTkFrame(self)
        frame_sexo.pack()
        tk.Radiobutton(frame_sexo, text="Masculino", variable=self.sexo, value="Masculino", command=self.actualizar_imc).pack(side="left", padx=10)
        tk.Radiobutton(frame_sexo, text="Femenino", variable=self.sexo, value="Femenino", command=self.actualizar_imc).pack(side="left", padx=10)
        
        # Sección para mostrar el IMC
        ctk.CTkLabel(self, text="Cálculo IMC:").pack(pady=5)
        self.imc_entry = ctk.CTkEntry(self, state="readonly", width=100)
        self.imc_entry.pack()
        
        # Sección para mostrar la interpretación del IMC
        ctk.CTkLabel(self, text="Segun su IMC, usted tiene:").pack(pady=5)
        self.resultado_label = ctk.CTkLabel(self, text="", wraplength=350)
        self.resultado_label.pack(pady=5)
        
    def actualizar_imc(self, *args):
        peso = self.peso_slider.get()
        altura = self.altura_slider.get() / 100  # Se convierte la altura de cm a metros
        
        # Actualiza el campo de entrada con el peso seleccionado
        self.peso_entry.configure(state="normal")
        self.peso_entry.delete(0, tk.END)
        self.peso_entry.insert(0, str(peso))
        self.peso_entry.configure(state="readonly")
        
        # Actualiza el campo de entrada con la altura seleccionada
        self.altura_entry.configure(state="normal")
        self.altura_entry.delete(0, tk.END)
        self.altura_entry.insert(0, str(altura * 100))
        self.altura_entry.configure(state="readonly")
        
        # Verifica que la altura sea válida antes de calcular el IMC
        if altura > 0:
            imc = round(peso / (altura ** 2), 2)  # Fórmula del IMC
            
            # Muestra el IMC calculado en la interfaz
            self.imc_entry.configure(state="normal")
            self.imc_entry.delete(0, tk.END)
            self.imc_entry.insert(0, str(imc))
            self.imc_entry.configure(state="readonly")
            
            # Muestra la interpretación del IMC según el sexo
            interpretacion = self.interpretar_imc(imc, self.sexo.get())
            self.resultado_label.configure(text=interpretacion)
        
    def interpretar_imc(self, imc, sexo):
        # Criterios de clasificación del IMC para hombres
        if sexo == "Masculino":
            if imc < 18.5:
                return "Bajo peso."
            elif 18.5 <= imc < 24.9:
                return "Peso normal."
            elif 25 <= imc < 29.9:
                return "Sobrepeso."
            elif 30 <= imc < 34.9:
                return "Obesidad grado 1."
            elif 35 <= imc < 39.9:
                return "Obesidad grado 2."
            else:
                return "Obesidad grado 3."
        
        # Criterios de clasificación del IMC para mujeres
        elif sexo == "Femenino":
            if imc < 18.0:
                return "Bajo peso."
            elif 18.0 <= imc < 23.9:
                return "Peso normal."
            elif 24 <= imc < 28.9:
                return "Sobrepeso."
            elif 29 <= imc < 34.9:
                return "Obesidad grado 1."
            elif 35 <= imc < 39.9:
                return "Obesidad grado 2."
            else:
                return "Obesidad grado 3."

if __name__ == "__main__":
    app = IMCApp()
    app.mainloop()  # Ejecuta la aplicación
