def cria_posicao(col, lin):
    """
    Recebe um caracter e um inteiro correspondentes à coluna e à linha e  a posição correspondente 
    
    Args:
    - col: Caracter representativo da coluna
    - lin: Inteiro representativo da linha
    """
    if type(col) != str or type(lin) != int or len(col) != 1 or col not in 'abdcefghij' or lin not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        raise ValueError("cria_posicao: argumentos invalidos")
    return (col, lin)


def obtem_pos_col(p):
    """
    Recebe uma posição e devolve a coluna correspondente
    
    Args:
    - p: Posição (caracter, inteiro)
    """
    return str(p[0])


def obtem_pos_lin(p):
    """
    Recebe uma posição e devolve a linha correspondente

    Args:
    - p: Posição (caracter, inteiro)
    """
    return int(p[1])


def eh_posicao(arg):
    """
    Recebe um argumento e verifica se o argumento é um TAD posicao

    Args:
    - arg: Argumento a verificar
    """
    return obtem_pos_col(arg) in 'abcdefghi' and type(obtem_pos_lin(arg)) == int and 1 <= obtem_pos_lin(arg) <= 10


def posicoes_iguais(p1, p2):
    """
    Recebe duas posições e verifica se as posições são iguais


    Args:
    - p1: Posição 1
    - p2: Posição 2
    """
    #Verifca se as duas posicões são mesmo posições e verifica se são iguais
    return eh_posicao(p1) and eh_posicao(p2) and obtem_pos_col(p1) == obtem_pos_col(p2) and obtem_pos_lin(p1) == obtem_pos_lin(p2)


def posicao_para_str(p):
    """
    Recebe uma posição e devolve uma string com a representação da posição

    Args:
    - p: Posição a converter
    """
    if eh_posicao(p):
        return obtem_pos_col(p) + str(obtem_pos_lin(p))


def str_para_posicao(s):
    """
    Recebe uma string com a representação da posição e devolve a posição representada pelo seu argumento

    Args:
    - s: String com a representação da posição
    """
    return (obtem_pos_col(s)), int(obtem_pos_lin(s))


def eh_posicao_valida(p, n):
    """
    Recebe uma posição e o numero de orbitas e verifica se a posição é válida dentro do tabuleiro Orbito-n

    Args:
    - p: Posição a verificar
    - n: Numero de orbitas
    """
    return eh_posicao(p) and 0 < obtem_pos_lin(p) <= n * 2 and obtem_pos_col(p) in 'abcdefghij'[:n*2]


def obtem_posicoes_adjacentes(p, n, d):
    """
    Recebe uma posição, o numero de orbitas e um bool. Devolve um tuplo com as posições adjacentes à posição caso o bool seja True,
    ou as posições adjacentes ortogonais caso o bool seja False

    Args:
    - p: Posição
    - n: Numero de orbitas
    - d: Bool. True para adjacentes diagonais, False para adjacentes ortogonais
    """
    #Obter a coluna, a linha da posição e criar uma lista para guardar as possiveis posições adjacentes
    col = obtem_pos_col (p)
    lin = obtem_pos_lin(p)
    adjacentes = []
    #Caso d seja True
    if d:
        #Guarda-se na lista das adjacentes as suas possiveis posições adjacentes ordenadas em sentido horario
        adjacentes = [
            (col, lin - 1), (chr(ord(col) + 1), lin - 1), (chr(ord(col) + 1), lin),
            (chr(ord(col) + 1), lin + 1), (col, lin + 1), (chr(ord(col) - 1), lin + 1),
            (chr(ord(col) - 1), lin), (chr(ord(col) - 1), lin -1)
        ]
    else:
        #Guarda-se na lista das adjacentes as suas possiveis posições adjacentes ortogonais ordenadas em sentido horario
        adjacentes = [
            (col, lin - 1), (chr(ord(col) + 1), lin), 
            (col, lin + 1), (chr(ord(col) - 1), lin)
        ]
    #Para as posições dentro da lista verifica-se se as posições são válidas    
    adjacentes = [pos for pos in adjacentes if eh_posicao_valida(pos, n)]          
    return tuple(adjacentes)


