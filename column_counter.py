def column_count(num_decimal):
    '''
    Function to convert a decimal number into
    a counter like Excel columns
    (ex: Decimal =>  1, 2, ..., 26, 27, ..., 52, 53, ..., 702, 703, ...
         Column  =>  A, B, ...,  Z, AA, ..., AZ, BA, ...,  ZZ, AAA, ...)
    '''
    # Variables
    n_dig = soma = 0
    base='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tamanho = len(base)
    digitos = []
    res_str = ''  
    # Verifiying number of digits
    while soma < num_decimal:
        n_dig += 1
        soma += tamanho ** n_dig
    # Calculating Digits
    for i in range(n_dig - 1, -1, -1):
        dig = num_decimal // (tamanho ** i)
        num_decimal = num_decimal % (tamanho ** i)
        digitos.append(dig)
    # Resolving the Zeroes
    for j in range(len(digitos) - 1, 0, -1):
        if digitos[j] <= 0:
            digitos[j] += tamanho
            digitos[j - 1] -= 1
    # Converting into string
    for char in digitos:
        res_str += base[char - 1]
    return res_str


for i in range(1,1000):
    print(f'{i:>4} => {column_count(i)}')