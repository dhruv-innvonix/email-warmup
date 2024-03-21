
# Email-warmup_tool

Python Django application

### Installing - Backend (Local)

- Install postgresql database server

    ```
    https://www.tecmint.com/install-postgresql-and-pgadmin-in-ubuntu/
    ```
    Create "EmailwarmupDB" database using pgadmin 

- Add .env file

    Copy `example.env` file to `.env` file in root directory and update the required values


- Install latest version of python (3.10): 
    Note: linux needs  python3.10-dev 
    ```
    https://www.python.org/downloads/
    ```

- Install pip and pipenv

    ##### Unix/macOS
    ```
    python -m pip install -U pip
    pip install --user pipx
    pipx install pipenv
    ```
    ##### Windows
    ```
    py -m pip install -U pip
    pip install --user pipx
    pipx install pipenv
    ```

- Install packages

    ```
    pipenv install
    ```

- Start pipenv

    ```
    pipenv shell
    ```

- Make and apply migrations (create database tables)
    ```
    pipenv run python manage.py makemigrations --settings=backend.settings
    pipenv run python manage.py migrate --settings=backend.settings
    ```

- Start dev server
    ```
    pipenv run python manage.py runserver --settings=backend.settings
    ```

### Setting-up VPN
 - Install and create account 

    ```
    https://protonvpn.com/blog/linux-vpn-cli-beta/
    ```
    Create your account and save your credentials in local files and variables.py -- (Vpn_starter())

    Change username and password according to your signup credentials

    for better understanding refer
    ```
    https://protonvpn.com/support/linux-openvpn/
    ```

- Some simple steps if got stucked with vpn setup

    sudo apt-get install {/path/to/}protonvpn-stable-release_1.0.0-1_all.deb

    sudo apt-get update

    sudo apt-get install openvpn

    sudo apt install resolvconf

    https://account.protonvpn.com/downloads ----download file free

    sudo openvpn us-free-41.protonvpn.net.udp.ovpn  --- you can download other nations vpn file instead of 'us'
    
    https://account.protonvpn.com/account  --> check your password and username

- File configurations
    
    change the file location and system password for sudo in Vpn_starter()
    

        -->/home/shiva/Innvonix/Projects/email-warmup-tool/email_warmup/us-free-41.protonvpn.net.udp.ovpn

        --> 'echo "system_password_for_sudo"

        subprocess.Popen('echo "system_password_for_sudo" | sudo -S openvpn --config /home/shiva/Innvonix/Projects/email-warmup-tool/email_warmup/us-free-41.protonvpn.net.udp.ovpn --auth-user-pass /home/shiva/Innvonix/Projects/email-warmup-tool/email_warmup/credentials.txt', shell=True)

    change the credentials text location as per your location

        -->r"/home/shiva/Innvonix/Projects/email-warmup-tool/email_warmup/credentials.txt"

        --> with open(r"/home/shiva/Innvonix/Projects/email-warmup-tool/email_warmup/credentials.txt", "w") as f:
