#!/usr/bin/env python3


import os 
import sys 
import glob
import copy
import mammoth
from bs4 import BeautifulSoup
import weasyprint



lang_codes = {}
lang_codes["english"]    = "en"
lang_codes["arabic"]     = "ar"
lang_codes["bengali"]    = "bn"
lang_codes["farsi"]      = "fa"
lang_codes["french"]     = "fr"
lang_codes["georgian"]   = "ka"
lang_codes["hindi"]      = "hi"
lang_codes["luganda"]    = "lg"
lang_codes["mandarin"]   = "zh"
lang_codes["nepali"]     = "ne"
lang_codes["pashto"]     = "ps"
lang_codes["portuguese"] = "pt"
lang_codes["russian"]    = "ru"
lang_codes["sinhala"]    = "si"
lang_codes["spanish"]    = "es"
lang_codes["tamil"]      = "ta"
lang_codes["turkish"]    = "tr"
lang_codes["urdu"]       = "ur"
lang_codes["uzbek"]      = "uz"
lang_codes["vietnamese"] = "vi"
lang_codes["gujarati"]   = "gu"
lang_codes["punjabi"]    = "pa"
lang_codes["ukrainian"]  = "uk"
lang_codes["kurdish"]    = "ku"
#lang_codes[""] = ""
#lang_codes[""] = ""




translation_dict = {}
translation_dict[("english", "Border Aid")] = "Border Aid"
translation_dict[("arabic", "Border Aid")] = "المساعدات الحدودية"
translation_dict[("bengali", "Border Aid")] = "সীমান্ত সাহায্য"
translation_dict[("mandarin", "Border Aid")] = "边境援助"
translation_dict[("french", "Border Aid")] = "Aide Aux Frontières"
translation_dict[("georgian", "Border Aid")] = "სასაზღვრო დახმარება"
translation_dict[("gujarati", "Border Aid")] = "સરહદ સહાય"
translation_dict[("hindi", "Border Aid")] = "सीमा सहायता"
translation_dict[("kurdish", "Border Aid")] = "Alîkariya Sînor"
translation_dict[("nepali", "Border Aid")] = "सीमा सहायता"
translation_dict[("pashto", "Border Aid")] = "سرحدی مرسته"
translation_dict[("portuguese", "Border Aid")] = "Ajuda Fronteiriça"
translation_dict[("punjabi", "Border Aid")] = "ਸਰਹੱਦੀ ਸਹਾਇਤਾ"
translation_dict[("russian", "Border Aid")] = "Пограничная помощь"
translation_dict[("spanish", "Border Aid")] = "Asistencia Fronteriza"
translation_dict[("turkish", "Border Aid")] = "Sınır yardımı"
translation_dict[("ukrainian", "Border Aid")] = "прикордонна допомога"
translation_dict[("urdu", "Border Aid")] = "سرحدی امداد"
translation_dict[("uzbek", "Border Aid")] = "Chegara yordami"
translation_dict[("vietnamese", "Border Aid")] = "Viện trợ biên giới"
translation_dict[("luganda", "Border Aid")] = "Obuyambi ku nsalo"


