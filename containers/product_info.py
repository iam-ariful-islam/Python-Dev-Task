# scraping product info from html data
def scrap_product_info(soup):
    scrap = dict()
    
    tag = ['span', 'tr']
    key = ['class', 'id']
    attrs = {'Product title': 'a-size-large product-title-word-break', 'Price': 'a-offscreen','Band': 'a-spacing-small po-brand', 'Model': 'a-spacing-small po-model_name', 'Style': 'a-spacing-small po-style',
             'Color': 'a-spacing-small po-color', 'Screen Size': 'a-spacing-small po-display.size', 'Shape': 'a-spacing-small po-item_shape',
             'Target': 'a-spacing-small po-target_audience', 'Age Range': 'a-spacing-small po-age_range_description'}

    for k, v in attrs.items():
        x = None
        t = 0
        while x is None:
            x = soup.find(tag[t], attrs={key[0], v})
            t += 1
        try: x = x.string.strip().replace(',', '')
        except: x = x.find(tag[0], attrs={'class', 'a-size-base po-break-word'}).string.strip().replace(',', '')
        scrap[k] = x
        
    try: review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')
    except AttributeError: review_count = 'N/A'
    scrap['Total reviews'] = review_count
    
    try: rating = soup.find(tag[0], attrs={key[0], 'a-icon-alt'}).string.strip().replace(',', '')
    except AttributeError: rating = 'N/A'
    scrap['Rating'] = rating

    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find(tag[0]).string.strip().replace(',', '')
    except AttributeError: available = 'N/A'
    scrap['Availability'] = available
    
    scrap['Price'] = 'N/A' if scrap['Price'][0]!='$' else scrap['Price']

    return scrap