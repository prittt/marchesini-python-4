import re

def is_date_v1(s: str) -> bool:
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    return bool(re.match(pattern, s))

def is_date_v2(s: str) -> bool:
    # Verifica se la lunghezza è corretta
    if len(s) != 10:
        return False
    
    # Verifica se i separatori sono corretti
    if s[2] != '/' or s[5] != '/':
        return False
    
    # Verifica se giorno, mese e anno sono numeri
    giorno = s[:2]
    mese = s[3:5]
    anno = s[6:]
    
    if not (giorno.isdigit() and mese.isdigit() and anno.isdigit()):
        return False
    
    # Converte in interi
    giorno, mese, anno = int(giorno), int(mese), int(anno)
    
    # Controlla validità dei valori
    if not (1 <= mese <= 12):
        return False
    if not (1 <= giorno <= 31):
        return False
    if anno < 1000 or anno > 9999:
        return False
    
    return True


print(is_date_v1("10/07/2015")) 
print(is_date_v1("56/07/2015")) 
print(is_date_v1("10-7-15"))     
print(is_date_v1("10.07.2015"))  
print(is_date_v1("1/07/2015"))   
print(is_date_v1("10/7/2015"))   
print(is_date_v1("10/07/15"))    

print(is_date_v2("10/07/2015")) 
print(is_date_v2("56/07/2015")) 
print(is_date_v2("10-7-15"))     
print(is_date_v2("10.07.2015"))  
print(is_date_v2("1/07/2015"))   
print(is_date_v2("10/7/2015"))   
print(is_date_v2("10/07/15"))    
