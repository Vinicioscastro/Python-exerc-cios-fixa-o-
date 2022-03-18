
#SIMPLEX, METODO TO SOLVE, PROGRAMAÇÃO LINEAR, IMPLEMENTADO O BIG M
#  biblioteca externa: Numpy
# Tutorial de: David Toro Meneses
# ALUNO: VINICIOS PEREIRA DA COSTA CASTRO



import numpy as np
import warnings


def simplex(type, A, B, C, D, M):
    """Calcula um ponto ideal para o modelo de programação linear dado por A * x <= B, Otimizar z = C '* x
    Argumentos:
    tipo - tipo de otimização, pode ser 'max' ou 'min'
    A - Uma matriz do modelo (matriz numpy)
    B - Matriz B do modelo, vetor coluna (matriz numpy)
    Matriz C - C do modelo, vetor coluna (matriz numpy)
    D - vetor coluna com os tipos de restrições do modelo (matriz numpy), 1 é <=, 0 é =, -1 é> =
            para <= restrições não faça nada
            para = restrições adicione variáveis ​​artificiais e um grande M no objetivo
            função (min -> + M, max -> -M)
            para> = restrições, multiplique por -1
    M - grande valor M
    """

    # m - número de restrições
    # n - número de variáveis
    (m, n)= A.shape

    basic_vars = []
    count = n

    # matriz com novas variáveis
    R = np.eye(m)

    # valores das novas variáveis
    P = B

    # indicador de posição de variáveis ​​artificiais
    artificial= []

    for i in range(m):
        if D[i] == 1:
            # adicione a variável slack à função objetivo
            C = np.vstack((C, [[0]]))
            
            # registra a variável de folga como variável básica
            count = count + 1
            basic_vars = basic_vars + [count-1]

            artificial = [artificial, 0]

        elif D[i] == 0:
            # adicione a variável artificial à função objetivo com o grande valor M
            if type == 'min':
                C = np.vstack((C, [[M]]))
            else:
                C = np.vstack((C, [[-M]]))

           
            # registrar a variável artificial como variável básica
            count = count + 1
            basic_vars = basic_vars + [count-1]

            artificial = [artificial, 1]
        elif D[i] == -1:
            # adicione as variáveis ​​excedentes e artificiais à função objetivo
            if type == 'min':
                C = np.vstack((C, [[0], [M]]))
            else:
                C = np.vstack((C, [[0], [-M]]))

            R = repeatColumnNegative(R, count + 1 - n)
            P = insertZeroToCol(P, count + 1 - n)

            # registrar a variável artificial como variável básica
            count = count + 2
            basic_vars = basic_vars + [count-1]

            artificial = [artificial, 0, 1]
        else:
            print("invalid case")

    # vértice atual
    X = np.vstack((np.zeros((n, 1)), P))

    # adicionar novas variáveis ​​à matriz A
    A = np.hstack((A, R))

    # simplex tableau
    st = np.vstack((np.hstack((-np.transpose(C), np.array([[0]]))), np.hstack((A, B))))

    # numero de colunas
    (rows, cols) = st.shape

    # basic_vars = ((n + 1):n+m)'

    print('\nsimplex tableau\n')
    print(st)
    print('\nvariaveis basicas atuais\n')
    print(basic_vars)
    print('\nponto otimo\n')
    print(X)

    # verifique se z! = 0 (quando existem variáveis ​​artificiais)
    z_optimal = np.matmul(np.transpose(C), X)

    print('\nZ atual\n\n', z_optimal)

    if z_optimal != 0:
        for i in range(m):
            if D[i] == 0 or D[i] == -1:
                if type == 'min':
                    st[0,:]= st[0,:] + M * st[1+i,:]
                else:
                    st[0,:]= st[0,:] - M * st[1+i,:]

        print('\nsimplex tableau corrigido\n')
        print(st)

    iteration = 0
    while True:
    # for zz in range(2):
        if type == 'min':
            # select the more positive value
            w = np.amax(st[0, 0:cols-1])
            iw = np.argmax(st[0, 0:cols-1])
        else:
            # select the more negative value
            w = np.amin(st[0, 0:cols-1])
            iw = np.argmin(st[0, 0:cols-1])

        if w <= 0 and type == 'min':
            print('\nponto otimo global\n')
            break
        elif w >= 0 and type == 'max':
            print('\nponto otimo global\n')
            break
        else:
            iteration = iteration + 1

            print('\n----------------- interacao {} -------------------\n'.format(iteration))

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                T = st[1:rows, cols-1] / st[1: rows, iw]

            R = np.logical_and(T != np.inf, T > 0)
            (k, ik) = minWithMask(T, R)

            # Z atual da linha
            cz = st[[0],:]

            # elemento pivô
            pivot = st[ik+1, iw]

            # linha pivô dividida por elemento pivô
            prow = st[ik+1,:] / pivot

            st = st - st[:, [iw]] * prow

            # linha pivô é um caso especial
            st[ik+1,:]= prow

            # nova variavel basica
            basic_vars[ik] = iw

            print('\nVariavel basica atual\n')
            print(basic_vars)

            # novo vertice
            basic = st[:, cols-1]
            X = np.zeros((count, 1))

            t = np.size(basic_vars)

            for k in range(t):
                X[basic_vars[k]] = basic[k+1]

            print('\nponto ótimo atual\n')
            print(X)

            # novo valor de Z
            C = -np.transpose(cz[[0], 0:count])

            z_optimal = cz[0, cols-1] + np.matmul(np.transpose(C), X)
            st[0, cols-1] = z_optimal

            print('\nsimplex tableau\n\n')
            print(st)

            print('\nZ atual\n\n')
            print(z_optimal)

    # verifique se alguma variável artificial é positiva (solução inviável)
    tv = np.size(artificial)
    for i in range(tv):
        if artificial[i] == 1:
            if X[n + i] > 0:
                print('\nsolução inviável\n')
                break

    return (z_optimal[0, 0], X)


