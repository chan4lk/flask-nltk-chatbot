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
py trainModel.py
```

# Run Flask API
```shell
py -m flask --app app run
```

# Call api
```http
http://127.0.0.1:5000/message?text=Hi
```