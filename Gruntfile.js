module.exports = function (grunt) {

    grunt.initConfig({
        wiredep: {
            task: {
                // Point to the files that should be updated when
                // you run `grunt wiredep`
                src: [
                    'templates/base/head/base.html'
                ],

                ignorePath: '../../../bower_components/',
                fileTypes: {
                    html: {
                        block: /(([ \t]*)<!--\s*bower:*(\S*)\s*-->)(\n|\r|.)*?(<!--\s*endbower\s*-->)/gi,
                        detect: {
                            js: /<script.*src=['"]([^'"]+)/gi,
                            css: /<link.*href=['"]([^'"]+)/gi
                        },
                        replace: {
                            js: '<script src="{% static "{{filePath}}" %}"></script>',
                            css: '<link rel="stylesheet" href="{% static "{{filePath}}" %}" />'
                        }
                    }
                },
                options: {
                    // See wiredep's configuration documentation for the options
                    // you may pass:

                    // https://github.com/taptapship/wiredep#configuration
                }
            }
        },
        includeSource: {
            options: {
                basePath: 'apps/',
                baseUrl: '',
                templates: {
                    html: {
                        js: '<script type="text/javascript" src="{% static  "{filePath}" %}"></script>',
                        css: '<link rel="stylesheet" type="text/css" href="{%static "{filePath}"%}" />',
                        scss: '<link rel="stylesheet" type="text/x-scss" href="{%static "{filePath}"%}" />',
                        sass: '<link rel="stylesheet" type="text/x-sass" href="{%static "{filePath}"%}" />',
                    }
                },
                rename: function (dest, matchedSrcPath, options) {
                    matchedSrcPath = matchedSrcPath.split("/").slice(2, 10).join("/");
                    return dest + matchedSrcPath;
                }
            },

            myTarget: {
                files: {
                    'templates/base/head/base.html': 'templates/base/head/base.tpl.html'
                }
            }
        }
    });
    grunt.loadNpmTasks('grunt-wiredep');
    grunt.loadNpmTasks('grunt-include-source');
    grunt.registerTask('default', ['wiredep']);

};
