# Arcade Game
Arcade Game - це аркадна гра, де гравець керує платформою, яка рухається горизонтально, та намагається відбити м'яч, який відскакує від верхньої частини екрану.

## Запуск проекту
Для запуску проекту все, що вам знадобиться - це скачати проект і запустити файл  [main.py](https://github.com/hoowalex/Arcade_game/blob/master/main.py)


## Використані принципи програмування
- **DRY (Don't Repeat Yourself)**: У коді немає повторень. Вся логіка розбита на окремі методи та класи, щоб забезпечити їхню одноразову реалізацію та використання(без врахування ui компонентів).

- **KISS (Keep It Simple, Stupid)**: Код дуже простий та зрозумілий. Немає громіздких методів або класів, що робить його легким у розумінні та роботі з ним.

- **SR (Single Responsibility)**: Кожен клас в моєму проекті виконує лише одну основну функцію. Наприклад, клас [Ball](https://github.com/hoowalex/Arcade_game/blob/master/ball.py) відповідає за рух м'яча та взаємодію з платформою, а клас [Platform](https://github.com/hoowalex/Arcade_game/blob/master/platform.py) - за рух платформи. Це дозволяє підтримувати чистоту та легкість розуміння коду.

- **DIP (Dependency Inversion Principle)**:  Класи залежать від абстракцій, а не від конкретних реалізацій. Наприклад, клас [Ball](https://github.com/hoowalex/Arcade_game/blob/master/ball.py) залежить від стратегій збільшення швидкості, а не від конкретних реалізацій цих стратегій.

- **COI (Composition Over Inheritance)**: У моєму проекті я більше використовую композицію об'єктів, ніж успадкування класів. Наприклад, я використовую композицію для реалізації взаємодії між м'ячем та платформою, а не успадковую логіку руху від платформи до м'яча.

- **YAGNI(You Aren't Gonna Need It)**: уникнув додавання зайвого функціоналу до програми, якого насправді не потрібно.


## Використанні патерни проектування
- **Strategy (Стратегія)** Паттерн стратегії було використано для зміни швидкості м'яча в залежності від рахунку гравця. Цей паттерн дозволяє визначити різні алгоритми або стратегії, які можуть бути вибрані на льоту, відповідно до потреб програми. У моєму випадку стратегії визначають, як швидкість м'яча змінюється в залежності від рахунку.

- **Singleton(Одинак)** Паттерн сінглтон для створення [RecordManager](https://github.com/hoowalex/Arcade_game/blob/master/record_manager.py), який відповідає за управління рекордом гри. Цей паттерн гарантує, що клас має лише один екземпляр і надає глобальну точку доступу до цього екземпляру.

- **Observer(Спостерігач)** Паттерн спостерігача було використано для оновлення рахунку гравця на екрані. Клас [Scoreboard](https://github.com/hoowalex/Arcade_game/blob/master/scoreboard/scoreboard.py) служить як суб'єкт, який сповіщає своїх спостерігачів (наприклад, [WindowScoreboardObserver](https://github.com/hoowalex/Arcade_game/blob/master/scoreboard/scoreboard_observer.py#L7-L15)) про зміни в рахунку гравця.

- **Factory Method(Фабричний метод)** Хоча цей паттерн не використовувався безпосередньо в коді, проте концепція фабричного методу використовується при створенні нових екземплярів об'єктів. Наприклад, при створенні нового м'яча (Ball) я використовую конструктор класу для створення нового екземпляру.

## Використані Техніки рефакторингу
- **Extract Class**: Коли було необхідно використати певний функціонал, я виділив його у окремий клас, що дозволило зменшити залежність та зробити код більш модульним.

- **Extract Method**: Виділення фрагменту коду в окремий метод для зменшення дублювання коду та покращення читабельності та підтримки. Було застосовано під час написання програмного коду.

- **Rename Method**: Виправлення імена змінних та методів з метою поліпшення зрозумілості та читабельності коду. Було застосовано під час написання програмного коду.

- **Inline Temp**: Заміна локальної змінної викликом її значення для полегшення читання та зменшення зайвих проміжних кроків у коді.Було застосовано під час написання програмного коду.

- **Split into Files**: Код було розділено на окремі файли згідно з їхньою функціональністю, що дозволило зберегти структурованість та зрозумілість проекту.
