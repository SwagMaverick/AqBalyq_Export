# -*- coding: utf-8 -*-
# All site text lives here. Edit a string, run `python3 build.py`, re-upload the `site` folder.

# Contact details shown on every page. security.txt expiry date is set in build.py.
CONTACT = {
    "phone": "+7 702 476 56 37",          # main number (Yermek), shown first
    "phone_href": "+77024765637",
    "whatsapp": "https://wa.me/77024765637",
    "phone2": "+7 777 199 17 99",         # second number
    "phone2_href": "+77771991799",
    "email": "aqbalyq2022@gmail.com",
    "site_url": "https://aqbalyq-export.netlify.app",  # must match the final Netlify name or domain
}

GRADES = ["20–40", "40–70", "70–120", "120–170", "170–230", "230–300", "300–500", "500–800", "800+"]

PHOTOS = [
    ("skinless-fillet-116g", "skinless", 116, None),
    ("skinless-fillet-184g", "skinless", 184, None),
    ("skin-on-fillet-286g-skin-side", "skinon", 286, "skin"),
    ("skinless-fillet-318g", "skinless", 318, None),
    ("skin-on-fillet-358g-flesh-side", "skinon", 358, "flesh"),
    ("skinless-fillet-422g", "skinless", 422, None),
    ("skin-on-fillet-594g-flesh-side", "skinon", 594, "flesh"),
    ("skinless-fillet-610g", "skinless", 610, None),
    ("skin-on-fillet-886g-skin-side", "skinon", 886, "skin"),
]

STEPS_MEDIA = ["p1-catch", "p2-fillet", "p3-grade", "p4-weigh", "p5-pack"]

T = {}

