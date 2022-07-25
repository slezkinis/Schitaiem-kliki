# Обрезка ссылок с помощью Битли

С помощью моей программы можно укорачивать ссылки, а потом получать количество переходов по ссылке

### Как установить

1. Создайте файл .env и добавьте токен, полученный из Bitlink. Вот пример:
```
BITLINK_TOKEN=[Ваш токен]
```

2. Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

1. Укорачивание ссылок:
Нужно ввести команду в терминал. Например:
`python main.py https://yandex.ru/`

Вывод будет примерно таким:
`Битлинк: https://bit.ly/3OvMqRd`

2. Получение количества переходов по короткой ссылке:
Нужно ввести коману в терминале. Например:
`python main.py https://bit.ly/3OvMqRd`

Вывод будет примерно таким:
`Число кликов: 1`

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
 
