import requests
import csv 
import time

cookies = {
    'zguid': '24|%240bfb7799-46dd-4ec3-8866-e6a64587d2c9',
    'zjs_anonymous_id': '%220bfb7799-46dd-4ec3-8866-e6a64587d2c9%22',
    'zjs_user_id': 'null',
    'zg_anonymous_id': '%2298171e59-62b2-4370-bebd-04cd1a5cceb9%22',
    'x-amz-continuous-deployment-state': 'AYABeI93%2FNauB+4Oril1bQFWl7YAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxNTk1MzcxVEJNNTJaWDdPU09PAAEAAkNEABpDb29raWUAAACAAAAADFLs80TIYTUlv54ImQAwzkE59nQXE5w+pAoTi2aWjLTmiBgYhzY%2FleBBR26vBBYB1g6wPsr3W1sAqWL3uoezAgAAAAAMAAQAAAAAAAAAAAAAAAAAAHCyPggMQSWsP2RSeMeUFib%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxxv+L%2FzEzNXX9MsUSs8U6%2FcWeuPHFrC+T3Z8bS',
    'JSESSIONID': '625AEBAE2BDFA2064C1E033B1C72A9C9',
    'zgsession': '1|5909079c-48d3-49d4-8114-f651bee8f661',
    'search': '6|1687385877007%7Crect%3D45.08167979796596%252C-78.35352209516445%252C42.147535713307256%252C-81.26489904828945%26rid%3D792723%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%09792723%09%09%09%09%09%09',
    'g_state': '{"i_p":1684880286566,"i_l":2}',
    'AWSALB': 'F5OnOpB06BDTba9UZTOtBLmtl865eCEtedgloolsZ+ZpPVJj/4bSlNdLoYUZez7YYa8yEVRRNlKPFM0lxty9DkUEgU1UbEpeDBQfRVu/JQc0vJ0zh2Ng3NfpwKni',
    'AWSALBCORS': 'F5OnOpB06BDTba9UZTOtBLmtl865eCEtedgloolsZ+ZpPVJj/4bSlNdLoYUZez7YYa8yEVRRNlKPFM0lxty9DkUEgU1UbEpeDBQfRVu/JQc0vJ0zh2Ng3NfpwKni',
}

headers = {
    'authority': 'www.zillow.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'zguid=24|%240bfb7799-46dd-4ec3-8866-e6a64587d2c9; zjs_anonymous_id=%220bfb7799-46dd-4ec3-8866-e6a64587d2c9%22; zjs_user_id=null; zg_anonymous_id=%2298171e59-62b2-4370-bebd-04cd1a5cceb9%22; x-amz-continuous-deployment-state=AYABeI93%2FNauB+4Oril1bQFWl7YAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxNTk1MzcxVEJNNTJaWDdPU09PAAEAAkNEABpDb29raWUAAACAAAAADFLs80TIYTUlv54ImQAwzkE59nQXE5w+pAoTi2aWjLTmiBgYhzY%2FleBBR26vBBYB1g6wPsr3W1sAqWL3uoezAgAAAAAMAAQAAAAAAAAAAAAAAAAAAHCyPggMQSWsP2RSeMeUFib%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxxv+L%2FzEzNXX9MsUSs8U6%2FcWeuPHFrC+T3Z8bS; JSESSIONID=625AEBAE2BDFA2064C1E033B1C72A9C9; zgsession=1|5909079c-48d3-49d4-8114-f651bee8f661; search=6|1687385877007%7Crect%3D45.08167979796596%252C-78.35352209516445%252C42.147535713307256%252C-81.26489904828945%26rid%3D792723%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%09792723%09%09%09%09%09%09; g_state={"i_p":1684880286566,"i_l":2}; AWSALB=F5OnOpB06BDTba9UZTOtBLmtl865eCEtedgloolsZ+ZpPVJj/4bSlNdLoYUZez7YYa8yEVRRNlKPFM0lxty9DkUEgU1UbEpeDBQfRVu/JQc0vJ0zh2Ng3NfpwKni; AWSALBCORS=F5OnOpB06BDTba9UZTOtBLmtl865eCEtedgloolsZ+ZpPVJj/4bSlNdLoYUZez7YYa8yEVRRNlKPFM0lxty9DkUEgU1UbEpeDBQfRVu/JQc0vJ0zh2Ng3NfpwKni',
    'dnt': '1',
    'pragma': 'no-cache',
    'prefer': 'safe',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
}

# To change the listing areas, you need to change the "regionSelection" list and all of its dictioanries inside. Right click on the zillow listing area, view source code, and search up "regionid", then copy and paste that dictionary into the list. Remember that you should only have 5 dictionaries in the list at all times.
params = {
    'searchQueryState': '{"pagination":{},"mapBounds":{"north":45.08167979796596,"east":-78.35352209516445,"south":42.147535713307256,"west":-81.26489904828945},"regionSelection":[{"regionId":792682,"regionType":6}, {"regionId":792723,"regionType":6}, {"regionId":792711,"regionType":6}, {"regionId":792689,"regionType":6}, {"regionId":792829,"regionType":6}],"isMapVisible":true,"filterState":{"ah":{"value":true},"sort":{"value":"globalrelevanceex"}},"isListVisible":true,"mapZoom":8}',
}
csv_lst = []

