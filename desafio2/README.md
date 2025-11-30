# Desafio 2 – Volumes e Persistência

Neste desafio é usado SQLite para mostrar como um volume Docker mantém os dados mesmo depois que o container é removido.

## Como rodar

```bash
cd desafio2
docker volume create desafio2-data
docker build -t desafio2-sqlite .
docker run --rm -v desafio2-data:/data desafio2-sqlite
```

Cada vez que o container é executado, um novo registro é gravado no banco e a lista completa é exibida.  
Mesmo recriando o container, o arquivo `/data/desafio2.sqlite` continua armazenado no volume.
