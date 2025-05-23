import tkinter as tk # library untuk gui python
# pastikan sudah memasang python dan menginstall ekstensi tkinter jika menjalankan kode lewat terminal
# maaf berantakan

def on_click(btn_text):
    current = entry.get()
    if btn_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "error")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)
        
# window utama untuk kalkulator
root = tk.Tk()
root.title("kalkulator sederhana")

# input (menampilkan angka dan hasil)
entry = tk.Entry(
    root, width=20, font=('Arial', 24), borderwidth=2, relief="solid", justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# list tombol untuk kalkulator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# membuat tombol tombol dari list 
row = 1
col = 0
for btn in buttons:
    action = lambda x=btn: on_click(x)
    # membuat tombol di grid
    tk.Button(
        root, text=btn, width=5, height=2, font=('Arial', 18), command=action
    ).grid(row=row, column=col, padx=5, pady=5)
    
    col += 1
    if col > 3:
        col = 0
        row += 1
        
# loop utama untuk aplikasi
root.mainloop() 

    
    
