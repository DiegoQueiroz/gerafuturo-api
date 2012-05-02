# -*- coding: utf-8 -*-
'''
Created on May 1, 2012

@author: "DiegoQueiroz"
'''

from xml.dom.minidom import parseString
from datetime import datetime
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
        
        strparams = urllib.urlencode(params)
        return self.portalurl + '?show=' + page + '&' + strparams
        
        
    def getPage(self,page,params):
        
        url = self.__buildURL(page,params)
        
        # Download URL, exception must propagate
        pageref = urllib.urlopen( url )
        self.page = pageref.read()
        
        # Get encoding and decode page
        encoding = pageref.headers['Content-type'].split('charset=')[1]
        self.page = self.page.decode(encoding)
        
        # Remove comments
        self.page = self.page.replace('<!--','').replace('-->','')
        
        return url
        
        
    def parsePage(self):
        
        content = dict()
        doc = parseString(self.page)

        for reg in doc.getElementsByTagName("tr"):
            values = list()
            for info in reg.getElementsByTagName("td"):
                if info.hasChildNodes() and info.childNodes[0].hasChildNodes():
                    values.append(str(info.childNodes[0].childNodes[0].nodeValue))
                    
            if len(values) >= 1:
                try:
                    values[0] = datetime.strptime(values[0],'%d/%m/%Y').date()
                except:
                    pass
                
                try:
                    values[1] = float(values[1].replace(',','.'))
                except:
                    pass
                
                content[values[0]] = values[1:] 
            else:
                # unknown registry
                pass
        
        return content
        
        

x = Parser()

params = dict()
params['id_fundo_clube'] = '1'
params['busca']          = 's'
params['dataInicio']     = '01/01/1900'
params['dataFim']        = '30/04/2012'

print(x.getPage('produtos.resultado_historico_cotas',params))
print(x.parsePage())


