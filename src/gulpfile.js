'use strict';

// Load npm modules
var gulp = require('gulp'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    sass = require('gulp-sass');

// Sass
gulp.task('css:sass', function() {
    return gulp.src(['static/sources/styles/imports.scss'])
        .pipe(sass({ outputStyle: 'compressed' }))
        .pipe(concat('main.min.css'))
        .pipe(gulp.dest('static/dist/css/'));
});

// Javascript
gulp.task('scripts', function() {
    return gulp.src(['static/sources/js/**/*.js'])
        .pipe(concat('main.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest(paths.jsOutput));
});

// Watchs
gulp.task('watch', function() {
    gulp.watch('./static/sources/styles/**/*.*', ['css:sass']);
    gulp.watch('static/sources/js/**/*.js', ['scripts']);
});

// Default
gulp.task('default', ['css:sass', 'scripts', 'watch']);
