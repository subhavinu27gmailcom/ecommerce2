{% else %}
see our new collections
{% endif %}
{% endblock %}
{% block content %}
{% if category %}
<div>
<div class="row my_row_class">
    <div class="mx_auto">

<a href="{% url 'shopapp:allProdCat' %}">OUR PRODUCT COLLECTION</a>
</div>
    </div>
</div>
{% endif %}
<div class="mx_auto">
{% if category %}
    <img class="my_image" src="{{category.image.url}}" alt="{{category.name}}">
</div>
<br>
<div>
    <h1 class="text-center my_title"> {{category.name}}</h1>
     <p class="text-justify"> {{category.description}}</p>
</div>
{% else %}
<div>
<img src="{% static 'img/banner.png' %}" alt="our products">
</div>
<br>
<div>
    <h1>our product ccollection </h1>
    <p>What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum </p>
</div>
{% endif %}
<div class="container">
        <div class="row mx_auto">

    {% for product in products %}
    <div class="my_bottom_margin col-9 col-sm-12 col-md-4 xol-lg-4">
        <div class="card text-center" style="min-width:18rem;">
       <a href="{{product.get_url}}"><img class="card-img-top my_image" src="{{product.image.url}}" alt="{{product.name}}"></a>

        <div class="card-body">
            <h4>{{product.name}}</h4>
            <p>{{product.price}}<p>
        </div>
        </div>
    </div>
    {% endfor %}
</div>



</div>
{% endblock %}