# ---------------------------------------------------------------- ENGLISH
T["en"] = dict(
    html_lang="en", path="/", thanks_path="/thanks/", num_sep=",",
    meta_title="Aq Balyq | Wild zander and perch fillets from Kazakhstan",
    meta_desc="Frozen IQF fillets of wild pike-perch (zander), perch and pike from the Aral Sea basin, Lake Balkhash and Lake Zaysan. EU-approved plant KZ N.01/G2-1622/E. Full reefer trucks to Europe.",
    skip="Skip to content",
    nav=[("products", "Products"), ("grades", "Size grades"), ("process", "Process"), ("quality", "Quality"), ("logistics", "Logistics"), ("contact", "Contact")],
    menu="Menu",
    cta_offer="Request an offer",
    cta_products="See products",
    hero_h1="Wild-caught zander and perch, filleted and frozen in Aralsk for European buyers.",
    hero_sub="Aq Balyq is a family fish business from Kazakhstan. We supply frozen fillets of wild freshwater fish to importers, wholesalers and foodservice distributors, by the full reefer truck.",
    video_label="Pike-perch fillets on the processing line in Aralsk",
    label_title="Frozen pike-perch fillet",
    label_rows=[("Species", "Sander lucioperca"), ("Catch", "Wild, seine nets"), ("Plant", "EU approval KZ N.01/G2-1622/E"), ("Carton", "5 kg, 4.5 kg net fish"), ("Shelf life", "24 months")],
    label_foot="Keep frozen at −18 °C or colder",

    about_h="A producer, not a trader",
    about_p=[
        "Our fish is caught wild in the Aral Sea basin, Lake Balkhash and Lake Zaysan, and processed at LLP Karashalan Balyk in Aralsk, a plant on the European Union’s official list of approved establishments.",
        "Since 2025 we have shipped full trucks of frozen fillets to importers in Poland, Germany, the Czech Republic and Lithuania. Buyers deal with one contact, a fixed specification and a document pack that is ready for EU border control.",
    ],
    about_facts=[("Since 2025", "regular truck shipments to the EU"), ("4 countries", "Poland, Germany, Czech Republic, Lithuania"), ("3 waters", "Aral Sea basin, Balkhash, Zaysan")],

    products_h="What we produce",
    products_intro="All products are frozen, with no phosphates or other additives. The glaze is potable water only, at 10% or 20%, at the buyer’s choice.",
    products_cols=["Product", "Species", "Format", "Size grades"],
    products=[
        ("Pike-perch (zander) fillet", "Sander lucioperca", "IQF, skin-on or skinless", "20–40 g up to 800+ g", True),
        ("Perch fillet", "Perca fluviatilis", "IQF", "20–40, 40–60, 60–80 g", False),
        ("Pike fillet", "Esox lucius", "IQF", "On request", False),
        ("Carp fillet", "Cyprinus carpio", "Frozen", "On request", False),
        ("Snakehead fillet", "Channa argus", "Frozen", "On request", False),
    ],
    grades_title="Pike-perch fillet grades, g",
    grades_note="Pin bones are not removed. Every grade is produced to order.",

    grades_h="Every grade, weighed",
    grades_p="Unedited photos from the plant floor, August 2026. One fillet on the scale per photo, from 116 g to 886 g.",
    ph_skinless="Skinless", ph_skinon="Skin-on", ph_skin="skin side", ph_flesh="flesh side", g="g",
    scroll_hint="Scroll sideways to see all grades",

    process_h="From the lake to the carton",
    steps=[
        ("Wild catch", "Fish is caught with seine nets in the Aral Sea basin, Lake Balkhash and Lake Zaysan, then brought to the plant in Aralsk."),
        ("Filleting and skinning", "Fillets are cut by hand. The skinless line goes through a skinning machine."),
        ("Grading", "Fillets are sorted into size grades from 20–40 g up to 800+ g."),
        ("Weighing", "Each lot is weighed so that every carton holds a guaranteed 4.5 kg of net fish."),
        ("Freezing and packing", "Individually quick frozen, glazed with potable water and packed in a food-grade bag inside a 5 kg carton with an English label for each lot."),
    ],

    quality_h="Documents your border inspection will ask for",
    quality=[
        ("EU-approved plant", "LLP Karashalan Balyk, approval No. KZ N.01/G2-1622/E. Cold store approval No. KZ N.01/W2-1875/E."),
        ("Certificates with every truck", "EU health certificate, veterinary certificate and a full set of customs documents."),
        ("Nothing added", "No phosphates, polyphosphates or water-retaining agents. Glaze tolerance +2% / −0% of the declared level."),
        ("Fixed net weight", "4.5 kg of fish in every carton. Only the glaze layer varies, never the fish."),
        ("Packaging for EU rules", "EAEU declarations of conformity for the bags and cartons. PPWR packaging information on request."),
    ],
    verify_link="Check the EU list of approved establishments",
    docs_note="Product specification, carton label and a sample health certificate are available on request.",
    docs_cta="Ask for the document pack",

    logistics_h="One truck, by the numbers",
    truck=[("Carton", "5 kg", "4.5 kg net fish"), ("Pallet", "120 cartons", "600 kg at 10% glaze"), ("Truck", "31 pallets", "3,720 cartons, 16,740 kg net fish")],
    times="×",
    terms=[("Delivery", "By road to the EU on DAP or CPT terms"), ("Shelf life", "24 months at −18 °C or colder"), ("Labelling", "English carton labels for each lot"), ("Delivered to", "Poland, Germany, Czech Republic, Lithuania")],

    partners_h="Who we want to work with",
    partners=["Seafood importers and wholesalers", "Foodservice distributors", "Processors buying zander and perch fillet", "Retail chains"],
    partners_p="We sell into the EU and are opening Switzerland, Canada and the CIS. Agents and trade representatives who work with fish buyers in these markets are welcome to contact us too.",

    contact_h="Request an offer",
    contact_p="Tell us the product, grade and volume. We reply with price, availability and the earliest loading date.",
    f_name="Your name", f_company="Company", f_country="Country", f_email="Email", f_phone="Phone or WhatsApp", f_optional="optional",
    f_products="Products", f_products_opts=["Pike-perch fillet", "Perch fillet", "Pike fillet", "Carp or snakehead fillet"],
    f_volume="Expected volume", f_volume_opts=["One truck", "1 truck per month", "2 or more trucks per month", "Not sure yet"],
    f_msg="Grades, glaze, destination or anything else", f_send="Send request",
    f_privacy="We use your details only to answer this request.",
    direct_h="Prefer to write directly?",
    contact_person="Yermek, export sales",
    rep_label="Commercial representative",
    rep="Sole proprietor YZY Marketing, Almaty, Kazakhstan",
    producer_label="Producer",
    producer="LLP Karashalan Balyk, 166 Baktybai Batyr St., Aralsk, Kyzylorda Region, Kazakhstan",
    footer_note="Aq Balyq. Wild freshwater fish fillets from Kazakhstan.",
    thanks_title="Request sent",
    thanks_p="Thank you. We will reply to the email you gave us with price, availability and the earliest loading date.",
    thanks_back="Back to the site",
    lang_names={"en": "EN", "ru": "RU", "kz": "KZ"},
)

