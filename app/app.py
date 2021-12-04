from flask import Flask, render_template, request

application = Flask(__name__)


@application.route('/')
def index():
    home = True
    return render_template('index.html', home=home)

@application.route('/certificate')
def certificate():
    title = "Сертификаты и допуски"
    content = ""
    slogan = "Самый полный перечень допусков по СФО"
    return render_template('content.html', title=title, content=content, slogan=slogan)

@application.route('/diagnostics')
def diagnostics():
    title = "Диагностика неисправностей систем вентиляции"
    content = """
<div class="container">    
<p><strong>С какими проблемами сталкиваются наши Заказчики:</strong></p>
<ul>
<li>Если вентиляция не включается или не выполняет необходимых функций</li>
<li>Вентиляция работает но выдувает плохо.</li>
<li>Трубы вентиляции запотевшие (мокрые)</li>
<li>При работе вентиляции в помещении холодно</li>
<li>При работе вентиляция сильно шумит</li>
</ul>
<p></p>
<p><strong>Мы знаем причины и можем помочь Вам.</strong></p>
<ul>
<li>Нам нужно приехать к Вам и провести диагностическое обследование системы вентиляции, провести ряд замеров и понять почему вентиляция не работает как надо.</li>
<li>На выходе вы получите диагностический лист с конкретными неисправностями и вариантами как убрать данную неисправность.</li>
<li>Мы постараемся устранить неисправность сразу на месте если это будет возможно.</li>
</ul>

<h3>Примеры</h3>
<img src="/static/images/IMG_1889.JPG" alt="" style="float: left;"  height="200" />
<img src="/static/images/IMG_1889.JPG" alt="" style="float: left;"  height="200" />
<img src="/static/images/IMG_2322.JPG" alt="" style="float: left;"  height="200" />
<img src="/static/images/IMG_3746.JPG" alt="" style="float: left;"  height="200" />
<img src="/static/images/IMG_9915.JPG" alt="" style="float: left;"  height="200" />

</div>
    """
    slogan = "Выезд специалистов для диагностики ваших систем"
    return render_template('content.html', title=title, content=content, slogan=slogan)


@application.route('/service')
def service():
    title = "Обслуживание вентиляционных установок"
    content = """
    <div class="container">    
    <h4>Задачи:</h4>

<p>1. Необходимо, чтобы вентиляционная установка работала без сбоев и с заданными характеристиками.</p>
<p>2. Стоимость обслуживания должна быть не дорогой</p>
<p>3. Необходимо вести документацию по системам вентиляции</p>
<p>4. Отсутствие претензий (замечаний) от органов санитарного и пожарного надзоров</p>
<p></p>
<h4>Мы понимаем Вас</h4>
<p>Мы готовы закрыть для Вас эти вопросы (задачи)</p>
<p><strong>И так что мы предлагаем:</strong></p>
<p><strong>1. Годовое обслуживание вент систем под ключ:</strong></p>
<ul>
<li>Ведение всей необходимой документации согласно требований (____)</li>
<li>Ежеквартальное Периодическое обследование системы с целью поиска неисправностей (от 2-4 раз в год)</li>
<li>Введение журнала работ и выявленных дефектов</li>
<li>Замена всех необходимых фильтров.</li>
<li>Поддержание установки в заданных характеристиках.</li>
<li>Мелкосрочные ремонты</li>
</ul>
<p></p>
<h4>Вам этого недостаточно:</h4>
<ul>
<li>Можем взять и чистку системы на себя.</li>
<li>Тогда у Вас будет полностью рабочая система со всеми документами и еще и чистая внутри.</li>
</ul>

<h3>Примеры</h3>
<img src="\static\images\Servis\Акт2.jpeg" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\Акт1.jpeg" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\Инструкция по вентиляции на кухне МБДОУ №1.pdf" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\IMG_1890.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\IMG_2251.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\Акт1.jpg" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\Акт2.jpg" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\Акт 4 ТО В-2 кухня стр. 2.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\99_Вид После.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\IMG_9876.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\Акт 1 ТО ПВ-1 подвал стр.1.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\IMG_9879.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\Акт 4 ТО В-2 кухня стр. 1.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\91_Вид до.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\IMG_9240.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\72_Фильтр до.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\IMG_1889_Конденсатор под замену.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\IMG_2243.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\75_Фильтр после.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\Servis\IMG_2257.JPG" alt="" style="float: left;"  height="200" />

</div>
    """
    slogan = "Системное обслуживание"
    return render_template('content.html', title=title, content=content, slogan=slogan)