def minWithMask(x, mask):

    min = 0
    imin = 0

    n = np.size(x)

    for i in range(n):
        if mask[i] == 1:
            if min == 0:
                min = x[i]
                imin = i
            else:
                if min > x[i]:
                    min = x[i]
                    imin = i

    return (min, imin)


def repeatColumnNegative(Mat, h):
    """Repita a coluna h multiplicada por - 1"""
    (r, c) = Mat.shape
    Mat = np.hstack((Mat[:, 0:h-1], -Mat[:, [h-1]], Mat[:, h-1:c]))

    return Mat


def insertZeroToCol(col, h):
    """insira zero na coluna"""
    k = np.size(col)
    col = np.vstack((col[0:h-1, [0]], np.array([[0]]), col[h-1:k, [0]]))

    return col


if __name__ == '__main__':
    np.set_printoptions(suppress=True)

    '''(z, x) = simplex('min', np.array([[3, 1], [4, 3], [1, 2]]),
                            np.array([[3], [6], [4]]),
                            np.array([[4], [1]]),
                            np.array([[0], [-1], [1]]),200)
  
    (z, x) = simplex('min', np.array([[2, 1], [1, 2], [1, 3]]),
                            np.array([[16], [11], [15]]),
                            np.array([[300], [500]]),
                            np.array([[0], [-1], [1]]),10000)

    (z, x) = simplex('min', np.array([[1, 2], [-1, 1], [-2, -4]]),
                            np.array([[4], [1], [0]]),
                            np.array([[-2], [-4]]),
                            np.array([[0], [-1], [1]]),400)
    ''' 
    (z, x) = simplex('min', np.array([[3, 6], [4, 2]]),
                            np.array([[60], [32]]),
                            np.array([[20], [24]]),
                            np.array([[0], [-1], [1]]),200)
    
    