file = open('zillow.csv', 'w', newline='', encoding='utf-8')

for i in range(1, 200):
    try:
        writer = csv.writer(file)
        writer.writerow(["Address", "Type", "Price", "Features"])
        
        # Instead of scraping the link itself, this code reverse engineered the requests which the site sends and so you can't change the link in the code. You need to change the "regionSelection" list as stated above.
        response = requests.get(f'https://www.zillow.com/toronto-on/{i}_p/', params=params, cookies=cookies, headers=headers)

        from bs4 import BeautifulSoup

        # create a new soup

        soup = BeautifulSoup(response.text, 'html.parser')

        # Get a list of all divs with class = 'StyledPropertyCardDataWrapper-c11n-8-84-0__sc-1omp4c3-0 cXTjvn property-card-data'

        # Get a list of all divs with "StyledPropertyCard" in the class name

        divs = soup.find_all('div', class_='StyledPropertyCardDataWrapper-c11n-8-84-0__sc-1omp4c3-0 cXTjvn property-card-data')

        # extend the divs list with divs of class 'StyledPropertyCardDataWrapper-c11n-8-84-0__sc-1omp4c3-0 cXTjvn property-card-data'

        divs.extend(soup.find_all('div', class_='StyledPropertyCardDataWrapper-c11n-8-84-0__sc-1omp4c3-0 cXTjvn property-card-data'))

        # Extend the divs list iwth divs with class 'StyledCard-c11n-8-84-0__sc-rmiu6p-0 vlmfT StyledPropertyCardBody-c11n-8-84-0__sc-1p5uux3-0 ibnQgp'

        divs.extend(soup.find_all('div', class_='StyledCard-c11n-8-84-0__sc-rmiu6p-0 vlmfT StyledPropertyCardBody-c11n-8-84-0__sc-1p5uux3-0 ibnQgp'))


        # Now, we need to print the info in each div
        for div in divs:
            # Step 0: Get the address
            # The address is in the address tag
            address = div.find('address').text
            print(address)
            csv_lst.append(address)
            # Get the parent of the address tag
            parent = div.find('address').parent
            # The parent is an anchor tag - we will need this URL later to get more info about the property
            url = parent['href']
            # Step 1: Get the listing type
            # The listing type is contained in the div with class StyledPropertyCardDataArea-c11n-8-84-0__sc-yipmu-0 exsYeB
            type = div.find('div', class_='StyledPropertyCardDataArea-c11n-8-84-0__sc-yipmu-0 exsYeB').text
            print(type)
            csv_lst.append(type)
            # Step 2: Get the price
            # The price is under the div with class 'StyledPropertyCardDataArea-c11n-8-84-0__sc-yipmu-0 dJxUgr'
            price_div = div.find('div', class_='StyledPropertyCardDataArea-c11n-8-84-0__sc-yipmu-0 dJxUgr') or div.find('div', class_='StyledCard-c11n-8-84-0__sc-rmiu6p-0 vlmfT StyledPropertyCardBody-c11n-8-84-0__sc-1p5uux3-0 ibnQgp') or div.find('div', class_='StyledPropertyCardDataWrapper-c11n-8-84-0__sc-1omp4c3-0 cXTjvn property-card-data')
            
            # The actual price is under the span with class = 'property-card-price'
            price = price_div.find('span').text
            print(price)
            csv_lst.append(price)
            print("Listing Features:")
            
            # Now we will do another scraping on the url we got earlier
            # We will get the number of beds, baths and sqft
            new_response = requests.get(url, headers=headers)
            new_soup = BeautifulSoup(new_response.text, 'html.parser')
            # Find a list of all h4s 
            h4s = new_soup.find_all('h4')
            # Now we want to find the h4 with the text "Facts and features"
            tag = None
            for h4 in h4s:
                if h4.text == 'Facts and features':
                    tag = h4
                    break
            # Now we want to get the parent of the h4 tag
            parent = tag.parent
            
            # Now we want to extract the facts and features 
            # We're after Interior details and Property details
            
            # Step one: Interior details
            # We need to find the h5 with the text "Interior details"
            h5s = parent.find_all('h5')
            for h5 in h5s:
                if h5.text == 'Interior details':
                    tag = h5
                    break
            
            # Now, we get the parent of the h5 tag
            parent = tag.parent
            
            # Now, we will get all of the divs inside of the parent
            divs = parent.find_all('div')
            for div in divs:
                # Get the H6 element in the div
                h6 = div.find('h6')
                csv_lst.append(h6.text)
                # Get a list of all spans inside of the div
                spans = div.find_all('span')
                for span in spans:
                    csv_lst.append(span.text)
            
            # Repeat the same process for Property details

            for h5 in h5s:
                csv_lst.append(h5.text)
                parent = tag.parent
                divs = parent.find_all('div')
                for div in divs:
                    # Get the H6 element in the div
                    h6 = div.find('h6')
                    csv_lst.append(h6.text)
                    # Get a list of all spans inside of the div
                    spans = div.find_all('span')
                    for span in spans:
                        csv_lst.append(span.text)
            writer.writerow(csv_lst)
            csv_lst = []    
            time.sleep(2)
    except:
        pass
    finally:
        # file.close()
        print(f"Done scraping {i} pages")