@application.route('/clear')
def clear():
    title = "Очистка от пылевых и жировых загрязнений"
    content = """
<div class="container">
<h4>Отчистка от пылевых и жировых загрязнений</h4>
<ul>
<li align="LEFT">Очистка и дезинфекция систем вентиляции проводится согласно санитарным нормам, установленным действующим законодательством страны. Согласно указанным нормативам, диагностика и дезинфекция воздуховодов проводится с разной периодичностью очистки, в зависимости от типа строения:</li>
<li align="LEFT">Рабочие офисы, административные и торговые центры &ndash; 1 раз в год;</li>
<li align="LEFT">Производственные и промышленные помещения - от 2 раз в год;</li>
<li align="LEFT">Организации общественного питания и здравоохранения &ndash; единожды в 3 месяца;</li>
<li align="LEFT">Образовательные учреждения &ndash; 2 раза в год.</li>
</ul>
<p align="LEFT"><strong>Регулярной чистке подвергаются следующие элементы вентиляционной системы:</strong></p>
<ul>
<li align="LEFT">Вытяжки и приемные устройства;</li>
<li align="LEFT">Огнезадерживающие клапаны, обратные и регулирующие заслонки;</li>
<li align="LEFT">Теплообменники калориферов;</li>
<li align="LEFT">Элементы конструкции вентиляторов;</li>
<li align="LEFT">Жировые фильтры;</li>
<li align="LEFT">Зонты местного отсоса;</li>
<li align="LEFT">Диффузоры.</li>
</ul>

<h3>Примеры</h3>
<img src="\static\images\clear\IMG_2325.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\clear\Процесс отмывки с полным демонтажом01.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\clear\Вентилятор ДО4.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\clear\Вентилятор и воздуховоды ДО17.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\clear\Фильтр до.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\clear\Фильтр после.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\clear\Вентилятор и воздуховоды После3.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\clear\Вентилятор ПОСЛЕ4.JPG" alt="" style="float: left;"  height="200" />
</div>
    """
    slogan = "Полное восстановление"
    return render_template('content.html', title=title, content=content, slogan=slogan)


@application.route('/check')
def check():
    title = "Проверка эффективности вентиляционных систем"
    content = """
<div class="container">
<h4 align="JUSTIFY">Проверка эффективности вентиляции</h4>
<p align="JUSTIFY">Цель вентиляции &ndash;&nbsp;обеспечение как минимум нормативного воздухообмена.</p>
<p align="JUSTIFY">Любое отклонения от нормативного воздухообмена в меньшую сторону вредно для здоровья. Воздуха не хватает для эффективного разбавления выделяющихся вредностей и поддержания приемлемой концентрации кислорода. В помещениях с людьми наиболее характерно повышение концентрации углекислого газа.</p>
<p align="LEFT"><strong>проверка эффективности вентиляционных систем проводится:</strong></p>
<ul>
<li>
<p align="LEFT">в помещениях с выделением горючих, взрывчатых, радиоактивных или ядовитых веществ I-II классов &ndash;&nbsp;1 раз в 30 дней;</p>
</li>
<li>
<p align="LEFT">в помещениях с приточно-вытяжными системами &ndash;&nbsp;1 раз в 12 месяцев;</p>
</li>
<li>
<p align="LEFT">в помещениях с естественной или механической общеобменной системой &ndash;&nbsp;1 раз в 36 месяцев.</p>
</li>
<li>
<p align="LEFT">Нормативные документы:</p>
</li>
<li>
<p align="LEFT">Выходные документы:</p>
</li>
</ul>

<h3>Примеры</h3>
<img src="\static\images\chek\IMG_9854.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\chek\IMG_9864.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\chek\IMG_9964.JPG" alt="" style="float: left;"  height="200" />
<img src="\static\images\chek\Проверка терморегулятора_исправен.PNG" alt="" style="float: left;"  height="200" />
<img src="\static\images\chek\Проверка терморегулятора_исправен.jpg" alt="" style="float: left;"  height="200" />
<img src="\static\images\chek\Протокол испытаний_Страница_3.jpg" alt="" style="float: left;"  height="200" />
<img src="\static\images\chek\Протокол испытаний_Страница_2.jpg" alt="" style="float: left;"  height="200" />
<img src="\static\images\chek\Протокол испытаний_Страница_1.jpg" alt="" style="float: left;"  height="200" />
<img src="\static\images\chek\Проверка терморегулятора_Не исправен.jpg" alt="" style="float: left;"  height="200" />
<img src="\static\images\chek\Проверка терморегулятора_Не исправен.PNG" alt="" style="float: left;"  height="200" />
</div>
    """
    slogan = "Работаем по высшим стандартам качества ISO9001"
    return render_template('content.html', title=title, content=content, slogan=slogan)

