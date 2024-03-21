## Installation

To run the Messenger Bot on Replit.com, follow these steps:

1. Clone this repository to your Repl in your Replit account using your GitHub token for One use command [Github Docs For Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

    ```bash
    git clone https://your_username:your_token@github.com/D-Redouane/nticdocs.messenger.git
    ```

   Replace `your_username` with your GitHub username, `your_token` with your GitHub token, and `your_repo` with the name of your repository.

2. Configurations of the environment variables:
   
   1. For the normal repo, Copy the environment variables from the `.env.example` file and create a new `.env` file in the root directory of the project:

    ```plaintext
    cp .env.example .env
    ```

   Then, populate the `.env` file with the necessary variables:
   

    ```plaintext
     # Update the following values with your credentials:

     # Your Facebook Page Token. For more information, refer to the documentation: 
     # https://developers.facebook.com/docs/messenger-platform/getting-started/quick-start
     TOKEN=YOUR_FACEBOOK_PAGE_TOKEN

     # Ngrok Verify Token. For details on how to obtain and use the token, visit:
     # https://ngrok.com/docs#http-verify
     VERIFY_TOKEN=YOUR_VERIFY_TOKEN

     # Ngrok Domain. Read the documentation for information on Ngrok domains:
     # https://ngrok.com/docs#http-domains
     NGROK_DOMAIN=YOUR_NGROK_DOMAIN

     # Path to the JSON file containing the directory structure.
     JSON_FILE_PATH=./tree/NTIC-Constantine2_Licence-S1.json
    ```


   2. For Replit repo , add them from the `Secrets` Section Look to the [docs of Secrets](https://docs.replit.com/programming-ide/workspace-features/secrets)

<!-- 3. Run the Flask application:

    ```bash
    python main.py
    ``` -->

## Usage

Once the bot is up and running, you can interact with it via Facebook Messenger. Here are some available commands:

- `/start` or `/help`: Start or get help with the bot.
- `/list`: Browse the directory.
- `/template`: Display a template message.
- `/button`: Display a message with buttons.
- `/quickr`: Display a message with quick replies.
- `/list2`: Display a list message.
- `/hi`: Say hello to the bot.
- `/image`: Send an image.
- `/receipt`: Send a receipt message.

## Webhook

The bot uses a webhook to receive messages and events from Facebook Messenger. The webhook is configured to handle incoming messages and postbacks.

To set up the webhook, create a Facebook app and page, then configure the webhook URL to point to your ngrok domain.

## Ngrok Configuration
1. Configuration From zero
   
    1. Download Ngrok from the official website: [Ngrok Download](https://ngrok.com/download)
     Or
     
      ```bash
      # exemple: wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
      ```

  2. Unzip the downloaded file.
     
      ```bash
      # exemple: tar -xvzf ngrok-v3-stable-linux-amd64.tgz
      ```
     
  3. Configure Ngrok with your authentication token from your ngrok account [Ngrok Account](https://dashboard.ngrok.com):

      ```bash
      ./ngrok/ngrok authtoken YOUR_AUTH_TOKEN
      ```

  4. Run Ngrok to expose your local server:

      ```bash
      ./ngrok/ngrok http --domain=YOUR_NGROK_DOMAIN 8080
      ```

2. From already Setted in this repo : 
   
    1. Add to the Config file in .config/ngrok/ngrok.yml add the `authtoken`  variable by the verify token of ngrok and also the `web_allow_hosts` variable that you will add the replit url to it 
     
      ```
      version: "2"

      # TOKEN EXAMPLE: 2dm5qK8N02uxQGScSNaO5ZBK5et_2e7o5AnM9kuenSLSSdXeJ
      authtoken: <YOUR NGROK AUTH TOKEN>

      web_addr: 127.0.0.1:4040
      web_allow_hosts:
        - localhost

        # YOUR REPL URL EXAMPLE: https://f9d74caa-2f25-4dc1-8ae5-e5a0f672db39-00-2ju51o8qw2tef.picard.repl.co/
        - <YOUR REPL URL>
      ```     
     
  2. Run Ngrok to expose your local server:

      ```bash
      ./ngrok/ngrok http --domain=YOUR_NGROK_DOMAIN 8080
      ```


## Directory Structure

The directory structure of the repository is as follows:

```
messenger
├── .gitignore
├── .env.example
├── .replit
├── LICENSE.md
├── README.md
├── main.py
├── src
│   ├── functions.py
│   ├── routes.py
│   └── variables.py
├── .config
│   └── ngrok
│       └── ngrok.yml
├── ngrok
│   └── ngrok
└── tree
    └── NTIC-Constantine2_Licence-S1.json
```

## License

This project is licensed under the the Creative Commons Attribution-NonCommercial 4.0 International License. - see the [LICENSE.md](LICENSE.md) file for details.

## Contributors

Special thanks to the contributors who helped with this project:

- [DADDIOUAMER Redouane](https://github.com/D-Redouane)



---



<div align="center">
  <img src="https://avatars.githubusercontent.com/u/162585510?s=200&v=4" alt="Reserved Rights Logo" width="100">
</div>

<div align="center">
  © 2024, All rights reserved to - NTIC Documents.
</div>
