# ENEL-Automatization
Projeto que usa selenium-webdriver para automatizar a geração de boletos bancarios a do site da ENEL.
# Instruções para instalação:
. Faça o download do diretório do projeto e extraia todos os arquivos necessários.
. É necessario ter python3 instalado no computador, e ter tanto o python como o PIP (package manager) adicionados ao PATH do sistema operacional. Abra o terminal e digite os comandos "python --version" e "pip --version". Caso esteja tudo ok, você deve ver mensagens do tipo:

$python --version
Python 3.7.7
$pip --version
pip 20.0.2

OBS: Os numeros das versoes nao precisam ser exatamente esses, mas é importante garantir que a versao do python é da forma 3.x.x

Para mais informações sobre como baixar o python e adicionar ambos ao PATH do sistema operacional, verificar o tutorial abaixo:
https://phoenixnap.com/kb/how-to-install-python-3-windows (windows)

. É necessario também fazer o download do chromedriver. Esse é um driver do google chrome que vai ser usado no processo de automatização. Primeiro verifique no seu google chrome browser qual versão está sendo usada, e entao use o link https://sites.google.com/a/chromium.org/chromedriver/downloads para baixar o driver correspondente a sua versão. Caso tenha dificuldades em descobrir qual versão do chrome esta usando, use o seguinte link https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have. 

. Após o download do driver, adicione novamente o caminho do arquivo ao PATH do sistema operacional.
Para garantir que está tudo ok, abra o terminal, digite o seguinte comando, e verifique se a resposta esta parecida:

$chromedriver
Starting ChromeDriver 83.0.4103.39 (...) on port xxxx
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.

. Agora estamos praticamente no final do processo. Abra o terminal e vá para o diretorio do projeto baixado no primerio passo. Digite o seguinte comando para instalar as dependências finais:

$pip install -r requirements.txt

. Povoe o arquivo clientes.csv com os clientes que voce deseja extrair os boletos, usando o formato csv indicado no cabeçalho do arquivo.

Exemplo de arquivo correto com 2 clientes:
Numero do Cliente,CNPJ
0000000,12345678912345
1111111,98765421987654

. Agora podemos rodar o proejto. Basta usar o seguinte comando:
$python main.py

E o boleto para todos os clientes será gerado e guardado na pasta "/boletos_pdf/" no formato numerocliente-cnpj.pdf
 
. Aguarde novas versões para um produto mais completo...
