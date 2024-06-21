NBA Information API Documentation
Overview

This API provides information about NBA players, upcoming games, and player status (active or inactive).
Base URL

arduino

https://api.example.com/nba

Authentication

No authentication is required to access the endpoints.
Endpoint: /active_players
Description

This endpoint retrieves information about active players in the NBA.
Usage

Send a GET request to /active_players to retrieve information about active players.
Response Format

The response contains a JSON object with information about active players in the NBA. Each player includes details such as their name, team, position, height, weight, and more.
Example Request

bash

GET /active_players

Example Response

json

{
    "active_players": [
        {
            "full_name": "LeBron James",
            "team": "Los Angeles Lakers",
            "position": "Forward",
            "height": "6-9",
            "weight": "250 lbs",
            ...
        },
        {
            "full_name": "Kevin Durant",
            "team": "Brooklyn Nets",
            "position": "Forward",
            "height": "6-10",
            "weight": "240 lbs",
            ...
        },
        ...
    ]
}

Error Handling

If an error occurs while retrieving the active player information, the endpoint returns a JSON object with an "error" key containing a description of the error.
Example Error Response

json

{
    "error": "Failed to retrieve active player information: Connection timeout"
}

Endpoint: /games
Description

This endpoint retrieves information about upcoming games in the NBA.
Usage

Send a GET request to /games to retrieve information about upcoming games.
Response Format

The response contains a JSON object with information about the upcoming games. Each game includes details such as teams, date, and venue.
Example Request

bash

GET /games

Example Response

json

{
    "games": [
        {
            "home_team": "Los Angeles Lakers",
            "away_team": "Golden State Warriors",
            "date": "2024-04-26",
            "venue": "Staples Center"
        },
        {
            "home_team": "Boston Celtics",
            "away_team": "Brooklyn Nets",
            "date": "2024-04-26",
            "venue": "TD Garden"
        },
        ...
    ]
}

Error Handling

If an error occurs while retrieving the game information, the endpoint returns a JSON object with an "error" key containing a description of the error.
Example Error Response

json

{
    "error": "Failed to retrieve game information: Connection timeout"
}

Endpoint: /player/{player}
Description

This endpoint retrieves information about an NBA player based on their name.
Usage

Send a GET request to /player/{player} to retrieve information about a player. Replace {player} with the full name of the player.
Response Format

The response contains a JSON object with information about the player. This includes details such as their team, position, height, weight, and more.
Example Request

bash

GET /player/LeBron James

Example Response

json

{
    "player": {
        "full_name": "LeBron James",
        "team": "Los Angeles Lakers",
        "position": "Forward",
        "height": "6-9",
        "weight": "250 lbs",
        ...
    }
}

Error Handling

If an error occurs while retrieving the player information, the endpoint returns a JSON object with an "error" key containing a description of the error.
Example Error Response

json

{
    "error": "Failed to retrieve player information: Player not found"
}

Endpoint: /inactive_players
Description

This endpoint retrieves information about inactive players in the NBA.
Usage

Send a GET request to /inactive_players to retrieve information about inactive players.
Response Format

The response contains a JSON object with information about inactive players in the NBA. Each player includes details such as their name, team, position, height, weight, and more.
Example Request

bash

GET /inactive_players

Example Response

json

{
    "inactive_players": [
        {
            "full_name": "Kobe Bryant",
            "team": "Retired",
            "position": "Guard",
            "height": "6-6",
            "weight": "212 lbs",
            ...
        },
        {
            "full_name": "Tim Duncan",
            "team": "Retired",
            "position": "Forward-Center",
            "height": "6-11",
            "weight": "250 lbs",
            ...
        },
        ...
    ]
}

Error Handling

If an error occurs while retrieving the inactive player information, the endpoint returns a JSON object with an "error" key containing a description of the error.
Example Error Response

json

{
    "error": "Failed to retrieve inactive player information: Connection timeout"
}

Documentação da API de Informações da NBA
Visão Geral

Esta API fornece informações sobre jogadores da NBA, jogos futuros e status dos jogadores (ativos ou inativos).
URL Base

arduino

https://api.example.com/nba

Autenticação

Nenhuma autenticação é necessária para acessar os endpoints.
Endpoint: /active_players
Descrição

Este endpoint recupera informações sobre jogadores ativos na NBA.
Utilização

Envie uma solicitação GET para /active_players para recuperar informações sobre jogadores ativos.
Formato da Resposta

A resposta contém um objeto JSON com informações sobre jogadores ativos na NBA. Cada jogador inclui detalhes como seu nome, time, posição, altura, peso e mais.
Exemplo de Solicitação

