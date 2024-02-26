#!/usr/bin/env python3


import os 
import sys 
import glob
import copy
import mammoth
from bs4 import BeautifulSoup
import weasyprint


lang_codes = {}
lang_codes["english"] = "en"
lang_codes["arabic"] = "ar"
lang_codes["bengali"] = "bn"
lang_codes["farsi"] = "fa"
lang_codes["french"] = "fr"
lang_codes["georgian"] = "ka"
lang_codes["hindi"] = "hi"
lang_codes["luganda"] = "lg"
lang_codes["mandarin"] = "cmn"
lang_codes["nepali"] = "ne"
lang_codes["pashto"] = "ps"
lang_codes["portuguese"] = "pt"
lang_codes["russian"] = "ru"
lang_codes["sinhala"] = "si"
lang_codes["spanish"] = "es"
lang_codes["tamil"] = "ta"
lang_codes["turkish"] = "tr"
lang_codes["urdu"] = "ur"
lang_codes["uzbek"] = "uz"
lang_codes["vietnamese"] = "vi"
lang_codes["gujarati"] = "gu"
lang_codes["punjabi"] = "pa"
lang_codes["ukrainian"] = "uk"
lang_codes["kurdish"] = "ku"
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

"""
translation_dict[("", "")] = ""
translation_dict[("", "")] = ""
translation_dict[("", "")] = ""
translation_dict[("", "")] = ""
"""


scripts_dir = os.path.dirname(os.path.abspath(sys.argv[0])) 
root_dir = scripts_dir.replace(scripts_dir.split("/")[-1], "")
raw_dir = root_dir + "media/raw/"

output_dir = raw_dir + "ouput/"
#html_dir = raw_dir + "html/"
#pdf_dir = raw_dir + "pdf/"
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
    #print(file)

    filename_segs = file.split("-")
    translator = filename_segs[1].strip().lower()
    language = filename_segs[2].strip().lower()
    file_date_mmddyyyy = filename_segs[3].strip().replace(".docx", "").lower()

    month = file_date_mmddyyyy[0:2]
    day = file_date_mmddyyyy[2:4]
    year = file_date_mmddyyyy[4:]

    html_filename = html_dir + language + ".html"
    pdf_filename = "jacumba-flyer-" + month + "-" + day + "-" + year + "-" + translator + "-" + language + ".pdf"
    pdf_filepath = pdf_dir + pdf_filename
    #print(html_filename)
    #print(pdf_filepath)

    with open(file, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value # The generated HTML
        messages = result.messages # Any messages, such as warnings during conversion

        soup = BeautifulSoup(html, 'html.parser')

        page_soup = copy.copy(template_soup)

        page_soup.html['lang'] = lang_codes[language]
        page_soup.head.title.string = translation_dict[(language, "Border Aid")]
        page_soup.header.h1.string = translation_dict[(language, "If You Are in a Border Camp")]
        page_soup.find(attrs={'id':'download-link'})['href'] = "../media/general-flyers/" + pdf_filename

        if ((language == "arabic") or (language == "farsi") or (language == "urdu") ):
            page_soup.body['class'] = "rtl-text"
        else:
            continue

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

            with open("tmp.html", "w") as tmp_html:
                tmp_html.write(page_soup.prettify())

            pdf_outf.write(weasyprint.HTML("tmp.html").write_pdf())

        