def calcula_distancia_fora_tab(p, n):
    """
    Recebe uma posição e o numero de orbitas e devolve a distancia até a borda do tabuleiro

    Args:
    - p: Posição
    - n: Numero de orbitas
    """
    col = obtem_pos_col(p)
    lin = obtem_pos_lin(p)

    # Define-se as bordas do tabuleiro tendo em conta o numero de orbitas
    boundaries = {
        'top': 1,
        'bottom': n * 2,
        'left': 'a',
        'right': chr(ord('a') + n * 2 - 1)
    }
    # Calcula a distancia para as todas as bordas do tabuleiro
    dist_top = abs(boundaries['top'] - lin)
    dist_bottom = abs(lin - boundaries['bottom'])
    dist_left = abs(ord(col) - ord(boundaries['left']))
    dist_right = abs(ord(boundaries['right']) - ord(col))

    # Retoma a distancia minima para uma das bordas do tabuleiro
    return min(dist_top, dist_bottom, dist_left, dist_right)


def ordena_posicoes(tup, n):
    """
    Ordena um tuplo de posições no tabuleiro Orbito-n.
    Primeiro, pela órbita (mais interna para a mais externa),depois pela linha (de cima para baixo) e, 
    por último, pela coluna (da esquerda para a direita).

    Args:
    - tup: Tuplo de posições
    - n: Numero de orbitas
    """
    # Ordena primeiro pela órbita, depois pela linha e, por último, pela coluna
    return tuple(sorted(tup, key=lambda p: (-calcula_distancia_fora_tab(p, n), obtem_pos_lin(p), obtem_pos_col(p))))


def cria_pedra_branca():
    """
    Devolve uma pedra pertencente ao jogador branco
    """
    return 'O'
def cria_pedra_preta():
    """
    Devolve uma pedra pertencente ao jogador preto
    """
    return 'X'
def cria_pedra_neutra():
    """
    Devolve uma pedra neutra
    """
    return ' '


def eh_pedra(arg):
    """
    Recebe um argumento e verifica se o argumento é um TAD pedra

    Args:
    - arg: Argumento a verificar
    """
    return arg in (cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra())

def eh_pedra_branca(pedra):
    """
    Recebe uma pedra e verifca se a pedra é do jogador branco

    Args:
    - pedra: Pedra a verificar
    """
    return pedra == cria_pedra_branca()

def eh_pedra_preta(pedra):
    """
    Recebe uma pedra e verifica se a pedra é do jogador preto

    Args:
    - pedra: Pedra a verificar
    """
    return pedra == cria_pedra_preta()


def pedras_iguais(p1, p2):
    """
    Recebe duas pedras e verifica se são pedras e se são iguais
    """
    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2

def pedra_para_str(pedra):
    """
    Recebe uma pedra e devolve a cadeia de caracteres que representa o jogador dono da pedra

    Args:
    - pedra: Pedra a converter
    """
    if eh_pedra(pedra):  #Verifica que o argumento é uma pedra
        return pedra
        

def eh_pedra_jogador(pedra):
    """
    Recebe uma pedra e verifica se a pedra pertence a um dos jogadores

    Args:
    - pedra: Pedra a verificar
    """
    return eh_pedra_branca(pedra) or eh_pedra_preta(pedra)

def pedra_para_int(pedra):
    """
    Recebe uma pedra e devolve um inteiro 1, -1 ou 0, dependendo se a pedra é do jogador preto, branco ou neutra

    Args:
    - pedra: Pedra a converter
    """
    if pedra == cria_pedra_branca():
        return -1
    elif pedra == cria_pedra_preta():
        return 1
    elif pedra == cria_pedra_neutra():
        return 0
    
def int_para_pedra(int):
    if int == 0:
        return cria_pedra_neutra()
    elif int == 1:
        return cria_pedra_preta()
    elif int == -1:
        return cria_pedra_branca()
    
def cria_tabuleiro_vazio(n):
    """
    Recebe o numero de orbitas e devolve um tabuleiro vazio com n orbitas sem posições ocupadas

    Args:
    - n: Numero de orbitas
    """
    #Verifica o argumento
    if type(n) != int or n < 2 or n > 5:
        raise ValueError("cria_tabuleiro_vazio: argumento invalido")
    #Cria um dicionario vazio e obtem as colunas pertencentes a n
    tab = {}
    colunas = 'abcdefghij' [:n*2]
    #Percorre as colunas e adiciona ao dicionario a chave com a coluna e o valor com uma lista vazia
    for i in colunas:
        tab[i] = list(cria_pedra_neutra() for _ in range(n*2))
    return tab

