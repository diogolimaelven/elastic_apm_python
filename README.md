# elastic_apm_python
Turma Cohort

## Setup servidor 
Instalar docker e docker compose

```
git clone <projeto>
```
## Setup elastic stack

```
sysctl -w vm.max_map_count=262144
```

### Subindo a stack 

```
docker compose up -d
```
```
Postgres port : 5432
Kibana port : 5601
Elastic port : 9200
APM : 8200
```
## Aplicação localhost

```
git clone <projeto>
python3 -m venv .
source ./bin/activate
```

### Instalando todas as dependencias 

```
pip3 install --no-cache-dir -r requirements.txt
python app.py


```

### Adicionando os logs no apm

```
'DEBUG': True
apm.capture_message(app.logger.critical(err), level='error')
```

### Desativando venv
```
deactivate
```