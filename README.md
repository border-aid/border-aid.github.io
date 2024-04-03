# border-aid.github.io

## Wed Development Technical References
[Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/HTML)

[W3Schools](https://www.w3schools.com/html/default.asp)

[template page/HTML cheat sheet](https://border-aid.github.io/template.html)


## Notes

`clean-pdfs.sh` is the script used to strip metadata from PDFs and optimize them. It uses [ExifTool](https://exiftool.org/) and [QPDF](https://github.com/qpdf/qpdf), and assumes that they have been downloaded and built already.



```python
translation_dict = {}

translation_dict[("arabic", "Border Aid")] = "المساعدات الحدودية"
translation_dict[("arabic", "If You Are in a Border Camp")] = "إذا كنت في معسكر حدودي"
translation_dict[("arabic", "Home Page")] = "الصفحة الرئيسية"
translation_dict[("arabic", "If You Go to the Hospital")] = "إذا ذهبت إلى المستشفى"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("arabic", "Skip to main content")] = "انتقل إلى المحتوى الرئيسي"
translation_dict[("arabic", "footer")] = """
لسهولة الاستخدام من قبل المهاجرين الذين نخدمهم، قد يشير هذا الموقع إلى مواقع الاحتجاز في الهواء الطلق باسم "معسكرات الحدود" أو "مواقع الاحتجاز الخارجية" أو ما شابه ذلك. ومع ذلك، لا تخطئ: فهذه كلها لا تزال نفس مواقع الاحتجاز الخارجية التي تديرها إدارة الجمارك وحماية الحدود.
"""



translation_dict[("bengali", "Border Aid")] = "সীমান্ত সাহায্য"
translation_dict[("bengali", "Border Aid")] = "সীমান্ত সাহায্য"
translation_dict[("bengali", "If You Are in a Border Camp")] = "আপনি যদি সীমান্ত ক্যাম্পে থাকেন"
translation_dict[("bengali", "Home Page")] = "হোম পেজ"
translation_dict[("bengali", "If You Go to the Hospital")] = "আপনি যদি হাসপাতালে যান"
translation_dict[("bengali", "If You Are at the Airport")] = ""
translation_dict[("bengali", "Old Town Transit Station")] = ""
translation_dict[("bengali", "Legal Resources")] = ""
translation_dict[("bengali", "Skip to main content")] = "স্কিপ করে মূল কন্টেন্ট এ যাও"
translation_dict[("bengali", "footer")] = "আমরা যে অভিবাসীদের পরিবেশন করি তাদের ব্যবহারের সহজতার জন্য, এই সাইটটি উন্মুক্ত বায়ু আটকের স্থানগুলিকে 'বর্ডার ক্যাম্প', 'আউটডোর হোল্ডিং সাইট' বা অনুরূপ হিসাবে উল্লেখ করতে পারে। যাইহোক, কোন ভুল করবেন না: এই সব এখনও একই বহিরঙ্গন আটক সাইট CBP দ্বারা রক্ষণাবেক্ষণ করা হয়."



translation_dict[("english", "Border Aid")] = "Border Aid"
translation_dict[("english", "If You Are in a Border Camp")] = "If You Are in a Border Camp"
translation_dict[("english", "Home Page")] = "Home"
translation_dict[("english", "If You Go to the Hospital")] = "If You Go to the Hospital"
translation_dict[("english", "If You Are at the Airport")] = "If You Are at the Airport"
translation_dict[("english", "Old Town Transit Station")] = "Old Town Transit Station"
translation_dict[("english", "Legal Resources")] = "Legal Resources"
translation_dict[("english", "Skip to main content")] = "Skip to main content"
translation_dict[("english", "footer")] = "For ease of use by the migrants we serve, this site may refer to open air detention sites as 'border camps', 'outdoor holding sites', or similar. However, make no mistake: these are all still the same outdoor detention sites maintained by CBP."



translation_dict[("farsi", "Border Aid")] = "کمک های مرزی"
translation_dict[("farsi", "If You Are in a Border Camp")] = "اگر در یک کمپ مرزی هستید"
translation_dict[("farsi", "Home Page")] = "صفحه نخست"
translation_dict[("farsi", "If You Go to the Hospital")] = "اگر به بیمارستان بروید"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("farsi", "Skip to main content")] = "رفتن به محتوای اصلی"
translation_dict[("farsi", "footer")] = "برای سهولت استفاده مهاجرانی که به آنها خدمت می کنیم، این سایت ممکن است به مکان های بازداشت در هوای آزاد به عنوان «کمپ های مرزی»، «محل نگهداری در فضای باز» یا موارد مشابه اشاره کند. با این حال، اشتباه نکنید: اینها هنوز همان مکان های بازداشت در فضای باز هستند که توسط CBP نگهداری می شوند."


translation_dict[("french", "Border Aid")] = "Aide Aux Frontières"
translation_dict[("french", "If You Are in a Border Camp")] = "Si vous êtes dans un camp frontalier"
translation_dict[("french", "Home Page")] = "page d'accueil"
translation_dict[("french", "If You Go to the Hospital")] = "Si vous allez à l'hôpital"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("french", "Skip to main content")] = "Passer au contenu principal"
translation_dict[("french", "footer")] = "Pour faciliter l'utilisation par les migrants que nous servons, ce site peut faire référence aux sites de détention en plein air comme « camps frontaliers », « sites de détention en plein air » ou similaires. Cependant, ne vous y trompez pas : ce sont toujours les mêmes sites de détention extérieurs entretenus par le CBP."



translation_dict[("georgian", "Border Aid")] = "სასაზღვრო დახმარება"
translation_dict[("georgian", "If You Are in a Border Camp")] = "თუ სასაზღვრო ბანაკში ხართ"
translation_dict[("georgian", "Home Page")] = "მთავარი გვერდი"
translation_dict[("georgian", "If You Go to the Hospital")] = "თუ საავადმყოფოში მიდიხარ"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("georgian", "Skip to main content")] = "გადადით მთავარ შინაარსზე"
translation_dict[("georgian", "footer")] = "იმ მიგრანტების მიერ, რომლებსაც ჩვენ ვემსახურებით, ამ საიტმა შეიძლება მოიხსენიოს ღია ცის ქვეშ დაკავების ადგილები, როგორც „სასაზღვრო ბანაკები“, „გარე მოთავსების ადგილები“ ან მსგავსი. თუმცა, არ შეცდეთ: ეს ყველაფერი ჯერ კიდევ იგივე გარე დაკავების ადგილებია, რომელსაც აწარმოებს CBP."



translation_dict[("gujarati", "Border Aid")] = "સરહદ સહાય"
translation_dict[("gujarati", "If You Are in a Border Camp")] = "જો તમે બોર્ડર કેમ્પમાં છો"
translation_dict[("gujarati", "Home Page")] = "હોમ પેજ"
translation_dict[("gujarati", "If You Go to the Hospital")] = "જો તમે હોસ્પિટલ જાઓ"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("gujarati", "Skip to main content")] = "મુખ્ય સામગ્રી પર જાઓ"
translation_dict[("gujarati", "footer")] = "અમે સેવા આપીએ છીએ તે સ્થળાંતર કરનારાઓ દ્વારા ઉપયોગમાં સરળતા માટે, આ સાઇટ ઓપન એર ડિટેન્શન સાઇટ્સને 'બોર્ડર કેમ્પ', 'આઉટડોર હોલ્ડિંગ સાઇટ્સ' અથવા સમાન તરીકે ઉલ્લેખ કરી શકે છે. જો કે, કોઈ ભૂલ કરશો નહીં: આ તમામ હજુ પણ CBP દ્વારા જાળવવામાં આવતી સમાન આઉટડોર ડિટેન્શન સાઇટ્સ છે."



translation_dict[("hindi", "Border Aid")] = "सीमा सहायता"
translation_dict[("hindi", "If You Are in a Border Camp")] = "यदि आप किसी सीमा शिविर में हैं"
translation_dict[("hindi", "Home Page")] = "होम पेज"
translation_dict[("hindi", "If You Go to the Hospital")] = "यदि आप अस्पताल जाते हैं"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("hindi", "Skip to main content")] = "मुख्य विषयवस्तु में जाएं"
translation_dict[("hindi", "footer")] = "जिन प्रवासियों की हम सेवा करते हैं उनके उपयोग में आसानी के लिए, यह साइट खुली हवा में हिरासत स्थलों को 'सीमा शिविर', 'आउटडोर होल्डिंग साइट' या इसी तरह के रूप में संदर्भित कर सकती है। हालाँकि, कोई गलती न करें: ये सभी अभी भी सीबीपी द्वारा बनाए गए वही बाहरी हिरासत स्थल हैं।"



translation_dict[("kurdish", "Border Aid")] = "Alîkariya Sînor"
translation_dict[("kurdish", "If You Are in a Border Camp")] = "eger hûn li kampeke sînor bin"
translation_dict[("kurdish", "Home Page")] = "rûpela malê"
translation_dict[("kurdish", "If You Go to the Hospital")] = "Ger hûn biçin nexweşxaneyê"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("kurdish", "Skip to main content")] = "Biçe ser naveroka sereke"
translation_dict[("kurdish", "footer")] = "Ji bo karanîna hêsan ji hêla koçberên ku em jê re xizmetê dikin, ev malper dibe ku cîhên binçavkirinê yên vekirî wekî 'kampên sînorî', 'cihên ragirtinê yên li derve', an jî mîna wan binav bike. Lêbelê, xelet nekin: ev hemî hîn jî heman cihên binçavkirinê yên li derve ne ku ji hêla CBP ve têne parastin."



translation_dict[("luganda", "Border Aid")] = "Obuyambi ku nsalo"
translation_dict[("luganda", "If You Are in a Border Camp")] = "Bw’oba oli mu nkambi y’ensalo"
translation_dict[("luganda", "Home Page")] = "Omuko gw'Awaka"
translation_dict[("luganda", "If You Go to the Hospital")] = "Bwogenda Mu Ddwaliro"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("luganda", "Skip to main content")] = "Buuka ku bikulu ebirimu"
translation_dict[("luganda", "footer")] = "Okusobola okwanguyirwa okukozesa ababundabunda be tuweereza, omukutu guno guyinza okuyita ebifo eby’okusibiramu abantu mu bbanga nga ‘enkambi z’ensalo’, ‘ebifo eby’ebweru w’okusibira abantu’, oba ebifaananako bwe bityo. Kyokka tokola nsobi: bino byonna bikyali bifo bye bimu eby’okusibirwamu abantu nga bikuumibwa CBP."



translation_dict[("mandarin", "Border Aid")] = "边境援助"
translation_dict[("mandarin", "If You Are in a Border Camp")] = "如果您在边境营地"
translation_dict[("mandarin", "Home Page")] = "主页"
translation_dict[("mandarin", "If You Go to the Hospital")] = "如果你去医院"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("mandarin", "Skip to main content")] = "跳至主要内容"
translation_dict[("mandarin", "footer")] = "为了便于我们服务的移民使用，本网站可能将露天拘留场所称为“边境营地”、“户外拘留场所”或类似名称。 但是，请不要误会：这些仍然是 CBP 维护的相同室外拘留场所。"



translation_dict[("nepali", "Border Aid")] = "सीमा सहायता"
translation_dict[("nepali", "If You Are in a Border Camp")] = "यदि तपाईं सीमा शिविरमा हुनुहुन्छ भने"
translation_dict[("nepali", "Home Page")] = "गृह पृष्ठ"
translation_dict[("nepali", "If You Go to the Hospital")] = "यदि तपाईं अस्पताल जानुहुन्छ"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("nepali", "Skip to main content")] = "मुख्य सामग्रीमा जानुहोस्"
translation_dict[("nepali", "footer")] = "हामीले सेवा गर्ने आप्रवासीहरूद्वारा प्रयोगको सहजताको लागि, यो साइटले 'सीमा शिविर', 'आउटडोर होल्डिङ साइटहरू', वा यस्तै रूपमा खुला वायु हिरासत साइटहरूलाई सन्दर्भ गर्न सक्छ। यद्यपि, कुनै गल्ती नगर्नुहोस्: यी सबै अझै पनि CBP द्वारा राखिएको उही बाहिरी नजरबन्द साइटहरू हुन्।"



translation_dict[("pashto", "Border Aid")] = "سرحدی مرسته"
translation_dict[("pashto", "Border Aid")] = "سرحدی مرسته"
translation_dict[("pashto", "If You Are in a Border Camp")] = "که تاسو په سرحدي کمپ کې یاست"
translation_dict[("pashto", "Home Page")] = "کور پاڼه"
translation_dict[("pashto", "If You Go to the Hospital")] = "که تاسو روغتون ته لاړ شئ"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("pashto", "Skip to main content")] = "اصلي منځپانګې ته لاړ شئ"
translation_dict[("pashto", "footer")] = """
د مهاجرینو د اسانتیا لپاره چې موږ یې خدمت کوو، دا سایټ کیدای شي د پرانیستې هوا توقیف ځایونو ته د "سرحد کمپونو"، "د بهر د ساتلو ځایونو"، یا ورته ورته اشاره وکړي. په هرصورت، هیڅ غلطي مه کوئ: دا ټول لاهم د ورته بهرنی توقیف ځایونه دي چې د CBP لخوا ساتل کیږي.
"""



translation_dict[("portuguese", "Border Aid")] = "Ajuda Fronteiriça"
translation_dict[("portuguese", "If You Are in a Border Camp")] = "Se você estiver em um acampamento fronteiriço"
translation_dict[("portuguese", "Home Page")] = "pagina inicial"
translation_dict[("portuguese", "If You Go to the Hospital")] = "Se você for ao hospital"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("portuguese", "Skip to main content")] = "Ir para o conteúdo principal"
translation_dict[("portuguese", "footer")] = "Para facilitar a utilização pelos migrantes que servimos, este site pode referir-se aos locais de detenção ao ar livre como “campos fronteiriços”, “locais de detenção ao ar livre” ou similares. No entanto, não se engane: estes ainda são os mesmos locais de detenção ao ar livre mantidos pelo CBP."



translation_dict[("punjabi", "Border Aid")] = "ਸਰਹੱਦੀ ਸਹਾਇਤਾ"
translation_dict[("punjabi", "If You Are in a Border Camp")] = "ਜੇਕਰ ਤੁਸੀਂ ਸਰਹੱਦੀ ਕੈਂਪ ਵਿੱਚ ਹੋ"
translation_dict[("punjabi", "Home Page")] = "ਮੁੱਖ ਪੰਨਾ"
translation_dict[("punjabi", "If You Go to the Hospital")] = "ਜੇਕਰ ਤੁਸੀਂ ਹਸਪਤਾਲ ਜਾਂਦੇ ਹੋ"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("punjabi", "Skip to main content")] = "ਮੁੱਖ ਸਮੱਗਰੀ ਤੇ ਜਾਓ"
translation_dict[("punjabi", "footer")] = "ਸਾਡੇ ਦੁਆਰਾ ਸੇਵਾ ਕਰਨ ਵਾਲੇ ਪ੍ਰਵਾਸੀਆਂ ਦੁਆਰਾ ਵਰਤੋਂ ਵਿੱਚ ਸੌਖ ਲਈ, ਇਹ ਸਾਈਟ ਓਪਨ ਏਅਰ ਡਿਟੈਂਸ਼ਨ ਸਾਈਟਾਂ ਨੂੰ 'ਬਾਰਡਰ ਕੈਂਪ', 'ਆਊਟਡੋਰ ਹੋਲਡਿੰਗ ਸਾਈਟਸ', ਜਾਂ ਇਸ ਤਰ੍ਹਾਂ ਦੇ ਤੌਰ 'ਤੇ ਹਵਾਲਾ ਦੇ ਸਕਦੀ ਹੈ। ਹਾਲਾਂਕਿ, ਕੋਈ ਗਲਤੀ ਨਾ ਕਰੋ: ਇਹ ਸਾਰੀਆਂ ਅਜੇ ਵੀ ਉਹੀ ਬਾਹਰੀ ਨਜ਼ਰਬੰਦੀ ਸਾਈਟ ਹਨ ਜੋ CBP ਦੁਆਰਾ ਬਣਾਈਆਂ ਜਾਂਦੀਆਂ ਹਨ।"



translation_dict[("russian", "Border Aid")] = "Пограничная помощь"
translation_dict[("russian", "If You Are in a Border Camp")] = "Если вы находитесь в пограничном лагере"
translation_dict[("russian", "Home Page")] = "Домашняя страница"
translation_dict[("russian", "If You Go to the Hospital")] = "Если вы пойдете в больницу"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("russian", "Skip to main content")] = "Перейти к основному содержанию"
translation_dict[("russian", "footer")] = "Для удобства использования мигрантами, которых мы обслуживаем, на этом сайте места содержания под открытым небом могут называться «пограничными лагерями», «местами содержания под открытым небом» и т.п. Однако не заблуждайтесь: это все те же места содержания под открытым небом, которые обслуживает CBP."



translation_dict[("sinhala", "Border Aid")] = "දේශසීමා ආධාර"
translation_dict[("sinhala", "If You Are in a Border Camp")] = "ඔබ මායිම් කඳවුරක සිටින්නේ නම්"
translation_dict[("sinhala", "Home Page")] = "මුල් පිටුව"
translation_dict[("sinhala", "If You Go to the Hospital")] = "ඔබ රෝහලට ගියොත්"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("sinhala", "Skip to main content")] = "ප්‍රධාන අන්තර්ගතය වෙත යන්න"
translation_dict[("sinhala", "footer")] = "අප සේවය කරන සංක්‍රමණිකයන්ගේ භාවිතයේ පහසුව සඳහා, මෙම වෙබ් අඩවිය විවෘත ගුවන් රැඳවුම් ස්ථාන 'දේශසීමා කඳවුරු', 'එළිමහන් රඳවන ස්ථාන' හෝ ඊට සමාන ලෙස සඳහන් කළ හැක. කෙසේ වෙතත්, කිසිදු වරදක් නොකරන්න: මේ සියල්ල තවමත් CBP විසින් පවත්වාගෙන යනු ලබන එළිමහන් රැඳවුම් ස්ථාන වේ."



translation_dict[("spanish", "Border Aid")] = "Asistencia Fronteriza"
translation_dict[("spanish", "If You Are in a Border Camp")] = "Si Estás en Un Campamento Fronterizo"
translation_dict[("spanish", "Home Page")] = "Página Principal"
translation_dict[("spanish", "If You Go to the Hospital")] = "Si Vas Al Hospital"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("spanish", "Skip to main content")] = "Saltar al contenido principal"
translation_dict[("spanish", "footer")] = "Para facilitar el uso por parte de los migrantes a los que servimos, este sitio puede referirse a los sitios de detención al aire libre como 'campamentos fronterizos', 'sitios de detención al aire libre' o similares. Sin embargo, no se equivoque: todos estos siguen siendo los mismos sitios de detención al aire libre mantenidos por la CBP."



translation_dict[("tamil", "Border Aid")] = "எல்லை உதவி"
translation_dict[("tamil", "If You Are in a Border Camp")] = "நீங்கள் ஒரு எல்லை முகாமில் இருந்தால்"
translation_dict[("tamil", "Home Page")] = "முகப்பு பக்கம்"
translation_dict[("tamil", "If You Go to the Hospital")] = "நீங்கள் மருத்துவமனைக்குச் சென்றால்"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("tamil", "Skip to main content")] = "முக்கிய உள்ளடக்கத்திற்கு செல்க"
translation_dict[("tamil", "footer")] = "நாங்கள் சேவை செய்யும் புலம்பெயர்ந்தோர் எளிதாகப் பயன்படுத்துவதற்கு, இந்தத் தளம் திறந்தவெளி தடுப்பு முகாம்களை 'எல்லை முகாம்கள்', 'வெளிப்புற ஹோல்டிங் தளங்கள்' அல்லது அது போன்றவற்றைக் குறிப்பிடலாம். இருப்பினும், எந்த தவறும் செய்யாதீர்கள்: இவை அனைத்தும் இன்னும் CBP ஆல் பராமரிக்கப்படும் அதே வெளிப்புற தடுப்புத் தளங்கள்."



translation_dict[("turkish", "Border Aid")] = "Sınır yardımı"
translation_dict[("turkish", "If You Are in a Border Camp")] = "Eğer bir sınır kampındaysanız"
translation_dict[("turkish", "Home Page")] = "Ana Sayfa"
translation_dict[("turkish", "If You Go to the Hospital")] = "Eğer Hastaneye Giderseniz"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("turkish", "Skip to main content")] = "Ana içeriğe atla"
translation_dict[("turkish", "footer")] = "Hizmet verdiğimiz göçmenlerin kullanım kolaylığı açısından bu site, açık hava gözaltı alanlarından 'sınır kampları', 'açık havada tutma alanları' veya benzeri isimlerle söz edebilir. Ancak hata yapmayın: bunların hepsi hala CBP'nin muhafaza ettiği açık hava gözaltı alanlarıdır."



translation_dict[("ukrainian", "Border Aid")] = "прикордонна допомога"
translation_dict[("ukrainian", "If You Are in a Border Camp")] = "Якщо ви в прикордонному таборі"
translation_dict[("ukrainian", "Home Page")] = "Домашня сторінка"
translation_dict[("ukrainian", "If You Go to the Hospital")] = "Якщо ви йдете в лікарню"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("ukrainian", "Skip to main content")] = "Перейти до основного вмісту"
translation_dict[("ukrainian", "footer")] = "Для зручності використання мігрантами, які ми обслуговуємо, цей сайт може називати місця утримання під відкритим небом «прикордонними таборами», «майданчиками просто неба» тощо. Однак не помиляйтесь: це все ті самі місця ув’язнення під відкритим небом, які підтримує CBP."



translation_dict[("urdu", "Border Aid")] = "سرحدی امداد"
translation_dict[("urdu", "If You Are in a Border Camp")] = "اگر آپ سرحدی کیمپ میں ہیں۔"
translation_dict[("urdu", "Home Page")] = "ہوم پیج"
translation_dict[("urdu", "If You Go to the Hospital")] = "اگر آپ ہسپتال جاتے ہیں۔"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("urdu", "Skip to main content")] = "مرکزی مواد پر جائیں۔"
translation_dict[("urdu", "footer")] = "ہم جن مہاجرین کی خدمت کرتے ہیں ان کے استعمال میں آسانی کے لیے، یہ سائٹ کھلی فضائی حراستی جگہوں کو 'بارڈر کیمپ'، 'آؤٹ ڈور ہولڈنگ سائٹس'، یا اسی طرح کا حوالہ دے سکتی ہے۔ تاہم، کوئی غلطی نہ کریں: یہ سب اب بھی وہی بیرونی حراستی سائٹیں ہیں جو CBP کے زیر انتظام ہیں۔"



translation_dict[("uzbek", "Border Aid")] = "Chegara yordami"
translation_dict[("uzbek", "If You Are in a Border Camp")] = "Agar siz chegara lagerida bo'lsangiz"
translation_dict[("uzbek", "Home Page")] = "Bosh sahifa"
translation_dict[("uzbek", "If You Go to the Hospital")] = "Agar siz kasalxonaga borsangiz"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("uzbek", "Skip to main content")] = "Asosiy tarkibga o'tish"
translation_dict[("uzbek", "footer")] = "Biz xizmat ko‘rsatayotgan migrantlar uchun qulaylik yaratish maqsadida ushbu sayt ochiq havoda saqlash joylarini “chegara lagerlari”, “ochiq havoda saqlash joylari” yoki shunga o‘xshash tarzda ko‘rsatishi mumkin. Biroq, xato qilmang: bularning barchasi CBP tomonidan boshqariladigan bir xil ochiq qamoqxonalardir."



translation_dict[("vietnamese", "Border Aid")] = "Viện trợ biên giới"
translation_dict[("vietnamese", "If You Are in a Border Camp")] = "Nếu bạn đang ở trong trại biên giới"
translation_dict[("vietnamese", "Home Page")] = "Trang chủ"
translation_dict[("vietnamese", "If You Go to the Hospital")] = "Nếu Bạn Đến Bệnh Viện"
translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
translation_dict[("vietnamese", "Skip to main content")] = "Chuyển đến nội dung chính"
translation_dict[("vietnamese", "footer")] = "Để những người di cư mà chúng tôi phục vụ dễ sử dụng, trang này có thể gọi các địa điểm giam giữ ngoài trời là 'trại biên giới', 'địa điểm giam giữ ngoài trời' hoặc tương tự. Tuy nhiên, đừng nhầm lẫn: đây vẫn là những địa điểm giam giữ ngoài trời do CBP duy trì."
```