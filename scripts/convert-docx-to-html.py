#!/usr/bin/env python3


import os 
import sys 
import glob
import copy
import mammoth
from bs4 import BeautifulSoup
import weasyprint



scripts_dir = os.path.dirname(os.path.abspath(sys.argv[0])) 
root_dir = scripts_dir.replace(scripts_dir.split("/")[-1], "")
raw_dir = root_dir + "media/raw/"

output_dir = raw_dir + "ouput/"
pdf_dir = root_dir + "media/general-flyers/"


para_compas_dir = root_dir + "para-compas/"
html_dir = para_compas_dir

para_compas_template = para_compas_dir + "para-compas-template.html"



lang_codes = {}
lang_codes["amharic"]        = "am"
lang_codes["arabic"]         = "ar"
lang_codes["bengali"]        = "bn"
lang_codes["english"]        = "en"
lang_codes["farsi"]          = "fa"
lang_codes["french"]         = "fr"
lang_codes["georgian"]       = "ka"
lang_codes["gujarati"]       = "gu"
lang_codes["haitian-creole"] = "ht"
lang_codes["hindi"]          = "hi"
lang_codes["kurdish"]        = "ku"
lang_codes["luganda"]        = "lg"
lang_codes["mandarin"]       = "zh"
lang_codes["nepali"]         = "ne"
lang_codes["pashto"]         = "ps"
lang_codes["portuguese"]     = "pt"
lang_codes["punjabi"]        = "pa"
lang_codes["russian"]        = "ru"
lang_codes["sinhala"]        = "si"
lang_codes["spanish"]        = "es"
lang_codes["swahili"]        = "sw"
lang_codes["tamil"]          = "ta"
lang_codes["turkish"]        = "tr"
lang_codes["ukrainian"]      = "uk"
lang_codes["urdu"]           = "ur"
lang_codes["uzbek"]          = "uz"
lang_codes["vietnamese"]     = "vi"





"""
Abkhazian 	ab
Afar 	aa
Afrikaans 	af
Akan 	ak
Albanian 	sq

Aragonese 	an
Armenian 	hy
Assamese 	as
Avaric 	av
Avestan 	ae
Aymara 	ay
Azerbaijani 	az
Bambara 	bm
Bashkir 	ba
Basque 	eu
Belarusian 	be

Bihari 	bh
Bislama 	bi
Bosnian 	bs
Breton 	br
Bulgarian 	bg
Burmese 	my
Catalan 	ca
Chamorro 	ch
Chechen 	ce
Chichewa, Chewa, Nyanja 	ny

Chinese (Simplified) 	zh-Hans
Chinese (Traditional) 	zh-Hant
Chuvash 	cv
Cornish 	kw
Corsican 	co
Cree 	cr
Croatian 	hr
Czech 	cs
Danish 	da
Divehi, Dhivehi, Maldivian 	dv
Dutch 	nl
Dzongkha 	dz

Esperanto 	eo
Estonian 	et
Ewe 	ee
Faroese 	fo
Fijian 	fj
Finnish 	fi

Fula, Fulah, Pulaar, Pular 	ff
Galician 	gl
Gaelic (Scottish) 	gd
Gaelic (Manx) 	gv

German 	de
Greek 	el
Greenlandic 	kl
Guarani 	gn

Haitian Creole 	ht
Hausa 	ha
Hebrew 	he
Herero 	hz

Hiri Motu 	ho
Hungarian 	hu
Icelandic 	is
Ido 	io
Igbo 	ig
Indonesian 	id, in
Interlingua 	ia
Interlingue 	ie
Inuktitut 	iu
Inupiak 	ik
Irish 	ga
Italian 	it
Japanese 	ja
Javanese 	jv
Kalaallisut, Greenlandic 	kl
Kannada 	kn
Kanuri 	kr
Kashmiri 	ks
Kazakh 	kk
Khmer 	km
Kikuyu 	ki
Kinyarwanda (Rwanda) 	rw
Kirundi 	rn
Kyrgyz 	ky
Komi 	kv
Kongo 	kg
Korean 	ko

Kwanyama 	kj
Lao 	lo
Latin 	la
Latvian (Lettish) 	lv
Limburgish ( Limburger) 	li
Lingala 	ln
Lithuanian 	lt
Luga-Katanga 	lu

Luxembourgish 	lb
Manx 	gv
Macedonian 	mk
Malagasy 	mg
Malay 	ms
Malayalam 	ml
Maltese 	mt
Maori 	mi
Marathi 	mr
Marshallese 	mh
Moldavian 	mo
Mongolian 	mn
Nauru 	na
Navajo 	nv
Ndonga 	ng
Northern Ndebele 	nd

Norwegian 	no
Norwegian bokmål 	nb
Norwegian nynorsk 	nn
Nuosu 	ii
Occitan 	oc
Ojibwe 	oj
Old Church Slavonic, Old Bulgarian 	cu
Oriya 	or
Oromo (Afaan Oromo) 	om
Ossetian 	os
Pāli 	pi

Polish 	pl

Quechua 	qu
Romansh 	rm
Romanian 	ro

Sami 	se
Samoan 	sm
Sango 	sg
Sanskrit 	sa
Serbian 	sr
Serbo-Croatian 	sh
Sesotho 	st
Setswana 	tn
Shona 	sn
Sichuan Yi 	ii
Sindhi 	sd

Siswati 	ss
Slovak 	sk
Slovenian 	sl
Somali 	so
Southern Ndebele 	nr

Sundanese 	su

Swati 	ss
Swedish 	sv
Tagalog 	tl
Tahitian 	ty
Tajik 	tg

Tatar 	tt
Telugu 	te
Thai 	th
Tibetan 	bo
Tigrinya 	ti
Tonga 	to
Tsonga 	ts
Turkish 	tr
Turkmen 	tk
Twi 	tw
Uyghur 	ug

Venda 	ve

Volapük 	vo
Wallon 	wa
Welsh 	cy
Wolof 	wo
Western Frisian 	fy
Xhosa 	xh
Yiddish 	yi, ji
Yoruba 	yo
Zhuang, Chuang 	za
Zulu 	zu
"""


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



