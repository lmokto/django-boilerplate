'use strict';

// Load npm modules
var gulp = require('gulp'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    stylus = require('gulp-stylus');

// Paths
var paths = {
    css_input: ['./static/source/css/_imports_all.styl'],
    css_output: './static/dist/css',
    js_input: ['./static/source/js/*.js'],
    js_output: './static/dist/js'
};


// Stylus y CSS
gulp.task('stylus', function() {

    return gulp.src(paths.css_input)
        .pipe(stylus({'include css': true, 'compress': true}))
        .pipe(concat('main.min.css'))
        .pipe(gulp.dest(paths.css_output));

});

// Javascript
gulp.task('scripts', function() {

    return gulp.src(paths.js_input)
        .pipe(concat('main.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest(paths.js_output));

});

// Watchs
gulp.task('watch', function() {
    gulp.watch('./static/source/css/*.*', ['stylus']);
    gulp.watch('./static/source/js/*.*', ['scripts']);
});

// Default
gulp.task('default', ['stylus', 'scripts', 'watch']);
