# cpfgen
Scrape to cpf generator website and copy it to clipboard.

This project uses as base [this page](https://www.4devs.com.br/gerador_de_cpf). It just turns it easier to get Brazilian taxpayer registry (CPF). Feel free to modify the project!

## How To Run It
Run pip install requirements.txt to install dependencies.

### Alias
A greate way to use this is setting a function in an alias file, so you can call it from your terminal. You can do it creating a file called ~/.bash_aliases and in it you can add the following.

```python
alias cpfgen='cpfgen'
cpfgen() {
    cd path-to-file
    python app.py
}
```

### Preview
[![Video Preview](https://user-images.githubusercontent.com/30248076/224189846-24e607fe-dd80-4661-a3c0-a867a852acfb.png)](https://user-images.githubusercontent.com/30248076/224191541-6d81721a-4a86-44b3-a8b4-f669ad9fd002.mp4)

Notice that the returned value automatically goes to my clipboard. So, when I press Ctrl + v, there it is. :)
