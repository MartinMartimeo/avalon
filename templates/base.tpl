<!DOCTYPE html>
<html>
<head>
    {% if not is_ajax %}
    <script src="http://cdnjs.cloudflare.com/ajax/libs/require-jquery/0.25.0/require-jquery.min.js"
            type="application/javascript"></script>

    <link href="{{ request.protocol }}://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.0.0/css/bootstrap.min.css"
          rel="stylesheet">
    <script src="{{ request.protocol }}://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.0.0/js/bootstrap.min.js"
            type="application/javascript"></script>

    <script src="{{ static_url('js/avalon.js') }}"
            type="application/javascript"></script>
    <script src="{{ static_url('js/tornado-backbone.js') }}"
            type="application/javascript"></script>

    <link href="{{ static_url('css/avalon.css') }}"
          rel="stylesheet">
    <link href="{{ static_url('css/avalon-landscape.css') }}"
          media="all and (orientation:landscape)"
          rel="stylesheet">
    <link href="{{ static_url('css/avalon-portrait.css') }}"
          media="all and (orientation:portrait)"
          rel="stylesheet">
    {% end %}

    {% block head %}

    {% end %}
</head>
<body>
{% block body %}
{% raw content %}
{% end %}
</body>
</html>

