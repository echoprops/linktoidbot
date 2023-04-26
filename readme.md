## LinkToId Telegram Bot

### (projeto sem funcionar corretamente)
#### tentativa fracassada de fazer um bot pra Telegram que faz links diretos para ID de usuários, mas não é possivel devido as politicas de privacidade do Telegram, conta com um bot em python e uma ferramenta em Shell para automatizar que tem erro em umas linhas que não consegui descobrir pelo fato de eu não conseguir debugar o shell, conta apenas como aprendizado

simple bot for Telegram that generates a direct link to a person's telegram account using their user ID, which uses [telebot](https://github.com/eternnoir/pyTelegramBotAPI) and [Telegram's own URI](https://core.telegram.org/api/links#id-links) 

**requirements:**
- lastest python 3.x version
- pip3
- lastest pytelegrambotapi version

**instructions (manual mode):**

 - first install the dependencies:
````bash
pip3 install pytelegrambotapi --upgrade
````
- create .env file:
````bash
touch .env
echo "export TOKEN=<YOUR_BOT_TOKEN>" >> .env
````
 - then run the bot
 ````bash
 source .env
 cd src
 python3 link_to_id_bot.py
 ````
**instructions (suggs)**
````bash
./suggs create-env <YOUR_BOT_TOKEN> # to create env file
./suggs pull # to download pip3 dependencies
./suggs execute # to execute bot
````

