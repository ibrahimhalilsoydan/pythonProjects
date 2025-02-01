from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import base64

def encode(key,clear):
    enc=[]

    for i in range(len(clear)):
        key_c=key[i%len(key)]
        enc_c=chr((ord(clear[i])+ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key,enc):
    dec=[]
    enc=base64.urlsafe_b64decode(enc).decode()

    for i in range(len(enc)):
        key_c=key[i%len(key)]
        dec_c=chr((256+ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def save_and_encrypt_notes():
    title = title_entry.get()
    message = input_text.get("1.0", END)
    master_secret= master_secret_input.get()

    if len(title)==0 or len(message)==0 or len(master_secret)==0:
        messagebox.showwarning("Warning", "Please fill all fields")
    else:
        message_encrypted = encode(master_secret,message)

        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            title_entry.delete(0, END)
            master_secret_input.delete(0, END)
            input_text.delete("1.0", END)

def decrypt_notes():
    message_encrypted = input_text.get("1.0", END)
    master_secret= master_secret_input.get()

    if len(message_encrypted)==0 or len(master_secret)==0:
        messagebox.showwarning("Warning", "Please fill all fields")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypted)
            input_text.delete("1.0", END)
            input_text.insert("1.0", decrypted_message)
        except:
            messagebox.showwarning("Warning", "Please fill all fields")

FONT = ("Verdana", 20, "normal")
window = Tk()
window.title("Secret Notes")
window.config(padx=20, pady=20)

# Resmi yükle (PNG)
image = Image.open("secret.png")  # PNG dosyasını açıyoruz
image = image.resize((150, 150))  # Boyutu 150x150 piksellik bir alana küçültüyoruz

# Resmi PhotoImage formatına çevir
photo = ImageTk.PhotoImage(image)

# Fotoğrafı en üste ekliyoruz
photo_label = Label(window, image=photo)
photo_label.pack(side=TOP, pady=10)  # Fotoğrafı üstte göster


# UI Elemanları
title_info_label = Label(text="İPUCU", font=FONT)
title_info_label.pack()

title_entry = Entry(width=40)
title_entry.pack()

input_info_label = Label(text="ŞİFRELENECEK BİLGİ &\nŞİFRELİ BİLGİ", font=FONT)
input_info_label.pack()

input_text = Text(width=30, height=8)
input_text.pack()

master_secret_label = Label(text="PAROLANIZ", font=FONT)
master_secret_label.pack()

master_secret_input = Entry(width=40)
master_secret_input.pack()

save_button = Button(text="Kaydet ve Şifrele",command=save_and_encrypt_notes)
save_button.pack(pady=10)

decrypt_button = Button(text="Şifreyi Kaldır",command=decrypt_notes)
decrypt_button.pack(pady=10)

# Pencereyi başlat
window.mainloop()
