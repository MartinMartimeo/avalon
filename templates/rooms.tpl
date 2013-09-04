<!-- > rooms.tpl -->

<div class="list-group">
    <a href="/room/new" class="list-group-item">
        <span class="badge">&raquo;</span>
        <h4 class="list-group-item-heading">{{ _('new-room-heading') }}</h4>

        <p class="list-group-item-text">{{ _('new-room-text') }}</p>
    </a>
</div>
<div class="list-group" data-collection="roomCollection" data-require="/api/js/room">
    <a href="/room/<%= _id %>" class="list-group-item">
        <span class="badge"><%= users.length %></span>
        <h4 class="list-group-item-heading"><%= name %></h4>

        <p class="list-group-item-text">...</p>
    </a>
</div>

<!-- < rooms.tpl -->