def make_html_page(html_filename, template_soup, file):
    with open(file, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value # The generated HTML
        messages = result.messages # Any messages, such as warnings during conversion

        soup = BeautifulSoup(html, 'html.parser')

        page_soup = copy.copy(template_soup)

        page_soup.html['lang'] = iso639_code

        page_soup.head.title.string = translation_dict[(language, "Border Aid")]
        page_soup.header.h1.string = translation_dict[(language, "If You Are in a Border Camp")]
        
        hospital_label = translation_dict[(language, "If You Go to the Hospital")]
        hospital_btn = page_soup.new_tag("button")
        hospital_btn.string = hospital_label
        hospital_link = page_soup.find(attrs={'id': 'hospital-btn'})
        hospital_link.append(hospital_btn)

        home_label = translation_dict[(language, "Home Page")]
        home_btn = page_soup.new_tag("button")
        home_btn.string = home_label
        home_link = page_soup.find(attrs={'id': 'home-btn'})
        home_link.append(home_btn)

        skip_nav_msg = translation_dict[(language, "Skip to main content")]
        skip_nav_elem = page_soup.find(attrs={'id': 'skip-to-content'})
        skip_nav_elem.string = skip_nav_msg
        skip_nav_elem['title'] = skip_nav_msg

        oads_term_disclaimer = translation_dict[(language, "footer")]

        page_soup.footer.string = oads_term_disclaimer

        disclaimer_elem = page_soup.new_tag("a")
        disclaimer_elem.string = "*"
        disclaimer_elem['id'] = "jump-to-footer"
        disclaimer_elem['href'] = "#footer"
        disclaimer_elem['title'] = oads_term_disclaimer
        page_soup.header.h1.append(disclaimer_elem)

        page_soup.find(attrs={'id': 'hospital-btn'})['href'] = "./" + language + "/hospital.html"
        page_soup.find(attrs={'id': 'download-link'})['href'] = "../media/general-flyers/" + pdf_filename

        if ((language == "arabic") or (language == "farsi") or (language == "urdu") ):
            page_soup.body['class'] = "rtl-text"

        page_soup.main.insert(0, soup)

        with open(html_filename, "w") as html_outf:
            html_outf.write(page_soup.prettify())

        return page_soup


# add large "IN CASE OF EMERGENCY DIAL 911"
def make_pdf(pdf_filepath, page_soup):
    with open(pdf_filepath, "wb") as pdf_outf:

        # get rid of CSS stylesheets
        for link_elems in page_soup.find_all("link"): 
            link_elems.decompose()

        for btn_elems in page_soup.find_all("button"): 
            btn_elems.decompose()

        for nav in page_soup.find_all("nav"):
            nav.decompose()

        for f in page_soup.find_all("footer"):
            f.decompose()

        for f in page_soup.find_all(attrs={'id': 'jump-to-footer'}):
            f.decompose()

        with open("tmp.html", "w") as tmp_html:
            tmp_html.write(page_soup.prettify())

        pdf_outf.write(weasyprint.HTML("tmp.html").write_pdf())



def update_download_center(all_pdfs):
    all_jacumba_flyers = glob.glob(pdf_dir + "jacumba-flyer-*.pdf")

    for f in all_jacumba_flyers:
        basename = f.replace(pdf_dir, "").replace(".pdf", "")
        filename_segs = basename.split("-")
        lang = filename_segs[-1]
        if lang not in all_pdfs.keys():
            all_pdfs[lang] = f.replace(root_dir, "./")



    with open(root_dir + "index.html", "r") as index_html:
        index_soup = BeautifulSoup(index_html, 'html.parser')

        for l in all_pdfs.keys():

            downloadables = index_soup.find(attrs={'id': l + "-downloadables"})

            if downloadables is not None:
                jacumba_flyer_link = downloadables.find(attrs={'class': 'jacumba-flyer'})
                jacumba_flyer_link['href'] = all_pdfs[l]


    with open(root_dir + "index.html", "w") as html_outf:
        html_outf.write(index_soup.prettify())










with open(para_compas_template, "r") as template_file:
    template_text = template_file.read()
    template_soup = BeautifulSoup(template_text, 'html.parser')

os.chdir(raw_dir)

raw_docs = glob.glob("*.docx")

all_pdfs = {}

for file in raw_docs:

    filename_segs = file.split("-")
    translator = filename_segs[1].strip().lower()
    language = filename_segs[2].strip().lower()
    file_date_mmddyyyy = filename_segs[3].strip().replace(".docx", "").lower()

    iso639_code = lang_codes[language]

    month = file_date_mmddyyyy[0:2]
    day = file_date_mmddyyyy[2:4]
    year = file_date_mmddyyyy[4:]

    html_filename = html_dir + language + ".html"
    pdf_filename = "jacumba-flyer-" + month + "-" + day + "-" + year + "-" + translator + "-" + language + ".pdf"
    pdf_filepath = pdf_dir + pdf_filename

    page_soup = make_html_page(html_filename, template_soup, file)
    make_pdf(pdf_filepath, page_soup)

    all_pdfs[language] = pdf_filepath.replace(root_dir, "./")

update_download_center(all_pdfs)

"""
 <header>
<h1>
 If You Are in a Border Camp
 <a href="#footer" id="jump-to-footer" title="For ease of use by the migrants we serve, this site may refer to open air detention sites as 'border camps', 'outdoor holding sites', or similar. However, make no mistake: these are all still the same outdoor detention sites maintained by CBP.">
  *
 </a>
</h1>

<nav>

<a href="#main-content" id="skip-to-content" title="Skip to main content">
Skip to main content
</a>

 <a href="../index.html" id="home-btn" target="_self">
<button>
Home
  </button>
 </a>

<a href="./english/hospital.html" id="hospital-btn" target="_self">
<button>
If You Go to the Hospital
</button>
</a>

<a target="_self" href="./english/airport.html">
<button>If You Are at the Airport</button>
</a>

<a target="_self" href="./english/old-town-station.html">
<button>Old Town Transit Station</button>
</a>

<a target="_self" href="./english/legal.html">
<button>Legal Resources</button>
</a>

</nav>
  </header>

translation_dict[("", "If You Are at the Airport")] = ""
translation_dict[("", "Old Town Transit Station")] = ""
translation_dict[("", "Legal Resources")] = ""
"""