translation_dict[("english", "If You Are in a Border Camp")] = "If You Are in a Border Camp"
translation_dict[("arabic", "If You Are in a Border Camp")] = "إذا كنت في معسكر حدودي"
translation_dict[("bengali", "If You Are in a Border Camp")] = "আপনি যদি সীমান্ত ক্যাম্পে থাকেন"
translation_dict[("mandarin", "If You Are in a Border Camp")] = "如果您在边境营地"
translation_dict[("french", "If You Are in a Border Camp")] = "Si vous êtes dans un camp frontalier"
translation_dict[("georgian", "If You Are in a Border Camp")] = "თუ სასაზღვრო ბანაკში ხართ"
translation_dict[("gujarati", "If You Are in a Border Camp")] = "જો તમે બોર્ડર કેમ્પમાં છો"
translation_dict[("hindi", "If You Are in a Border Camp")] = "यदि आप किसी सीमा शिविर में हैं"
translation_dict[("kurdish", "If You Are in a Border Camp")] = "eger hûn li kampeke sînor bin"
translation_dict[("nepali", "If You Are in a Border Camp")] = "यदि तपाईं सीमा शिविरमा हुनुहुन्छ भने"
translation_dict[("pashto", "If You Are in a Border Camp")] = "که تاسو په سرحدي کمپ کې یاست"
translation_dict[("portuguese", "If You Are in a Border Camp")] = "Se você estiver em um acampamento fronteiriço"
translation_dict[("punjabi", "If You Are in a Border Camp")] = "ਜੇਕਰ ਤੁਸੀਂ ਸਰਹੱਦੀ ਕੈਂਪ ਵਿੱਚ ਹੋ"
translation_dict[("russian", "If You Are in a Border Camp")] = "Если вы находитесь в пограничном лагере"
translation_dict[("spanish", "If You Are in a Border Camp")] = "Si Estás en Un Campamento Fronterizo"
translation_dict[("turkish", "If You Are in a Border Camp")] = "Eğer bir sınır kampındaysanız"
translation_dict[("ukrainian", "If You Are in a Border Camp")] = "Якщо ви в прикордонному таборі"
translation_dict[("urdu", "If You Are in a Border Camp")] = "اگر آپ سرحدی کیمپ میں ہیں۔"
translation_dict[("uzbek", "If You Are in a Border Camp")] = "Agar siz chegara lagerida bo'lsangiz"
translation_dict[("vietnamese", "If You Are in a Border Camp")] = "Nếu bạn đang ở trong trại biên giới"
translation_dict[("luganda", "If You Are in a Border Camp")] = "Bw’oba oli mu nkambi y’ensalo"

# Home Page
translation_dict[("english", "Home Page")] = "Home"
translation_dict[("arabic", "Home Page")] = "الصفحة الرئيسية"
translation_dict[("bengali", "Home Page")] = "হোম পেজ"
translation_dict[("mandarin", "Home Page")] = "主页"
translation_dict[("french", "Home Page")] = "page d'accueil"
translation_dict[("georgian", "Home Page")] = "მთავარი გვერდი"
translation_dict[("gujarati", "Home Page")] = "હોમ પેજ"
translation_dict[("hindi", "Home Page")] = "होम पेज"
translation_dict[("kurdish", "Home Page")] = "rûpela malê"
translation_dict[("nepali", "Home Page")] = "गृह पृष्ठ"
translation_dict[("pashto", "Home Page")] = "کور پاڼه"
translation_dict[("portuguese", "Home Page")] = "pagina inicial"
translation_dict[("punjabi", "Home Page")] = "ਮੁੱਖ ਪੰਨਾ"
translation_dict[("russian", "Home Page")] = "Домашняя страница"
translation_dict[("spanish", "Home Page")] = "página principal"
translation_dict[("turkish", "Home Page")] = "Ana Sayfa"
translation_dict[("ukrainian", "Home Page")] = "Домашня сторінка"
translation_dict[("urdu", "Home Page")] = "ہوم پیج"
translation_dict[("uzbek", "Home Page")] = "Bosh sahifa"
translation_dict[("vietnamese", "Home Page")] = "Trang chủ"
translation_dict[("luganda", "Home Page")] = "Omuko gw'Awaka"


