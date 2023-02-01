# cpfgen
Scrape to cpf generator website.

This project uses as base [this page](https://www.4devs.com.br/gerador_de_cpf). It just turns it easier to get Brazilian taxpayer registry (CPF). Feel free to modify the project!

## How To Run It
Run pip install requirements.txt to install dependencies.

### Alias
A greate way to use this is setting a function in an alias file, so you can call it from your terminal. You can do it creating a file called ~/.bash_aliases and in it you can add the following.

```
alias cpfgen='cpfgen'
cpfgen() {
    cd path-to-file
    python app.py
}
```
