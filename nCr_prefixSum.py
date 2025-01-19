        fact = [0]*(n+1)
        infact = [0]*(n+1)
        fact[0] = 1
        for i in range(1,n+1):
            fact[i] = i*fact[i-1] % M
            
        infact[-1] = pow(fact[n], M-2, M)
        for i in range(n-1, -1, -1):
            infact[i] = (i+1)*infact[i+1] %M

        pref = [0]*(n+1)
        #from [0,n]
        for i in range(0,n+1):
            #from [0, min(k, i)]
            for j in range(min(i+1, k+1)):
                #iCj
                a = fact[i]
                b = infact[j]
                c = infact[i-j]
                res = a*(b*c%M)%M
                pref[i]+= a*(b*c%M)%M
