import pandas as pd
        
simp = pd.read_html('https://es.wikipedia.org/wiki/Anexo:Episodios_de_Los_Simpson')
print(simp[1])