# ---------------------------------------------------------------- RUSSIAN
T["ru"] = dict(
    html_lang="ru", path="/ru/", thanks_path="/ru/thanks/", num_sep=" ",
    meta_title="Aq Balyq | Филе дикого судака и окуня из Казахстана",
    meta_desc="Замороженное филе IQF дикого судака, окуня и щуки из бассейна Аральского моря, озёр Балхаш и Зайсан. Завод с евроодобрением KZ N.01/G2-1622/E. Полные рефрижераторы в Европу.",
    skip="Перейти к содержанию",
    nav=[("products", "Продукция"), ("grades", "Калибры"), ("process", "Производство"), ("quality", "Качество"), ("logistics", "Логистика"), ("contact", "Контакты")],
    menu="Меню",
    cta_offer="Запросить предложение",
    cta_products="Смотреть продукцию",
    hero_h1="Дикий судак и окунь, разделанные и замороженные в Аральске для покупателей в Европе.",
    hero_sub="Aq Balyq: семейный рыбный бизнес из Казахстана. Мы поставляем замороженное филе дикой пресноводной рыбы импортёрам, оптовикам и дистрибьюторам HoReCa полными рефрижераторами.",
    video_label="Филе судака на линии переработки в Аральске",
    label_title="Филе судака мороженое",
    label_rows=[("Вид", "Sander lucioperca"), ("Вылов", "Дикий, неводом"), ("Завод", "Евроодобрение KZ N.01/G2-1622/E"), ("Короб", "5 кг, 4,5 кг рыбы нетто"), ("Срок годности", "24 месяца")],
    label_foot="Хранить при −18 °C и ниже",

    about_h="Мы производитель, а не перекупщик",
    about_p=[
        "Наша рыба выловлена в дикой природе: в бассейне Аральского моря, на озёрах Балхаш и Зайсан. Переработка идёт на ТОО «Карашалан Балык» в Аральске. Завод входит в официальный список предприятий, одобренных Европейским союзом.",
        "С 2025 года мы отгружаем полные фуры замороженного филе импортёрам в Польше, Германии, Чехии и Литве. У покупателя один контакт, стабильная спецификация и пакет документов, готовый к ветеринарному контролю на границе ЕС.",
    ],
    about_facts=[("С 2025 года", "регулярные отгрузки фурами в ЕС"), ("4 страны", "Польша, Германия, Чехия, Литва"), ("3 водоёма", "бассейн Арала, Балхаш, Зайсан")],

    products_h="Что мы производим",
    products_intro="Вся продукция замороженная, без фосфатов и других добавок. Для глазури используется только питьевая вода, 10% или 20% на выбор покупателя.",
    products_cols=["Продукт", "Вид", "Формат", "Калибры"],
    products=[
        ("Филе судака", "Sander lucioperca", "IQF, с кожей или без кожи", "от 20–40 г до 800+ г", True),
        ("Филе окуня", "Perca fluviatilis", "IQF", "20–40, 40–60, 60–80 г", False),
        ("Филе щуки", "Esox lucius", "IQF", "По запросу", False),
        ("Филе сазана", "Cyprinus carpio", "Замороженное", "По запросу", False),
        ("Филе змееголова", "Channa argus", "Замороженное", "По запросу", False),
    ],
    grades_title="Калибры филе судака, г",
    grades_note="Межмышечная кость не удаляется. Каждый калибр производится под заказ.",

    grades_h="Каждый калибр на весах",
    grades_p="Фото без обработки с производства, август 2026 года. На каждом фото одно филе на весах, от 116 г до 886 г.",
    ph_skinless="Без кожи", ph_skinon="С кожей", ph_skin="сторона кожи", ph_flesh="сторона мяса", g="г",
    scroll_hint="Прокрутите вбок, чтобы увидеть все калибры",

    process_h="От озера до короба",
    steps=[
        ("Дикий вылов", "Рыбу ловят неводом в бассейне Аральского моря, на Балхаше и Зайсане и доставляют на завод в Аральске."),
        ("Разделка и снятие кожи", "Филе режут вручную. Филе без кожи проходит через шкуросъёмную машину."),
        ("Калибровка", "Филе сортируют по калибрам: от 20–40 г до 800+ г."),
        ("Взвешивание", "Каждую партию взвешивают, чтобы в каждом коробе было гарантированно 4,5 кг рыбы нетто."),
        ("Заморозка и упаковка", "Индивидуальная быстрая заморозка, глазурь питьевой водой, пищевой пакет в коробе 5 кг и этикетка на английском для каждой партии."),
    ],

    quality_h="Документы, которые спросят на границе",
    quality=[
        ("Завод с евроодобрением", "ТОО «Карашалан Балык», номер одобрения KZ N.01/G2-1622/E. Холодильник: KZ N.01/W2-1875/E."),
        ("Сертификаты с каждой фурой", "Ветеринарный сертификат ЕС, ветеринарное свидетельство и полный пакет таможенных документов."),
        ("Без добавок", "Без фосфатов, полифосфатов и влагоудерживающих агентов. Допуск по глазури +2% / −0% от заявленного уровня."),
        ("Фиксированный вес нетто", "4,5 кг рыбы в каждом коробе. Меняется только слой глазури, а не количество рыбы."),
        ("Упаковка по правилам ЕС", "Декларации соответствия ЕАЭС на пакеты и короба. Информация по PPWR по запросу."),
    ],
    verify_link="Проверить в списке одобренных предприятий ЕС",
    docs_note="Спецификация, образец этикетки и образец ветеринарного сертификата доступны по запросу.",
    docs_cta="Запросить пакет документов",

    logistics_h="Одна фура в цифрах",
    truck=[("Короб", "5 кг", "4,5 кг рыбы нетто"), ("Паллета", "120 коробов", "600 кг при глазури 10%"), ("Фура", "31 паллета", "3 720 коробов, 16 740 кг рыбы нетто")],
    times="×",
    terms=[("Доставка", "Автотранспортом в ЕС на условиях DAP или CPT"), ("Срок годности", "24 месяца при −18 °C и ниже"), ("Маркировка", "Этикетки на английском для каждой партии"), ("Поставляли в", "Польшу, Германию, Чехию, Литву")],

    partners_h="С кем мы хотим работать",
    partners=["Импортёры и оптовики рыбы", "Дистрибьюторы HoReCa", "Переработчики, покупающие филе судака и окуня", "Розничные сети"],
    partners_p="Мы продаём в ЕС и выходим на рынки Швейцарии, Канады и СНГ. Агентам и торговым представителям, работающим с покупателями рыбы на этих рынках, тоже будем рады.",

    contact_h="Запросить предложение",
    contact_p="Укажите продукт, калибр и объём. Мы ответим с ценой, наличием и ближайшей датой загрузки.",
    f_name="Ваше имя", f_company="Компания", f_country="Страна", f_email="Email", f_phone="Телефон или WhatsApp", f_optional="необязательно",
    f_products="Продукция", f_products_opts=["Филе судака", "Филе окуня", "Филе щуки", "Филе сазана или змееголова"],
    f_volume="Ожидаемый объём", f_volume_opts=["Одна фура", "1 фура в месяц", "2 и более фуры в месяц", "Пока не знаю"],
    f_msg="Калибры, глазурь, пункт назначения или другие детали", f_send="Отправить запрос",
    f_privacy="Мы используем ваши данные только для ответа на этот запрос.",
    direct_h="Хотите написать напрямую?",
    contact_person="Ермек, экспортные продажи",
    rep_label="Коммерческий представитель",
    rep="ИП «YZY Marketing», Алматы, Казахстан",
    producer_label="Производитель",
    producer="ТОО «Карашалан Балык», ул. Бактыбай батыра, 166, г. Аральск, Кызылординская область, Казахстан",
    footer_note="Aq Balyq. Филе дикой пресноводной рыбы из Казахстана.",
    thanks_title="Запрос отправлен",
    thanks_p="Спасибо. Мы ответим на указанный email с ценой, наличием и ближайшей датой загрузки.",
    thanks_back="Вернуться на сайт",
    lang_names={"en": "EN", "ru": "RU", "kz": "KZ"},
)

