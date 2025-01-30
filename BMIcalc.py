import tkinter

window = tkinter.Tk()
window.minsize(300,300)
window.title("Vücut Kitle Endeksi")
window.config(padx=30, pady=30)


def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if height =="" or weight =="":
        result_label.config(text="Boy ve kilo alanları boş bırakılamaz !!!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string=write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Lütfen doğru formatta bilgileri giriniz!!!")
###

weight_input_label =tkinter.Label(text="Kilonuzu giriniz :")
weight_input_label.pack()

weight_input = tkinter.Entry(width=15)
weight_input.pack()

height_input_label = tkinter.Label(text="Boyunuzu giriniz :")
height_input_label.pack()

height_input = tkinter.Entry(width=15)
height_input.pack()

calculate_button = tkinter.Button(text= "Hesapla", command=calculate_bmi)
calculate_button.pack(pady=20)

result_label = tkinter.Label()
result_label.pack()

def write_result(bmi):
    result_string=f"Kilo endeksizin : {round(bmi,2)}.\n Kategoriniz : "

    if bmi <= 16:
        result_string += "Ciddi derecede zayıf"
    elif 16 < bmi <= 17:
        result_string += "Orta derecede zayıf"
    elif 17 < bmi <= 18.5:
        result_string += "Hafif zayıf"
    elif 18.5 < bmi <= 25:
        result_string += "Normal"
    elif 25 < bmi <= 30:
        result_string += "Fazla kilolu"
    elif 30 < bmi <= 35:
        result_string += "Birinci derece obezite"
    elif 35 < bmi <= 40:
        result_string += "İkinci derece obezite"
    else:
        result_string += "Üçüncü derece obezite"
    return result_string
window.mainloop()