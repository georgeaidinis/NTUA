# Software-Engineering

## Backend

### Install python3
```
sudo apt install python3
```

### Install pipenv virtual environment
```
pip3 install pipenv
```

### Install mysql or mariadb
```
sudo apt-get install mysql-server
```

### Activate virtual environment
Inside backend/ direcotry
```
pipenv shell
```

### Create the Database (inside the /data folder)
```
mysql -u root -p < create_database.txt
```

### Install mysqlclient with pip3
```
pip3 install mysqlclient
```

### Install all dependencies from requirements.txt
```
pipenv install
```
### Change config.py file with the appropriate values for your configuration

### Copy config.template.py with name config.py in the same file
```
cp  config.py config.template.py
```



### Run the backend application
```
python run.py
```
### Create the alias of the cli
```
alias energy_group005="python3 cli1.py"
```
### Run the CLI of the application
```
python cli1.py
```


## Frontend

### Install NodeJS
```
curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Install Angular/CLI
```
npm install -g @angular/cli
npm update
```

### Install dependencies
(after pulling an angular project, to install all the required dependencies run )
```
npm install
```

### Create an Angular project
```
ng new ProjectName
```

### Create new component
```
ng g c componentName
```

### Generate service
```
ng g s serviceName
```

### Run project locally
(use flag -o to open a browser tab)
```
ng s -o
```


### Download data files
```
sudo sh data.sh
```