import os
import glob
import pandas as pd

def consolidar_dados_perf(pasta_origem, arquivo_saida):
    
    padrao_busca = os.path.join(pasta_origem, "*.csv")
    arquivos_csv = glob.glob(padrao_busca)
    
    if not arquivos_csv:
        print(f"Nenhum arquivo CSV encontrado na pasta: {pasta_origem}")
        return

    dados_consolidados = []

    
    for caminho_arquivo in arquivos_csv:
        nome_arquivo = os.path.basename(caminho_arquivo)
        
        
        linha = {
            'Arquivo': nome_arquivo,
            'Consumo Energia (Joules)': 0.0,
            'User Time (s)': 0.0,
            'System Time (s)': 0.0,
            'Duration Time (s)': 0.0,
            'CPU Time (s)': 0.0
        }
        
        try:
            with open(caminho_arquivo, 'r') as f:
                for texto_linha in f:
                    partes = texto_linha.strip().split(';')
                    
                    
                    if len(partes) < 3:
                        continue
                    
                    
                    val_str = partes[0].replace('.', '').replace(',', '.')
                    try:
                        valor = float(val_str)
                    except ValueError:
                        continue
                    
                    evento = partes[2].strip()
                    unidade = partes[1].strip()
                    
                    
                    if 'power/energy-pkg/' in evento:
                        linha['Consumo Energia (Joules)'] = valor
                    elif 'user_time' in evento:
                        
                        linha['User Time (s)'] = valor / 1e6 if unidade == 'ns' else valor * 1000
                    elif 'system_time' in evento:
                        linha['System Time (s)'] = valor / 1e6 if unidade == 'ns' else valor * 1000
                    elif 'duration_time' in evento:
                        linha['Duration Time (s)'] = valor / 1e6 if unidade == 'ns' else valor *1000
            
            
            linha['CPU Time (s)'] = linha['User Time (s)'] + linha['System Time (s)']
            
            dados_consolidados.append(linha)
            print(f"[OK] Processado: {nome_arquivo}")
            
        except Exception as e:
            print(f"Falha ao ler o arquivo {nome_arquivo}: {e}")

    
    df = pd.DataFrame(dados_consolidados)
    
    
    df = df.sort_values(by="Arquivo")
    
    
    df.to_csv(arquivo_saida, index=False, sep=';', decimal=',')
    
    print(f"\n{len(dados_consolidados)}")
    print(f"{arquivo_saida}")

pasta_dos_arquivos = 'C:\\Users\\arthu\\OneDrive\\Área de Trabalho\\PROGRAMAS\\Python\\projeto_benchmark\\dados_csv\\selection_v2\\50000' 


nome_do_arquivo_final = 'selection_v2_50000.csv'

consolidar_dados_perf(pasta_dos_arquivos, nome_do_arquivo_final)