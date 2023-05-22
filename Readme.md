# Install dependencies
```shell
py -m pip install -r requirements.txt
```

# Activate venv
```shell
.\Scripts\activate.bat
```

# Train
```shell
python trainModel.py
```

# Run Flask API
```shell
python -m flask --app app run
```

# Call api
```http
http://127.0.0.1:5000/?text=Hi
```