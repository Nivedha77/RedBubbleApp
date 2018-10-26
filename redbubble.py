import json, pandas as pd, sys

def getPrice(in_pType, in_size, in_col) :

    for i, row in df_P[df_P['product-type'] == in_pType].iterrows():
        if in_pType == 'hoodie' :
           d_siz = row.options['size']
           d_col = row.options['colour']
           if in_col in d_col and in_size in d_siz : return(row['base-price'])
        elif in_pType == 'sticker' :
           d_siz = row.options['size']
           if in_size in d_siz : return(row['base-price'])
        elif in_pType == 'leggings' : return(row['base-price'])

#------------------------------------------
# Main Function
#------------------------------------------
if __name__ == '__main__':

   if len(sys.argv) != 3:
      print( "Missing json files. \n Sytanx: redbubble.py <cart>.json <baseprice>.json")
      exit()

   global df_P, df_C 

   df_P = pd.read_json(sys.argv[2])
   df_C = pd.read_json(sys.argv[1])

   xtotal_price = 0
   for i, row in df_C.iterrows():
       
       crtPType   = row['product-type']
       crtIQty    = row['quantity']
       crtIMarkup = row['artist-markup']

       crtIColour = ''
       crtISize   = ''
       if crtPType  == 'hoodie' :  
          crtIColour = row['options']['colour']
          crtISize   = row['options']['size']
       elif crtPType  == 'sticker' :  
          crtISize   = row['options']['size']
	 
       xbase_price = getPrice(crtPType, crtISize, crtIColour)
       xtotal_price += (xbase_price + round(xbase_price*(crtIMarkup/100)))*crtIQty

   print(xtotal_price)
