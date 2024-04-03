#!/usr/bin/env python3


import os 
import sys 
import glob
import copy
import json
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
template_dir = para_compas_dir + "templates/"
in_oads_template = template_dir + "in-oads-template.html"
airport_template = template_dir + "airport-template.html"
old_town_template = template_dir + "old-town-template.html"

copytext_json_file = scripts_dir + "/copytext-trxl8ns.json"

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


def add_oads_page_features(page_soup, language, lang_copytext, pdf_filename):
    page_soup.head.title.string = lang_copytext["Border Aid"]
    page_soup.header.h1.string = lang_copytext["If You Are in a Border Camp"]
    
    home_label = lang_copytext["Home Page"]
    home_btn = page_soup.new_tag("button")
    home_btn.string = home_label
    home_link = page_soup.find(attrs={'id': 'home-btn'})
    home_link.append(home_btn)

    hospital_label = lang_copytext["If You Go to the Hospital"]
    hospital_btn = page_soup.new_tag("button")
    hospital_btn.string = hospital_label
    hospital_link = page_soup.find(attrs={'id': 'hospital-btn'})
    hospital_link.append(hospital_btn)

    airport_label = lang_copytext["If You Are at the Airport"]
    airport_btn = page_soup.new_tag("button")
    airport_btn.string = airport_label
    airport_link = page_soup.find(attrs={'id': 'airport-btn'})
    airport_link.append(airport_btn)

    # Old Town Station
    old_town_label = lang_copytext["Old Town Transit Station"]
    old_town_btn = page_soup.new_tag("button")
    old_town_btn.string = old_town_label
    old_town_link = page_soup.find(attrs={'id': 'old-town-btn'})
    old_town_link.append(old_town_btn)

    # Legal Resources
    legal_label = lang_copytext["Legal Resources"]
    legal_btn = page_soup.new_tag("button")
    legal_btn.string = legal_label
    legal_link = page_soup.find(attrs={'id': 'legal-resource-btn'})
    legal_link.append(legal_btn)

    skip_nav_msg = lang_copytext["Skip to main content"]
    skip_nav_elem = page_soup.find(attrs={'id': 'skip-to-content'})
    skip_nav_elem.string = skip_nav_msg
    skip_nav_elem['title'] = skip_nav_msg

    oads_term_disclaimer = lang_copytext["footer"]

    page_soup.footer.string = oads_term_disclaimer

    disclaimer_elem = page_soup.new_tag("a")
    disclaimer_elem.string = "*"
    disclaimer_elem['id'] = "jump-to-footer"
    disclaimer_elem['href'] = "#footer"
    disclaimer_elem['title'] = oads_term_disclaimer
    page_soup.header.h1.append(disclaimer_elem)

    page_soup.find(attrs={'id': 'hospital-btn'})['href'] = "./" + language + "/hospital.html"
    page_soup.find(attrs={'id': 'airport-btn'})['href'] = "./" + language + "/airport.html"
    page_soup.find(attrs={'id': 'old-town-btn'})['href'] = "./" + language + "/old-town-station.html"
    page_soup.find(attrs={'id': 'legal-resource-btn'})['href'] = "./" + language + "/legal.html"
    page_soup.find(attrs={'id': 'download-link'})['href'] = "../media/general-flyers/" + pdf_filename



def add_airport_page_features(page_soup, language, lang_copytext):
    page_soup.head.title.string = lang_copytext["If You Are at the Airport"]
    page_soup.header.h1.string = lang_copytext["If You Are at the Airport"]
    
    home_label = lang_copytext["Home Page"]
    home_btn = page_soup.new_tag("button")
    home_btn.string = home_label
    home_link = page_soup.find(attrs={'id': 'home-btn'})
    home_link.append(home_btn)

    oads_label = lang_copytext["If You Are in a Border Camp"]
    oads_btn = page_soup.new_tag("button")
    oads_btn.string = oads_label
    oads_link = page_soup.find(attrs={'id': 'oads-btn'})
    oads_link.append(oads_btn)

    hospital_label = lang_copytext["If You Go to the Hospital"]
    hospital_btn = page_soup.new_tag("button")
    hospital_btn.string = hospital_label
    hospital_link = page_soup.find(attrs={'id': 'hospital-btn'})
    hospital_link.append(hospital_btn)

    # Old Town Station
    old_town_label = lang_copytext["Old Town Transit Station"]
    old_town_btn = page_soup.new_tag("button")
    old_town_btn.string = old_town_label
    old_town_link = page_soup.find(attrs={'id': 'old-town-btn'})
    old_town_link.append(old_town_btn)

    # Legal Resources
    legal_label = lang_copytext["Legal Resources"]
    legal_btn = page_soup.new_tag("button")
    legal_btn.string = legal_label
    legal_link = page_soup.find(attrs={'id': 'legal-resource-btn'})
    legal_link.append(legal_btn)

    skip_nav_msg = lang_copytext["Skip to main content"]
    skip_nav_elem = page_soup.find(attrs={'id': 'skip-to-content'})
    skip_nav_elem.string = skip_nav_msg
    skip_nav_elem['title'] = skip_nav_msg

    page_soup.find(attrs={'id': 'hospital-btn'})['href'] = "hospital.html"
    page_soup.find(attrs={'id': 'oads-btn'})['href'] = "../" + language + ".html"
    page_soup.find(attrs={'id': 'old-town-btn'})['href'] = "old-town-station.html"
    page_soup.find(attrs={'id': 'legal-resource-btn'})['href'] = "legal.html"



