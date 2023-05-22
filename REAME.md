## Instalando virtual enviroment

- Python 3.8
- Pip
  - Verificar se o gerenciador de pacote do python está instalado:
  ```
  $ pip -V
  ```
  - Caso não esteja instalado:
  ```
  $ sudo apt-get install python3-pip
  ```

- Virtual environment

  Instalando

	```
  $ sudo apt-get install -y python3-virtualenv
  ```

  ou

  ```
  $ sudo pip3 install virtualenv
  ```

  Criar venv

	```
  $ virtualenv venv
  ```

- Ativação e desativação
	```
  $ source venv/bin/activate
	$ source venv/bin/deactivate
  ```

  No Windows:
    ```
    $ python -m venv venv
    $ .\venv\Scripts\Activate.ps1
    ```

- Instalando as dependências

  ```
  $ pip install -r requirements.txt
  ```

## Controle de versões de banco de dados
você pode criar um repositório de migração com o seguinte comando:
```
$ flask db init
```
Isso adicionará uma pasta de migrações ao seu aplicativo. O conteúdo desta pasta precisa ser adicionado ao controle de versão junto com seus outros arquivos de origem.

Você pode então gerar uma migração inicial:
```
$ flask db migrate -m "Initial migration."
```

Em seguida, você pode aplicar as alterações descritas pelo script de migração ao seu banco de dados:
```
$ flask db upgrade
```****