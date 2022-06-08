#adar katzir 209502293
def neville(datax, datay, x):

    n = len(datax)
    p = n*[0]
    for k in range(n):
        iteration = k
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
            else:
                p[i] = ((x-datax[i+k])*p[i]+ \
                        (datax[i]-x)*p[i+1])/ \
                        (datax[i]-datax[i+k])
                print(f"polimnoial {i},{iteration}={p[i]:.5f}")
            if(k+1 != n):
                print('\n ***********'+ str(k+1) + 'iteration***************** ')
    print("\nF("+str(x)+')')
    return p[0]
datax = [0.35,0.4,0.55,0.65,0.7,0.85,0.9]
datay = [-213.5991,-204.4416,-194.9375,-185.0256,-174.6711,-163.8656,-152.6271]
print(neville(datax,datay,0.75))