import tkinter as tk

calculation = ''


def add_to_calculator(symbol):
  global calculation
  calculation += str(symbol)
  text.delete(1.0, 'end')
  text.insert(1.0, calculation)


def evaluate_calculation():
  global calculation
  try:
    calculation = str(eval(calculation))
    text.delete(1.0, 'end')
    text.insert(1.0, calculation)
  except:
    clear_calculation()
    text.insert(1.0, 'Error')


def clear_calculation():
  global calculation
  calculation = ''
  text.delete(1.0, 'end')


root = tk.Tk()
root.geometry('306x275')

text = tk.Text(root, height=1, width=15, font=('Arial', 24))
text.grid(columnspan=5)

btn = tk.Button(root,
                text='1',
                command=lambda: add_to_calculator(1),
                width=3,
                font=('Arial', 15))
btn.grid(row=2, column=1)
btn2 = tk.Button(root,
                 text='2',
                 command=lambda: add_to_calculator(2),
                 width=3,
                 font=('Arial', 15))
btn2.grid(row=2, column=2)
btn3 = tk.Button(root,
                 text='3',
                 command=lambda: add_to_calculator(3),
                 width=3,
                 font=('Arial', 15))
btn3.grid(row=2, column=3)
btn_a = tk.Button(root,
                  text='+',
                  command=lambda: add_to_calculator('+'),
                  width=3,
                  font=('Arial', 15))
btn_a.grid(row=2, column=4)

btn4 = tk.Button(root,
                 text='4',
                 command=lambda: add_to_calculator(4),
                 width=3,
                 font=('Arial', 15))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root,
                 text='5',
                 command=lambda: add_to_calculator(5),
                 width=3,
                 font=('Arial', 15))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root,
                 text='6',
                 command=lambda: add_to_calculator(6),
                 width=3,
                 font=('Arial', 15))
btn6.grid(row=3, column=3)
btn_s = tk.Button(root,
                  text='-',
                  command=lambda: add_to_calculator('-'),
                  width=3,
                  font=('Arial', 15))
btn_s.grid(row=3, column=4)

btn7 = tk.Button(root,
                 text='7',
                 command=lambda: add_to_calculator(7),
                 width=3,
                 font=('Arial', 15))
btn7.grid(row=4, column=1)
btn8 = tk.Button(root,
                 text='8',
                 command=lambda: add_to_calculator(8),
                 width=3,
                 font=('Arial', 15))
btn8.grid(row=4, column=2)
btn_9 = tk.Button(root,
                  text='9',
                  command=lambda: add_to_calculator(9),
                  width=3,
                  font=('Arial', 15))
btn_9.grid(row=4, column=3)
btn_m = tk.Button(root,
                  text='*',
                  command=lambda: add_to_calculator('*'),
                  width=3,
                  font=('Arial', 15))
btn_m.grid(row=4, column=4)

btn_0 = tk.Button(root,
                  text='0',
                  command=lambda: add_to_calculator(0),
                  width=3,
                  font=('Arial', 15))
btn_0.grid(row=5, column=2)

btn_d = tk.Button(root,
                  text='/',
                  command=lambda: add_to_calculator('/'),
                  width=3,
                  font=('Arial', 15))
btn_d.grid(row=5, column=4)

btn_openbracket = tk.Button(root,
                            text='(',
                            command=lambda: add_to_calculator('('),
                            width=3,
                            font=('Arial', 15))
btn_openbracket.grid(row=5, column=1)
btn_closebracket = tk.Button(root,
                             text=')',
                             command=lambda: add_to_calculator(')'),
                             width=3,
                             font=('Arial', 15))
btn_closebracket.grid(row=5, column=3)

btn_equal = tk.Button(root,
                      text='=',
                      command=evaluate_calculation,
                      width=3,
                      font=('Arial', 15))
btn_equal.grid(row=7, column=3)

btn_clear = tk.Button(root,
                      text='C',
                      command=clear_calculation,
                      width=3,
                      font=('Arial', 15))
btn_clear.grid(row=7, column=4)

root.mainloop()
