{% extends 'base.tpl' %}

{% block body %}
<div class="row">
    <div class="col-sm-6">
        {% block left %}{% raw left %}{% end %}
    </div>
    <div class="col-sm-6">
        {% block right %}{% raw right %}{% end %}
    </div>
</div>
{% end %}
