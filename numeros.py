class glifos:
    def __init__(self):
        self.num=[]
        #self.dicc={}
        self.lista=[]
        self.inicio=1
        self.fin=10
        self.diccF={}
        self.dicc={
            1:'Σ',
            5:'Λ',
            10:'Ω',
            50:'Δ',
            100:'Φ',
            500:'Ψ',
            1000:'Ξ'
        }
   
    def cargar(self,ruta):

        with open(ruta,"r") as f:
            for linea in f:
                linea=linea.strip()
                if linea=='0':
                    break
                else:
                    if linea.isdigit():
                        self.num.append(int(linea))
                    else:
                        self.num.append(linea)

    def procesar(self):
        for numero in self.num:
            if isinstance(numero,str):
                self.diccF[numero]='ERROR: Formato de entrada inválido. No es un número entero positivo'
                
            else:
                if numero<4000 and numero>=1:
                    cont=1
                    self.inicio=1
                    self.fin=10
                    self.lista=[]
                    self.dividir(numero,cont)
                    self.diccF[numero]=self.lista
                    
                else:
                   self.diccF[numero]=' ERROR: Número fuera de rango (1-3999)'
                   
            

    def dividir(self,n,cont):

        if n==0:
            self.lista.reverse()
            return 
        
        valor=10**cont
        npicado=n%valor
        cont+=1

        if npicado !=0:
            self.transformar(npicado)

        n=n-npicado
        self.inicio=self.fin
        self.fin=self.fin * 10
        self.dividir(n,cont)
        n=0


    def transformar(self,n):

        if n==0:
            return
        
        if n in self.dicc:
            self.lista.append(self.dicc[n])
        
        else:
            for clave in self.dicc:
                if self.inicio<=clave<=self.fin:
                    if self.inicio*9==n or self.inicio*4==n:
                        if clave>n:
                            self.lista.append(self.dicc[clave])
                            self.lista.append(self.dicc[self.inicio])
                            break
                        
                    else:
                        if clave<n :
                            n=n-clave
                            self.lista.append(self.dicc[clave])
                            self.transformar(n)
                            break
    
    def getRespuesta(self):
        return self.diccF
        
a=glifos()
#a.cargar()
#a.procesar()
#a.getRespuesta()