@application.route('/passport')
def passport():
    title = "Паспортизация вентиляционных систем"
    content = """
<div class="container">
<p>Паспортизация систем вентиляции &mdash; это проверка рабочего состояния вентиляционного оборудования и систем вентиляции с помощью инструментальных исследований, оформленная в виде паспорта на вентиляционную установку.</p>
<p>Паспортизация вентиляционных установок обязательна для всех предприятий и всех типов вентиляционных систем.</p>
<p>Согласно СанПиН 2.1.3.2630-10 все установленные и смонтированные системы механической приточно-вытяжной вентиляции должны иметь паспорт вентиляционной установки.</p>
<p>Перечень работ, выполняемых при паспортизации системы вентиляции</p>
<p>1. Визуальный осмотр. На этом этапе, как правило, выявляют типы, модели и серийные номера установленного оборудования.</p>
<p>2. Замеры. Посредством измерения определяют фактические размеры сечений воздуховодов, диаметров колёс и шкивов вентиляторов, электродвигателей и т. д. Для составления фактической схемы системы вентиляции определяют геометрические размеры сети, её верхние и нижние отметки, уровни расположения оборудования относительно чистого пола и т. п.</p>
<p>3. Испытания. Аэродинамические испытания вентиляционной системы, результаты которых необходимы для проведения паспортизации, проводят в соответствии с требованиями ГОСТ 12.3.018&ndash;79 &laquo;Система стандартов безопасности труда (ССБТ). Системы вентиляционные. Методы аэродинамических испытаний&raquo;.</p>
<p>4. Расчёты и обработка результатов. Первичные результаты замеров и испытаний используют для расчёта требуемых для паспорта показателей.</p>
</div>
"""
    slogan = "Наши паспорта - это знак качества"
    return render_template('content.html', title=title, content=content, slogan=slogan)

@application.route('/start')
def start():
    title = "Пусконаладочные работы в системах вентиляции"
    content = """
<div class="container">
<p>Пусконаладочные работы это завершающий этап монтажных работ.</p>
<p><strong>Для чего они нужны:</strong></p>
<p>1. Установить, насколько система соответствует данным проекта;</p>
<p>2. Провести оценку качества монтажных работ;</p>
<p>3. Оценить работу системы в период активной эксплуатации;</p>
<p>4. Оценить соответствие системы требованиям санитарных норм.</p>
<p><strong>Зачем делать с нами если это могут сделать монтажная организация которая монтировала вентиляцию?</strong></p>
<p>Потому что, Мы являемся независимой оценкой, нам все-равно кто монтировал, ВАЖНО чтобы установка работала как требует проект и правила.</p>
<p>А тем кто монтировал не захочет раскрывать свои недочеты и ошибки.</p>
<p>А с этим Вам придется разбираться самим в процессе эксплуатации.</p>
<h4>Этапы пусконаладочных работ:</h4>
<p>1.Подготовительный этап</p>
<p>Изучить и проанализировать проектную, рабочую и заводскую документацию на предмет правильности принятых решений по технологическим схемам, применяемому оборудованию, алгоритмам управления, защитам и блокировкам; определить соответствие проектной, рабочей документации требованиям нормативных документов, регламентирующих производство ПНР, типовым решениям; подготовить техническое заключение в виде рекомендаций и предложений по корректировке и улучшению отдельных частей проектной документации</p>
<p>2. Приемка из монтажа в наладку</p>
<p>3. Индивидуальные испытания оборудования</p>
<p>4. Поузловая наладка оборудования</p>
<p>5. Комплексное опробование установки</p>
</div>
    """
    slogan = "Делаем под ключ"
    return render_template('content.html', title=title, content=content, slogan=slogan)