# If You Go to the Hospital
translation_dict[("english", "If You Go to the Hospital")] = "If You Go to the Hospital"
translation_dict[("arabic", "If You Go to the Hospital")] = "إذا ذهبت إلى المستشفى"
translation_dict[("bengali", "If You Go to the Hospital")] = "আপনি যদি হাসপাতালে যান"
translation_dict[("mandarin", "If You Go to the Hospital")] = "如果你去医院"
translation_dict[("french", "If You Go to the Hospital")] = "Si vous allez à l'hôpital"
translation_dict[("georgian", "If You Go to the Hospital")] = "თუ საავადმყოფოში მიდიხარ"
translation_dict[("gujarati", "If You Go to the Hospital")] = "જો તમે હોસ્પિટલ જાઓ"
translation_dict[("hindi", "If You Go to the Hospital")] = "यदि आप अस्पताल जाते हैं"
translation_dict[("kurdish", "If You Go to the Hospital")] = "Ger hûn biçin nexweşxaneyê"
translation_dict[("nepali", "If You Go to the Hospital")] = "यदि तपाईं अस्पताल जानुहुन्छ"
translation_dict[("pashto", "If You Go to the Hospital")] = "که تاسو روغتون ته لاړ شئ"
translation_dict[("portuguese", "If You Go to the Hospital")] = "Se você for ao hospital"
translation_dict[("punjabi", "If You Go to the Hospital")] = "ਜੇਕਰ ਤੁਸੀਂ ਹਸਪਤਾਲ ਜਾਂਦੇ ਹੋ"
translation_dict[("russian", "If You Go to the Hospital")] = "Если вы пойдете в больницу"
translation_dict[("spanish", "If You Go to the Hospital")] = "Si vas al hospital"
translation_dict[("turkish", "If You Go to the Hospital")] = "Eğer Hastaneye Giderseniz"
translation_dict[("ukrainian", "If You Go to the Hospital")] = "Якщо ви йдете в лікарню"
translation_dict[("urdu", "If You Go to the Hospital")] = "اگر آپ ہسپتال جاتے ہیں۔"
translation_dict[("uzbek", "If You Go to the Hospital")] = "Agar siz kasalxonaga borsangiz"
translation_dict[("vietnamese", "If You Go to the Hospital")] = "Nếu Bạn Đến Bệnh Viện"
translation_dict[("luganda", "If You Go to the Hospital")] = "Bwogenda Mu Ddwaliro"


# Skip to main content
translation_dict[("english", "Skip to main content")] = "Skip to main content"
translation_dict[("arabic", "Skip to main content")] = "انتقل إلى المحتوى الرئيسي"
translation_dict[("bengali", "Skip to main content")] = "স্কিপ করে মূল কন্টেন্ট এ যাও"
translation_dict[("mandarin", "Skip to main content")] = "跳至主要内容"
translation_dict[("french", "Skip to main content")] = "Passer au contenu principal"
translation_dict[("georgian", "Skip to main content")] = "გადადით მთავარ შინაარსზე"
translation_dict[("gujarati", "Skip to main content")] = "મુખ્ય સામગ્રી પર જાઓ"
translation_dict[("hindi", "Skip to main content")] = "मुख्य विषयवस्तु में जाएं"
translation_dict[("kurdish", "Skip to main content")] = "Biçe ser naveroka sereke"
translation_dict[("nepali", "Skip to main content")] = "मुख्य सामग्रीमा जानुहोस्"
translation_dict[("pashto", "Skip to main content")] = "اصلي منځپانګې ته لاړ شئ"
translation_dict[("portuguese", "Skip to main content")] = "Ir para o conteúdo principal"
translation_dict[("punjabi", "Skip to main content")] = "ਮੁੱਖ ਸਮੱਗਰੀ ਤੇ ਜਾਓ"
translation_dict[("russian", "Skip to main content")] = "Перейти к основному содержанию"
translation_dict[("spanish", "Skip to main content")] = "Saltar al contenido principal"
translation_dict[("turkish", "Skip to main content")] = "Ana içeriğe atla"
translation_dict[("ukrainian", "Skip to main content")] = "Перейти до основного вмісту"
translation_dict[("urdu", "Skip to main content")] = "مرکزی مواد پر جائیں۔"
translation_dict[("uzbek", "Skip to main content")] = "Asosiy tarkibga o'tish"
translation_dict[("vietnamese", "Skip to main content")] = "Chuyển đến nội dung chính"
translation_dict[("luganda", "Skip to main content")] = "Buuka ku bikulu ebirimu"


