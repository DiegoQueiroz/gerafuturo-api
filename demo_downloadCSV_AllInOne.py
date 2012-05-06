'''
Created on May 4, 2012

@author: "DiegoQueiroz"
'''

from fundo import Fundo
from datetime import date, timedelta
from csv import writer as csvwriter

if __name__ == '__main__':

    csv_delimiter  = ';'
    quote_char     = '"'
    interval       = 20 # years
    
    # Last 20 years interval
    iniDate = date.today() - timedelta(days= 365 * interval)
    endDate = date.today()

    with open('FUNDOS.csv','wb') as f:

        arqcsv = csvwriter(f, delimiter=csv_delimiter,quotechar=quote_char)

        for idfundo in Fundo.FUNDS:
        
            fundoatual = Fundo(idfundo)
            fundoatual.updatePrices(iniDate, endDate)
            
            data = [ ( [idfundo, x] + y ) for x,y in fundoatual.prices.items() ]
            data = sorted(data,key=lambda x: x[1])
            
            arqcsv.writerows(data)
                
            print("Download %s successful!" % ( idfundo ))
        
