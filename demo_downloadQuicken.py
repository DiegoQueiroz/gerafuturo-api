# -*- coding: utf-8 -*-

from GF_fundo import Fundo
from datetime import date, timedelta
from csv import writer as csvwriter
import sys

# Output file format:
#
#   QUOTE , DATE , VALUE, VOLUME


if __name__ == '__main__':

    csv_delimiter  = ','
    quote_char     = '"'
    try:
        interval   = int(sys.argv[1]) # days
    except:
        interval   = 90 # days
    
    # Last 20 years interval
    iniDate = date.today() - timedelta(days=interval)
    endDate = date.today()

    with open('FUNDOS_GF_QUICKEN.csv','wb') as f:

        arqcsv = csvwriter(f, delimiter=csv_delimiter,quotechar=quote_char)

        for idfundo in Fundo.FUNDS:
        
            fundoatual = Fundo(idfundo)
            fundoatual.updatePrices(iniDate, endDate)        
            fundoatual.updateToday()    
            
            data = [ ( [ 'GF_' + str(Fundo.FUNDS[idfundo]), qdate.strftime("%d/%m/%Y"), qvalue, qvolume] )
                    for qdate,(qvalue,qvolume) in fundoatual.prices.items() ]
            
            arqcsv.writerows(data)
                
            print("Download %s successful!" % ( idfundo ))
        