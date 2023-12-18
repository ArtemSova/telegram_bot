from config_db.daily_holiday_db import HolidaySQL
from config_db.board_games import BoardGamesSQL


# Заполнение БД настолок
def board_games_db_fill():
    BoardGamesSQL().insert_board_games('Каркассон-Река')
    BoardGamesSQL().insert_board_games('7 Драконов')
    BoardGamesSQL().insert_board_games('Гномы-Вредители')
    BoardGamesSQL().insert_board_games('7 Чудес')
    BoardGamesSQL().insert_board_games('Каркассон')
    BoardGamesSQL().insert_board_games('Пряности')
    BoardGamesSQL().insert_board_games('Стамбул')
    BoardGamesSQL().insert_board_games('Билет на поезд Америка')
    BoardGamesSQL().insert_board_games('Билет на поезд Европа')
    BoardGamesSQL().insert_board_games('Цитадели')
    BoardGamesSQL().insert_board_games('Бункер')

# Заполнение БД празников
def holiday_db_fill():
    HolidaySQL().holidays(1, 1, 'Опохмелительный день!')
    HolidaySQL().holidays(1, 2, 'Всемирный день интроверта!')
    HolidaySQL().holidays(1, 3, 'Праздник сонного дня!')
    HolidaySQL().holidays(1, 4, 'День флирта!')
    HolidaySQL().holidays(1, 5, 'Международный разгрузочный день!')
    HolidaySQL().holidays(1, 6, 'День рождения Тани Катан!!!')
    HolidaySQL().holidays(1, 7, 'Рождество, православное!')
    HolidaySQL().holidays(1, 8, 'День вращения Земли!')
    HolidaySQL().holidays(1, 9, 'День авантюриста!')
    HolidaySQL().holidays(1, 10, 'Путанин день!')
    HolidaySQL().holidays(1, 11, 'Хозяйственный день!')
    HolidaySQL().holidays(1, 12, 'День чудака!')
    HolidaySQL().holidays(1, 13, 'Старый Новый Год!')
    HolidaySQL().holidays(1, 14, 'День «Приберитесь в своём доме»!')
    HolidaySQL().holidays(1, 15, 'Всемирный день шаурмы!')
    HolidaySQL().holidays(1, 16, 'День недоразумений!')
    HolidaySQL().holidays(1, 17, 'День нарушения новогодних обещаний!')
    HolidaySQL().holidays(1, 18, 'День снеговика!')
    HolidaySQL().holidays(1, 19, 'День апельсиновых сказок!')
    HolidaySQL().holidays(1, 20, 'Международный день фетиша!')
    HolidaySQL().holidays(1, 21, 'День объятий!')
    HolidaySQL().holidays(1, 22, 'Китайский Новый год!')
    HolidaySQL().holidays(1, 23, 'День рождения Азима!!!')
    HolidaySQL().holidays(1, 24, 'День рождения баночного пива!')
    HolidaySQL().holidays(1, 25, 'Татьянин день!')
    HolidaySQL().holidays(1, 26, 'День случайных направлений!')
    HolidaySQL().holidays(1, 27, 'Международный день портвейна!')
    HolidaySQL().holidays(1, 28, 'День снежных горок!')
    HolidaySQL().holidays(1, 29, 'Международный день без интернета!')
    HolidaySQL().holidays(1, 30, 'День воздушно-пузырчатой упаковки!')
    HolidaySQL().holidays(1, 31, 'День рождения русской водки!')
    HolidaySQL().holidays(2, 1, 'День рождения Димы!!!')
    HolidaySQL().holidays(2, 2, 'День самообновления!')
    HolidaySQL().holidays(2, 3, 'Международный день нежности!')
    HolidaySQL().holidays(2, 4, 'День чудесных чудаков!')
    HolidaySQL().holidays(2, 5, 'Всемирный день «Нутеллы»!')
    HolidaySQL().holidays(2, 6, 'Всемирный день отказа от мобильного телефона!')
    HolidaySQL().holidays(2, 7, 'Международный день безопасного интернета!')
    HolidaySQL().holidays(2, 8, 'Международный день шотландского виски!')
    HolidaySQL().holidays(2, 9, 'Международный день пиццы!')
    HolidaySQL().holidays(2, 10, 'День памяти Александра Сергеевича Пушкина!')
    HolidaySQL().holidays(2, 11, 'Всемирный день кино!')
    HolidaySQL().holidays(2, 12, 'День прокладывания тропинок!')
    HolidaySQL().holidays(2, 13, 'День русского мата!')
    HolidaySQL().holidays(2, 14, 'День всех влюбленных!')
    HolidaySQL().holidays(2, 15, 'День завязывания узелков на счастье!')
    HolidaySQL().holidays(2, 16, 'День свежего ананаса!')
    HolidaySQL().holidays(2, 17, 'День спонтанного проявления доброты!')
    HolidaySQL().holidays(2, 18, 'День, когда всё понятно без слов!')
    HolidaySQL().holidays(2, 19, 'Международный день перетягивания каната!')
    HolidaySQL().holidays(2, 20, 'День профессионального алкоголина!')
    HolidaySQL().holidays(2, 21, 'Международный день блина!')
    HolidaySQL().holidays(2, 22, 'Всемирный день размышлений!')
    HolidaySQL().holidays(2, 23, 'День защитника Отечества!')
    HolidaySQL().holidays(2, 24, 'Праздник съехавшей крыши!')
    HolidaySQL().holidays(2, 25, 'День открытия спирта!')
    HolidaySQL().holidays(2, 26, 'Прощёное Воскресенье (Проводы Масленицы)!')
    HolidaySQL().holidays(2, 27, 'Международный день оптимиста!')
    HolidaySQL().holidays(2, 28, 'День ухода зимы!')
    HolidaySQL().holidays(2, 29, 'День Кащея-Чернобога!')
    HolidaySQL().holidays(3, 1, 'Всемирный день комплимента!')
    HolidaySQL().holidays(3, 2, 'Международный день спички!')
    HolidaySQL().holidays(3, 3, 'День вкусного завтрака!')
    HolidaySQL().holidays(3, 4, 'Международный день игровых мастеров!')
    HolidaySQL().holidays(3, 5, 'Всенародный праздник без названия!')
    HolidaySQL().holidays(3, 6, 'Всероссийский день гурмана!')
    HolidaySQL().holidays(3, 7, 'День прогуливания уроков!')
    HolidaySQL().holidays(3, 8, 'Международный женский день!')
    HolidaySQL().holidays(3, 9, 'День нестандартно мыслящих людей!')
    HolidaySQL().holidays(3, 10, 'Международный день крутизны!')
    HolidaySQL().holidays(3, 11, 'День пандемии коронавируса!')
    HolidaySQL().holidays(3, 12, 'День запрета на уныние!')
    HolidaySQL().holidays(3, 13, 'День заглядывания в замочные скважины!')
    HolidaySQL().holidays(3, 14, 'День рождения бутерброда!')
    HolidaySQL().holidays(3, 15, 'Всемирный день защиты прав потребителя!')
    HolidaySQL().holidays(3, 16, 'День спонтанности!')
    HolidaySQL().holidays(3, 17, 'День святого Патрика!')
    HolidaySQL().holidays(3, 18, 'День яичницы!')
    HolidaySQL().holidays(3, 19, 'Профессиональный праздник самогонщиков!')
    HolidaySQL().holidays(3, 20, 'Международный день счастья!')
    HolidaySQL().holidays(3, 21, 'День песен на крыше!')
    HolidaySQL().holidays(3, 22, 'Хакасский Новый год «Чыл Пазы»!')
    HolidaySQL().holidays(3, 23, 'День атеиста!')
    HolidaySQL().holidays(3, 24, 'Международный день борьбы с депрессией!')
    HolidaySQL().holidays(3, 25, 'Международный день вафель!')
    HolidaySQL().holidays(3, 26, 'Всемирный день вермута!')
    HolidaySQL().holidays(3, 27, 'Международный день виски!')
    HolidaySQL().holidays(3, 28, 'День «Съешь эскимо»!')
    HolidaySQL().holidays(3, 29, 'День самопознания!')
    HolidaySQL().holidays(3, 30, 'День прогулки по парку!')
    HolidaySQL().holidays(3, 31, 'Международный день декольте!')
    HolidaySQL().holidays(4, 1, 'День смеха!')
    HolidaySQL().holidays(4, 2, 'Международный день проверки фактов!')
    HolidaySQL().holidays(4, 3, 'Всемирный день вечеринки!')
    HolidaySQL().holidays(4, 4, 'Международный день моркови!')
    HolidaySQL().holidays(4, 5, 'Международный день супа!')
    HolidaySQL().holidays(4, 6, 'Международный день асексуальности!')
    HolidaySQL().holidays(4, 7, 'Всемирный день здоровья!')
    HolidaySQL().holidays(4, 8, 'День сброса зимней шкурки!')
    HolidaySQL().holidays(4, 9, 'Международный день автономной сенсорной меридиональной реакции!')
    HolidaySQL().holidays(4, 10, 'День гречки!')
    HolidaySQL().holidays(4, 11, 'Праздник неумелых рук!')
    HolidaySQL().holidays(4, 12, 'Всемирный день авиации и космонавтики!')
    HolidaySQL().holidays(4, 13, 'Всемирный день рок-н-ролла!')
    HolidaySQL().holidays(4, 14, 'День «Посмотри на небо»!')
    HolidaySQL().holidays(4, 15, 'Международный день культуры и искусства!')
    HolidaySQL().holidays(4, 16, 'День добрых дел!')
    HolidaySQL().holidays(4, 17, 'Международный день кофе!')
    HolidaySQL().holidays(4, 18, 'День пляски в проснувшемся лесу!')
    HolidaySQL().holidays(4, 19, 'День велосипеда!')
    HolidaySQL().holidays(4, 20, 'Национальный день донора крови!')
    HolidaySQL().holidays(4, 21, 'Международный день пряника!')
    HolidaySQL().holidays(4, 22, 'Международный день Матери-Земли!')
    HolidaySQL().holidays(4, 23, 'Международный день ковыряния в носу!')
    HolidaySQL().holidays(4, 24, 'День рождения газированной воды!')
    HolidaySQL().holidays(4, 25, 'День бумажных самолётиков!')
    HolidaySQL().holidays(4, 26, 'День «Обними друга»!')
    HolidaySQL().holidays(4, 27, 'День «Обожаю твои бёдра»!')
    HolidaySQL().holidays(4, 28, 'Всемирный день охраны труда!')
    HolidaySQL().holidays(4, 29, 'Международный день танца!')
    HolidaySQL().holidays(4, 30, 'Международный день джаза!')
    HolidaySQL().holidays(5, 1, 'День международной солидарности трудящихся!')
    HolidaySQL().holidays(5, 2, 'Международный день ничегонеделания!')
    HolidaySQL().holidays(5, 3, 'Международный день хватания за грудь!')
    HolidaySQL().holidays(5, 4, 'День «Звёздных войн»!')
    HolidaySQL().holidays(5, 5, 'Международный день принцесс!')
    HolidaySQL().holidays(5, 6, 'Международный день против диеты!')
    HolidaySQL().holidays(5, 7, 'День рождения Артема!!!')
    HolidaySQL().holidays(5, 8, 'День перешагивания через ступеньку!')
    HolidaySQL().holidays(5, 9, 'День победы в ВОВ!')
    HolidaySQL().holidays(5, 10, 'День семейных трусов!')
    HolidaySQL().holidays(5, 11, 'День глаженых шнурков!')
    HolidaySQL().holidays(5, 12, 'Международный день синдрома хронической усталости!')
    HolidaySQL().holidays(5, 13, 'Всемирный день одуванчика!')
    HolidaySQL().holidays(5, 14, 'День большого бодуна!')
    HolidaySQL().holidays(5, 15, 'Международный день семьи!')
    HolidaySQL().holidays(5, 16, 'Праздник подлиз!')
    HolidaySQL().holidays(5, 17, 'День окарин, дудок и свистелок в своё удовольствие!')
    HolidaySQL().holidays(5, 18, 'Международный день сирени!')
    HolidaySQL().holidays(5, 19, 'День конной авиации!')
    HolidaySQL().holidays(5, 20, 'Всемирный день пчёл!')
    HolidaySQL().holidays(5, 21, 'Международный день чая!')
    HolidaySQL().holidays(5, 22, 'День винегрета!')
    HolidaySQL().holidays(5, 23, 'Праздник жевальщиков стирательных резинок!')
    HolidaySQL().holidays(5, 24, 'День валяния в траве!')
    HolidaySQL().holidays(5, 25, 'День полотенца!')
    HolidaySQL().holidays(5, 26, 'День хождения босиком!')
    HolidaySQL().holidays(5, 27, 'День смелых решений!')
    HolidaySQL().holidays(5, 28, 'День пофигиста!')
    HolidaySQL().holidays(5, 29, 'День гадания на ромашках!')
    HolidaySQL().holidays(5, 30, 'День рождения Зарины!!!')
    HolidaySQL().holidays(5, 31, 'День рождения Алены!!!')
    HolidaySQL().holidays(6, 1, 'Международный день защиты детей!')
    HolidaySQL().holidays(6, 2, 'Международный день блудниц!')
    HolidaySQL().holidays(6, 3, 'Всемирный день сидра!')
    HolidaySQL().holidays(6, 4, 'День любителей лета!')
    HolidaySQL().holidays(6, 5, 'Праздник солнечных зайчиков!')
    HolidaySQL().holidays(6, 6, 'День рисования драконов!')
    HolidaySQL().holidays(6, 7, 'День кувыркальщиков!')
    HolidaySQL().holidays(6, 8, 'День таинственных знаков и предсказаний!')
    HolidaySQL().holidays(6, 9, 'Международный день друзей!')
    HolidaySQL().holidays(6, 10, 'Всемирный день мороженого!')
    HolidaySQL().holidays(6, 11, 'День неукротимой страсти!')
    HolidaySQL().holidays(6, 12, 'День гуляния с воздушным шариком!')
    HolidaySQL().holidays(6, 13, 'День маленького путешествия!')
    HolidaySQL().holidays(6, 14, 'Международный банный день!')
    HolidaySQL().holidays(6, 15, 'Праздник мужских недостатков!')
    HolidaySQL().holidays(6, 16, 'День без оранжевой одежды!')
    HolidaySQL().holidays(6, 17, 'Всемирный день мартини!')
    HolidaySQL().holidays(6, 18, 'Всемирный день гармонии!')
    HolidaySQL().holidays(6, 19, 'День спиртоглотов!')
    HolidaySQL().holidays(6, 20, 'День рождения Андрея!!!')
    HolidaySQL().holidays(6, 21, 'Международный день медлительности!')
    HolidaySQL().holidays(6, 22, 'Праздник лоботрясов!')
    HolidaySQL().holidays(6, 23, 'День без обид!')
    HolidaySQL().holidays(6, 24, 'Всемирный день смурфиков!')
    HolidaySQL().holidays(6, 25, 'День улыбок незнакомым людям!')
    HolidaySQL().holidays(6, 26, 'День блаженства!')
    HolidaySQL().holidays(6, 27, 'День записывания случайных мыслей!')
    HolidaySQL().holidays(6, 28, 'Международный день пирсинга!')
    HolidaySQL().holidays(6, 29, 'Международный день грязи!')
    HolidaySQL().holidays(6, 30, 'День экономиста!')
    HolidaySQL().holidays(7, 1, 'Международный день шутки!')
    HolidaySQL().holidays(7, 2, 'Праздник трезвенников и язвенников!')
    HolidaySQL().holidays(7, 3, 'День рождения Сережи!')
    HolidaySQL().holidays(7, 4, 'День отдыха от праздников!')
    HolidaySQL().holidays(7, 5, 'Всемирный день бикини!')
    HolidaySQL().holidays(7, 6, 'Всемирный день поцелуя!')
    HolidaySQL().holidays(7, 7, 'Глобальный день прощения!')
    HolidaySQL().holidays(7, 8, 'Международный день купания нагишом!')
    HolidaySQL().holidays(7, 9, 'День фантазии и юмора!')
    HolidaySQL().holidays(7, 10, 'День Николы Теслы!')
    HolidaySQL().holidays(7, 11, 'Всемирный день шоколада!')
    HolidaySQL().holidays(7, 12, 'Всемирный день профилактики йододефицита!')
    HolidaySQL().holidays(7, 13, 'Международный день головоломки!')
    HolidaySQL().holidays(7, 14, 'Международный день плюшевого мишки!')
    HolidaySQL().holidays(7, 15, 'День русской лени!')
    HolidaySQL().holidays(7, 16, 'Всемирный день поэзии!')
    HolidaySQL().holidays(7, 17, 'Праздник куража')
    HolidaySQL().holidays(7, 18, 'День прогулок под дождём!')
    HolidaySQL().holidays(7, 19, 'День пирожков с малиновым вареньем!')
    HolidaySQL().holidays(7, 20, 'День рождения Маши!!!')
    HolidaySQL().holidays(7, 21, 'День "Пригласи инопланетянина жить с вами"!')
    HolidaySQL().holidays(7, 22, 'Международный день куриных крылышек!')
    HolidaySQL().holidays(7, 23, 'День заливной тоски!')
    HolidaySQL().holidays(7, 24, 'Международный день заботы о себе!')
    HolidaySQL().holidays(7, 25, 'День памяти Владимира Высоцкого!')
    HolidaySQL().holidays(7, 26, 'День рождения Насти!!!')
    HolidaySQL().holidays(7, 27, 'День рождения Лены!!!')
    HolidaySQL().holidays(7, 28, 'День загадывания желаний!')
    HolidaySQL().holidays(7, 29, 'День поворачивания налево!')
    HolidaySQL().holidays(7, 30, 'День цветных напитков!')
    HolidaySQL().holidays(7, 31, 'День вспоминания любимых книжек!')
    HolidaySQL().holidays(8, 1, 'День бумажных салфеток!')
    HolidaySQL().holidays(8, 2, 'День рождения Винни-Пуха!')
    HolidaySQL().holidays(8, 3, 'День арбуза!')
    HolidaySQL().holidays(8, 4, 'День качания на качелях!')
    HolidaySQL().holidays(8, 5, 'День разглядывания горизонта!')
    HolidaySQL().holidays(8, 6, 'Международный день подкаблучника!')
    HolidaySQL().holidays(8, 7, 'Праздник холостяка!')
    HolidaySQL().holidays(8, 8, 'Международный день кошек!')
    HolidaySQL().holidays(8, 9, 'День воздушных поцелуев!')
    HolidaySQL().holidays(8, 10, 'День попутного ветра!')
    HolidaySQL().holidays(8, 11, 'День вредной еды!')
    HolidaySQL().holidays(8, 12, 'Международный день повара!')
    HolidaySQL().holidays(8, 13, 'Международный день левшей!')
    HolidaySQL().holidays(8, 14, 'Праздник воспалённого воображения!')
    HolidaySQL().holidays(8, 15, 'День памяти Виктора Цоя!')
    HolidaySQL().holidays(8, 16, 'День малинового варенья!')
    HolidaySQL().holidays(8, 17, 'День секонд-хенда!')
    HolidaySQL().holidays(8, 18, 'День «Никогда не сдавайся»!')
    HolidaySQL().holidays(8, 19, 'Всемирный день фотографии!')
    HolidaySQL().holidays(8, 20, 'Всемирный день лени!')
    HolidaySQL().holidays(8, 21, 'День сбора диких трав!')
    HolidaySQL().holidays(8, 22, 'День растительного молока')
    HolidaySQL().holidays(8, 23, 'День полёта божьих коровок!')
    HolidaySQL().holidays(8, 24, 'День валяния в стоге сена!')
    HolidaySQL().holidays(8, 25, 'День лазанья по деревьям!')
    HolidaySQL().holidays(8, 26, 'День устраивания секретиков!')
    HolidaySQL().holidays(8, 27, 'День российского кино!')
    HolidaySQL().holidays(8, 28, 'День надутых губ!')
    HolidaySQL().holidays(8, 29, 'День гуляний по крышам!')
    HolidaySQL().holidays(8, 30, 'Международный день вина «Каберне Совиньон»!')
    HolidaySQL().holidays(8, 31, 'День шёпота травы!')
    HolidaySQL().holidays(9, 1, 'День любителей сериалов!')
    HolidaySQL().holidays(9, 2, 'Всемирный день бороды!')
    HolidaySQL().holidays(9, 3, 'Шуфутинов день, День прощания!')
    HolidaySQL().holidays(9, 4, 'Всемирный день сексуального здоровья!')
    HolidaySQL().holidays(9, 5, 'Международный день благотворительности!')
    HolidaySQL().holidays(9, 6, 'День рождения Леши!!!')
    HolidaySQL().holidays(9, 7, 'День рассказов о лете!')
    HolidaySQL().holidays(9, 8, 'Международный день грамотности!')
    HolidaySQL().holidays(9, 9, 'Международный день красоты!')
    HolidaySQL().holidays(9, 10, 'День портвейна!')
    HolidaySQL().holidays(9, 11, 'Всероссийский день трезвости!')
    HolidaySQL().holidays(9, 12, 'Международный день борьбы с мигренью!')
    HolidaySQL().holidays(9, 13, 'День шарлоток и осенних пирогов!')
    HolidaySQL().holidays(9, 14, 'Праздник междусобойщиков!')
    HolidaySQL().holidays(9, 15, 'Международный день точки!')
    HolidaySQL().holidays(9, 16, 'Международный день поедания яблок!')
    HolidaySQL().holidays(9, 17, 'Международный день гнома!')
    HolidaySQL().holidays(9, 18, 'День запахов пряностей для глинтвейна!')
    HolidaySQL().holidays(9, 19, 'Международный день подражания пиратам!')
    HolidaySQL().holidays(9, 20, 'День рождения Тани Скоробогатовой!!!')
    HolidaySQL().holidays(9, 21, 'Всемирный день русского единения!')
    HolidaySQL().holidays(9, 22, 'Всемирный день без автомобиля!')
    HolidaySQL().holidays(9, 23, 'День астрономии!')
    HolidaySQL().holidays(9, 24, 'День незапланированных безумств!')
    HolidaySQL().holidays(9, 25, 'Всемирный день мечты!')
    HolidaySQL().holidays(9, 26, 'Всемирный день контрацепции!')
    HolidaySQL().holidays(9, 27, 'День чешского пива!')
    HolidaySQL().holidays(9, 28, 'День тульского пряника!')
    HolidaySQL().holidays(9, 29, 'День осеннего одиночества!')
    HolidaySQL().holidays(9, 30, 'День мурлыканья и потягивания!')
    HolidaySQL().holidays(10, 1, 'День рождения Вити!!!')
    HolidaySQL().holidays(10, 2, 'Всемирный день без алкоголя!')
    HolidaySQL().holidays(10, 3, 'Всемирный день трезвости!')
    HolidaySQL().holidays(10, 4, 'День рождения Тани!!!')
    HolidaySQL().holidays(10, 5, 'День напутствий улетающим птицам!')
    HolidaySQL().holidays(10, 6, 'День висения на люстре!')
    HolidaySQL().holidays(10, 7, 'Международный день экономных развлечений!')
    HolidaySQL().holidays(10, 8, 'Всемирный день зомби!')
    HolidaySQL().holidays(10, 9, 'День любопытных событий!')
    HolidaySQL().holidays(10, 10, 'День шуршания листьями!')
    HolidaySQL().holidays(10, 11, 'Международный день каминг-аута!')
    HolidaySQL().holidays(10, 12, 'День шоколадных сюрпризов!')
    HolidaySQL().holidays(10, 13, 'День без бюстгальтера и День целомудрия!')
    HolidaySQL().holidays(10, 14, 'День плетения облаков!')
    HolidaySQL().holidays(10, 15, 'День плетения облаков!')
    HolidaySQL().holidays(10, 16, 'Всемирный день здорового питания!')
    HolidaySQL().holidays(10, 17, 'День посиделок при свечах!')
    HolidaySQL().holidays(10, 18, 'Всемирный день женского счастья!')
    HolidaySQL().holidays(10, 19, 'День мужского счастья!')
    HolidaySQL().holidays(10, 20, 'День пополнения запасов на зиму!')
    HolidaySQL().holidays(10, 21, 'День вымышленного праздника!')
    HolidaySQL().holidays(10, 22, 'Международный день защиты мужской нервной системы от насильственных действий со стороны женщины!')
    HolidaySQL().holidays(10, 23, 'День отбрасывания хвоста!')
    HolidaySQL().holidays(10, 24, 'День любви к тёплым носкам!')
    HolidaySQL().holidays(10, 25, 'Всемирный день макарон!')
    HolidaySQL().holidays(10, 26, 'Всемирная ночь воя на луну!')
    HolidaySQL().holidays(10, 27, 'Международный день шампанского!')
    HolidaySQL().holidays(10, 28, 'День домашнего печенья!')
    HolidaySQL().holidays(10, 29, 'День подушки!')
    HolidaySQL().holidays(10, 30, 'Всемирный день жизни!')
    HolidaySQL().holidays(10, 31, 'Хэллоуин!')
    HolidaySQL().holidays(11, 1, 'День гадания на кофейной гуще!')
    HolidaySQL().holidays(11, 2, 'День кормления птиц овсяным печеньем!')
    HolidaySQL().holidays(11, 3, 'День оладуше!')
    HolidaySQL().holidays(11, 4, 'Всемирный день мужчин!')
    HolidaySQL().holidays(11, 5, 'День варенья!')
    HolidaySQL().holidays(11, 6, 'День независимых, гордых и одиноких женщин!')
    HolidaySQL().holidays(11, 7, 'День холодца!')
    HolidaySQL().holidays(11, 8, 'Всемирный день без Wi-Fi!')
    HolidaySQL().holidays(11, 9, 'Всемирный день курицы!')
    HolidaySQL().holidays(11, 10, 'День просмотра чёрно-белого фильма!')
    HolidaySQL().holidays(11, 11, 'Международный день фитнеса!')
    HolidaySQL().holidays(11, 12, 'Международный день скороговорок!')
    HolidaySQL().holidays(11, 13, 'Всемирный день доброты!')
    HolidaySQL().holidays(11, 14, 'День расслабленности и беззаботности!')
    HolidaySQL().holidays(11, 15, 'День молочных коктейлей и шоколадного кекса!')
    HolidaySQL().holidays(11, 16, 'День рождения Андрея Цветкова!!!')
    HolidaySQL().holidays(11, 17, 'День знакомства с новым чаем!')
    HolidaySQL().holidays(11, 18, 'День придумывания секретов!')
    HolidaySQL().holidays(11, 19, 'День запаха свежего хлеба!')
    HolidaySQL().holidays(11, 20, 'Прекрасный день!')
    HolidaySQL().holidays(11, 21, 'День рождения Лины!!!')
    HolidaySQL().holidays(11, 22, 'День отогревания в кофейнях!')
    HolidaySQL().holidays(11, 23, 'День вставания с той ноги!')
    HolidaySQL().holidays(11, 24, 'Всемирный день отказа от покупок!')
    HolidaySQL().holidays(11, 25, 'День смотрения по сторонам!')
    HolidaySQL().holidays(11, 26, 'День переворачивания мира!')
    HolidaySQL().holidays(11, 27, 'Международный день гитариста!')
    HolidaySQL().holidays(11, 28, 'День пьяного ёжика!')
    HolidaySQL().holidays(11, 29, 'День счастливого человека!')
    HolidaySQL().holidays(11, 30, 'Международный день секса!')
    HolidaySQL().holidays(12, 1, 'День Антарктиды!')
    HolidaySQL().holidays(12, 2, 'Международный день духа игры!')
    HolidaySQL().holidays(12, 3, 'День положительных ответов!')
    HolidaySQL().holidays(12, 4, 'Международный день объятий!')
    HolidaySQL().holidays(12, 5, 'Самый несносный день в году!')
    HolidaySQL().holidays(12, 6, 'День лентяя!')
    HolidaySQL().holidays(12, 7, 'День собутыльника и собеседника!')
    HolidaySQL().holidays(12, 8, 'День путешественника во времени!')
    HolidaySQL().holidays(12, 9, 'День баянов!')
    HolidaySQL().holidays(12, 10, 'День сидения на окне!')
    HolidaySQL().holidays(12, 11, 'День близкого родственника!')
    HolidaySQL().holidays(12, 12, 'День почёсывания за ухом!')
    HolidaySQL().holidays(12, 13, 'Банный день!')
    HolidaySQL().holidays(12, 14, 'Совестливый день!')
    HolidaySQL().holidays(12, 15, 'Международный день чая!')
    HolidaySQL().holidays(12, 16, 'День грёз!')
    HolidaySQL().holidays(12, 17, 'Праздник утренних иллюзий!')
    HolidaySQL().holidays(12, 18, 'День рождения Паши К!!!')
    HolidaySQL().holidays(12, 19, 'День согласия!')
    HolidaySQL().holidays(12, 20, 'День трезвого взгляда на мир!')
    HolidaySQL().holidays(12, 21, 'День справедливости!')
    HolidaySQL().holidays(12, 22, 'День энергетика!')
    HolidaySQL().holidays(12, 23, 'День чужой жены!')
    HolidaySQL().holidays(12, 24, 'Покаянный день!')
    HolidaySQL().holidays(12, 25, 'День беспечности!')
    HolidaySQL().holidays(12, 26, 'День напрасных сожалений!')
    HolidaySQL().holidays(12, 27, 'День мудрых мыслей!')
    HolidaySQL().holidays(12, 28, 'День пешехода!')
    HolidaySQL().holidays(12, 29, 'Вселенский день нового русского!')
    HolidaySQL().holidays(12, 30, 'День рождения Паши и Леши!!!')
    HolidaySQL().holidays(12, 31, 'Новый год!!!')

# board_games_db_fill()
# holiday_db_fill()
