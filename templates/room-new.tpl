<!-- > room-new.tpl -->

<form action="/api/room" method="post" data-model="roomModel" data-require="/api/js/room" role="form">
    <fieldset>
        <legend>{{ _('new-room-heading') }}</legend>

        <div class="form-group" data-fields="name" data-editor-class="form-control"></div>
    </fieldset>
    <footer class="form-group">
        <input type="submit" class="btn btn-default btn-block" value="{{ _('new-room-submit') }}"/>
    </footer>
</form>

<!-- < room-new.tpl -->


