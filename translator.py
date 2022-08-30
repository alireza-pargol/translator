from tkinter import *
import googletrans
import textblob
from tkinter import ttk,messagebox

# پاک کردن کل دیتا های موجود در باکس ها
def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

#تبدیل کردن زبان های موجود به یک لیست پایتونی
languages = googletrans.LANGUAGES
language_list = list(languages.values())

def translate():
    translated_text.delete(1.0,END) #پاک کردن ترجمه قبلی
    try:
        # به دست اوردن کلید زبان ورودی
        for key,value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key
        # به دست اوردن کلید زبان خروجی
        for key,value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key
        #ذخیره کردن کلمات و ترجمه کردن آنها
        words = textblob.TextBlob(original_text.get(1.0, END))
        words = words.translate(from_lang=from_language_key
                                , to=to_language_key)
        translated_text.insert(1.0, words) # نمایش ترجمه
    except Exception as e:
        messagebox.showerror("Translator", e)

window = Tk()
window.title("Adak - Translator")
window.geometry("880x300")

#متن اصلی
original_text = Text(window, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)
#متن ترجمه شده
translated_text = Text(window, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)
# کلید ترجمه کردن
translate_btn = Button(window, text="Translate",
                       font=("Arial", 24),
                       command=translate)
translate_btn.grid(row=0, column=1, padx=10)

#لیست بازشونده زبانهای مبدا
original_combo = ttk.Combobox(window, width=50
                              , value=language_list)
# انتخاب زبان فارسی برای ورودی پیشفرض
original_combo.current(72)
original_combo.grid(row=1, column=0)

#لیست بازشوند زبانهای مقصد
translated_combo = ttk.Combobox(window, width=50
                                , value=language_list)
# انتخاب زبان انگلیسی برای خروجی پیشفرض
translated_combo.current(21)
translated_combo.grid(row=1, column=2)

#کلید پاک کننده باکس ها
clear_btn = Button(window, text="Clear", command=clear)
clear_btn.grid(row=2, column=1)

window.mainloop()