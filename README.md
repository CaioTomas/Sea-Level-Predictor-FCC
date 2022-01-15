## English description

This is a repo with my solution to the *Sea Level Predictor* project for the **Data Analysis with Python** course from freeCodeCamp. Portuguese description is down below.

### Assignment

You will anaylize a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

Use the data to complete the following tasks:

* Use Pandas to import the data from `epa-sea-level.csv`.
* Use matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axis.
* Use the `linregress` function from `scipy.stats` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
* Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
* The x label should be "Year", the y label should be "Sea Level (inches)", and the title should be "Rise in Sea Level".

Unit tests are written for you under `test_module.py`.

### Development

For development, you can use `main.py` to test your functions. Click the "run" button and `main.py` will run.

### Testing 

We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.

### Data Source
Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.
https://datahub.io/core/sea-level-rise

------------------------------------------------------------------------------------------------------------------------

## Descrição em portugês

Esse é o repositório com a minha solução para o projeto *Sea Level Predictor* do curso **Data Analysis with Python** do freeCodeCamp. A tradução é livre e feita por mim.

### Tarefa

Você irá analisar o dataset de mudança média global no nível do mar desde 1880 e usá-lo para prever a mudança no nível do mar até o ano 2050.

Use os dados para completar as seguintes tarefas:

* Use Pandas para importar os dados de `epa-sea-level.csv`.
* Use matplotlib para criar um scatter plot usando a coluna "Year" no eixo x e a coluna "CSIRO Adjusted Sea Level" no eixo y.
* Use a função `linregress` de `scipy.stats` para pegar a inclinação e o y-intercept da reta de melhor ajuste. Plote a reta de melhor ajuste sobre o scatter plot. Faça a reta passar pelo ano 2050 para predizer o aumento no nível do mar em 2050.
* Plote uma nova reta de melhor ajuste usando os dados de 2000 até o ano mais recente no dataset. Faça a reta passar por 2050 para prever o aumento no nível do mar se a taxa a partir de 2000 se mantiver.
* O label do eixo x deve ser "Year", e o do eixo y deve ser "Sea Level (inches)", e o título deve ser "Rise in Sea Level".

Testes unitários foram escritos para você em `test_module.py`.

### Desenvolvimento

Escreve seu código em `prob_calculator.py`. Para desenvolvimento, use `main.py` para testar o código. Clique em "run" `main.py` rodará.

### Testando 

Os testes unitários para este projeto estão em `test_module.py`. Importamos os testes de `test_module.py` para `main.py` por conveniência. Os teste vão rodar automaticamente quando clicar em "run".

### Submissão

Copie a URL do projeto e submeta-a ao freeCodeCamp.

### Fonte dos dados
Global Average Absolute Sea Level Change, 1880-2014 da Agência de Proteção Ambiental dos EUA usando dados de CSIRO, 2015; NOAA, 2015.
https://datahub.io/core/sea-level-rise
