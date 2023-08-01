from random import sample
import random
import pandas as pd
import time

qtt_aviao = 7

class airport:
    def __init__(self,qtt_aviao=qtt_aviao):
        self.dummy = ''
        self.qtt_aviao = qtt_aviao
        
    def avioes(self,qtt_aviao):
        lista = []
        for i in range(1,qtt_aviao):
            lista.append(random.randint(1,qtt_aviao))
        lista.sort()
        return lista



    def combustivel(self,qtt_aviao):
        lista = []
        for i in range(1,qtt_aviao):
            lista.append(random.randint(1,7))
        lista.sort()
        return lista


    def condition(self,x):
        if x==7:
            return '100 min'
        elif x==6:
            return '70 min'
        elif x==5:
            return '60 min'
        elif x==4:
             return '40 min'
        elif x==3:
             return '30 min'  
        elif x==2:
             return 'baixo. Preparando para pousar'
        elif x==1:
             return 'muito baixo. Pousando....'
        else:
             return 'Avião em solo'

    def aviao_nome(self,x):
        if x==7:
            return 'BOEING 737'
        if x==6:
            return 'BOEING 352'
        if x==5:
            return 'BOEING 773'
        elif x==4:
            return 'BOEING 224'
        elif x==3:
            return 'Beluga 234'  
        elif x==2:
            return 'AirBus 344'
        else:
            return 'AirBus 123'

    def create(self):
        avioes = self.avioes(qtt_aviao)
        lista = self.combustivel(qtt_aviao)

        #
        df1 = pd.DataFrame({'avioes':avioes,
                            'nivel_comb':lista
                           })

        #
        df1['avioes']=df1['avioes'].apply(self.aviao_nome)

        #
        df1['tempo_voo'] = df1['nivel_comb'].apply(self.condition)

        #
        df1['tipo_voo'] = df1['avioes'].apply(lambda x: 'Carga' 
                                                     if 'Beluga 234' in x
                                                     else 'Comercial')

        return df1


    #
    def main(self):
        df = self.create()
        print('################# AEROPORTO DE URSAL - EXCLUSIVO PARA ESQUERDISTAS #################\n\n')
        for i in range(0,df['nivel_comb'].max()):
                         
                        df['nivel_comb'] = df['nivel_comb'].apply(lambda x: 0 if x<=0 else x-1)
                        df['tempo_voo'] = df['nivel_comb'].apply(self.condition)
                        for a in range(0,len(df['nivel_comb'])):
                            if df['nivel_comb'].iloc[-1] == 0:
                                print(f"o {df.iloc[a].avioes} está sem combustivel. {df.iloc[a].tempo_voo} ")
                                time.sleep(2)
                            else:
                                print(f"o {df.iloc[a].avioes} está com o nivel de combustivel {df.iloc[a].nivel_comb} e seu tempo de voo restante  é {df.iloc[a].tempo_voo} ")
                                time.sleep(2)
                        print("\n\n################# Atualização de status de aeronaves #################\n ")
                        if df['nivel_comb'].iloc[-1] == 0:
                            print('Aeroporto Fechado')
                            quest = input('gostaria de abrir o aeroporto novamente?:')
                            if quest == 'sim':
                                self.main()
                            else:
                                print('\n\nObrigado, companheiro(a). Até a próxima!')
                        else:
                            pass
                        time.sleep(2)
        return True
    
    
if __name__ == "__main__":
    udp = airport()
    udp.main()