# ---------------------------------------------------------------- KAZAKH
T["kz"] = dict(
    html_lang="kk", path="/kz/", thanks_path="/kz/thanks/", num_sep=" ",
    meta_title="Aq Balyq | Қазақстандық жабайы көксерке мен алабұға филесі",
    meta_desc="Арал теңізі алабы, Балқаш және Зайсан көлдерінен ауланған жабайы көксерке, алабұға және шортанның мұздатылған IQF филесі. ЕО мақұлдаған зауыт KZ N.01/G2-1622/E. Еуропаға толық рефрижераторлармен жеткізу.",
    skip="Мазмұнға өту",
    nav=[("products", "Өнімдер"), ("grades", "Калибрлер"), ("process", "Өндіріс"), ("quality", "Сапа"), ("logistics", "Логистика"), ("contact", "Байланыс")],
    menu="Мәзір",
    cta_offer="Ұсыныс сұрау",
    cta_products="Өнімдерді көру",
    hero_h1="Жабайы көксерке мен алабұға: Арал қаласында бөлшектеліп, еуропалық сатып алушыларға мұздатылады.",
    hero_sub="Aq Balyq: Қазақстандағы отбасылық балық кәсібі. Біз жабайы тұщы су балығының мұздатылған филесін импорттаушыларға, көтерме саудагерлерге және HoReCa дистрибьюторларына толық рефрижераторлармен жеткіземіз.",
    video_label="Арал қаласындағы өңдеу желісіндегі көксерке филесі",
    label_title="Мұздатылған көксерке филесі",
    label_rows=[("Түрі", "Sander lucioperca"), ("Аулау", "Жабайы, ау-сүзекі"), ("Зауыт", "ЕО мақұлдауы KZ N.01/G2-1622/E"), ("Қорап", "5 кг, таза балық 4,5 кг"), ("Сақтау мерзімі", "24 ай")],
    label_foot="−18 °C және одан төмен температурада сақтаңыз",

    about_h="Біз делдал емес, өндірушіміз",
    about_p=[
        "Біздің балық Арал теңізі алабында, Балқаш және Зайсан көлдерінде жабайы түрде ауланады. Ол Арал қаласындағы «Қарашалаң Балық» ЖШС-да өңделеді. Бұл зауыт Еуропалық одақ мақұлдаған кәсіпорындардың ресми тізімінде бар.",
        "2025 жылдан бастап біз Польша, Германия, Чехия және Литвадағы импорттаушыларға мұздатылған филені толық фуралармен жөнелтіп келеміз. Сатып алушыда бір байланыс, тұрақты спецификация және ЕО шекарасындағы бақылауға дайын құжаттар топтамасы болады.",
    ],
    about_facts=[("2025 жылдан", "ЕО-ға тұрақты фура жөнелтілімдері"), ("4 ел", "Польша, Германия, Чехия, Литва"), ("3 су айдыны", "Арал алабы, Балқаш, Зайсан")],

    products_h="Біз не өндіреміз",
    products_intro="Барлық өнім мұздатылған, фосфаттар мен басқа қоспаларсыз. Глазурь тек ауыз су, сатып алушының таңдауы бойынша 10% немесе 20%.",
    products_cols=["Өнім", "Түрі", "Пішімі", "Калибрлер"],
    products=[
        ("Көксерке филесі", "Sander lucioperca", "IQF, терісімен немесе терісіз", "20–40 г-нан 800+ г-ға дейін", True),
        ("Алабұға филесі", "Perca fluviatilis", "IQF", "20–40, 40–60, 60–80 г", False),
        ("Шортан филесі", "Esox lucius", "IQF", "Сұрау бойынша", False),
        ("Сазан филесі", "Cyprinus carpio", "Мұздатылған", "Сұрау бойынша", False),
        ("Жыланбас филесі", "Channa argus", "Мұздатылған", "Сұрау бойынша", False),
    ],
    grades_title="Көксерке филесінің калибрлері, г",
    grades_note="Бұлшықет аралық сүйектер алынбайды. Әр калибр тапсырыс бойынша өндіріледі.",

    grades_h="Әр калибр таразыда",
    grades_p="Өндірістен өңделмеген фотолар, 2026 жылғы тамыз. Әр фотода таразыда бір филе, 116 г-нан 886 г-ға дейін.",
    ph_skinless="Терісіз", ph_skinon="Терісімен", ph_skin="тері жағы", ph_flesh="ет жағы", g="г",
    scroll_hint="Барлық калибрді көру үшін бүйірге айналдырыңыз",

    process_h="Көлден қорапқа дейін",
    steps=[
        ("Жабайы аулау", "Балық Арал теңізі алабында, Балқаш пен Зайсанда ау-сүзекімен ауланып, Арал қаласындағы зауытқа жеткізіледі."),
        ("Бөлшектеу және терісін сыпыру", "Филе қолмен кесіледі. Терісіз филе тері сыпыратын машинадан өтеді."),
        ("Калибрлеу", "Филе калибрлерге сұрыпталады: 20–40 г-нан 800+ г-ға дейін."),
        ("Өлшеу", "Әр қорапта кепілді 4,5 кг таза балық болуы үшін әр партия өлшенеді."),
        ("Мұздату және қаптау", "Жедел дара мұздату, ауыз сумен глазурьлеу, 5 кг қорап ішіндегі тағамдық пакет және әр партияға ағылшын тіліндегі заттаңба."),
    ],

    quality_h="Шекарада сұралатын құжаттар",
    quality=[
        ("ЕО мақұлдаған зауыт", "«Қарашалаң Балық» ЖШС, мақұлдау нөмірі KZ N.01/G2-1622/E. Тоңазытқыш қойма: KZ N.01/W2-1875/E."),
        ("Әр фурамен сертификаттар", "ЕО ветеринарлық сертификаты, ветеринарлық куәлік және кедендік құжаттардың толық топтамасы."),
        ("Қоспасыз", "Фосфаттар, полифосфаттар және ылғал ұстағыш заттар қолданылмайды. Глазурь бойынша рұқсат +2% / −0%."),
        ("Тұрақты таза салмақ", "Әр қорапта 4,5 кг балық. Тек глазурь қабаты өзгереді, балық мөлшері өзгермейді."),
        ("ЕО ережелеріне сай қаптама", "Пакеттер мен қораптарға ЕАЭО сәйкестік декларациялары. PPWR бойынша ақпарат сұрау бойынша беріледі."),
    ],
    verify_link="ЕО мақұлдаған кәсіпорындар тізімінен тексеру",
    docs_note="Спецификация, заттаңба үлгісі және ветеринарлық сертификат үлгісі сұрау бойынша беріледі.",
    docs_cta="Құжаттар топтамасын сұрау",

    logistics_h="Бір фура сандармен",
    truck=[("Қорап", "5 кг", "таза балық 4,5 кг"), ("Паллет", "120 қорап", "10% глазурьде 600 кг"), ("Фура", "31 паллет", "3 720 қорап, таза балық 16 740 кг")],
    times="×",
    terms=[("Жеткізу", "ЕО-ға автокөлікпен, DAP немесе CPT шарттарымен"), ("Сақтау мерзімі", "−18 °C және одан төмен температурада 24 ай"), ("Таңбалау", "Әр партияға ағылшын тіліндегі заттаңбалар"), ("Жеткізілген елдер", "Польша, Германия, Чехия, Литва")],

    partners_h="Кіммен жұмыс істегіміз келеді",
    partners=["Балық импорттаушылары мен көтерме саудагерлер", "HoReCa дистрибьюторлары", "Көксерке мен алабұға филесін сатып алатын өңдеушілер", "Бөлшек сауда желілері"],
    partners_p="Біз ЕО-ға сатамыз және Швейцария, Канада мен ТМД нарықтарына шығып жатырмыз. Осы нарықтарда балық сатып алушылармен жұмыс істейтін агенттер мен сауда өкілдерін де күтеміз.",

    contact_h="Ұсыныс сұрау",
    contact_p="Өнімді, калибрді және көлемді көрсетіңіз. Біз баға, қолжетімділік және ең жақын тиеу күнімен жауап береміз.",
    f_name="Атыңыз", f_company="Компания", f_country="Ел", f_email="Email", f_phone="Телефон немесе WhatsApp", f_optional="міндетті емес",
    f_products="Өнімдер", f_products_opts=["Көксерке филесі", "Алабұға филесі", "Шортан филесі", "Сазан немесе жыланбас филесі"],
    f_volume="Күтілетін көлем", f_volume_opts=["Бір фура", "Айына 1 фура", "Айына 2 және одан көп фура", "Әзірге белгісіз"],
    f_msg="Калибрлер, глазурь, баратын жер немесе басқа мәліметтер", f_send="Сұрау жіберу",
    f_privacy="Деректеріңізді тек осы сұрауға жауап беру үшін пайдаланамыз.",
    direct_h="Тікелей жазғыңыз келе ме?",
    contact_person="Ермек, экспорттық сату",
    rep_label="Коммерциялық өкіл",
    rep="«YZY Marketing» ЖК, Алматы, Қазақстан",
    producer_label="Өндіруші",
    producer="«Қарашалаң Балық» ЖШС, Бақтыбай батыр к-сі, 166, Арал қ., Қызылорда облысы, Қазақстан",
    footer_note="Aq Balyq. Қазақстандық жабайы тұщы су балығының филесі.",
    thanks_title="Сұрау жіберілді",
    thanks_p="Рақмет. Көрсетілген email-ге баға, қолжетімділік және ең жақын тиеу күнімен жауап береміз.",
    thanks_back="Сайтқа оралу",
    lang_names={"en": "EN", "ru": "RU", "kz": "KZ"},
)

