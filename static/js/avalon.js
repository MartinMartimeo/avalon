/**
 * User: Martin Martimeo
 * Date: 30.08.13
 * Time: 23:45
 */

require.config({
    baseUrl: '/static/',
    paths: {
        underscore: "http://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.1/underscore-min",
        backbone: "http://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.0.0/backbone-min",

        "backbone-relational": "http://cdnjs.cloudflare.com/ajax/libs/backbone-relational/0.8.5/backbone-relational.min",

        "backbone-forms": "/static/js/backbone-forms"
    },
    shim: {
        underscore: {
            exports: '_'
        },
        backbone: {
            deps: ["underscore", "jquery"],
            exports: "Backbone"
        },
        "backbone-relational": {
            deps: ["backbone"]
        },
        "backbone-forms": {
            deps: ["backbone"]
        }
    }
});

require(["jquery", "underscore", "backbone"], function ($, _, Backbone) {
    var Avalon = Backbone.Router.extend({
        $left: $("body > .row > div:first-child"),
        $right: $("body > .row > div:last-child"),

        routes: {
            ":template": "showLeft",
            ":template:/:sub:": "showRight"
        },

        show: function (template, where) {
            var $node, $template = $("script[data-for='" + template + "']");

            if (where == "left") {
                $node = this.$left.empty();
            } else {
                $node = this.$right.empty();
            }

            if ($template.length == 0) {
                $template = $("head").append("<script>");
                $template.attr("type", "text/template");
                $template.attr("data-for", template);
                $template.load("/" + template + " #body", function () {
                    $node.html($template.html());
                });
            } else {
                $node.html($template.html());
            }
        },

        showLeft: function (template) {
            this.show(template, "left");
        },

        showRight: function (template, sub) {
            this.show(template + "/" + sub, "right");
        }

    });

    $(function () {
        window.Avalon = new Avalon();
        Backbone.history.start({pushState: true, silent: true});
    });

});