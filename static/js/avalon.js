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
        "backbone-forms": "//cdnjs.cloudflare.com/ajax/libs/backbone-forms/0.12.0/backbone-forms.min"
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