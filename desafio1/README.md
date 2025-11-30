# Desafio 1 – Containers em Rede

Este desafio usa dois containers conversando pela mesma rede Docker:

- `server`: aplicação Flask na porta 8080.
- `client`: script em shell que chama o servidor usando `curl` em loop.

## Como rodar

```bash
cd desafio1
./run.sh
```

O script cria a rede `desafio1-net`, constrói as imagens e sobe os dois containers.  
No terminal do cliente é possível ver as respostas HTTP que o servidor está enviando.