def cria_tabuleiro(n, tp, tb):
    """
    Recebe o numero de orbitas e um tuplo com posições do jogador preto e do jogador branco e devolve um tabuleiro com as posições
    ocupadas pelos respetivos jogadores

    Args:
    - n: Numero de orbitas
    - tp: Tuplo com as posições do jogador preto
    - tb: Tuplo com as posições do jogador branco
    """
    #Verifica os argumentos
    if type(n) != int or n < 2 or n > 5 or type(tp) != tuple or type(tb) != tuple:
        raise ValueError("cria_tabuleiro: argumentos invalidos")
    for i in tp:
        if not eh_posicao(i) or i in tb:
            raise ValueError("cria_tabuleiro: argumentos invalidos")
    for i in tb:
        if not eh_posicao(i) or i in tp:
            raise ValueError("cria_tabuleiro: argumentos invalidos")
    #Cria um dicionario vazio e obtem as colunas pertencentes a n
    tab = {}
    colunas = 'abcdefghij'[:n*2]
    #Percorre as colunas e adiciona ao dicionario a chave com a coluna e o valor com uma lista vazia
    for i in colunas:
        tab[i] = list(cria_pedra_neutra() for _ in range(n*2))
        #Adiciona as pedras aos tabuleiro
        for j in range(1, int(n*2) + 1):
            pos = cria_posicao(i, j)
            if pos == tp or pos in tp:
                tab[i][j-1] = cria_pedra_preta()
            elif pos == tb or pos in tb:
                tab[i][j-1] = cria_pedra_branca()
    return tab

def cria_copia_tabuleiro(t):
    """
    Recebe um tabuleiro e devolve uma cópia do tabuleiro
    
    Args:
    - t: Tabuleiro a copiar
    """
    return {k: list(v) for k, v in t.items()}

def obtem_numero_orbitas(t):
    """
    Recebe um tabuleiro e devolve o numero de orbitas deste

    Args:
    - t: Tabuleiro a verificar
    """
    return int(len(t) / 2)

def obtem_pedra(t, p):
    """
    Recebe um tabuleiro e uma posição e devolve a pedra dessa posição. Caso a posição não estiver ocupada devolve uma pedra neutra

    Args:
    - t: Tabuleiro
    - p: Posição a verificar
    """
    return t[obtem_pos_col(p)][obtem_pos_lin(p) - 1]


def obtem_posicoes_tab(t):
    """
    Recebe um tabuleiro e devolve um tuplo com as todas as posicões pertencentes ao tabuleiro

    Args:
    - t: Tabuleiro
    """
    res = []
    #Percorrer todas as posições do tabuleiro t
    for lin in range(1, obtem_numero_orbitas(t) * 2 + 1):
        for col in range(ord('a'), ord('a') + obtem_numero_orbitas(t) * 2):
            pos = cria_posicao(chr(col), lin)
            res.append(pos)
    return tuple(res)


def obtem_orbita(t, p):
    """
    Recebe um tabuleiro e uma posição e devolve o numero da orbita em que a posição se encontra

    Args:
    - t: Tabuleiro
    - p: Posição a verificar
    """
    n = obtem_numero_orbitas(t)
    if calcula_distancia_fora_tab(p, n) == 0:
        return n
    elif calcula_distancia_fora_tab(p, n) == 1:
        return n -1
    elif calcula_distancia_fora_tab(p, n) == 2:
        return n - 2
    elif calcula_distancia_fora_tab(p, n) == 3:
        return n - 3
    elif calcula_distancia_fora_tab(p, n) == 4:
        return n - 4 


def obtem_linha_horizontal(t, p):
    """
    Recebe um tabuleiro e uma posição e devolve um tuplo com as posições que ocupam a mesma linha que a posição com o seu valor

    Args:
    - t: Tabuleiro
    - p: Posição a verificar
    """
    #Obtem a linha da posição
    linha = obtem_pos_lin(p)
    res = []
    #Percorre as chaves do dicionario tabuleiro e adiciona à lista res as posições que ocupam a mesma linha que a posição e o seu valor
    for i in t.keys():
        pos = cria_posicao(i, linha)
        res.append((pos, obtem_pedra(t, pos)))
    return tuple(res)