@application.route('/about')
def about():
    title = "О нас"
    content = """
    <section id="about">
            <div class="container">

                <div class="row">
                    <div class="col-md-3 col-sm-3 col-xs-6">
                        <div class="about-item scrollpoint sp-effect2">
                            <i class="fa fa-expand fa-2x"></i>
                            <h3>Большая компания</h3>
                            <p>Офисы компании уже работают в 4 городах России:
								Москва,
								Санкт-Петербург,
								Новосибирск,
								Красноярск
							</p>
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-3 col-xs-6" >
                        <div class="about-item scrollpoint sp-effect5">
                            <i class="fa fa-angle-double-up fa-2x"></i>
                            <h3>Опыт 9 лет</h3>
                            <p>Вентиляционные системы это сложные инженерные объекты требующие колоссальный опыт и квалификацию.</p>
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-3 col-xs-6" >
                        <div class="about-item scrollpoint sp-effect5">
                            <i class="fa fa-certificate fa-2x"></i>
                            <h3>Менеджмент качества</h3>
                            <p>Работает по стандартам качества ISO 9001, располагаем всем спектром лицензий и допусков на проведения работ.</p>
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-3 col-xs-6" >
                        <div class="about-item scrollpoint sp-effect1">
                            <i class="fa fa-cubes fa-2x"></i>
                            <h3>Ресурс</h3>
                            <p>собственная производственная база и поставщики вентиляционного оборудования в том числе импортного производства</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    """
    slogan = "Большая инженерная компания"
    return render_template('content.html', title=title, content=content, slogan=slogan)

@application.route('/faq')
def faq():
    title = "Советы от мастеров"
    content = ""
    slogan = "Большая инженерная компания"
    return render_template('content.html', title=title, content=content, slogan=slogan)

@application.route('/uslugi')
def uslugi():
    title = "Наши услуги"
    content = """
<div class="container">
<ul>
<li>
<h4><a href="http://127.0.0.1:5000/diagnostics">Диагностика неисправностей систем вентиляции</a></h4>
</li>
<li>
<h4><a href="http://127.0.0.1:5000/service">Обслуживание вентиляционных установок</a></h4>
</li>
<li>
<h4><a href="http://127.0.0.1:5000/clear">Очистка от пылевых и жировых загрязнений</a></h4>
</li>
<li>
<h4><a href="http://127.0.0.1:5000/check">Проверка эффективности систем вентиляции</a></h4>
</li>
<li>
<h4><a href="http://127.0.0.1:5000/passport">Паспортизация вентиляционных систем</a></h4>
</li>
<li>
<h4><a href="http://127.0.0.1:5000/start">Пусконаладочные работы в системах вентиляции</a></h4>
</li>
</ul>
</div>
    """
    slogan = "Большая инженерная компания"
    return render_template('content.html', title=title, content=content, slogan=slogan)

@application.route('/call', methods=['POST'])
def call():
    fio = request.form['fio']
    phone = request.form['phone']
    if fio and phone:
        data = "https://sms.ru/sms/send?"
    return 'ok'

if __name__ == '__main__':
    application.run()