bash

GET /active_players

Exemplo de Resposta

json

{
    "jogadores_ativos": [
        {
            "nome_completo": "LeBron James",
            "time": "Los Angeles Lakers",
            "posição": "Ala",
            "altura": "6-9",
            "peso": "250 lbs",
            ...
        },
        {
            "nome_completo": "Kevin Durant",
            "time": "Brooklyn Nets",
            "posição": "Ala",
            "altura": "6-10",
            "peso": "240 lbs",
            ...
        },
        ...
    ]
}

Tratamento de Erros

Se ocorrer um erro durante a recuperação das informações dos jogadores ativos, o endpoint retorna um objeto JSON com uma chave "error" contendo uma descrição do erro.
Exemplo de Resposta de Erro

json

{
    "error": "Falha ao recuperar as informações dos jogadores ativos: Tempo limite de conexão"
}

Endpoint: /games
Descrição

Este endpoint recupera informações sobre os próximos jogos na NBA.
Utilização

Envie uma solicitação GET para /games para recuperar informações sobre os próximos jogos.
Formato da Resposta

A resposta contém um objeto JSON com informações sobre os próximos jogos. Cada jogo inclui detalhes como equipes, data e local.
Exemplo de Solicitação

bash

GET /games

Exemplo de Resposta

json

{
    "jogos": [
        {
            "time_casa": "Los Angeles Lakers",
            "time_visitante": "Golden State Warriors",
            "data": "2024-04-26",
            "local": "Staples Center"
        },
        {
            "time_casa": "Boston Celtics",
            "time_visitante": "Brooklyn Nets",
            "data": "2024-04-26",
            "local": "TD Garden"
        },
        ...
    ]
}

Tratamento de Erros

Se ocorrer um erro durante a recuperação das informações do jogo, o endpoint retorna um objeto JSON com uma chave "error" contendo uma descrição do erro.
Exemplo de Resposta de Erro

json

{
    "error": "Falha ao recuperar as informações do jogo: Tempo limite de conexão"
}

Endpoint: /player/{player}
Descrição

Este endpoint recupera informações sobre um jogador da NBA com base em seu nome.
Utilização

Envie uma solicitação GET para /player/{player} para recuperar informações sobre um jogador. Substitua {player} pelo nome completo do jogador.
Formato da Resposta

A resposta contém um objeto JSON com informações sobre o jogador. Isso inclui detalhes como seu time, posição, altura, peso e mais.
Exemplo de Solicitação

bash

GET /player/LeBron James

Exemplo de Resposta

json

{
    "jogador": {
        "nome_completo": "LeBron James",
        "time": "Los Angeles Lakers",
        "posição": "Ala",
        "altura": "6-9",
        "peso": "250 lbs",
        ...
    }
}

Tratamento de Erros

Se ocorrer um erro durante a recuperação das informações do jogador, o endpoint retorna um objeto JSON com uma chave "error" contendo uma descrição do erro.
Exemplo de Resposta de Erro

json

{
    "error": "Falha ao recuperar as informações do jogador: Jogador não encontrado"
}

Endpoint: /inactive_players
Descrição

Este endpoint recupera informações sobre jogadores inativos na NBA.
Utilização

Envie uma solicitação GET para /inactive_players para recuperar informações sobre jogadores inativos.
Formato da Resposta

A resposta contém um objeto JSON com informações sobre jogadores inativos na NBA. Cada jogador inclui detalhes como seu nome, time, posição, altura, peso e mais.
Exemplo de Solicitação

bash

GET /inactive_players

Exemplo de Resposta

json

{
    "jogadores_inativos": [
        {
            "nome_completo": "Kobe Bryant",
            "time": "Aposentado",
            "posição": "Ala-armador",
            "altura": "6-6",
            "peso": "212 lbs",
            ...
        },
        {
            "nome_completo": "Tim Duncan",
            "time": "Aposentado",
            "posição": "Pivô-Ala",
            "altura": "6-11",
            "peso": "250 lbs",
            ...
        },
        ...
    ]
}

Tratamento de Erros

Se ocorrer um erro durante a recuperação das informações dos jogadores inativos, o endpoint retorna um objeto JSON com uma chave "error" contendo uma descrição do erro.
Exemplo de Resposta de Erro

json

{
    "error": "Falha ao recuperar as informações dos jogadores inativos: Tempo limite de conexão"
}

Este README combina informações dos endpoints /active_players, /games, /player/{player}, e /inactive_players, apresentando uma documentação completa tanto em inglês quanto em português para facilitar o uso da API de informações da NBA.
