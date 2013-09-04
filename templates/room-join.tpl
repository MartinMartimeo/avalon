<!-- > room-join.tpl -->

<form action="/api/user" method="post" data-model="userModel" data-require="/api/js/user" role="form">
    <fieldset>
        <legend>{{ _('join-room-heading') }}</legend>

        <input type="hidden" name="_room_id" value="{{ handler.current_room._id }}"/>

        <div class="form-group" data-fields="user.name" data-editor-class="form-control"></div>
    </fieldset>
    <footer class="form-group">
        <input type="submit" class="btn btn-default btn-block" value="{{ _('join-room-submit') }}"/>
    </footer>
</form>

<!-- < room-join.tpl -->


