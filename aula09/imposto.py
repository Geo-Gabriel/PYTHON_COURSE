def calculo_inss(salario):

    if (salario > 0 and salario <= 1751.81):
        inss = salario * 0.08
    elif salario > 1751.81 and salario <= 2919.72:
        inss = salario * 0.095
    elif salario > 2919.72 and  salario <= 5839.45:
        inss = salario * 0.11
    else:
        inss = 642.34
    return inss

def calculo_irrf(salario,inss):
    
    if (salario > 1903.98 and salario <= 2826.65):
        irrf = ((salario - inss)-142.90) * 0.075
    elif salario > 2826.66 and salario <= 3751.05:
        irrf = ((salario - inss)-354.80) * 0.15
    elif salario > 3751.05 and  salario <= 4664.68:
        irrf = ((salario - inss)-636.13) * 0.225
    elif salario > 4664.68:
        irrf = ((salario - inss)-869.36) * 0.275
    return irrf