# Instruções para Agendar a Execução Automática do Script no Cron

Este guia fornece instruções passo a passo sobre como agendar a execução automática de um script Python no Cron, um agendador de tarefas em sistemas Unix-like. Isso permitirá que você execute o seu script periodicamente em horários específicos.

## Pré-requisitos

- Certifique-se de que o Python esteja instalado no seu sistema.
- Tenha o script Python que deseja agendar em seu diretório.

## Passo 1: Abra o Terminal

Abra um terminal ou console no seu sistema.

## Passo 2: Abra o Crontab para Edição

Digite o seguinte comando no terminal para abrir o crontab para edição:

```bash
crontab -e

Isso abrirá o crontab em um editor de texto padrão, geralmente o vi ou nano.

Passo 3: Agende a Execução do Script
Adicione uma linha ao arquivo crontab para agendar a execução do seu script. A sintaxe geral é a seguinte:

bash
Copy code
* * * * * comando_a_ser_executado
Os cinco asteriscos representam, respectivamente, os minutos, as horas, os dias do mês, os meses e os dias da semana em que o script será executado. Você pode personalizar esses valores de acordo com suas necessidades.
Por exemplo, para executar o seu script todos os dias às 2 da manhã, você pode adicionar a seguinte linha:

bash
Copy code
0 2 * * * /usr/bin/python3 /caminho/completo/para/seu_script.py
Certifique-se de substituir /caminho/completo/para/seu_script.py pelo caminho completo para o seu script Python.

Passo 4: Salve e Saia
Depois de adicionar a linha ao crontab, salve e saia do editor de texto de acordo com as instruções do seu editor.

No vi, você pode pressionar Esc, digitar :wq e pressionar Enter.
No nano, você pode pressionar Ctrl + O, pressionar Enter e, em seguida, pressionar Ctrl + X.
Passo 5: Verifique a Lista de Tarefas Cron
Para verificar se a tarefa foi adicionada corretamente, digite o seguinte comando no terminal:

bash
Copy code
crontab -l