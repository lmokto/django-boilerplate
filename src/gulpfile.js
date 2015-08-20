'use strict';

// Load npm modules
var gulp = require('gulp'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    sass = require('gulp-sass');

// Paths
var paths = {
    stylesheets: ['./static/sources/stylesheets/imports.scss'],
    cssOutput: './static/dist/css/',
    scripts: ['./static/sources/js/*.js'],
    jsOutput: './static/dist/js/'
};

// Stylus y CSS
gulp.task('css:sass', function() {
    return gulp.src(paths.stylesheets)
        .pipe(sass({ outputStyle: 'compressed' }))
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
    gulp.watch('./static/sources/stylesheets/**/*.*', ['css:sass']);
    gulp.watch('./static/sources/js/**/*.*', ['scripts']);
});

// Default
gulp.task('default', ['css:sass', 'scripts', 'watch']);
