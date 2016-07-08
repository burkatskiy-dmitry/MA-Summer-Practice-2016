# Семінар 0. Основи Python

Розглянуті питання
----------------------------------------

* Написання Hello World додатку
* Підключення Flask
* Статична сторінка
* Робота з колекціями

Фронтенд
----------------------------------------
* Заінсталювати [NodeJS](https://nodejs.org/en/), разом з ним інсталюється NPM - пакетний менеджер.
* Створити проект, для прикладу – blog-frontend.
* В ньому запустити команду npm init, заповнити необхідну інформацію, яка створить конфіг (package.json) для вашого проекту.
* Через NPM заінсталювати Gulp, gulp-sass, gulp-cssnano, gulp-postcss, Autoprefixer.
* Створити Gulpfile.js і додати 1 task, котрий буде юзати всі ці пакети. Докладніше почитайте [frontender](http://frontender.info/no-need-to-grunt-take-a-gulp-of-fresh-air/) і [css-tricks](https://css-tricks.com/gulp-for-beginners/).
* Макет блогу [тут](https://goo.gl/2eL17C).
* Потрібно [responsive'но](https://css-tricks.com/the-difference-between-responsive-and-adaptive-design/) зверстати макет, нагологую ще раз на тому что ваша верстка має буди responsive, а не adaptive.
* Макет тільки для мобільного девайсу, але потрібно продумати десктопну версію самостійно. Якщо з цим будуть проблеми – пишіть в скайпик.
* Усі іконки, їх аж цілих 2, мають бути в SVG. І вставлені на сторінку через (symbol + svg use) метод.
* Також вони мають бути оптимізовані через [svgo-cli](https://github.com/svg/svgo) або [svgo-online](https://jakearchibald.github.io/svgomg/).
* Заюзати якусь структуру файлів для проекту, аби не було все в одній папці, для прикладу [front-end architecture](https://www.sitepoint.com/good-front-end-architecture/).

Домашнє завдання
----------------------------------------
* форкнути цей репозиторій, створити в ньому каталог для домашніх завдань
* зробити простий блог (фронтенд і бекенд)


Корисні посилання
----------------------------------------

* [Вікіпідручник Flask](https://ru.wikibooks.org/wiki/Flask)
* [Setting Up Postgres, SQLAlchemy, and Alembic](https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
* [REST](https://habrahabr.ru/post/38730/)
* [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete/)
* [Gulp](http://gulpjs.com/)
* [SCSS](http://sass-lang.com/guide)