def obtem_linha_vertical(t, p):
    """
    Recebe um tabuleiro e uma posição e devolve um tupplo com as posições que ocupam a mesma coluna que a posição com o seu valor

    Args:
    - t: Tabuleiro
    _ p: Posição a verificar
    """
    #Obtem a coluna da posição
    coluna = obtem_pos_col(p)
    res = []
    #Adiciona à lista res as posições que ocupam a mesma coluna que a posição e o seu valor
    for i in range(1, len(t[coluna]) + 1):
        pos = cria_posicao(coluna, i)
        res.append((pos, obtem_pedra(t, pos)))
    return tuple(res)


def obtem_linhas_diagonais(t, p):
    """
    Recebe um tabuleiro e uma posição e devolve um tuplo de tuplo com as posições na mesma diagonal,
    e da antidiagonal com o valor das posições.

    Args:
    - t: Tabuleiro
    - p: Posição a verificar
    """

    #Obtem a coluna, a linha da posição
    coluna = obtem_pos_col(p)
    linha = obtem_pos_lin(p)
    #Obtem a ultima coluna e a ultima linha do tabuleiro
    ultima_col = list(t.keys())[-1]
    ultima_linha = obtem_numero_orbitas(t) * 2
    #Cria uma lista vazia para a diagonal e a antidiagonal
    diagonal = []
    antidiagonal = []

    #Atualiza a posição até ser a primeira da diagonal
    while not (linha == 1 or coluna == 'a'):
        linha -= 1
        coluna = chr(ord(coluna) - 1)
    #Adiciona à lista as posições da diagonal e o seu valor 
    while coluna <= ultima_col and linha <= len(t['a']):
        pos = cria_posicao(coluna, linha)
        diagonal.append((pos, obtem_pedra(t, pos)))
        linha += 1
        coluna = chr(ord(coluna) + 1)
    #Volta-se a obter a coluna e a linha da posição
    coluna = obtem_pos_col(p)
    linha = obtem_pos_lin(p)
    #Atualiza-se a posição até ser a primeira da antidiagonal
    while not (linha == ultima_linha or coluna == 'a'):
        linha += 1
        coluna = chr(ord(coluna) - 1)
    #Adiciona à lista as posições da antidiagonal e o seu valor
    while coluna <= 'd' and linha >= 1:
        pos = cria_posicao(coluna, linha)
        antidiagonal.append((pos, obtem_pedra(t, pos)))
        linha -= 1
        coluna = chr(ord(coluna) + 1)
    #Retoma o tuplo com a digonal e antidiagonal
    return (tuple(diagonal), tuple(antidiagonal))


def obtem_posicoes_pedra(t, j):
    """
    Recebe um tabuleiro e um jogador e devolve um tuplo com as posições ocupadas pelo jogador

    Args:
    - t: Tabuleiro
    - j: Jogador a verificar
    """
    res = []
    for pos in obtem_posicoes_tab(t):
        if obtem_pedra(t, pos) == j:
            res.append(pos)
    return ordena_posicoes(tuple(res), obtem_numero_orbitas(t))


def coloca_pedra(t, p, j):
    """
    Recebe um tabuleiro, uma posição e um jogador e modifica o tabuleiro colocando a pedra na posição do tabuleiro colocando

    Args:
    - t: Tabuleiro
    - p: Posição a colocar a pedra
    - j: Jogador
    """
    t[obtem_pos_col(p)][obtem_pos_lin(p) - 1] = j
    return t

def remove_pedra(t, p):
    """
    Recebe um tabuleiro e uma posição e modifica o tabuleiro removendo a pedra da posição

    Args:
    - t: Tabuleiro
    - p: Posição a remover a pedra
    """
    t[obtem_pos_col(p)][obtem_pos_lin(p) - 1] = cria_pedra_neutra()
    return t

def eh_tabuleiro(arg):
    """
    Recebe um argumento e verifica se o argumento é um TAD tabuleiro

    Args:
    - arg: Argumento a verificar
    """
    return 2 <= obtem_numero_orbitas(arg) <= 5 

