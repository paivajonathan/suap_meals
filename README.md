# Como Executar Automaticamente via GitHub
## 1. Faça um Fork do Projeto
- No canto superior direito, clique no botão "Fork";
- Clique no botão verde para confirmar.
## 2. Configure as Credenciais do SUAP
- Tendo posse de seu próprio repositório, acesse o menu de "Settings", no centro da tela;
- Role para baixo até poder visualizar o item "Secrets and Variables" na barra da esquerda e clique nele;
- Clique na opção que irá aparecer, nomeada "Actions";
- No último tópico, de "Repository secrets", dois pares chave-valor, a partir do botão "New repository secret":
  1. **Name:** *SUAP_USERNAME* | **Secret:** *[sua_matricula_aqui]*
  1. **Name:** *SUAP_PASSWORD* | **Secret:** *[sua_senha_aqui]*
## 3. Por Fim, Aguarde a Execução
- O próprio GitHub executará o projeto automaticamente, **toda 1:00 da madrugada!**

<br>

# Como Executar Manualmente
## 1. Instale o Git no seu Computador
- Selecione a plataforma desejada nesse link: [Clique Aqui](https://git-scm.com/downloads);
- Clique em próximo até concluir a instalação.
## 2. Instale o Python no seu Computador
- Selecione a versão desejada nesse link: [Clique Aqui](https://www.python.org/downloads/);
- Selecione a opção de adicionar Python ao Path do sistema;
- Clique em próximo até concluir a instalação.
## 3. Crie a Pasta em que Deseja o Projeto
- Usando o Prompt de Comando, navegue até a pasta de desejo;
- Utilize `cd [nome_pasta]` para entrar numa pasta;
- Utilize `mkdir [nome_pasta]` para criar uma pasta;
- Crie de preferência uma pasta que não tenha espaços ou caracteres especiais, para evitar conflitos no Python.
## 4. Clone o Repositório para a Pasta
- Dentro da pasta, execute o comando `git clone https://github.com/paivajonathan/suap_meals.git .` para baixar o código do repositório. **Não esqueça do ponto no final!**
## 5. Execute o Script de Configuração do Projeto
- Execute o comando `setup.bat`, para configurar o ambiente de desenvolvimento/execução.
## 6. Configure o arquivo .env, de Variáveis de Ambiente
- Para a automação poder entrar na sua conta do suap, você precisa indicar qual a sua matrícula e senha;
- Não se preocupe, essas informações são utilizadas apenas por você.
## 7. Por fim, Execute o Projeto
- Execute o comando `run.bat` para executar o projeto.

