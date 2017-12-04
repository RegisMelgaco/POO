def primo(numero):
    try:
        if(numero != 1):
            i=2
            while(i < numero):
                if(numero % i == 0):
                    raise Exception
                i += 1
            print("é primo")
        else:
            print("é de primo")
    except:
        print("Exceção: o numero escolhido não é primo")