# ---------------------------------------------------------------- ADDITIONS: privacy, consent, fraud warning, video controls
PRIVACY_UPDATED = "2026-10-20"

T["en"].update(
    privacy_path="/privacy/",
    privacy_link="Privacy notice",
    f_consent_a="I agree to the processing of my personal data as described in the ",
    f_consent_b="privacy notice",
    fraud_h="Payment safety",
    fraud_p="Our bank details are given only in the signed contract and invoice. We never change them by email or messenger. If you get a message about new bank details, call us before paying.",
    pause_video="Pause video", play_video="Play video",
    pause_clips="Pause videos", play_clips="Play videos",
    nf_title="Page not found", nf_p="This page does not exist. Go to the main page:",
    privacy_title="Privacy notice",
    privacy_updated="Last updated",
    privacy=[
        ("Who is responsible", "Sole proprietor YZY Marketing (ИП «YZY Marketing»), Almaty, Kazakhstan, is responsible for personal data collected through this website. Contact: {email}."),
        ("What we collect", "Only what you enter in the request form: name, company, country, email, phone or WhatsApp number if you give it, the products and volume you are interested in, and your message. We also record which language version of the site you used."),
        ("Why we collect it", "To answer your request, prepare a commercial offer and continue business correspondence with you. We do not use your data for advertising and do not sell or share it with anyone for their own purposes."),
        ("Legal basis", "Your consent, given by ticking the box in the form, and the steps needed to prepare a possible contract at your request."),
        ("Who processes it for us", "The site and its form are hosted by Netlify, Inc. (USA), which receives form submissions and forwards them to our email. Our email is provided by Google LLC (USA). This means your data is transferred outside Kazakhstan and outside the EU."),
        ("How long we keep it", "As long as needed to handle your request and any business relationship that follows, and no longer than 3 years after our last contact, unless the law requires us to keep it longer."),
        ("Cookies and tracking", "This site sets no cookies and uses no analytics, advertising or tracking scripts. The hosting provider keeps standard technical server logs, such as IP addresses, for security."),
        ("Your rights", "You can ask us what data we hold about you, ask us to correct or delete it, and withdraw your consent at any time by writing to {email}. Withdrawing consent does not affect processing that happened before."),
    ],
)

