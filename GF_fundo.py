'''
Created on May 1, 2012

@author: DiegoQueiroz
'''

from GF_parser import Parser
from datetime import date, timedelta

class Fundo(object):
    '''
    classdocs
    '''
    
    # Funds constant IDs
    FUNDS = {
        'FUNDO GERACAO FIA'                       : 1      ,
        #'FUNDO GF FGTS PETROBRAS'                 : 11     , #121497
        #'FUNDO GF FGTS VALE DO RIO DOCE'          : 12     , #123724
        'FUNDO GF DUQUE DE CAXIAS'                : 23800  ,
        'FUNDO GERACAO PROGRAMADO FIA'            : 152384 ,
        'FUNDO GF FIA MENINAS IRADAS'             : 156878 ,
        'FUNDO GERACAO FIC DE FI REFERENCIADO DI' : 202411 ,
        'FUNDO GF FIC RF CP'                      : 376240 ,
        'FUNDO GERACAO DIVIDENDOS FIA'            : 379869 ,
        'FUNDO GERACAO SELECAO FIA'               : 379877 ,
    }

    def __init__(self,fundid):
        '''
        Constructor
        '''
        if not isinstance(fundid,int):
            fundid = self.FUNDS.get(fundid,None)
        
        self.fundid     = fundid
        self.fundpage   = 'produtos.resultado_historico_cotas'
        self.prices     = dict() 
        
        
    def updatePrices(self,initialDate,endDate):
        
        parser = Parser()
        
        params = dict()
        params['id_fundo_clube']    = str(self.fundid)
        params['busca']             = 's'
        params['dataInicio']        = initialDate.strftime('%d/%m/%Y')
        params['dataFim']           = endDate.strftime('%d/%m/%Y')
        
        parser.getPage(self.fundpage, params)
        prices = parser.parsePage()
        
        self.prices.update(prices)
        

    def updateToday(self):

        if len(self.prices) >= 2:        
            ids = sorted(self.prices.keys(),reverse=True)[:2]
        
            self.prices[date.today()] = self.prices[ids[0]]
            self.prices[date.today() - timedelta(days=1)] = self.prices[ids[1]]
