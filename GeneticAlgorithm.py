import random
import math

class AlgoritmaGenetika:
    def __init__(self, jumlah_generasi, jumlah_kromosom, panjang_individu, prob_crossover, prob_mutasi,
                 batas_bawah_x, batas_atas_x, batas_bawah_y, batas_atas_y):
        self.jumlah_generasi = jumlah_generasi
        self.jumlah_kromosom = jumlah_kromosom
        self.panjang_individu = panjang_individu
        self.prob_crossover = prob_crossover
        self.prob_mutasi = prob_mutasi
        self.batas_bawah_x = batas_bawah_x
        self.batas_atas_x = batas_atas_x
        self.batas_bawah_y = batas_bawah_y
        self.batas_atas_y = batas_atas_y
        self.offspring = []
        self.populasi = []
        self.fitness = []
        self.bit_x = 0
        self.bit_y = 0
        self.inisialisasiPopulasi()
        self.cariOptimum()

    @staticmethod
    # natan
    def fungsiFitness(x, y):
        return 21.5 + (x * math.sin(4 * math.pi * x)) + (y * math.sin(20 * math.pi * y))

    # natan
    def cariBit(self):
        all_N_found = False
        N1_found = False
        N2_found = False
        N = 1
        while not all_N_found:
            #x
            if (2 ** (N - 1)) < (self.batas_atas_x - self.batas_bawah_x) * (10 ** self.panjang_individu) <= ((2 ** N) - 1):
                self.bit_x = N
                N1_found = True
            #y
            if (2 ** (N - 1)) < (self.batas_atas_y - self.batas_bawah_y) * (10 ** self.panjang_individu) <= ((2 ** N) - 1):
                self.bit_y = N
                N2_found = True

            if N1_found and N2_found:
                all_N_found = True
            N += 1

    # natan
    def inisialisasiPopulasi(self):
        self.cariBit()
        for _ in range(self.jumlah_kromosom):
            x_biner = format(random.randint(2 ** (self.bit_x - 1), 2 ** self.bit_x), '0b')
            y_biner = format(random.randint(2 ** (self.bit_y - 1), 2 ** self.bit_y), '0b')
            self.populasi.append(x_biner + y_biner)

    @staticmethod
    # natan
    def desimalKeVariabel(desimal, batas_atas, batas_bawah, bit):
        return batas_bawah + desimal * ((batas_atas - batas_bawah) / ((2 ** bit) - 1))

    # natan
    def cariOptimum(self):
        for _ in range(self.jumlah_generasi):
            self.offspring.clear()

            mutation = self.mutation()
            crossover = self.crossover()
            self.offspring += mutation + crossover

            # enlarge
            self.populasi += self.offspring
            self.hitungFitness()
            self.seleksi()

    # natan
    def hitungFitness(self):
        self.fitness = []
        for populasi in self.populasi:
            x = self.desimalKeVariabel(
                desimal=int(populasi[0:self.bit_x], 2),
                batas_atas=self.batas_atas_x,
                batas_bawah=self.batas_bawah_x,
                bit=self.bit_x
            )
            y = self.desimalKeVariabel(
                desimal=int(populasi[self.bit_x:len(populasi)], 2),
                batas_atas=self.batas_atas_y,
                batas_bawah=self.batas_bawah_y,
                bit=self.bit_y
            )
            self.fitness.append(self.fungsiFitness(x, y))

    # stanley
    def crossover(self):
        populasi_terpilih = []
        hasil_crossover = []
        # Pemilihan Populasi
        for i in range(self.jumlah_kromosom - 1):
            if random.random() < self.prob_crossover:
                populasi_terpilih.append(self.populasi[i])

        if len(populasi_terpilih) > 1:
            # crossover untuk populasi terpilih
            for i in range(len(populasi_terpilih)):
                for j in range(i+1, len(populasi_terpilih)):
                    # one cut point
                    cutpoint = random.randint(0, self.bit_x + self.bit_y - 1)
                    hasil_crossover.append(
                        populasi_terpilih[i][0:cutpoint]
                        + populasi_terpilih[j][cutpoint:len(populasi_terpilih[j])])
        return hasil_crossover

    # stanley
    def mutation(self):
        mutation = []
        for i in range(len(self.populasi)):
            if random.random() < self.prob_mutasi:
                kromosom = random.randint(0, len(self.populasi)-1)
                pos = random.randint(0, len(self.populasi[kromosom]) - 1)
                mutation.append(
                    self.populasi[kromosom][0:pos] +
                    ('1' if self.populasi[kromosom][pos] == '0' else '0') +
                    self.populasi[kromosom][pos+1:len(self.populasi[kromosom])+1])
        return mutation

    # natan
    def seleksi(self):
        # urutkan populasinya berdasarkan fitness terbesar
        for i in range(len(self.fitness)):
            for j in range(0, len(self.fitness)-i-1):
                if self.fitness[j] < self.fitness[j + 1]:
                    temp = self.populasi[j]
                    self.populasi[j] = self.populasi[j + 1]
                    self.populasi[j + 1] = temp
                    temp = self.fitness[j]
                    self.fitness[j] = self.fitness[j + 1]
                    self.fitness[j + 1] = temp
        # ambil top 10
        self.fitness = self.fitness[:self.jumlah_kromosom]
        self.populasi = self.populasi[:self.jumlah_kromosom]

def main():
    GA = AlgoritmaGenetika(jumlah_generasi=1000,
                           jumlah_kromosom=20,
                           panjang_individu=5,
                           prob_mutasi=0.2,
                           prob_crossover=0.3,
                           batas_bawah_x=-3.0,
                           batas_atas_x=12.1,
                           batas_bawah_y=4.1,
                           batas_atas_y=5.8)
    print(max(GA.fitness))

if __name__ == "__main__":
    main()

# print(GA.populasi)
# print(GA.bit_x)
# print(GA.bit_y)
#
# for i in range(GA.ukuran_populasi):
#     print(int(GA.populasi[i][GA.bit_x:(len(GA.populasi)-1)], 2))

# abc = [4,5,6]
# fgh = [7,8,9]
# abc += fgh
# print(abc)
#
# simulasi mutasi
# bde = ''
# bde = '10010100001'
# bdehasil = []
# a = random.randint(0, len(bde)-1)
# print(a)
# bdehasil.append(bde[0:a] + ('1' if bde[a] == '0' else '0') + bde[a+1:len(bde)+1])
# print(bdehasil)
# jfk = ['000', '001', '010']
#
# for i in range (len(bde)):
#     print(bde[i] + jfk[i])
#     print(bde[i][0:len(bde)])

# abc = list(range(1, 6))
#
# for i in range (len(abc)):
#     for j in range (i+1, len(abc)):
#         print(abc[i], " dengan ", abc[j])
