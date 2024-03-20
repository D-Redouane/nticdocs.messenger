## Installation

To run the Messenger Bot on Replit.com, follow these steps:

1. Clone this repository to your Repl in your Replit account using your GitHub token for One use command [Github Docs For Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

    ```bash
    git clone https://your_username:your_token@github.com/your_username/your_repo.git
    ```

   Replace `your_username` with your GitHub username, `your_token` with your GitHub token, and `your_repo` with the name of your repository.

2. Copy the environment variables from the `.env.example` file and create a new `.env` file in the root directory of the project:

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

3. Run the Flask application:

    ```bash
    python main.py
    ```

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
    ./ngrok authtoken YOUR_AUTH_TOKEN
    ```

4. Run Ngrok to expose your local server:

    ```bash
    ./ngrok http --domain=YOUR_NGROK_DOMAIN 8080
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
├── ngrok
│   └── ngrok
└── tree
    └── NTIC-Constantine2_Licence-S1.json
```

## License

This project is licensed under the the Creative Commons Attribution-NonCommercial 4.0 International License. - see the [LICENSE.md](LICENSE.md) file for details.