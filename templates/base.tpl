<!DOCTYPE html>
<html>
<head>

    <script src="http://cdnjs.cloudflare.com/ajax/libs/require-jquery/0.25.0/require-jquery.min.js"
            type="application/javascript"></script>

    <link href="{{ request.method }}://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.0.0-rc2/css/bootstrap.css"
          rel="stylesheet">
    <script src="{{ request.method }}://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.0.0-rc2/js/bootstrap.js"
            type="application/javascript"></script>

    <script src="{{ static_url('js/avalon.js') }}"
            type="application/javascript"></script>
    <script src="{{ static_url('js/tornado-backbone.js') }}"
            type="application/javascript"></script>

</head>

<body>
{% block content %}
Hello World
{% end %}
</body>
</html>