def add_old_town_page_features(page_soup, language, lang_copytext):
    page_soup.head.title.string = lang_copytext["Old Town Transit Station"]
    page_soup.header.h1.string = lang_copytext["Old Town Transit Station"]
    
    home_label = lang_copytext["Home Page"]
    home_btn = page_soup.new_tag("button")
    home_btn.string = home_label
    home_link = page_soup.find(attrs={'id': 'home-btn'})
    home_link.append(home_btn)

    oads_label = lang_copytext["If You Are in a Border Camp"]
    oads_btn = page_soup.new_tag("button")
    oads_btn.string = oads_label
    oads_link = page_soup.find(attrs={'id': 'oads-btn'})
    oads_link.append(oads_btn)

    hospital_label = lang_copytext["If You Go to the Hospital"]
    hospital_btn = page_soup.new_tag("button")
    hospital_btn.string = hospital_label
    hospital_link = page_soup.find(attrs={'id': 'hospital-btn'})
    hospital_link.append(hospital_btn)

    # Airport
    airport_label = lang_copytext["If You Are at the Airport"]
    airport_btn = page_soup.new_tag("button")
    airport_btn.string = airport_label
    airport_link = page_soup.find(attrs={'id': 'airport-btn'})
    airport_link.append(airport_btn)

    # Legal Resources
    legal_label = lang_copytext["Legal Resources"]
    legal_btn = page_soup.new_tag("button")
    legal_btn.string = legal_label
    legal_link = page_soup.find(attrs={'id': 'legal-resource-btn'})
    legal_link.append(legal_btn)

    skip_nav_msg = lang_copytext["Skip to main content"]
    skip_nav_elem = page_soup.find(attrs={'id': 'skip-to-content'})
    skip_nav_elem.string = skip_nav_msg
    skip_nav_elem['title'] = skip_nav_msg

    page_soup.find(attrs={'id': 'hospital-btn'})['href'] = "hospital.html"
    page_soup.find(attrs={'id': 'oads-btn'})['href'] = "../" + language + ".html"
    page_soup.find(attrs={'id': 'airport-btn'})['href'] = "airport.html"
    page_soup.find(attrs={'id': 'legal-resource-btn'})['href'] = "legal.html"



def make_html_page(language, iso639_code, html_filename, template_soup, file, page_type, pdf_filename):
    #lang_copytext = None
    with open(copytext_json_file, "r") as inf:
        copytext_data = json.load(inf)
        lang_copytext = copytext_data[language]

    with open(file, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value # The generated HTML
        messages = result.messages # Any messages, such as warnings during conversion

        soup = BeautifulSoup(html, 'html.parser')

        page_soup = copy.copy(template_soup)

        page_soup.html['lang'] = iso639_code

        if page_type == "If You Are in a Border Camp":
            add_oads_page_features(page_soup, language, lang_copytext, pdf_filename)
        elif page_type == "If You Are at the Airport":
            add_airport_page_features(page_soup, language, lang_copytext)
        elif page_type == "Old Town Transit Station":
            add_old_town_page_features(page_soup, language, lang_copytext)

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





def generate_oads_pages():
    with open(in_oads_template, "r") as template_file:
        template_text = template_file.read()
        template_soup = BeautifulSoup(template_text, 'html.parser')

    os.chdir(raw_dir)

    raw_docs = glob.glob("*.docx")

    all_pdfs = {}

    for file in raw_docs:

        filename_segs = file.split("-")
        translator = filename_segs[1].strip().lower()
        language = filename_segs[2].strip().lower().replace(" ", "-")
        file_date_mmddyyyy = filename_segs[3].strip().replace(".docx", "").lower()

        iso639_code = lang_codes[language]

        month = file_date_mmddyyyy[0:2]
        day = file_date_mmddyyyy[2:4]
        year = file_date_mmddyyyy[4:]

        html_filename = html_dir + language + ".html"
        pdf_filename = "jacumba-flyer-" + month + "-" + day + "-" + year + "-" + translator + "-" + language + ".pdf"
        pdf_filepath = pdf_dir + pdf_filename

        page_soup = make_html_page(language, iso639_code, html_filename, template_soup, file, "If You Are in a Border Camp", pdf_filepath)
        #make_pdf(pdf_filepath, page_soup)

        #all_pdfs[language] = pdf_filepath.replace(root_dir, "./")

    #update_download_center(all_pdfs)


def generate_airport_pages():
    with open(airport_template, "r") as template_file:
        template_text = template_file.read()
        template_soup = BeautifulSoup(template_text, 'html.parser')

    os.chdir(raw_dir + "airport/")

    raw_docs = glob.glob("*.docx")

    #all_pdfs = {}

    for file in raw_docs:

        filename_segs = file.split("-")
        language = "-".join(filename_segs[1:]).strip().replace(".docx", "").lower().replace(" ", "-")

        #print(language)
        iso639_code = lang_codes[language]

        html_filename = html_dir + language + "/airport.html"
        print(html_filename)

        page_soup = make_html_page(language, iso639_code, html_filename, template_soup, file, "If You Are at the Airport", None)


#generate_airport_pages()


def generate_old_town_pages():
    with open(old_town_template, "r") as template_file:
        template_text = template_file.read()
        template_soup = BeautifulSoup(template_text, 'html.parser')

    os.chdir(raw_dir + "old-town/")

    raw_docs = glob.glob("*.docx")

    #all_pdfs = {}

    for file in raw_docs:

        filename_segs = file.split("-")
        language = "-".join(filename_segs[2:]).strip().replace(".docx", "").lower().replace(" ", "-")

        #print(language)
        iso639_code = lang_codes[language]

        html_filename = html_dir + language + "/old-town-station.html"
        print(html_filename)

        page_soup = make_html_page(language, iso639_code, html_filename, template_soup, file, "Old Town Transit Station", None)

generate_old_town_pages()

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