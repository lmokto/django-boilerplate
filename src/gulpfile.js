'use strict';

// Load npm modules
var gulp = require('gulp'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    stylus = require('gulp-stylus');

// Paths
var paths = {
    stylesheets: ['./static/sources/stylesheets/imports.styl'],
    cssOutput: './static/dist/css/',
    scripts: ['./static/sources/js/*.js'],
    jsOutput: './static/dist/js/'
};

// Stylus y CSS
gulp.task('css:stylus', function() {
    return gulp.src(paths.stylesheets)
        .pipe(stylus({'include css': true, 'compress': true}))
        .pipe(concat('main.min.css'))
        .pipe(gulp.dest(paths.cssOutput));
});

// Javascript
gulp.task('scripts', function() {
    return gulp.src(paths.scripts)
        .pipe(concat('main.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest(paths.jsOutput));
});

// Watchs
gulp.task('watch', function() {
    gulp.watch('./static/source/stylesheets/**/*.*', ['css:stylus']);
    gulp.watch('./static/source/js/*.*', ['scripts']);
});

// Default
gulp.task('default', ['css:stylus', 'scripts', 'watch']);
