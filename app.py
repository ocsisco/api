
from flask import Flask, jsonify
import grequests
import markdown
import markdown.extensions.fenced_code
from gevent import monkey
monkey.patch_all()
from generators import num_of_pages_and_amount,url_generator_list


app = Flask(__name__)

url = 'https://api.fbi.gov/wanted/v1/list'





@app.route("/")
def main():


    readme = open("README.md","r")
    template = markdown.markdown(readme.read(), extensions=["fenced_code"])

    return template




@app.route('/search-with-parameters/<search_parameters>')
def search_by_valid_parameters(search_parameters):


    pages = num_of_pages_and_amount(url,search_parameters)[0]
    amount = num_of_pages_and_amount(url,search_parameters)[1]
    urls = url_generator_list(url,search_parameters,pages)
    print("Download " + str(amount) + " elements in " + str(pages) + " pages.")

    rq = (grequests.get(url) for url in urls)
    rspns = grequests.map(rq)
    jsn = [rsp.json() for rsp in rspns]

    wanted = []
    

    while amount:

        for page in range(pages):

            if amount >= 20:


                for i in range(20):
                    data = [amount]+[jsn[page]['items'][i]['title']] + [jsn[page]['items'][i]['uid']]
                    wanted.append(data)
                    amount -= 1
                

            else:
                for i in range(amount):
                    data = [amount]+[jsn[page]['items'][i]['title']] + [jsn[page]['items'][i]['uid']]
                    wanted.append(data)
                    amount -= 1

    wanted = list(reversed(wanted))
    count = len(wanted)


    return jsonify(count,wanted)




@app.route('/search-any/<any>')
def search_by_any_words(any):

    search_parameters = "null"
    


    pages = num_of_pages_and_amount(url,search_parameters)[0]
    amount = num_of_pages_and_amount(url,search_parameters)[1]
    urls = url_generator_list(url,search_parameters,pages)
    print("Download " + str(amount) + " elements in " + str(pages) + " pages.")

    rq = (grequests.get(url) for url in urls)
    rspns = grequests.map(rq)
    jsn = [rsp.json() for rsp in rspns]

    wanted = []

        

    while amount:

        for page in range(pages):

            if amount >= 20:


                for i in range(20):
                    data = [jsn[page]['items'][i]]
                    wanted.append(data)
                    amount -= 1
                

            else:
                for i in range(amount):
                    data = [jsn[page]['items'][i]]
                    wanted.append(data)
                    amount -= 1

    wanted = (list(reversed(wanted)))
    result = []
    n=0

    if "+" in any:
        any = any.split("+")
        x=0
    
        
        for data in wanted:
            for dic in data:
                strdic = str(dic)
                for word in any:
                    if word in strdic:
                        x += 1
                    else:
                        x = 0
                        
                    if x == len(any):
                        n += 1
                        data = [n]+[dic['title']] + [dic['uid']]
                        result.append(data)
                        

    else:

        for data in wanted:
            for dic in data:
                strdic = str(dic)
                if any in strdic:
                    n += 1
                    data = [n]+[dic['title']] + [dic['uid']]
                    result.append(data)
                
    count = len(result)

    return jsonify(count,result)

    


@app.route('/search-any-with-parameters/<search_parameters>/<any>')
def search_by_any_words_with_parameters(search_parameters,any):

    pages = num_of_pages_and_amount(url,search_parameters)[0]
    amount = num_of_pages_and_amount(url,search_parameters)[1]
    urls = url_generator_list(url,search_parameters,pages)
    print("Download " + str(amount) + " elements in " + str(pages) + " pages.")

    rq = (grequests.get(url) for url in urls)
    rspns = grequests.map(rq)
    jsn = [rsp.json() for rsp in rspns]

    wanted = []

        

    while amount:

        for page in range(pages):

            if amount >= 20:


                for i in range(20):
                    data = [jsn[page]['items'][i]]
                    wanted.append(data)
                    amount -= 1
                

            else:
                for i in range(amount):
                    data = [jsn[page]['items'][i]]
                    wanted.append(data)
                    amount -= 1

    wanted = (list(reversed(wanted)))
    result = []
    n=0

    if "+" in any:
        any = any.split("+")
        x=0
    
        
        for data in wanted:
            for dic in data:
                strdic = str(dic)
                for word in any:
                    if word in strdic:
                        x += 1
                    else:
                        x = 0
                        
                    if x == len(any):
                        n += 1
                        data = [n]+[dic['title']] + [dic['uid']]
                        result.append(data)


    else:

        for data in wanted:
            for dic in data:
                strdic = str(dic)
                if any in strdic:
                    n += 1
                    data = [n]+[dic['title']] + [dic['uid']]
                    result.append(data)
                
    count = len(result)

    return jsonify(count,result)

    


@app.route('/view-file-by-id/<id>')
def search_by_id(id):

    search_parameters = "null"

    pages = num_of_pages_and_amount(url,search_parameters)[0]
    amount = num_of_pages_and_amount(url,search_parameters)[1]
    urls = url_generator_list(url,search_parameters,pages)
    print("Download " + str(amount) + " elements in " + str(pages) + " pages.")

    rq = (grequests.get(url) for url in urls)
    rspns = grequests.map(rq)
    jsn = [rsp.json() for rsp in rspns]

    wanted = []

        

    while amount:

        for page in range(pages):

            if amount >= 20:


                for i in range(20):
                    data = [jsn[page]['items'][i]]
                    wanted.append(data)
                    amount -= 1
                

            else:
                for i in range(amount):
                    data = [jsn[page]['items'][i]]
                    wanted.append(data)
                    amount -= 1

    wanted = (list(reversed(wanted)))
    result = []
    n=0

    if "+" in id:
        id = id.split("+")
        x=0
    
        
        for data in wanted:
            for dic in data:
                strdic = str(dic)
                for word in id:
                    if word in strdic:
                        n += 1
                        result.append([n]+[dic])
                        

    else:

        for data in wanted:
            for dic in data:
                strdic = str(dic)
                if id in strdic:
                    n += 1
                    result.append([n]+[dic])
                
    count = len(result)

    return jsonify(count,result)

    
    


    





if __name__ == '__main__':
    app.run(debug=True)