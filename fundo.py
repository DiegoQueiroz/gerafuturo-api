'''
Created on May 1, 2012

@author: DiegoQueiroz
'''

from parser import Parser
#from datetime import date

# Funds constant IDs
FUNDO_GERACAO_FIA                       = 1 
FUNDO_GF_FGTS_PETROBRAS                 = 11 
FUNDO_GF_FGTS_VALE_DO_RIO_DOCE          = 12
FUNDO_GF_DUQUE_DE_CAXIAS                = 23800 
FUNDO_GERACAO_PROGRAMADO_FIA            = 152384
FUNDO_GF_FIA_MENINAS_IRADAS             = 156878
FUNDO_GERACAO_FIC_DE_FI_REFERENCIADO_DI = 202411 
FUNDO_GF_FIC_RF_CP                      = 376240
FUNDO_GERACAO_DIVIDENDOS_FIA            = 379869
FUNDO_GERACAO_SELECAO_FIA               = 379877

class Fundo(object):
    '''
    classdocs
    '''

    def __init__(self,fundid):
        '''
        Constructor
        '''
        self.fundpage = 'produtos.resultado_historico_cotas'
        
        
    def updatePrices(self,initialDate,endDate):
        
        parser = Parser()
        
        params = dict()
        params['id_fundo_clube']    = str(self.fundid)
        params['busca']             = 's'
        params['dataInicio']        = initialDate.strftime('%d/%m/%Y')
        params['dataFim']           = endDate.strftime('%d/%m/%Y')
        
        parser.getPage(self.fundpage, params)
        prices = parser.parsePage()
        
        # TODO: update values with the ones provided
        
        
        