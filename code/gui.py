import tkinter as tk
import os
import recognize_language

SIZE = "500x300"
HEIGHT = 350
WIDTH = 500
results = {}
show = False
def getLanguage():
    url = website.get()
    results = recognize_language.main(url)
    min_err = min(list(results.values()))
    print(min_err)
    lang = ""
    for key, val in results.items():
        if val == min_err:
            lang = key
            break
    text_var.set(lang)

    other_str = "Other languages and euclidean distance (language model - this text): \n"
    for key, val in results.items():
        other_str += key + ': '
        other_str += str(val) + '\n'
    other_lang_text.set(other_str)


def getOtherLan():
    print(results)
    return 'asdfsdf 97\n asdfasdf 92\n sadfasdfsd 22'
def learnModels():
    # tanks
    thanks = tk.Text(window, width = WIDTH, height = 1)
    thanks.insert(tk.END, 'Thank you, next time languages models will be more accurate!')
    thanks.config(state = 'disabled')
    thanks.pack()
    a = 2
# window settings
window = tk.Tk()
window.title("Recognizing language of website")
window.geometry(SIZE)

# define all objects
text_var = tk.StringVar(window)
other_lang_text = tk.StringVar(window)
language = tk.Label(window, width = WIDTH, height = 1, textvariable = text_var)
intro = tk.Text(window,width = WIDTH, height = 2)
website = tk.Entry(window, width = 40)
other_lan = tk.Label(window, width = WIDTH, height = 6, textvariable = other_lang_text)
learning_text = tk.Text(window, width = WIDTH, height = 2)
confirm_learning = tk.Button(window, text = "Correct", width = 20, command = learnModels)
# introduction textbox settings

intro.insert(tk.END, 'To recognize language of website please enter a webite`s adress below.')
intro.insert(tk.END, '\n')
intro.insert(tk.END, 'Website`s adress:', ('p'))
intro.tag_add('p','1.0','1.0')
intro.tag_config('p', justify='center')
intro.config(state='disabled', bg = "gray")
intro.pack()

# entry website

website.pack()

# submit button settings

confirm = tk.Button(window, text = "submit", width = 20, command = getLanguage, bg = "gray")
confirm.pack()

# information about language settings


language.config(state='disabled', bg = "black")
language.pack()


# information about prababilities of other languages

other_lan.config(state = 'disabled', bg = "black")
other_lan.pack()

# Learning models
len_t = 'Please let me know if language of website is the same as this one which program predicted for you'

learning_text.insert(tk.END, len_t)
learning_text.config(state = 'disabled', bg = "gray")
learning_text.pack()

# Learning submit

confirm_learning.pack()
tk.mainloop()