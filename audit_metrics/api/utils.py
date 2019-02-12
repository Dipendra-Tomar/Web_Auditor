from urllib.error import URLError, HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def url_handle(raw_url):
    raw_url = raw_url.lower()
    if raw_url[-1] == '/':
        raw_url = raw_url
    else:
        raw_url = raw_url + '/'
    if raw_url[:4] == 'www.':
        url = 'http://' + raw_url
    elif raw_url[:8] == 'https://':
        url = raw_url
    elif raw_url[:7] == 'http://':
        url = raw_url
    else:
        url = 'http://www.' + raw_url
    return url


def get_basic_audit(url):
    page_response = urlopen(url)
    page_content = BeautifulSoup(page_response)
    page_title = page_content.title.text
    sitemapxml_status = get_sitemap_xml_status(url)
    robottxt_status = get_robots_txt_status(url)
    meta_keyword, meta_description = get_metatag_data(page_content)
    page_alinks_list = page_content.find_all('a')
    alink_count = len(page_alinks_list)
    alink_text_list = []
    if page_alinks_list:
        for link in page_alinks_list:
            link_attr_dict = link.attrs
            if 'href' in link_attr_dict:
                alink_text_list.append(link_attr_dict['href'])
    h1_count, h1_text_list = get_headingtag_data(1, page_content)
    h2_count, h2_text_list = get_headingtag_data(2, page_content)
    h3_count, h3_text_list = get_headingtag_data(3, page_content)
    context = {
        "page_title": page_title, "meta_keyword": meta_keyword,
        "meta_description": meta_description,
        "alink_count": alink_count, "alink_text_list": alink_text_list,
        "h1_count": h1_count, "h1_text_list": h1_text_list,
        "h2_count": h2_count, "h2_text_list": h2_text_list,
        "h3_count": h3_count, "h3_text_list": h3_text_list,
        "sitemapxml_status": sitemapxml_status,
        "robottxt_status": robottxt_status
    }
    return context


def get_sitemap_xml_status(url):
    sitemap_url = url + "sitemap.xml"
    try:
        response = urlopen(sitemap_url)
        response_status = response.status
    except HTTPError as e:
        response_status = e.code
    except URLError as e:
        response_status = 1
    if response_status == 200:
        sitemap_status = True
    else:
        sitemap_status = False
    return sitemap_status


def get_robots_txt_status(url):
    sitemap_url = url + "robots.txt"
    try:
        response = urlopen(sitemap_url)
        response_status = response.status
    except HTTPError as e:
        response_status = e.code
    except URLError as e:
        response_status = 1
    if response_status == 200:
        sitemap_status = True
    else:
        sitemap_status = False
    return sitemap_status


def get_headingtag_data(num, page_content):
    h_count = 0
    h_list = page_content.find_all('h{}'.format(num))
    h_text_list = []
    if h_list:
        h_count = len(h_list)
        for each in h_list:
            h_text_list.append(each.text)
    return h_count, h_text_list


def get_metatag_data(page_content):
    page_meta_list = page_content.find_all('meta')
    meta_keyword = None
    meta_description = None
    for meta in page_meta_list:
        attr_dict = meta.attrs
        if 'name' in attr_dict:
            if attr_dict['name'] == 'keywords':
                meta_keyword = attr_dict['content']
            if attr_dict['name'] == 'description':
                meta_description = attr_dict['content']
    return meta_keyword, meta_description