T["ru"].update(
    privacy_path="/ru/privacy/",
    privacy_link="Политика конфиденциальности",
    f_consent_a="Я согласен(на) на обработку моих персональных данных в соответствии с ",
    f_consent_b="политикой конфиденциальности",
    fraud_h="Безопасность платежей",
    fraud_p="Наши банковские реквизиты указываются только в подписанном договоре и счёте. Мы никогда не меняем их по email или в мессенджере. Если вы получили сообщение о новых реквизитах, позвоните нам до оплаты.",
    pause_video="Остановить видео", play_video="Включить видео",
    pause_clips="Остановить видео", play_clips="Включить видео",
    nf_title="Страница не найдена", nf_p="Такой страницы нет. Перейдите на главную:",
    privacy_title="Политика конфиденциальности",
    privacy_updated="Обновлено",
    privacy=[
        ("Кто отвечает за данные", "За персональные данные, собранные через этот сайт, отвечает ИП «YZY Marketing», Алматы, Казахстан. Контакт: {email}."),
        ("Какие данные мы собираем", "Только то, что вы указываете в форме запроса: имя, компанию, страну, email, телефон или WhatsApp (если укажете), интересующую продукцию и объём, а также ваше сообщение. Мы также фиксируем, какую языковую версию сайта вы использовали."),
        ("Зачем мы их собираем", "Чтобы ответить на ваш запрос, подготовить коммерческое предложение и вести с вами деловую переписку. Мы не используем ваши данные для рекламы и не продаём и не передаём их третьим лицам для их собственных целей."),
        ("Основание обработки", "Ваше согласие, которое вы даёте, отмечая галочку в форме, а также действия, необходимые для подготовки возможного договора по вашему запросу."),
        ("Кто обрабатывает данные по нашему поручению", "Сайт и форма размещены у Netlify, Inc. (США), который получает заявки и пересылает их на нашу почту. Нашу почту обслуживает Google LLC (США). Это означает, что ваши данные передаются за пределы Казахстана и ЕС."),
        ("Сколько мы храним данные", "Столько, сколько нужно для обработки запроса и последующего делового сотрудничества, но не дольше 3 лет после последнего контакта, если закон не требует хранить их дольше."),
        ("Cookies и отслеживание", "Сайт не устанавливает cookies и не использует аналитику, рекламные или отслеживающие скрипты. Хостинг-провайдер ведёт стандартные технические журналы сервера, например IP-адреса, в целях безопасности."),
        ("Ваши права", "Вы можете узнать, какие данные о вас у нас есть, попросить исправить или удалить их, а также отозвать согласие в любое время, написав на {email}. Отзыв согласия не влияет на обработку, проведённую до этого."),
    ],
)

