"use strict";
var fs = require('fs');
var gulp = require('gulp');
var sass = require('gulp-ruby-sass');
var notify = require('gulp-notify');
var bower = require('gulp-bower');
var watch = require('gulp-watch');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var minifycss = require('gulp-minify-css');
var prefix = require('gulp-autoprefixer');
var livereload = require('gulp-livereload');
var csslint = require('gulp-csslint');
var json = JSON.parse(fs.readFileSync('./package.json'));

var config = (function () {
    var appName = json.name;

    var path = {
        bower: './bower_components/',
        assets: './' + appName + '/assets',
        static: './' + appName + '/static'
    };

    return {
        path: path,
        scss: {
            input: path.assets + '/scss/style.scss',
            include: [
                path.bower + '/bootstrap-sass-official/assets/stylesheets',
                path.bower + '/fontawesome/scss',
                path.assets + '/scss/'
            ],
            output: path.static + "/css",
            watch: [
                path.assets + '/scss/**.scss'
            ]
        },
        icons: {
            input: [
                path.bower + '/font-awesome/fonts/**.*'
            ],
            output: path.static + "/fonts"
        },
        script: {
            input: [
                path.bower + '/jquery/dist/jquery.js',
                path.assets + '/js/*.js'
            ],
            output: {
                dir: path.static + "/js",
                filename: 'script.js'
            },
            watch: [
                path.assets + '/js/*.js'
            ]
        }
    };
}());

gulp.task('bower', function () {
    return bower(config.path.bower);
});

gulp.task('icons', function () {
    return gulp.src(config.icons.input)
        .pipe(gulp.dest(config.icons.output));
});

gulp.task('js', function () {
    return gulp.src(config.script.input)
        .pipe(concat(config.script.output.filename))
        .pipe(gulp.dest(config.script.output.dir))
        .pipe(livereload())
        .pipe(uglify())
        .pipe(rename({extname: '.min.js'}))
        .pipe(gulp.dest(config.script.output.dir))
        .pipe(livereload());
});

gulp.task('scss', function () {
    return sass(
        config.scss.input,
        {
            style: 'expanded',
            loadPath: config.scss.include,
            sourcemap: true
        }
    )
        .pipe(prefix("last 1 version", "> 1%", "ie 8", "ie 7"))
        .pipe(gulp.dest(config.scss.output))
        .pipe(livereload())
        .pipe(rename({extname: '.min.css'}))
        .pipe(minifycss())
        .pipe(gulp.dest(config.scss.output))
        .pipe(livereload());
});

// Rerun the task when a file changes
gulp.task('watch', function () {
    livereload.listen();
    config.scss.watch.forEach(function (path) {
        gulp.watch(path, ['scss']);
    });
    config.script.watch.forEach(function (path) {
        gulp.watch(path, ['js']);
    });
});

gulp.task('default', ['bower', 'icons', 'js', 'scss', 'watch']);
