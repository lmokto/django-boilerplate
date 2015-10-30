'use strict';

// Load npm modules
var gulp = require('gulp'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    sass = require('gulp-sass');

// Sass
gulp.task('css:sass', function() {
    return gulp.src(['static/src/styles/main.scss'])
        .pipe(sass({ outputStyle: 'compressed' }))
        .pipe(concat('main.min.css'))
        .pipe(gulp.dest('static/dist/css/'));
});

// Javascript
gulp.task('scripts', function() {
    return gulp.src(['static/src/js/**/*.js'])
        .pipe(concat('main.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('static/dist/js/'));
});

// Watchs
gulp.task('watch', function() {
    gulp.watch('static/src/styles/**/*.*', ['css:sass']);
    gulp.watch('static/src/js/**/*.js', ['scripts']);
});

// Default
gulp.task('default', ['css:sass', 'scripts', 'watch']);
