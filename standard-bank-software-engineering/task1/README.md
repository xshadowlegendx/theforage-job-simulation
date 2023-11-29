### facial image encoding from s3 bucket using aws lambda

### tools used
- python
- pdm - modern python package manager
- milvus - vector database to store face encodings and do face search

### development and testing
0. install `python` required by project (checks pyproject.toml)
1. install `pdm`
2. run `pdm install` to install project dependencies
3. install `docker`
4. run `docker-compose up -d` to setup local s3 server and vector database
5. run `pdm run src/facial_image_encoding/facial_image_encoding.py` to test the lambda function
