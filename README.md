# CleanMyVk

Автоматическая очистка стены и сообщений.
В данный момент вы только очищаете историю групповых чатов, но не ливаете из них

## Установка

Для использования данного приложения необходим python 3й версии.

### Unix
```
python3 -m pip install -r packeges.txt
```
### Windows
```
python -m pip install -r packeges.txt
```
или
```
python.exe -m pip install -r packeges.txt
```
## Перед запуском
**Перед запуском обязательно проверьте, что заполнили 'protected.json' в нем хранятся
те ид постов и диалогов, которые не будут удалены скриптом**

### Пример protected.json

```
{
  "posts": [30, 239, 1337],
  "messages": [30, 13371487, 13371486, 22830239]
}
```

"posts" - ид постов<br/>
"messages" - ид сообщений(диалог/чат)<br/>

**Ид поста со стены**
![Alt text](https://i.imgur.com/l9aSLJ8.png "Ид поста со стены")<br/>
**Ид диалога**
![Alt text](https://i.imgur.com/el1Ig17.png "Ид диалога")<br/>
**Ид чата**
![Alt text](https://i.imgur.com/WqnELpG.png "Ид чата")<br/>

## Запуск

### Unix
```
python3 ./src/cleanMyVk.py
```
### Windows
```
python ./src/cleanMyVk.py
```
или
```
python.exe ./src/cleanMyVk.py
```