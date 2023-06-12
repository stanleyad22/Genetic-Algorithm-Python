from tkinter import *
from tkinter import ttk
# import ttkbootstrap as ttk
from GeneticAlgorithm import AlgoritmaGenetika

counter = 1
def generate():
    global counter, log
    GA = AlgoritmaGenetika(jumlah_generasi=int(entry_jumlah_generasi.get()),
                           jumlah_kromosom=int(entry_jumlah_kromosom.get()),
                           panjang_individu=int(entry_panjang_kromosom.get()),
                           prob_mutasi=float(entry_probabilitas_mutasi.get()),
                           prob_crossover=float(entry_probabilitas_crossover.get()),
                           batas_bawah_x=float(entry_batas_bawah_x.get()),
                           batas_atas_x=float(entry_batas_atas_x.get()),
                           batas_bawah_y=float(entry_batas_bawah_y.get()),
                           batas_atas_y=float(entry_batas_atas_y.get()))

    #jg 1000 jk 20 pi 5 pm 0.2 pc 0.3 bbx -3.0 bax 12.1 bby 4.1 bay 5.8
    # print(max(GA.fitness))

    log.insert(parent='', index='end', id=str(counter),
                    values=(counter,
                            "%.6f" % max(GA.fitness)))
    counter += 1

# root = ttk.Window(themename="superhero")
root = Tk()
root.geometry('800x600')
root.title("Algoritma Genetika")

main_frame = LabelFrame(root, padx=5, pady=5, text="Genetic Algorithm", labelanchor="n")
main_frame.pack(ipadx=5, ipady=5, padx=3, pady=3)
Label(root, text="- Dibuat oleh : Stanley Adi Dewangga & Nathan Missionday Gloriant -").pack()

# Frame input
frame_input = LabelFrame(main_frame, padx=5, pady=5, text="Input parameter", labelanchor="n")
frame_input.grid(row=0, column=0, sticky="n")

# Label dan Entry untuk Jumlah Generasi
label_jumlah_generasi = Label(frame_input, text="Jumlah Generasi:")
label_jumlah_generasi.pack(anchor="w")
entry_jumlah_generasi = Entry(frame_input)
entry_jumlah_generasi.pack()

# Label dan Entry untuk Jumlah Kromosom
label_jumlah_kromosom = Label(frame_input, text="Jumlah Kromosom:")
label_jumlah_kromosom.pack(anchor="w")
entry_jumlah_kromosom = Entry(frame_input)
entry_jumlah_kromosom.pack()

# Label dan Entry untuk Panjang Kromosom
label_panjang_kromosom = Label(frame_input, text="Panjang Kromosom:")
label_panjang_kromosom.pack(anchor="w")
entry_panjang_kromosom = Entry(frame_input)
entry_panjang_kromosom.pack()

# Label dan Entry untuk Probabilitas Mutasi
label_probabilitas_mutasi = Label(frame_input, text="Probabilitas Mutasi:")
label_probabilitas_mutasi.pack(anchor="w")
entry_probabilitas_mutasi = Entry(frame_input)
entry_probabilitas_mutasi.pack()

# Label dan Entry untuk Probabilitas Crossover
label_probabilitas_crossover = Label(frame_input, text="Probabilitas Crossover:")
label_probabilitas_crossover.pack(anchor="w")
entry_probabilitas_crossover = Entry(frame_input)
entry_probabilitas_crossover.pack()

# Label dan Entry untuk Batas Bawah X
label_batas_bawah_x = Label(frame_input, text="Batas Bawah X:")
label_batas_bawah_x.pack(anchor="w")
entry_batas_bawah_x = Entry(frame_input)
entry_batas_bawah_x.pack()

# Label dan Entry untuk Batas Atas X
label_batas_atas_x = Label(frame_input, text="Batas Atas X:")
label_batas_atas_x.pack(anchor="w")
entry_batas_atas_x = Entry(frame_input)
entry_batas_atas_x.pack()

# Label dan Entry untuk Batas Bawah Y
label_batas_bawah_y = Label(frame_input, text="Batas Bawah Y:")
label_batas_bawah_y.pack(anchor="w")
entry_batas_bawah_y = Entry(frame_input)
entry_batas_bawah_y.pack()

# Label dan Entry untuk Batas Atas
label_batas_atas_y = Label(frame_input, text="Batas Atas Y:")
label_batas_atas_y.pack(anchor="w")
entry_batas_atas_y = Entry(frame_input)
entry_batas_atas_y.pack()

# Frame proses generasi
frame_generasi = LabelFrame(main_frame, padx=5, pady=5, text="Proses Generasi", labelanchor="n")
frame_generasi.grid(row=0, column=1, sticky="n")
# Label(frame_generasi, text="abc").pack()

# Frame kromosom ke n
# ++ kromosom, x, y dan fitness
frame_kromosom = LabelFrame(frame_generasi, padx=5, pady=5, text="Kromosom ke n", labelanchor="n")
frame_kromosom.grid(row=0, column=0, rowspan=2)
Label(frame_kromosom, text="abc").pack()

# Crossover
# ++ kromosom terpilih sebelum dan sesudah
frame_crossover = LabelFrame(frame_generasi, padx=5, pady=5, text="Crossover", labelanchor="n")
frame_crossover.grid(row=0, column=1)
tes = Label(frame_crossover, text="abc", relief=SUNKEN, bd=1)
tes.pack()

# Mutation
# ++ kromosom terpilih sebelum dan sesudah
frame_mutation = LabelFrame(frame_generasi, padx=5, pady=5, text="Mutation", labelanchor="n")
frame_mutation.grid(row=1, column=1)
Label(frame_mutation, text="abc").pack()

# Seleksi
# ++ kromosom, x, y dan fitness yang sudah disort
frame_seleksi = LabelFrame(frame_generasi, padx=5, pady=5, text="Proses Seleksi", labelanchor="n")
frame_seleksi.grid(row=0, column=2, rowspan=2)
Label(frame_seleksi, text="abc").pack()

# Frame Populasi ke n + 1
# ++ x, y dan fitness
frame_kromosom_2 = LabelFrame(frame_generasi, padx=5, pady=5, text="Kromosom ke n+1", labelanchor="n")
frame_kromosom_2.grid(row=0, column=3, rowspan=2)
Label(frame_kromosom_2, text="abc").pack()

log = ttk.Treeview(main_frame, height=5)
log['columns'] = ("No", "Hasil Optimum")

log.column("#0", width=0, stretch=NO)
log.column("No", anchor=CENTER, width=30, minwidth=25, stretch=TRUE)
log.column("Hasil Optimum", anchor=CENTER, width=100, minwidth=40, stretch=TRUE)

log.heading("#0", anchor=W)
log.heading("No", text="No", anchor=CENTER)
log.heading("Hasil Optimum", text="Hasil Optimum", anchor=CENTER)

log.grid(row=1, column=1, padx=10, rowspan=2, sticky=N)

# Button untuk Generate Nilai Optimum
generate = Button(main_frame, text="Generate", command=generate)
generate.grid(row=1, column=0, pady=10, sticky="n")

root.mainloop()