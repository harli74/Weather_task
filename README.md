# Training

## [Task 1](#task1). Weather API requests - основи

* Да покажеш какво е времето в момента за 20 random избрани града (избери София да е статично всеки път и останалите произволно):
	* Дали вали сняг, дъжд, слънчево ... etc. 
	* Каква е температурата в момента ?
	* Каква е влажността в момента ?

* Да изведе следните статистики:
	* Най-студен град
	* Средна температура за намерените градове

* **Да можеш да въведеш име на град и да ти покаже:** (бонус точки)
	* Облачно ли е ?
	* Колко е температурата ?


+ Нужни неща:
	- Обработване на JSON данни
	- HTTP/HTTPS Requests
	- Random generator
	- User Input


## [Task 2](#task2). Надграждане на [Task 1](#task1)

* Да се направи GUI interface със framework по избор
	* Tkinter (препоръчвам ти това :) )
	* Kivy (с това могат да се правят мобилни приложения)
	* Qt (това може да ти е сложно, но е много мощно)

## [Task 3](#task3). Разучаване на Flask

* Да направиш WEB app, който да прави нещата от [Task 1](#task1) посредством web interface с back-end с Flask microframework + front-end HTML/CSS/JS
	* Препоръчвам да прегледаш на бързо Bootstrap **CSS** и JQuery **JS**- Traversy Media пича има обяснени - много код се спестява :)
	* без да използваш бази данни да запазваш резултати
	* Графичната част както я направиш ... използвай Jinja2 template language за Flask

+ **Нужни неща**
	- Flask
	- JavaScript, CSS, HTML (базово ниво)

+ **Съвет**
	- Flask-a го почвай от Hello world app-a, ще се ориентираш

## [Task 4](#task4). Разучаване на Django
* Да повториш задачата от [Task 3](#task3)

+ **Съвет**
	- Django-то го почвай от Hello world app-a, малко по-сложно е първоначално понеже нещата са 
	разпилени в повече файлове и има повече boilerplate където ти се генерира автоматично


## [Task 5](#task5). DB Design

* Да си направиш база данни, която да се обновява при всяко натискане на REFRESH бутон някъде по страницата 
* Да ти презарежда новите стойности по страницата
* Да имаш опция да сравняваш последните 10 резултата за всеки параметър.


# ГЛОБАЛЕН СЪВЕТ

За всичко, което си помислиш, че е по-сложно за реализиране най-вероятно си има вече 
**готова функция/библиотека**, която просто трябва да използваш - НЕ се опитвай да откриваш
топлата вода отново :) някой вече го е направил.
Идеята е най-вече да пишеш модулно и да използваш готови модули.
Препоръчвам ти всяко дребно нещо да си го изнасяш във функции, а всички функции в последствие да ги групираш в класове.
Добавил съм ти един файл за codebase с реализиран basic class и функции в него 