def tabuleiros_iguais(t1, t2):
    """
    Recebe dois tabuleiros e verifica se os tabuleiros são iguais

    Args:
    - t1: Primeiro tabuleiro
    - t2: Segundo tabuleiro
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2

def tabuleiro_para_str(t):
    """
    Recebe um tabuleiro e devolve a cadeia de caracteres que representa o tabuleiro

    Args:
    - t: Tabuleiro a converter
    """
    res = []
    colunas = list(t.keys())

    for i in range(len(colunas)):
        linha = []
        linha.append(f"{i+1:02}")            
        for j in colunas:
            valor = t[j][i]
            linha.append(f"[{pedra_para_str(valor)}]")
        linha_formatada = " ".join(linha[:2]) + "-" + "-".join(linha[2:])
        res.append(linha_formatada)
        if i != len(colunas) - 1:
            res.append("    " + "|   " * (len(colunas) - 1) + "|")
    return "    "+"   ".join(colunas)+ "\n" + "\n".join(res)


def move_pedra(t, p1, p2):
    """
    Recebe um tabuleiro e duas posições. Modifica o tabuleiro movendo a pedra da posição p1 para p2

    Args:
    - t: Tabuleiro
    - p1: Posição da pedra a mover
    - p2: Posição para onde mover a pedra
    """
    valor = obtem_pedra(t, p1)
    coloca_pedra(t, p2, valor)
    remove_pedra(t, p1)
    return t

def obtem_posicao_seguinte(t, p, s):
    """
    Recebe um tabuleiro, uma posição e um bool. Devolve a posição da mesma orbita que a posição a seguir no tabuleiro. Em sentido
    horario caso s for True ou anti-horario caso s for False

    Args:
    - t: Tabuleiro
    - p: Posição a verificar
    - s: Sentido horario ou anti-horario
    """
    posicoes_orbita = ()
    orbita = obtem_orbita(t, p)
    for i in obtem_posicoes_tab(t):
        if obtem_orbita(t, i) == orbita:
            posicoes_orbita += (i,)
            

    min_linha = min(obtem_pos_lin(pos) for pos in posicoes_orbita)
    max_linha = max(obtem_pos_lin(pos) for pos in posicoes_orbita)
    min_coluna = min(obtem_pos_col(pos) for pos in posicoes_orbita)
    max_coluna = max(obtem_pos_col(pos) for pos in posicoes_orbita)

    borda_superior = sorted([pos for pos in posicoes_orbita if obtem_pos_lin(pos) == min_linha], key=lambda pos: obtem_pos_col(pos))
    borda_direita = sorted([pos for pos in posicoes_orbita if obtem_pos_col(pos) == max_coluna and pos not in borda_superior], key=lambda pos: obtem_pos_lin(pos))
    borda_inferior = sorted([pos for pos in posicoes_orbita if obtem_pos_lin(pos) == max_linha and pos not in borda_direita], key=lambda pos: obtem_pos_col(pos), reverse=True)
    borda_esquerda = sorted([pos for pos in posicoes_orbita if obtem_pos_col(pos) == min_coluna and pos not in borda_inferior and pos not in borda_superior], key=lambda pos: obtem_pos_lin(pos), reverse=True)
    posicoes_ordenadas = borda_superior + borda_direita + borda_inferior + borda_esquerda

    index_p = posicoes_ordenadas.index(p)
    if s:
        return posicoes_ordenadas[(index_p + 1) % len(posicoes_ordenadas)]
    return posicoes_ordenadas[(index_p - 1) % len(posicoes_ordenadas)]


def roda_tabuleiro(t):
    """
    Recebe um tabuleiro e modifica-o rodando todas as pedras uma posição em sentido anti-horario e devolve o próprio tabuleiro

    Args:
    - t: Tabuleiro
    """
    antigo_t = cria_copia_tabuleiro(t)
    for pos in obtem_posicoes_tab(t):
        valor = obtem_pedra(antigo_t, pos)
        posicao_seguinte = obtem_posicao_seguinte(t, pos, False)
        t = coloca_pedra(t, posicao_seguinte, valor)
    return t


def verifica_linha_pedras(t, p, j, k):
    """
    Recebe um tabuleiro, uma posição,um jogador e um inteiro. Verifica se existe pelo menos uma linha que contenha a posição com k ou 
    mais pedras consecutivas do jogador

    Args:
    - t: Tabuleiro
    - p: Posição a verificar
    - j: Jogador
    - k: Número de pedras consecutivas necessárias
    """
    if obtem_pedra(t, p) != j:
        return False
    
    posicoes_linhas = ()
    linha = obtem_linha_horizontal(t, p)
    for i in linha:
        posicoes_linhas += (i[0], )

    posicoes_colunas = ()
    coluna = obtem_linha_vertical(t, p)
    for i in coluna:
        posicoes_colunas += (i[0], )
    
    posicoes_diagonais = ()
    diagonais = obtem_linhas_diagonais(t, p)
    for i in diagonais:
        for c in i:
            posicoes_diagonais += (c[0], )

    def conta_sequencia(sequencia):
        contador = 0
        posicao_index = sequencia.index(p)
        for i, pos in enumerate(sequencia):
            if obtem_pedra(t, pos) == j:
                contador += 1
                if contador >= k and posicao_index in range(i-k+1, i+1):
                    return True
            else:
                contador = 0
        return False
    
    return (conta_sequencia(posicoes_linhas) or
            conta_sequencia(posicoes_colunas) or
            conta_sequencia(posicoes_diagonais))

def obtem_posicoes_livres(t):
    """
    Recebe um tabuleiro e devolve um tuplo com todas as posições não ocupadas do tabuleiro

    Args:
    - t: Tabuleiro
    """
    res = []
    posicoes = obtem_posicoes_tab(t)
    for pos in posicoes:
        if obtem_pedra(t, pos) == cria_pedra_neutra():
            res.append(pos)
    return tuple(res)


def eh_vencedor(t, j):
    """
    Recebe um tabuleiro e uma pedra de jogador e verifica se existe uma linha completa do tabuleiro de pedras do jogador

    Args:
    - t: Tabuleiro
    - j: Jogador
    """
    num_linhas = obtem_numero_orbitas(t) * 2
    posicoes = obtem_posicoes_tab(t)
    for p in posicoes:
        if verifica_linha_pedras(t, p, j, num_linhas):
            return True
    return False

def eh_fim_jogo(t):
    """
    Recebe um tabuleiro e verifica se o jogo acabou.
    
    Args:
    - t: Tabuleiro a verificar
    """
    if len(obtem_posicoes_livres(t)) == 0:
        return True
    if eh_vencedor(t, cria_pedra_branca()) or eh_vencedor(t, cria_pedra_preta()):
        return True
    return False

def escolhe_movimento_manual(t):
    """
    Recebe um tabuleiro e permite escolher uma posição livre do tabuleiro onde colocar uma pedra. A função não modifica o seu 
    argumento e devolve a posição escolhida

    Args:
    - t: Tabuleiro
    """
    while True:
        escolha_jogador = input("Escolha uma posicao livre:")
        pos = str_para_posicao(escolha_jogador)
        if pos in obtem_posicoes_livres(t):
            return pos
        
        
def escolha_auto_facil(t, j):
    """
    Recebe um tabuleiro e um jogador e devolve a posição escolhida tendo em conta a dificuldade Facil

    Args:
    - t: Tabuleiro
    - j: Jogador
    """
    posicoes_livres = obtem_posicoes_livres(t)
    n = obtem_numero_orbitas(t)

    for pos in ordena_posicoes(posicoes_livres, n):
        copia_t = cria_copia_tabuleiro(t)
        coloca_pedra(copia_t, pos, j)
        roda_tabuleiro(copia_t)

        adjacentes = ordena_posicoes(obtem_posicoes_adjacentes(pos, n, True), n)
        for adj in adjacentes:
            if pedras_iguais(obtem_pedra(copia_t, adj), j):
                return pos

    posicoes_livres = obtem_posicoes_livres(t)
    return ordena_posicoes(posicoes_livres, n)[0]


def escolha_auto_normal(t, j):
    # Obter o número de órbitas e calcular k (número de peças consecutivas para vencer)
    num_orbitas = obtem_numero_orbitas(t)
    k = 2 * num_orbitas
    posicoes_livres = obtem_posicoes_livres(t)

    # Função auxiliar para verificar se é possível formar uma linha de L peças
    def posicao_forma_linhas(t, p, jogador, l):
        return verifica_linha_pedras(t, p, jogador, l)

    # Passo 1: Verificar se há uma jogada que leva à vitória para o jogador
    for pos in posicoes_livres:  # Todas as posições livres
        # Simular a jogada do jogador e a rotação do tabuleiro
        copia_t = cria_copia_tabuleiro(t)
        coloca_pedra(copia_t, pos, j)
        roda_tabuleiro(copia_t)

        # Verifica se essa jogada resulta em uma linha de k peças para o jogador
        if posicao_forma_linhas(copia_t, pos, j, k):
            return pos  # Retorna a posição vencedora

    # Passo 2: Tentar bloquear o oponente se uma jogada vencedora não for encontrada
    oponente = cria_pedra_branca() if eh_pedra_preta(j) else cria_pedra_preta()
    for pos in obtem_posicoes_pedra(t, cria_pedra_neutra()):
        # Simular a jogada do oponente e a rotação do tabuleiro duas vezes
        copia_t = cria_copia_tabuleiro(t)
        coloca_pedra(copia_t, pos, oponente)
        roda_tabuleiro(copia_t)
        roda_tabuleiro(copia_t)

        # Verifica se essa posição permitiria que o oponente ganhe
        if posicao_forma_linhas(copia_t, pos, oponente, k):
            return pos  # Retorna a posição que bloqueia o oponente

    # Passo 3: Retorna a primeira posição livre na ordem de leitura, caso nenhuma condição estratégica seja atendida
    posicoes_livres = obtem_posicoes_pedra(t, cria_pedra_neutra())
    return posicoes_livres[0] if posicoes_livres else None


def escolhe_movimento_auto(t, j, lvl):
    if lvl == 'facil':
        return escolha_auto_facil(t, j)
    elif lvl == 'normal':
        return escolha_auto_normal(t, j)


def orbito(n, modo, jog):
    """
    É a função principal que permite jogar um jogo completo de Orbito-n. A função recebe o numero de orbitas do tabuleiro, o modo de jogo
    e a representação do jogador. O jogo começa sempre com o jogador com as pedras pretas e se desenvolve até o fim

    Args:
    - n: Número de orbitas do tabuleiro
    - modo: Modo de jogo ('facil', 'normal' ou '2jogadores')
    - jog: Representação do jogador (cria_pedra_branca() ou cria_pedra_preta())
    """
    if type(n) != int or n < 2 or n > 5 or modo not in ('facil', 'normal', '2jogadores') or jog not in (pedra_para_str(cria_pedra_branca()), pedra_para_str(cria_pedra_preta())):
        raise ValueError('orbito: argumentos invalidos')
    tab = cria_tabuleiro_vazio(n)
    jog = pedra_para_int(jog)

    print("Bem-vindo ao ORBITO-2.")
    if modo in ('facil', 'normal'):
        print(f"Jogo contra o computador ({modo}).")
        if jog == pedra_para_int(cria_pedra_preta()):
            print(f"O jogador joga com '{pedra_para_str(cria_pedra_preta())}'.")
        else:
            print(f"O jogador joga com '{pedra_para_str(cria_pedra_branca())}'.")
    else:
        print("Jogo para dois jogadores.")
    print(tabuleiro_para_str(tab))

    jogador_atual = 1

    while not eh_fim_jogo(tab):
        if modo in ('facil', 'normal'):
            if jogador_atual == jog:
                print("Turno do jogador.")
                pos = escolhe_movimento_manual(tab)
            else:
                print(f"Turno do computador ({modo}):")
                pos = escolhe_movimento_auto(tab, jogador_atual, modo)
            tab = coloca_pedra(tab, pos, int_para_pedra(jogador_atual))
            roda_tabuleiro(tab)
            jogador_atual = -jogador_atual
            print(tabuleiro_para_str(tab))
        else:
            print(f"Turno do jogador '{pedra_para_str(int_para_pedra(jogador_atual))}'.")
            pos = escolhe_movimento_manual(tab)
            tab = coloca_pedra(tab, pos, int_para_pedra(jogador_atual))
            roda_tabuleiro(tab)
            jogador_atual = -jogador_atual
            print(tabuleiro_para_str(tab))
        
    if modo in ('facil', 'normal'):
        if eh_vencedor(tab, int_para_pedra(jog)):
            print ("VITORIA")
            return jog
        elif eh_vencedor(tab, int_para_pedra(-jog)):
            print ("DERROTA")
            return -jog
        else:
            print ("EMPATE")
            return pedra_para_int(cria_pedra_neutra())
    else:
        if eh_vencedor(tab, cria_pedra_branca()):
            print (f"VITORIA DO JOGADOR '{pedra_para_str(cria_pedra_branca())}'")
            return pedra_para_int(cria_pedra_branca())
        elif eh_vencedor(tab, cria_pedra_preta()):
            print (f"VITORIA DO JOGADOR '{pedra_para_str(cria_pedra_preta())}'")
            return pedra_para_int(cria_pedra_preta())
        else:
            print ("Empate")
            return cria_pedra_neutra()