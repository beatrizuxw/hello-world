# 🤖 Ferramenta de otimização de FAQs com IA Generativa

Olá! Este repositório contém o código de uma ferramenta em Python criada para ajudar a otimizar a revisão de FAQs, identificando e gerenciando conteúdos duplicados ou muito similares.

A proposta é tornar a **tecnologia mais clara, intuitiva e humana**, utilizando a IA para resolver desafios práticos do dia a dia.

---

## 💡 Por que esta ferramenta?

A ideia surgiu de uma necessidade real durante a migração das nossas FAQs para a SmartContent: agilizar a identificação de conteúdos repetidos ou muito parecidos. Isso evita que a base de conhecimento fique poluída e que a IA tenha dificuldade em entregar a resposta mais precisa para a pessoa usuária.

### Como funciona?

* Lê arquivos Excel.
* Identifica temas duplicados ou similares.
* Oferece opções de ação (como visualizar ou remover as duplicações).
* **Importante:** Nunca altera o arquivo original! Todas as mudanças são feitas em uma nova versão, mantendo a integridade dos seus dados.

---

## ⚙️ O Processo de Criação (com IA Generativa!)

Este projeto foi desenvolvido com o apoio de IA generativa, usando apenas linguagem natural para "programar"!

1.  **Definição do Problema:** Identificar e consolidar temas únicos em bases de dados, eliminando redundâncias.
2.  **Elaboração do Prompt com IA:** Usei diferentes chats de IA para refinar as instruções, detalhando funcionalidades e expectativas. O objetivo era ter um prompt claro e bem estruturado.
3.  **Geração e Aprimoramento do Código:** A IA gerou a primeira versão do código em Python. Após testes e ajustes, voltei para a IA com feedback, e na segunda tentativa, a ferramenta já estava funcionando perfeitamente! 🚀

---

## 🚀 Comece a Usar!

Mesmo que você não seja expert em tecnologia, criei um guia simples para te ajudar a rodar a ferramenta. Se eu consegui, você também consegue! 😉

### Pré-requisitos

* Ter o Python instalado no seu computador.

### Guia para Iniciantes

1.  **Instalar o Python:**
    * Acesse: [https://www.python.org/downloads/](https://www.python.org/downloads/)
    * Clique no botão verde “Download Python”.
    * **Muito importante:** Marque a opção “**Add Python to PATH**” durante a instalação.
    * Siga as etapas: `Next` → `Next` → `Install`.

2.  **Verificar a Instalação do Python:**
    * Abra o **Prompt de Comando**:
        * No Windows: Pressione `Win + R`, digite `cmd` e `Enter`.
        * Ou pesquise por `cmd` no menu Iniciar.
    * Digite: `python --version`
    * Se aparecer algo como `Python 3.x.x` (ex: `Python 3.11.0`), deu tudo certo! ✅

3.  **Crie a Pasta e Salve o Código:**
    * Crie uma nova pasta no seu computador (ex: `MeuProcessadorExcel`).
    * Abra um editor de texto simples (como Bloco de Notas ou VS Code).
    * Cole o código da ferramenta (que estará no arquivo `app_excel.py` neste repositório).
    * Salve o arquivo dentro da pasta que você criou com o nome `app_excel.py`.
        * **Atenção:** O nome do arquivo precisa terminar com `.py` e o tipo deve ser "Todos os arquivos" ou "All Files".

4.  **Instale as Bibliotecas Necessárias:**
    * Abra o **Prompt de Comando** **DENTRO** da pasta que você criou.
        * Para fazer isso facilmente: navegue até a pasta no explorador de arquivos, segure a tecla `Shift`, clique com o botão direito em um espaço vazio dentro da pasta e selecione “Abrir janela de comando aqui” (ou similar).
    * Digite os comandos abaixo, um por vez, e pressione `Enter` após cada um:
        ```bash
        pip install streamlit
        pip install pandas
        pip install openpyxl
        ```

5.  **Rode a Ferramenta:**
    * No mesmo Prompt de Comando, digite:
        ```bash
        streamlit run app_excel.py
        ```
    * Isso vai abrir a ferramenta automaticamente no seu navegador padrão! 🎉

### 🆘 Se algo der errado...

* **`'python' não é reconhecido`**:
    * Provavelmente, você não marcou "Add Python to PATH" durante a instalação. Tente reinstalar o Python e marque essa opção.
* **`'pip' não funciona`**:
    * Tente este comando alternativo para instalar as bibliotecas:
        ```bash
        python -m pip install streamlit
        python -m pip install pandas
        python -m pip install openpyxl
        ```
---

**🔗 Acesse aqui o prompt e o código completo da ferramenta:**
https://github.com/beatrizuxw/hello-world/blob/main/app_excel.py 
https://github.com/beatrizuxw/hello-world/blob/main/prompt.txt
