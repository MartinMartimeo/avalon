<h4>{{instance.name}}</h4>

<div class="panel panel-default">
    <div class="panel-heading">
        <h3 class="panel-title">{{ _('users-list-heading') }}</h3>
    </div>
    <div class="panel-body">
        {% if not instance.users %}
            {{ _('users-list-empty') }}
        {% else %}
            <ul class="list-group">
                {% for user in instance.users %}
                    <li class="list-group-item">{{user.name}}</li>
                {% end %}
            </ul>
        {% end %}
        <hr />
        <form action="/api/user" method="post" data-model="userModel" data-require="/api/js/user" role="form">
            <fieldset>
                <legend>{{ _('join-room-heading') }}</legend>
                <input type="hidden" name="_room_id" value="{{ instance._id }}"/>
                <div class="form-group" data-fields="name" data-editor-class="form-control"></div>
            </fieldset>
            <button type="submit" class="btn btn-success btn-block">
                {{ _('join-room') }}
            </button>
        </form>
    </div>
</div>
