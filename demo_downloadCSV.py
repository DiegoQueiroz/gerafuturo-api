'''
Created on May 4, 2012

@author: "DiegoQueiroz"
'''

from GF_fundo import Fundo
from datetime import date, timedelta
from csv import writer as csvwriter

if __name__ == '__main__':

    csv_delimiter  = ';'
    quote_char     = '"'
    interval       = 20 # years
    
    # Last 20 years interval
    iniDate = date.today() - timedelta(days= 365 * interval)
    endDate = date.today()

    for idfundo in Fundo.FUNDS:
        
        fundoatual = Fundo(idfundo)
        fundoatual.updatePrices(iniDate, endDate)
        
        data = [ ( [x] + y ) for x,y in fundoatual.prices.items() ]
        data = sorted(data,key=lambda x: x[0])
        
        with open(idfundo.replace(' ','_') + '.csv','wb') as f:
            arqcsv = csvwriter(f, delimiter=csv_delimiter,quotechar=quote_char)
            arqcsv.writerows(data)
            
        print("Download %s successful!" % ( idfundo ))
        