# For ease of use by the migrants we serve, this site may refer to open air detention sites as 'border camps', 'outdoor holding sites', or similar. However, make no mistake: these are all still the same outdoor detention sites maintained by CBP.
translation_dict[("english", "footer")] = "For ease of use by the migrants we serve, this site may refer to open air detention sites as 'border camps', 'outdoor holding sites', or similar. However, make no mistake: these are all still the same outdoor detention sites maintained by CBP."
translation_dict[("arabic", "footer")] = ""
translation_dict[("bengali", "footer")] = ""
translation_dict[("mandarin", "footer")] = ""
translation_dict[("french", "footer")] = ""
translation_dict[("georgian", "footer")] = ""
translation_dict[("gujarati", "footer")] = ""
translation_dict[("hindi", "footer")] = ""
translation_dict[("kurdish", "footer")] = ""
translation_dict[("nepali", "footer")] = ""
translation_dict[("pashto", "footer")] = ""
translation_dict[("portuguese", "footer")] = ""
translation_dict[("punjabi", "footer")] = ""
translation_dict[("russian", "footer")] = ""
translation_dict[("spanish", "footer")] = ""
translation_dict[("turkish", "footer")] = ""
translation_dict[("ukrainian", "footer")] = ""
translation_dict[("urdu", "footer")] = ""
translation_dict[("uzbek", "footer")] = "Biz xizmat ko‘rsatayotgan migrantlar uchun qulaylik yaratish maqsadida ushbu sayt ochiq havoda saqlash joylarini “chegara lagerlari”, “ochiq havoda saqlash joylari” yoki shunga o‘xshash tarzda ko‘rsatishi mumkin. Biroq, xato qilmang: bularning barchasi CBP tomonidan boshqariladigan bir xil ochiq qamoqxonalardir."
translation_dict[("vietnamese", "footer")] = "Để những người di cư mà chúng tôi phục vụ dễ sử dụng, trang này có thể gọi các địa điểm giam giữ ngoài trời là 'trại biên giới', 'địa điểm giam giữ ngoài trời' hoặc tương tự. Tuy nhiên, đừng nhầm lẫn: đây vẫn là những địa điểm giam giữ ngoài trời do CBP duy trì."
translation_dict[("luganda", "footer")] = "Okusobola okwanguyirwa okukozesa ababundabunda be tuweereza, omukutu guno guyinza okuyita ebifo eby’okusibiramu abantu mu bbanga nga ‘enkambi z’ensalo’, ‘ebifo eby’ebweru w’okusibira abantu’, oba ebifaananako bwe bityo. Kyokka tokola nsobi: bino byonna bikyali bifo bye bimu eby’okusibirwamu abantu nga bikuumibwa CBP."




"""
translation_dict[("english", "")] = ""
translation_dict[("arabic", "")] = ""
translation_dict[("bengali", "")] = ""
translation_dict[("mandarin", "")] = ""
translation_dict[("french", "")] = ""
translation_dict[("georgian", "")] = ""
translation_dict[("gujarati", "")] = ""
translation_dict[("hindi", "")] = ""
translation_dict[("kurdish", "")] = ""
translation_dict[("nepali", "")] = ""
translation_dict[("pashto", "")] = ""
translation_dict[("portuguese", "")] = ""
translation_dict[("punjabi", "")] = ""
translation_dict[("russian", "")] = ""
translation_dict[("spanish", "")] = ""
translation_dict[("turkish", "")] = ""
translation_dict[("ukrainian", "")] = ""
translation_dict[("urdu", "")] = ""
translation_dict[("uzbek", "")] = ""
translation_dict[("vietnamese", "")] = ""
translation_dict[("luganda", "")] = ""
"""


scripts_dir = os.path.dirname(os.path.abspath(sys.argv[0])) 
root_dir = scripts_dir.replace(scripts_dir.split("/")[-1], "")
raw_dir = root_dir + "media/raw/"

output_dir = raw_dir + "ouput/"
pdf_dir = root_dir + "media/general-flyers/"


para_compas_dir = root_dir + "para-compas/"
html_dir = para_compas_dir

para_compas_template = para_compas_dir + "para-compas-template.html"

with open(para_compas_template, "r") as template_file:
    template_text = template_file.read()
    template_soup = BeautifulSoup(template_text, 'html.parser')

os.chdir(raw_dir)

raw_docs = glob.glob("*.docx")

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

            with open("tmp.html", "w") as tmp_html:
                tmp_html.write(page_soup.prettify())

            pdf_outf.write(weasyprint.HTML("tmp.html").write_pdf())

        

