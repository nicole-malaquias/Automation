import os

# Obtém o diretório atual onde o script está sendo executado
path_download = os.getcwd()

# Define o diretório de destino (Downloads)
download_dir = 'Downloads'

# Muda para o diretório de downloads
os.chdir(download_dir)

# Obtém o diretório atual (Downloads)
atual = os.getcwd()

# Lista todos os arquivos no diretório de downloads
list_arch = os.listdir()

# Lista de extensões únicas
extensao = [i.split('.')[-1] for i in list_arch if len(i.split('.')) > 1 and i.split('.')[-1] != "py"]

# Cria diretórios para cada extensão
for i in extensao:
    if not os.path.exists(os.path.join(atual, i)):
        os.mkdir(os.path.join(atual, i))

# Move os arquivos para os diretórios correspondentes
for i in list_arch:
    if len(i.split('.')) > 1 and i.split('.')[-1] != "py":
        ext = i.split('.')[-1]
        full_path = os.path.join(atual, ext, i)
        os.rename(os.path.join(atual, i), full_path)

# Retorna ao diretório original
os.chdir(path_download)
