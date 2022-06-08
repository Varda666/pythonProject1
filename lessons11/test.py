from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/',)
def page_index():
    page_content = """ 
    <h1> <strong> Котофей Семен </strong> </h1>
    <br/>
    <img src="https://chudo-prirody.com/uploads/posts/2021-08/1628755495_2-p-serii-kot-foto-2.jpg" width="300" height="200"/> 
    <br/>
    <div> <p> Привет, я серый кот, а это <a href="https://vplate.ru/koshki/serye">страничка </a> обо мне </p> 
    <p> На ней я буду публиковать свои <del>лапки</del> код </p>
    </div>
    <div>
    <p> <em> Еще буду публиковать <mark> фото своей хозяйки </mark>, когда она меня не кормит </em> </p>
    </div>
    """
    return page_content


app.run()