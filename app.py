from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Comida Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_praca.receber_avaliacao('Coud', 3)
restaurante_japones.receber_avaliacao('Less', 4)
restaurante_mexicano.receber_avaliacao('Sau', 5)

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()