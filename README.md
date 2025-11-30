# Projeto – Desafios com Docker e Microsserviços

Este repositório reúne cinco desafios de Docker e microsserviços.


- `desafio1`: dois containers na mesma rede Docker. Um é um servidor Flask na porta 8080 e o outro é um cliente que fica chamando o servidor com `curl`.
- `desafio2`: script em Python com SQLite gravando em `/data/desafio2.sqlite`, usando volume Docker para manter o arquivo mesmo depois que o container é removido.
- `desafio3`: três serviços subindo com Docker Compose: web (Flask), banco (Postgres) e cache (Redis). A aplicação grava acessos no banco e conta chamadas no Redis.
- `desafio4`: dois microsserviços HTTP. Um devolve uma lista de usuários e o outro consome esse serviço e monta frases do tipo “Usuário X ativo desde ...”.
- `desafio5`: dois microsserviços (usuários e pedidos) atrás de um API Gateway, que expõe os endpoints `/users` e `/orders`.

## Como usar

- Entre na pasta do desafio que você quer testar.
- Leia o `README.md` 