T["kz"].update(
    privacy_path="/kz/privacy/",
    privacy_link="Құпиялылық саясаты",
    f_consent_a="Дербес деректерімнің ",
    f_consent_b="құпиялылық саясатына сәйкес өңделуіне келісемін",
    fraud_h="Төлем қауіпсіздігі",
    fraud_p="Біздің банк деректемелеріміз тек қол қойылған шарт пен шот-фактурада көрсетіледі. Біз оларды ешқашан email немесе мессенджер арқылы өзгертпейміз. Жаңа деректемелер туралы хабар алсаңыз, төлем жасамас бұрын бізге қоңырау шалыңыз.",
    pause_video="Бейнені тоқтату", play_video="Бейнені қосу",
    pause_clips="Бейнелерді тоқтату", play_clips="Бейнелерді қосу",
    nf_title="Бет табылмады", nf_p="Мұндай бет жоқ. Басты бетке өтіңіз:",
    privacy_title="Құпиялылық саясаты",
    privacy_updated="Жаңартылған күні",
    privacy=[
        ("Деректерге кім жауапты", "Осы сайт арқылы жиналған дербес деректерге «YZY Marketing» ЖК (Алматы, Қазақстан) жауапты. Байланыс: {email}."),
        ("Қандай деректер жиналады", "Тек сұрау формасына енгізгеніңіз: аты-жөні, компания, ел, email, телефон немесе WhatsApp (көрсетсеңіз), қызықтыратын өнім мен көлем және хабарламаңыз. Сондай-ақ сайттың қай тілдегі нұсқасын пайдаланғаныңыз белгіленеді."),
        ("Не үшін жинаймыз", "Сұрауыңызға жауап беру, коммерциялық ұсыныс дайындау және сізбен іскерлік хат алмасу үшін. Деректеріңізді жарнамаға пайдаланбаймыз, сатпаймыз және үшінші тұлғаларға олардың өз мақсаттары үшін бермейміз."),
        ("Өңдеу негізі", "Формадағы белгі арқылы берген келісіміңіз және сіздің сұрауыңыз бойынша ықтимал шартты дайындауға қажетті әрекеттер."),
        ("Біздің атымыздан кім өңдейді", "Сайт пен форма Netlify, Inc. (АҚШ) серверлерінде орналасқан, ол сұрауларды қабылдап, біздің поштамызға жібереді. Поштамызды Google LLC (АҚШ) қамтамасыз етеді. Яғни деректеріңіз Қазақстаннан және ЕО-дан тыс жерге беріледі."),
        ("Қанша уақыт сақтаймыз", "Сұрауды өңдеуге және одан кейінгі іскерлік қарым-қатынасқа қажет уақыт бойы, бірақ соңғы байланыстан кейін 3 жылдан аспайды, егер заң одан ұзақ сақтауды талап етпесе."),
        ("Cookies және бақылау", "Сайт cookies орнатпайды және аналитика, жарнама немесе бақылау скрипттерін пайдаланбайды. Хостинг провайдері қауіпсіздік үшін IP мекенжайлары сияқты стандартты техникалық журналдарды жүргізеді."),
        ("Сіздің құқықтарыңыз", "{email} мекенжайына жазып, сіз туралы қандай деректер бар екенін білуге, оларды түзетуді немесе жоюды сұрауға және келісіміңізді кез келген уақытта кері қайтарып алуға болады. Келісімді кері қайтарып алу оған дейінгі өңдеуге әсер етпейді."),
    ],
)
