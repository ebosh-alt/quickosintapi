Как запустить проект:  
Перейти в файловый менеджер  
```cmd  
cd ...  
cd prj_1200  
cd quickosintapi  
python3 app.py  
```  

Как перезапустить проект:<br>  
```cmd
ctrl + c
python3 app.py
```

Как изменить token:
в файле config.py вставить новый ключ в кавычках и перезапустить проект

Как изменить адрес:<br>
в файле app.py необходимо изменить 9 строчку
```python
@app.route('/...')
```
заменить многоточие на необходимый адрес<br>
нельзя использовать пробелы и /

Данные для терминала:
логин: root  
пароль: `T92*jyeUoSEC` 
Сайт: http://31.129.109.127:5000/quickosintapi <br>  
Сайт на который ссылается api: https://quickosint.com <br>  
Документация api: https://quickosint.com/files/APIman.pdf