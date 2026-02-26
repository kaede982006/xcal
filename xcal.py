import tkinter as tk
from tkinter import ttk

def calculate(string):
    return eval(string)
def numeric_behavior(num, text):
    text.config(state=tk.NORMAL)
    global zero_available
    if zero_available==False and text.get("end-2c") == '0':
        return
    text.insert(tk.END, num)
    if num!='0':
        zero_available=True
    text.config(state=tk.DISABLED)

def general_operate_behavior(operator, text):
    text.config(state=tk.NORMAL)
    global zero_available
    if text.get("end-2c") in ["+","-","/","*"]:
        return
    text.insert(tk.END, operator)
    zero_available=False
    text.config(state=tk.DISABLED)

def immediate_operate_behavior(operator, text):
    text.config(state=tk.NORMAL)
    global zero_available
    if operator=='=':
        global out
        out.config(state=tk.NORMAL)
        out.delete("1.0", "end")
        out.insert(tk.END, calculate(text.get("1.0", "end")))
        out.config(state=tk.DISABLED)
    elif operator=='C':
        text.delete("1.0","end")
    zero_available=False
    text.config(state=tk.DISABLED)

zero_available=False
root = tk.Tk()
root.geometry('295x385')
root.resizable(False, False)

root.tk.call("source", "azure/azure.tcl")
root.tk.call("set_theme", "dark")

button_behavior_list = [
    numeric_behavior, numeric_behavior, numeric_behavior, general_operate_behavior,
    numeric_behavior, numeric_behavior, numeric_behavior, general_operate_behavior,
    numeric_behavior, numeric_behavior, numeric_behavior, general_operate_behavior,
    immediate_operate_behavior, numeric_behavior, immediate_operate_behavior, general_operate_behavior
]
button_character_list = list("123/456*789+C0=-")

text = tk.Text(root, width=36, height=10)
text.config(state=tk.DISABLED)
text.grid(row=0, column=0, columnspan=4, rowspan=2)

out = tk.Text(root, width=36, height=2)
out.config(state=tk.DISABLED)
out.grid(row=2, column=0, columnspan=4, rowspan=2)

button_list = []
for i, ch in enumerate(button_character_list):
    fn = button_behavior_list[i]
    btn = ttk.Button(
        root,
        text=ch,
        width=5,
        command=lambda ch=ch, fn=fn: fn(ch, text)   # 여기서 캡처
    )
    btn.grid(row=i // 4 + 4, column=i % 4, padx=5, pady=5)
    button_list.append(btn)

root.mainloop()
