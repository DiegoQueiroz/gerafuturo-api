'''
Created on May 1, 2012

@author: "DiegoQueiroz"
'''

import urllib

class Parser(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.portalurl = 'https://online.gerafuturo.com.br/onlineGeracao/PortalManager'
        self.page = None
        
        
    def __buildURL(self,page,params):
        # 'show' must always be the first parameter
        
        strparams = '&'.join([ key + '=' + params[key] for key in params ])
        return self.portalurl + '?show=' + page + '&' + strparams
        
        
    def getPage(self,page,params):
        
        url = self.__buildURL(page,params)
        
        # FIXME: remove this
        print(url)
        
        # Download URL, exception must propagate
        self.page = urllib.urlopen( url ).read()
        
    def parsePage(self):
        
        content = dict()
        
        # TODO: parse page to extract content
        
        return content
        
        

x = Parser()

params = dict()
params['id_fundo_clube'] = '1'
params['busca']          = 's'
params['dataInicio']     = '01/01/1900'
params['dataFim']        = '01/05/2012'

x.getPage('produtos.resultado_historico_cotas',params)
cont = x.parsePage()

print(cont)
